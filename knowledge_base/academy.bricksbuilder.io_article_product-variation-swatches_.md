---
title: "Product Variation Swatches (WooCommerce) – Bricks Academy"
url: https://academy.bricksbuilder.io/article/product-variation-swatches/
date: 2025-08-13T09:55:53.083672
status: success
---

# Product Variation Swatches (WooCommerce) – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/product-variation-swatches/](https://academy.bricksbuilder.io/article/product-variation-swatches/)*

## Table of Contents

- [Product Variation Swatches (WooCommerce)](#product-variation-swatches-woocommerce)
  - [Enable product variation swatches](#enable-product-variation-swatches)
  - [Assign a swatch type to product attributes](#assign-a-swatch-type-to-product-attributes)
    - [Set a fallback value (optional)](#set-a-fallback-value-optional)
  - [Assign swatch values to individual terms](#assign-swatch-values-to-individual-terms)
  - [Style swatches in the Add to cart element](#style-swatches-in-the-add-to-cart-element)
        - [Element: Checkout Login](#element-checkout-login)

## Product Variation Swatches (WooCommerce)

Bricks 2.0 introducesProduct variation swatches, giving you more control over how product attribute options (i.e. color, size, pattern) appear on the frontend.

Instead of dropdowns, you can now display your product variations ascolor swatches, image buttons, or custom labels, creating a more visual and intuitive shopping experience.

This feature integrates directly into theAdd to cartelement, letting you style variation swatches exactly how you want, without the need for extra plugins.

### Enable product variation swatches

To get started, go toBricks > Settings > WooCommerce > Enable product variation swatches.

Once enabled, you’ll be able to customize variation swatches directly from your product attribute settings.

### Assign a swatch type to product attributes

Go toProducts > Attributes, and click “Edit” on an existing attribute (or create a new one).

You’ll see a newSwatch typesetting with the following options:

- None (default): Standard WooCommerce behavior (dropdowns)
- Color: Displays swatches using color values
- Label: Displays custom text labels for each term
- Image: Displays swatches using images from your media library

Example:Use the “Color” swatch type to show red and blue color boxes, or choose “Label” for size options like S, M, L.

#### Set a fallback value (optional)

While editing the attribute, you can also set aFallback value. This fallback will be used if a specific term doesn’t have its own swatch value.

### Assign swatch values to individual terms

Next, clickConfigure termsfor the attribute you just edited.

Then, clickEditon a specific term (like “Red” or “Large”).

For each term, you’ll see a new input that matches the swatch type:

- Color→ Choose a color
- Image→ Select or upload an image
- Label→ Add custom text

These values are what will be shown on the frontend in the Add to cart element.

### Style swatches in the Add to cart element

Variation swatches are rendered inside theAdd to cartelement, as long as your product uses attributes with a swatch type.

To style them:

1. Select theAdd to cartelement (e.g in your single product template)
2. Open the newVariation swatchesgroup in the element settings

From there, you can adjust the size, spacing, borders, active states, tooltips, and more.

That’s it. With variation swatches, you can now turn standard variation dropdowns into polished, interactive product selectors, designed your way, directly in the Bricks builder.

###### Element: Checkout Login

