Installation
=======================================================

Step by step
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Drag and drop or import SDKConfig.plist to your project we will send private for you **
        
- Drag and drop or import OEGFramework.framework to your project. Download SDK: https://github.com/que-cera/oeg-ios-sdk/blob/develop/OEGFramework/SDK.zip

- Drag and drop or import folder Fonts to your project. Download fonts: https://github.com/que-cera/oeg-ios-sdk/blob/develop/Fonts.zip

- General tab ()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    Scroll to "Frameworks, Libraries, and Embedded Content" -> choose OEGFramework.framework -> Embed -> Embed & Sign

- Build Settings
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    Add value for “Other Linker Flags”: -all_load -ObjC -lc++
    -> Change value for “Allow Non-modular Includes in Framework Modules”: Yes

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

- Set up fonts.

.. code-block:: Objective-C

    <key>UIAppFonts</key>
	<array>
		<string>Inter-Black.ttf</string>
		<string>Inter-Bold.ttf</->
		<string>Inter-ExtraBold.ttf</string>
		<string>Inter-Light.ttf</string>
		<string>Inter-Medium.ttf</string>
		<string>Inter-Regular.ttf</string>
		<string>Inter-SemiBold.ttf</string>
		<string>Inter-Thin.ttf</string>
	</array>

- Import the OEGFramework to App Delegate

.. code-block:: Objective-C

        @import OEGFramework;

- In your AppDelegate.m at didFinishLaunchingWithOptions function call this line

.. code-block:: Objective-C
    
        [OEGManager handleDidFinishLaunchingWithOptions:launchOptions];
        // If you want to control Firebase push message you can add below code
        [[FirebaseService sharedManager] messagingDelegate:self];
        
- In your AppDelegate.m handle application action

.. code-block:: Objective-C
            
        - (void)applicationWillResignActive:(UIApplication *)application {
            [OEGManager handleWillResignActive];
        }
        
        - (void)applicationDidEnterBackground:(UIApplication *)application {
            [OEGManager handleDidEnterBackground];
        }
        
        - (void)applicationWillEnterForeground:(UIApplication *)application {
            [OEGManager handleWillEnterForeground];
        }
        
        - (void)applicationDidBecomeActive:(UIApplication *)application {
            [OEGManager handleDidBecomeActive];
        }
        
        - (void)applicationWillTerminate:(UIApplication *)application {
            [OEGManager handleWillTerminate];
        }
        
        - (void)application:(UIApplication *)application didRegisterForRemoteNotificationsWithDeviceToken:(NSData *)deviceToken {
            [OEGManager handleDidRegisterForRemoteNotificationsWithDeviceToken:deviceToken];
        }
        
        - (BOOL)application:(UIApplication *)app openURL:(NSURL *)url options:(NSDictionary<UIApplicationOpenURLOptionsKey,id> *)options {
            return [OEGManager handleOpenURL:url options:options];
        }
        
- Download SDK: https://github.com/que-cera/oeg-ios-sdk/blob/develop/OEGFramework/SDK.zip

- Download Sample: https://github.com/que-cera/oeg-ios-sdk/blob/develop/TestSDK.zip

- Download fonts: https://github.com/que-cera/oeg-ios-sdk/blob/develop/Fonts.zip

- Cài bản build OEG Demo SDK Horizontal: https://dply.me/vnc3nq

- Cài bản build OEG Demo SDK Vertical: https://dply.me/l0p6a5