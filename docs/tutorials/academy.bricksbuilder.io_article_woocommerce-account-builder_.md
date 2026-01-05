---
title: "WooCommerce Account Builder – Bricks Academy"
url: https://academy.bricksbuilder.io/article/woocommerce-account-builder/
date: 2026-01-05T11:09:30.210126
status: success
---

# WooCommerce Account Builder – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/woocommerce-account-builder/](https://academy.bricksbuilder.io/article/woocommerce-account-builder/)*

## Table of Contents

- [WooCommerce Account Builder](#woocommerce-account-builder)
  - [My Account Page (logged in)](#my-account-page-logged-in)
  - [Account – Login / Register](#account--login--register)
  - [Account – Lost / reset password](#account--lost--reset-password)
  - [Templates for specific account endpoints](#templates-for-specific-account-endpoints)
  - [Account template types & elements](#account-template-types--elements)
        - [WooCommerce Builder](#woocommerce-builder)
        - [Element: Checkout Coupon](#element-checkout-coupon)

## WooCommerce Account Builder

Bricks 1.9 introduces the My Account builder, which lets you customize the account area of your WooCommerce site.

This includes the My Account page (logged-in), the account login/register/lost & reset password pages (shown when not logged-in), and all My Account endpoints (e.g., Orders, Downloads, etc.).

IMPORTANT:In order to ensure that all your customizations to the WooCommerce My Account templates are properly applied, it is imperative that you complete the “My Account Page (logged in)” step.

### My Account Page (logged in)

To design your My Account page (navigation + content wrapper),please edit your “My Account” page directly. You’ll find a dedicated “Account Page” element that you can add and adjust its settings to your liking.

IMPORTANT:If you have the“Enable Bricks WooCommerce “Notice” element”Bricks setting enabled, please make sure that you have added the “Notice” element to your account page or to all account templates individually. So the notifications when submitting the account forms (e.g., address, reset password, etc.) are displayed.

### Account – Login / Register

The login form is displayed when a not-logged-in visitor views the My Account page. And the registration form, if you have the“Allow customers to create an account on the “My account” page”WooCommerce setting enabled.

You can design your account login/registration layout by creating a new template type “WooCommerce – Account – Login”.

When editing this template, you’ll find dedicated elements for the“Account – Login form”&“Account – Register form”as shown in the screenshot below:

You should also check theAccount creationsettings located atWooCommerce > Settings > Accounts & Privacysection to control what form to be displayed viaAccount – Register formelement.

IMPORTANT:Ensure you have inserted a Basic Text element with{do_action:woocommerce_before_customer_login_form}before your Login and Register form. And another Basic Text element with{do_action:woocommerce_after_customer_login_form}after the forms.

`{do_action:woocommerce_before_customer_login_form}`

`{do_action:woocommerce_after_customer_login_form}`

### Account – Lost / reset password

The WooCommerce account builder in Bricks also provides the following dedicated templates and elements for the lost & reset password pages:

### Templates for specific account endpoints

Designing the account content area for individual account endpoints (Orders, Downloads, etc.) is possible by creating templates of the corresponding template type.

In the example below, we created a “WooCommerce – Account – Orders” template, to which we then added the “Account – Orders” that we styled a bit.

When editing the template for an account endpoint (Orders, Downloads, etc.), the drag & drop area is located inside the account content area. Offering a better preview in the builder than just rendering an empty canvas without the account navigation.

The process of creating those account endpoint templates is the same for all other WooCommerce account template types.

### Account template types & elements

`/`

`orders/`

`orders/view-order/{order_id}/`

`downloads`

`edit-address/`

`edit-address/billing/`

`edit-address/shipping/`

`edit-account/`

###### WooCommerce Builder

###### Element: Checkout Coupon

