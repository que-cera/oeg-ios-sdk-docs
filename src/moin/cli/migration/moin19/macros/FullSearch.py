# Copyright: 2025 MoinMoin:UlrichB
# License: GNU GPL v2 (or any later version), see LICENSE.txt for details.

"""
MoinMoin CLI - Migration of FullSearch macro (moin1.9) to new ItemList macro (moin2) if possible
"""

from moin.cli.migration.moin19 import macro_migration
from moin.utils.tree import moin_page

CONTENT_TYPE_MACRO_FORMATTER = "x-moin/macro;name={}"
MACRO_NAME_FULLSEARCH = "FullSearch"
MACRO_NAME_FULLSEARCH_CACHED = "FullSearchCached"


def convert_fullsearch_macro_to_item_list(node):
    """Convert the given FullSearch macro node to an ItemList macro in-place

    The moin1.9 FullSearch macro is used in various situations. One case
    is the listing of all pages for a specific category. In moin2, the
    categories are replaced by tags. Therefore, all macro calls related to
    categories are converted to the moin2 macro ItemList.

    In all other cases, the FullSearch macro call is not changed.
    The same applies to the FullSearchCached macro.

    Example conversions:

    | PageList macro (moin1.9)                | ItemList macro (moin2)                       |
    |-----------------------------------------|----------------------------------------------|
    | <<FullSearch(CategorySample)>>          | <<ItemList(item="/", tag="CategorySample")>> |
    | <<FullSearch(category:CategorySample)>> | <<ItemList(item="/", tag="CategorySample")>> |

    :param node: the DOM node matching the FullSearch macro content type
    :type node: emeraldtree.tree.Element
    """

    # arguments
    args_before = None
    for elem in node.iter_elements():
        if elem.tag.name == "arguments":
            args_before = elem.text
    if args_before and args_before.startswith("Category"):
        # argument is a category name, lets migrate to ItemList macro
        args_after = f'item="/", tag="{args_before}"'
    elif args_before and args_before.startswith("category:"):
        # argument is a category name, strip keyword and migrate to ItemList macro
        args_after = f'item="/", tag="{args_before[9:]}"'
    else:
        # argument is not a category or empty, we keep the old FullSearch macro
        return

    # content type
    new_content_type = CONTENT_TYPE_MACRO_FORMATTER.format("ItemList")
    node.set(moin_page.content_type, new_content_type)

    for elem in node.iter_elements():
        if elem.tag.name == "arguments":
            elem.clear()
            elem.append(args_after)

    # 'alt' attribute
    new_alt = f"<<ItemList({args_after})>>"
    node.set(moin_page.alt, new_alt)


macro_migration.register_macro_migration(
    CONTENT_TYPE_MACRO_FORMATTER.format(MACRO_NAME_FULLSEARCH), convert_fullsearch_macro_to_item_list
)

macro_migration.register_macro_migration(
    CONTENT_TYPE_MACRO_FORMATTER.format(MACRO_NAME_FULLSEARCH_CACHED), convert_fullsearch_macro_to_item_list
)
