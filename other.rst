Other methods
=======================================================

Logout
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use this method to clear the saved token, Google and Facebook credential when user want to switch to new account

.. code-block:: Objective-C

        [[SGGManager sharedManager] logout];

Use this method to get stored ApiToken (return null if user haven't login yet)

.. code-block:: Objective-C

        [SGGManager getAPIToken]

Use this method to get stored uuid (return null if user haven't login yet)

.. code-block:: Objective-C

        [SGGManager getAPIUUID]

Tracking
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Tracking event with values

.. code-block:: Objective-C

        /// Log event and value
        /// @param eventName Contains name of event that could be provided from predefined constants
        /// @param values Contains dictionary
        - (void)logEvent:(NSString *)eventName withValues:(NSDictionary * _Nullable)values;
