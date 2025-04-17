Payment
=======================================================

IAP
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Call this method to start the payment process

.. code-block:: Objective-C
    
        /// Payment In-App-Purchase
        /// @param serverID serverID description
        /// @param roleID roleID description
        /// @param levels levels description
        /// @param accountID accountID description
        /// @param productID productID description
        /// @param extInfo productID description
        /// @param callback callback description
        - (void)inAppPurchaseWithServerID:(NSString *)serverID roleID:(NSString *)roleID levels:(NSString *)levels accountID:(nullable NSString *)accountID  productID:(nullable NSString *)productID extInfo:(NSString *)extInfo callback:(SGGIAPCallback)callback;

.. code-block:: Objective-C

        typedef void (^SGGIAPCallback)(SGGIAPStatus status, NSString *message, NSError  * _Nullable error);

.. code-block:: Objective-C
        
        typedef enum {
            SGGPurchasing = 0,
            SGGPurchased, // Purchased with Apple and verify server error
            SGGRestored,
            SGGFailed,
            SGGRequestError, // Request Product ID error
            SGGVerified // Purchased with Apple and verify server success
        }SGGIAPStatus;
