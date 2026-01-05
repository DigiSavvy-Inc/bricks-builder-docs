---
title: "WooCommerce Template Hooks – Bricks Academy"
url: https://academy.bricksbuilder.io/article/woocommerce-template-hooks/
date: 2026-01-05T11:09:32.971817
status: success
---

# WooCommerce Template Hooks – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/woocommerce-template-hooks/](https://academy.bricksbuilder.io/article/woocommerce-template-hooks/)*

## Table of Contents

- [WooCommerce Template Hooks](#woocommerce-template-hooks)
      - [WooCommerce actions list removed by Bricks when using the do_action tag](#woocommerce-actions-list-removed-by-bricks-when-using-the-doaction-tag)
  - [WooCommerce Single Product Template Hooks](#woocommerce-single-product-template-hooks)
  - [WooCommerce Product Archive Template Hooks](#woocommerce-product-archive-template-hooks)
  - [WooCommerce Empty Cart Template Hooks](#woocommerce-empty-cart-template-hooks)
  - [WooCommerce Cart Template Hooks](#woocommerce-cart-template-hooks)
  - [WooCommerce Pay Template](#woocommerce-pay-template)
        - [WooCommerce Notices](#woocommerce-notices)
        - [Checkout (WooCommerce)](#checkout-woocommerce)

## WooCommerce Template Hooks

Bricks 1.7 introduces a newdo_actiondynamic tag, which is designed to address the majority of compatibility issues between Bricks and third-party WooCommerce plugins. This new dynamic tag not only solves these compatibility issues but also enhances the flexibility of design by allowing users to place hooks anywhere they desire.

`do_action`

This article will guide you through the templates that need to be updated with the newdo_actiondynamic tag, though this step is optional if your Bricks-built WooCommerce website is already functioning properly.

`do_action`

Please note that when using thedo_actiondynamic tag with the specified hooks, Bricks will automatically remove certain native WooCommerce actions to prevent duplicate content.

`do_action`

``

`woocommerce_template_loop_rating`

`woocommerce_template_loop_price`

##### WooCommerce actions list removed by Bricks when using the do_action tag

Simply use a Basic Text element when applying the{do_action:xxx}dynamic tag within your template.

`{do_action:xxx}`

### WooCommerce Single Product Template Hooks

For the WooCommerce Single Product template, the following hooks are recommended to be used with thedo_actiondynamic tag:

`do_action`

- {do_action:woocommerce_before_single_product}– Important (WooCommerce notice)
- {do_action:woocommerce_before_single_product_summary}
- {do_action:woocommerce_single_product_summary}– Important (Many third-party plugins using this hook to inject their code)
- {do_action:woocommerce_after_single_product_summary}
- {do_action:woocommerce_after_single_product}

`{do_action:woocommerce_before_single_product}`

`{do_action:woocommerce_before_single_product_summary}`

`{do_action:woocommerce_single_product_summary}`

`{do_action:woocommerce_after_single_product_summary}`

`{do_action:woocommerce_after_single_product}`

Best to place all of these in your single product template if you are not sure which hook will be using by the third-party plugins.

### WooCommerce Product Archive Template Hooks

For the WooCommerce Product Archive template, the following hooks are recommended to be used with thedo_actiondynamic tag:

`do_action`

- {do_action:woocommerce_archive_description}
- {do_action:woocommerce_before_shop_loop}– Important (WooCommerce notice)
- {do_action:woocommerce_before_shop_loop_item}
- {do_action:woocommerce_before_shop_loop_item_title}
- {do_action:woocommerce_shop_loop_item_title}
- {do_action:woocommerce_after_shop_loop_item_title}
- {do_action:woocommerce_after_shop_loop_item}
- {do_action:woocommerce_after_shop_loop}

`{do_action:woocommerce_archive_description}`

`{do_action:woocommerce_before_shop_loop}`

`{do_action:woocommerce_before_shop_loop_item}`

`{do_action:woocommerce_before_shop_loop_item_title}`

`{do_action:woocommerce_shop_loop_item_title}`

`{do_action:woocommerce_after_shop_loop_item_title}`

`{do_action:woocommerce_after_shop_loop_item}`

`{do_action:woocommerce_after_shop_loop}`

In Bricks 1.7, the dynamic tagdo_actionhooks will be automatically included in the fields of the Products element (for newly inserted Products elements only).

`do_action`

### WooCommerce Empty Cart Template Hooks

For the WooCommerce Empty Cart template, the following hook is recommended to be used with thedo_actiondynamic tag:

`do_action`

- {do_action:woocommerce_cart_is_empty}– Important (WooCommerce notice)

`{do_action:woocommerce_cart_is_empty}`

### WooCommerce Cart Template Hooks

For the WooCommerce Cart template, the following hooks are recommended to be used with thedo_actiondynamic tag:

`do_action`

- {do_action:woocommerce_before_cart}– Important (WooCommerce notice)
- {do_action:woocommerce_before_cart_collaterals}
- {do_action:woocommerce_after_cart}

`{do_action:woocommerce_before_cart}`

`{do_action:woocommerce_before_cart_collaterals}`

`{do_action:woocommerce_after_cart}`

### WooCommerce Pay Template

For the WooCommerce Pay template, the following hooks are recommended to be used with thedo_actiondynamic tag:

`do_action`

- {do_action:woocommerce_pay_order_before_payment}

`{do_action:woocommerce_pay_order_before_payment}`

By following this guide, you can ensure that the templates created in Bricks are fully compatible with WooCommerce and that all necessary actions and details are displayed as intended.

###### WooCommerce Notices

###### Checkout (WooCommerce)

