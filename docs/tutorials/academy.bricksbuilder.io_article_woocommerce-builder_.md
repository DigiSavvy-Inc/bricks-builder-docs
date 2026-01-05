---
title: "WooCommerce Builder – Bricks Academy"
url: https://academy.bricksbuilder.io/article/woocommerce-builder/
date: 2026-01-05T11:09:31.565965
status: success
---

# WooCommerce Builder – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/woocommerce-builder/](https://academy.bricksbuilder.io/article/woocommerce-builder/)*

## Table of Contents

- [WooCommerce Builder](#woocommerce-builder)
  - [Getting Started](#getting-started)
  - [WooCommerce Templates](#woocommerce-templates)
  - [My Account builder](#my-account-builder)
  - [Shop page](#shop-page)
  - [WooCommerce elements](#woocommerce-elements)
  - [Dynamic Data](#dynamic-data)
  - [Bricks Settings: WooCommerce](#bricks-settings-woocommerce)
  - [Theme Styles](#theme-styles)
  - [WooCommerce Products Query Loop](#woocommerce-products-query-loop)
        - [Creating dynamic WooCommerce archive pages](#creating-dynamic-woocommerce-archive-pages)
        - [WooCommerce Account Builder](#woocommerce-account-builder)

## WooCommerce Builder

WooCommerce is a free plugin to manage the e-commerce functionality of your WordPress site. It is the world’s most popular open-source solution to create and manage a shop on the Internet, and therefore Bricks proudly integrates with it.

Bricks introduces the new in-theme WooCommerce Builder, which allows you to build your entire store with it. Including the main shop page, single product page, products archives, cart, checkout, and account pages.

To design these layouts, Bricks offers WooCommerce-specific elements and template types.

Certain elements only show when editing a specific template type.

TheCheckout customer detailselement, for example, is only available when editing theWooCommerce Checkouttemplate.

`Checkout customer details`

`WooCommerce Checkout`

### Getting Started

To access the WooCommerce Builder in Bricks, install and activate the free WooCommerce plugin available in the officialWordPress repositoryor through your WordPress dashboard underPlugins → Add New.

`Plugins → Add New`

After activation, you might want to set up the store using the in-site configuration wizard or do it manually through the WooCommerce settings menus.

Please note that during the configuration wizard, you won’t need to pick up a new theme because Bricks is already a theme and fully supports WooCommerce.

With the configuration done and after adding some products, you can start visually building your WooCommerce layouts with Bricks.

### WooCommerce Templates

With WooCommerce activated, you can visually create and style the following WooCommerce templates in Bricks:

### My Account builder

Starting at Bricks 1.9, you can also visually design your Account page. Including the login/registration, lost & reset password pages.

For more details, please refer to our dedicated Academy article about the new WooCommerce Account builder herehttps://academy.bricksbuilder.io/article/woocommerce-account-builder/

### Shop page

The shop page is a special WooCommerce page which is defined as the archive page for your products.

To design a unique Shop page layout, you can directly edit the Shop page with Bricks.

Or you could add a template condition in yourWooCommerce - Product Archivetemplate so this template is used for the Shop page as well. Since shop page is the archive for the product post type, just set it like this.

`WooCommerce - Product Archive`

### WooCommerce elements

Bricks aims to provide the most flexible approach to the visual design of the WooCommerce templates without losing the functionality & hooks WooCommerce already provides that many third-party WooCommerce plugins/extensions rely upon.

Among the general WooCommerce elements and Products element, Bricks has special elements for specific WooCommerce template types like the cart or the checkout.

More than 30 WooCommerce-specific elements in total are available to design your WooCommerce templates & pages with Bricks.

These are some of the WooCommerce-specific elements:

- Add to cart
- Product title
- Product gallery
- Product price
- Product stock
- Product meta
- Product rating
- Product reviews
- Product content
- Product short description
- Product additional information
- Product tabs
- Product up/cross-sells
- Related products

### Dynamic Data

The WooCommerce integration adds newdynamic data tagsto target product andorder properties.

`{woo_product_price}`

`{woo_product_regular_price}`

`{woo_product_sale_price}`

`{woo_product_regular_price:plain}`

`{woo_product_regular_price:value}`

`{woo_product_cat_image}`

`{woo_product_images}`

`:value`

`{woo_product_gallery_images}`

`:value`

`{woo_add_to_cart}`

`{woo_product_on_sale}`

`{woo_product_rating}`

`{woo_product_rating:plain}`

`{woo_product_rating:format}`

`{woo_product_sku}`

`{woo_product_excerpt}`

`{woo_product_stock}`

`{woo_product_stock_status}`

`{woo_product_badge_new}`

`.badge.new`

`{woo_product_badge_new:plain}`

You can use the basic dynamic tags as well.

`{post_id}`

`{post_title:link}`

`{post_terms_product_cat}`

`{post_terms_product_cat:plain}`

### Bricks Settings: WooCommerce

You’ll find a dedicated tab for the WooCommerce integration in your WordPress dashboard under “Bricks > Settings > WooCommerce”.

- Disable WooCommerce Builder– This toggle disables the Bricks’ WooCommerce integration.
- Product Badge “Sale”– Choose between not showing the on-sale badge, showing the “Sale” badge, or the discount percentage.
- Product Badge “New”– Show a “New” badge if the product was published in less than the .. days configured.
- Disable Product Gallery Zoom/Lightbox– Disable the product gallery zoom or lightbox scripts.

- AJAX add to cart Error action– Select either “Redirect to product page” or “Show notice” when an error occurs during the AJAX add to cart process. (@since 1.11)

### Theme Styles

When WooCommerce is active, you’ll find the following control groups in the Theme Styles panel:

- WooCommerce – Button
- WooCommerce – Notice

### WooCommerce Products Query Loop

You can use these checkboxes under WooCommerce section to easily retrieve WooCommerce products. Please select the “Products” post type; otherwise, the WooCommerce section will be hidden. (@since 1.10)Checkthis articlefor more examples.

`@since 1.10`

###### Creating dynamic WooCommerce archive pages

###### WooCommerce Account Builder

