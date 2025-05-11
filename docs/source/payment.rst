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
        - (void)showPaymentWithServerID:(NSString *)serverID roleID:(NSString *)roleID levels:(NSString *)levels accountID:(nullable NSString *)accountID  productID:(nullable NSString *)productID extInfo:(NSString *)extInfo callback:(OEGIAPCallback)callback;

.. code-block:: Objective-C

        typedef void (^OEGIAPCallback)(OEGIAPStatus status, NSString *message, NSError  * _Nullable error);

.. code-block:: Objective-C
        
        typedef enum {
            OEGPurchasing = 0,
            OEGPurchased, // Purchased with Apple and verify server error
            OEGRestored,
            OEGFailed,
            OEGRequestError, // Request Product ID error
            OEGVerified // Purchased with Apple and verify server success
        }OEGIAPStatus;
