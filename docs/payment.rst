Payment
=======================================================

IAP
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Call this method to start the payment process

.. code-block:: Objective-C
    
        /// Payment on Web
        /// Payment on Web
        /// @param serverID serverID description
        /// @param roleID roleID description
        /// @param levels levels description
        /// @param accountID accountID description
        /// @param productID productID description
        /// @param extInfo productID description
        /// @param callback callback description
        - (void)showPaymentWithServerID:(NSString *)serverID roleID:(NSString *)roleID levels:(NSString *)levels accountID:(nullable NSString *)accountID  productID:(nullable NSString *)productID extInfo:(NSString *)extInfo callback:(SunGameIAPCallback)callback;

.. code-block:: Objective-C

        typedef void (^SunGameIAPCallback)(SunGameIAPStatus status, NSString *message, NSError  * _Nullable error);

.. code-block:: Objective-C
        
        typedef enum {
            SunGamePurchasing = 0,
            SunGamePurchased, // Purchased with Apple and verify server error
            SunGameRestored,
            SunGameFailed,
            SunGameRequestError, // Request Product ID error
            SunGameVerified // Purchased with Apple and verify server success
        }SunGameIAPStatus;
