Authentication
=======================================================

Login and Register
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Call this methods to show login viewController

.. code-block:: Objective-C
    
        /// Show login from viewcontroller and callback
        /// @param viewController UIViewController
        /// @param callback OEGAccountCallback
        - (void)showLoginWithViewController:(nullable UIViewController *)viewController callback:(OEGAccountCallback)callback;
        
        /// Show login with callback
        /// @param callback OEGAccountCallback
        - (void)showLoginWithCallback:(OEGAccountCallback)callback;
        
- OEGAccountCallback

.. code-block:: Objective-C

        typedef void (^OEGAccountCallback)(OEGActionType type, id _Nullable response, BOOL success, NSError  * _Nullable error);
        
    
        1. OEGActionType:
        typedef enum {
            Register = 0,
            LoginOEGID,
            LoginFacebook,
            LoginGoogle,
            LoginApple,
            Playnow,
            Logout,
            Profile,
            ChangePassword,
            ForgotPassword,
            VerifyEmail,
            VerifyPhone,
            Close
        }OEGActionType;
        
    
        2. response is JSON that API return:
        {
            "status": "success",
            "token": "api_token",
            "uuid": "uuid",
            "message": "message"
        }
        
        3. success YES/NO
 
        4. error
