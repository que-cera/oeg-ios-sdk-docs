Installation
=======================================================

Step by step
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Drag and drop or import SDKConfig.plist to your project we will send private for you **
        
- Drag and drop or importSGGFramework.framework to your project.

- Import theSGGFramework to App Delegate

.. code-block:: Objective-C

        @importSGGFramework;

- In your AppDelegate.m at didFinishLaunchingWithOptions function call this line

.. code-block:: Objective-C
    
        [SGGManager handleDidFinishLaunchingWithOptions:launchOptions];
        // If you want to control Firebase push message you can add below code
        [[FirebaseService sharedManager] messagingDelegate:self];
        
- In your AppDelegate.m handle application action

.. code-block:: Objective-C
            
        - (void)applicationWillResignActive:(UIApplication *)application {
            [SGGManager handleWillResignActive];
        }
        
        - (void)applicationDidEnterBackground:(UIApplication *)application {
            [SGGManager handleDidEnterBackground];
        }
        
        - (void)applicationWillEnterForeground:(UIApplication *)application {
            [SGGManager handleWillEnterForeground];
        }
        
        - (void)applicationDidBecomeActive:(UIApplication *)application {
            [SGGManager handleDidBecomeActive];
        }
        
        - (void)applicationWillTerminate:(UIApplication *)application {
            [SGGManager handleWillTerminate];
        }
        
        - (void)application:(UIApplication *)application didRegisterForRemoteNotificationsWithDeviceToken:(NSData *)deviceToken {
            [SGGManager handleDidRegisterForRemoteNotificationsWithDeviceToken:deviceToken];
        }
        
        - (void)application:(UIApplication *)application didReceiveRemoteNotification:(NSDictionary *)userInfo fetchCompletionHandler:(void (^)(UIBackgroundFetchResult))completionHandler {
            [SGGManager handleRemoteNotification:userInfo];
        }
        
        - (BOOL)application:(UIApplication *)app openURL:(NSURL *)url options:(NSDictionary<UIApplicationOpenURLOptionsKey,id> *)options {
            return [SGGManager handleOpenURL:url options:options];
        }
        

- Build Settings
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    Add value for “Other Linker Flags”: -all_load -ObjC -lc++
    Change value for “Allow Non-modular Includes in Framework Modules”: Yes

- Info.plist config
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Now configure the .plist for your project: In Xcode right-click your .plist file and choose “Open As Source Code”.Copy & Paste the XML snippet into the body of your file (…).
– Config for login via facebook

.. code-block:: plist

    <key>FacebookAppID</key>
    <string>{FACEBOOK_APP_ID}</string>
    <key>FacebookDisplayName</key>
    <string>{FACEBOOK_APP_NAME}</string>
    <key>CFBundleURLTypes</key>
    <array>
        <dict>
            <key>CFBundleTypeRole</key>
            <string>Editor</string>
            <key>CFBundleURLName</key>
            <string></string>
            <key>CFBundleURLSchemes</key>
            <array>
                <string>fb{Facebook_App_Id}</string>
            </array>
        </dict>
        <dict>
            <key>CFBundleTypeRole</key>
            <string>Editor</string>
            <key>CFBundleURLName</key>
            <string></string>
            <key>CFBundleURLSchemes</key>
            <array>
                <string>{Bundle_Identifier}</string>
            </array>
        </dict>
    </array>

**Note: {Facebook_App_Id} and {Bundle_Identifier}, we will send private for you **

- Config for URL Types

.. code-block:: plist

    <key>CFBundleURLTypes</key>
        <array>
            <dict>
                <key>CFBundleTypeRole</key>
                <string>Editor</string>
                <key>CFBundleURLSchemes</key>
                <array>
                    <string>{GOOGLE_REVERSED_CLIENT_ID}</string>
                </array>
            </dict>
        </array>

**Note: {REVERSED_CLIENT_ID}, we will send private for you **

- Config file GoogleService-Info.plist
    - Drag and drop or import GoogleService-Info.plist to your project

**Note: File GoogleService-Info.plist we will send private for you **

- Config App Transport Security
.. code-block:: plist

    <key>NSAppTransportSecurity</key>
        <dict>
            <key>NSAllowsArbitraryLoads</key>
            <true/>
        </dict>

- Set up a NSUserTrackingUsageDescription to display a system-permission alert request for your app installed on end-user devices.
.. code-block:: plist

    <key>NSUserTrackingUsageDescription</key>
    <string>App would like to access IDFA for tracking purpose</string>
