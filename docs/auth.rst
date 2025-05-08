Authentication
=======================================================

Login and Register
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Call this methods to show login viewController

.. code-block:: Objective-C
    
        /// Show login from viewcontroller and callback
        /// @param viewController UIViewController
        /// @param callback SunGameAccountCallback
        - (void)showLoginWithViewController:(nullable UIViewController *)viewController callback:(SunGameAccountCallback)callback;
        
        /// Show login with callback
        /// @param callback SunGameAccountCallback
        - (void)showLoginWithCallback:(SunGameAccountCallback)callback;
        
- SunGameAccountCallback

.. code-block:: Objective-C

        typedef void (^SunGameAccountCallback)(SunGameActionType type, id _Nullable response, BOOL success, NSError  * _Nullable error);
        
    
        1. SunGameActionType:
        typedef enum {
            Register = 0,
            LoginSunID,
            LoginFacebook,
            LoginGoogle,
            LoginApple,
            Playnow,
            Logout,
            Close
        }SunGameActionType
        
    
        2. response is JSON that API return:
        {
            "status": "success",
            "api_token": "api_token",
            "uuid": "uuid",
            "message": "message"
        }
        
        3. success YES/NO
 
        4. error
