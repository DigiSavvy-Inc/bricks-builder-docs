---
title: "Checkout (WooCommerce) – Bricks Academy"
url: https://academy.bricksbuilder.io/article/checkout/
date: 2026-01-05T11:09:28.121121
status: success
---

# Checkout (WooCommerce) – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/checkout/](https://academy.bricksbuilder.io/article/checkout/)*

## Table of Contents

- [Checkout (WooCommerce)](#checkout-woocommerce)
  - [Checkout template](#checkout-template)
    - [Checkout customer details](#checkout-customer-details)
    - [Checkout order review](#checkout-order-review)
    - [Remove the checkout coupon form](#remove-the-checkout-coupon-form)
    - [Checkout Coupon & Checkout Login elements](#checkout-coupon--checkout-login-elements)
  - [Thank youtemplate](#thank-youtemplate)
  - [Pay template](#pay-template)
  - [Order receipt](#order-receipt)
        - [WooCommerce Template Hooks](#woocommerce-template-hooks)
        - [Cart (WooCommerce)](#cart-woocommerce)

## Checkout (WooCommerce)

The checkout page is a special WooCommerce page, created by default during WooCommerce installation. It contains WooCommerce Checkout gutenberg blocks. Please remove all gutenberg blocks and use[woocommerce_checkout]instead.

`[woocommerce_checkout]`

Remove the Gutenberg Checkout block if it is located within your Checkout Page. Instead, replace it with [woocommerce_checkout] or utilize the Shortcode element if you have edited the Checkout page with Bricks.

Bricks is only supporting[woocommerce_checkout]shortcode. You can either place the[woocommerce_checkout]shortcode directly in the Checkout page, or edit the Checkout page with Bricks, then use Shortcode element and set the content as[woocommerce_checkout]. Bricks offers four different template types (in this context, they are like template parts) to customize the checkout workflow:

`[woocommerce_checkout]`

`[woocommerce_checkout]`

`[woocommerce_checkout]`

- WooCommerce – Checkout
- WooCommerce – Thank you
- WooCommerce – Pay
- WooCommerce – Order receipt

The “WooCommerce – Checkout”, “WooCommerce – Pay”, “WooCommerce – Thank you”, and “WooCommerce – Order receipt” template types are only visible if you have the WooCommerce plugin installed and active. These templates are used inside the WooCommerce checkout shortcode logic andthey do not support template conditions (they are automatically rendered on the correct page).

### Checkout template

The default checkout page consists of a two-columns layout: one column with the billing and shipping details form and another one with the order summary + a button to proceed with the order.

Use theWooCommerce – Checkouttemplate type to change the appearance of this first checkout screen.

When editing this template with Bricks you’ll see two new elements (specific to this template type):

#### Checkout customer details

The checkout customer details element renders the billing and shipping details form.

You’ll be able to remove/hide some of the non-required fields (e.g. Company name) and style the form fields.

#### Checkout order review

The checkout order review element renders the order summary, the available payment methods, and the button to place the order. Using this element, you’ll be able to style its different parts.

#### Remove the checkout coupon form

If you have enabled the use of coupons in the WooCommerce general settings you’ll notice a blue coupon form on the top of the checkout form page. If you want to remove this form from the checkout page you may hide it using custom CSS or adding the following code to your child theme:

```
remove_action( 'woocommerce_before_checkout_form', 'woocommerce_checkout_coupon_form', 10 );
```

`remove_action( 'woocommerce_before_checkout_form', 'woocommerce_checkout_coupon_form', 10 );`

#### Checkout Coupon & Checkout Login elements

Starting at version 1.11.1 you have greater control over the location and design of the checkout coupon & login by enabling and using the following two checkout elements:

- Checkout Coupon element
- Checkout Login element

### Thank youtemplate

After placing an order, and depending on the payment workflow, you’ll get to the “Thank you” screen.

To style this screen, you’d create a Bricks template of typeWooCommerce – Thank you. And insert theCheckout Thank Youelement to customize the thank you message, and modify the styles of the different components of the order details.

### Pay template

For the situation where the visitor gets a link to pay for an unpaid order, there’s a special checkout screen that contains the order summary, the available payment gateways, and the button to pay for the order.

If you would like to customize this screen you’d need to add aWooCommerce – Paytemplate type where you’ll have access to two new elements: theCheckout order tableand theCheckout order paymentboth with style controls to customize the look and feel.

### Order receipt

For the situation where the visitor gets a link to the unpaid order receipt, the checkout workflow triggers thecheckout/order-receipt.phptemplate, which by default will look like this:

`checkout/order-receipt.php`

If you would like to customize this template you could add the BricksWooCommerce – Order receipttemplate type and inside the builder, you’ll have access to the order-specific Dynamic Data tags such as:

`{woo_order_id}`

`{woo_order_number}`

`{woo_order_date}`

`{woo_order_total}`

`{woo_order_payment_title}`

`{woo_order_email}`

NOTE:These Dynamic Data tags will also work inside theWooCommerce – Thank youtemplate type.

###### WooCommerce Template Hooks

###### Cart (WooCommerce)

