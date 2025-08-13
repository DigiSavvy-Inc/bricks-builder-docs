---
title: "How to get your Instagram Access Token – Bricks Academy"
url: https://academy.bricksbuilder.io/article/instagram-access-token/
date: 2025-02-27T15:31:53.209139
status: success
---

# How to get your Instagram Access Token – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/instagram-access-token/](https://academy.bricksbuilder.io/article/instagram-access-token/)*

## Table of Contents

- [How to get your Instagram Access Token](#how-to-get-your-instagram-access-token)
  - [Step 1: Ensure you have an Instagram Creator or Business account](#step-1-ensure-you-have-an-instagram-creator-or-business-account)
  - [Step 2: Set up an application](#step-2-set-up-an-application)
  - [Step 3: Add the Instagram product to your app](#step-3-add-the-instagram-product-to-your-app)
  - [Step 4: Generate your Instagram access token](#step-4-generate-your-instagram-access-token)
  - [Step 5: Add the access token to Bricks](#step-5-add-the-access-token-to-bricks)
        - [How to use Polylang with Bricks](#how-to-use-polylang-with-bricks)
        - [How to use WPML with Bricks](#how-to-use-wpml-with-bricks)

## How to get your Instagram Access Token

To use the Instagram Feed element (@since 1.9.1), you need an access token. This token allows secure retrieval of your Instagram account data. This guide explains how to get the token using the Instagram API with Instagram Login.

Before you can publish your app and generate an access token, you must connect your app to aBusiness that has completed Business Verification. Follow Meta’sBusiness Verification guidefor instructions.

### Step 1: Ensure you have an Instagram Creator or Business account

Before proceeding, make sure your Instagram account is either aCreatororBusinessaccount.

1. Log in to your Instagram account.
2. Convert your account by following these instructions:Set up a Creator Account.Convert to a Business Account.
3. Set up a Creator Account.
4. Convert to a Business Account.

- Set up a Creator Account.
- Convert to a Business Account.

### Step 2: Set up an application

You first have to set up an application on the Meta for Developers platform by following these steps:

1. Access yourMeta for Developers platform. You can use an existing account orcreate a new one.
2. ClickCreate App. A dialog window will appear, asking you to define your app’s functionalities:SelectOtheras the use case and clickNext.SelectBusinessas the app type to set the app permissions and clickNext.
3. SelectOtheras the use case and clickNext.
4. SelectBusinessas the app type to set the app permissions and clickNext.
5. Provide anApp NameandContact Email.
6. ClickNextto complete the setup.

- SelectOtheras the use case and clickNext.
- SelectBusinessas the app type to set the app permissions and clickNext.

You will be redirected to the app dashboard for your new app with products you can add to your app.

### Step 3: Add the Instagram product to your app

1. On the app dashboard, scroll down toProductsand locateInstagram.
2. ClickSet Upnext to Instagram.
3. SelectAPI Setup with Instagram Login(NOT API Setup with Facebook Login).

### Step 4: Generate your Instagram access token

To retrieve an access token:

1. Assign an Instagram account for token generation:In the App Dashboard, go toInstagram > API Setup with Instagram Login.ClickAdd an Instagram Account.Log in with your Instagram Creator or Business account credentials.
2. In the App Dashboard, go toInstagram > API Setup with Instagram Login.
3. ClickAdd an Instagram Account.
4. Log in with your Instagram Creator or Business account credentials.

- In the App Dashboard, go toInstagram > API Setup with Instagram Login.
- ClickAdd an Instagram Account.
- Log in with your Instagram Creator or Business account credentials.

1. Confirm the account connection:Your Instagram account must be public.If you manage multiple accounts, ensure the correct one is selected.
2. Your Instagram account must be public.
3. If you manage multiple accounts, ensure the correct one is selected.
4. Copy the generated access token tied to the assigned Instagram account.

- Your Instagram account must be public.
- If you manage multiple accounts, ensure the correct one is selected.

### Step 5: Add the access token to Bricks

To finalize the setup, navigate toBricks settings > API keysfrom your WordPress dashboard and paste the access token into theInstagram Access Tokeninput field, and save your changes.

`Bricks settings > API keys`

`Instagram Access Token`

For more information, refer to Meta’s official documentation:Create a Meta App for Instagram Platform.

Note:Once you retrieve and add the access token, Bricks will automatically refresh it every20 daysusing thebricks_refresh_instagram_access_tokenCRON job. No manual updates are required.

`bricks_refresh_instagram_access_token`

###### How to use Polylang with Bricks

###### How to use WPML with Bricks

