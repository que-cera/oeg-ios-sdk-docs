Other methods
=======================================================

Use this method to show screen Profile 
.. code-block:: Objective-C

        /// Show profile from viewcontroller and callback
        /// @param viewController UIViewController
        /// @param callback OEGAccountCallback
        - (void)showProfileWithViewController:(nullable UIViewController *)viewController callback:(OEGAccountCallback)callback;
        
        /// Show profile with callback
        /// @param callback OEGAccountCallback
        - (void)showProfileWithCallback:(OEGAccountCallback)callback;
        
Use this method to show screeen Change Password
.. code-block:: Objective-C

        /// Show change password from viewcontroller and callback
        /// @param viewController UIViewController
        /// @param callback OEGAccountCallback
        - (void)showChangePasswordWithViewController:(nullable UIViewController *)viewController callback:(OEGAccountCallback)callback;
        
        /// Show change password from viewcontroller and callback
        /// @param callback OEGAccountCallback
        - (void)showChangePasswordWithCallback:(OEGAccountCallback)callback;

Logout
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Use this method to clear the saved token, Google and Facebook credential when user want to switch to new account
.. code-block:: Objective-C

        [[OEGManager sharedManager] logout];

Use this method to get stored ApiToken (return null if user haven't login yet)

.. code-block:: Objective-C

        [OEGManager getAPIToken]

Use this method to get stored uuid (return null if user haven't login yet)

.. code-block:: Objective-C

        [OEGManager getAPIUUID]

Use this method to get Playnow Status (return NO if user haven't playnow yet)
.. code-block:: Objective-C

        [OEGManager isPlayNow]


Tracking
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Tracking event with values

.. code-block:: Objective-C

        /// Log event and value
        /// @param eventName Contains name of event that could be provided from predefined constants
        /// @param values Contains dictionary
        - (void)logEvent:(NSString *)eventName withValues:(NSDictionary * _Nullable)values;
