---
title: "Contextual Spacing – Bricks Academy"
url: https://academy.bricksbuilder.io/article/contextual-spacing/
date: 2026-01-05T11:09:11.044506
status: success
---

# Contextual Spacing – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/contextual-spacing/](https://academy.bricksbuilder.io/article/contextual-spacing/)*

## Table of Contents

- [Contextual Spacing](#contextual-spacing)
  - [How to use contextual spacing](#how-to-use-contextual-spacing)
  - [Settings overview](#settings-overview)
  - [Additional target elements](#additional-target-elements)
  - [Apply to more content areas](#apply-to-more-content-areas)
    - [Why not apply spacing to all headings and paragraphs by default?](#why-not-apply-spacing-to-all-headings-and-paragraphs-by-default)
  - [Example use case 1: Embedded post content](#example-use-case-1-embedded-post-content)
  - [Example use case 2: Mixed content layout](#example-use-case-2-mixed-content-layout)
        - [Bricks CSS: Compatibility guidelines](#bricks-css-compatibility-guidelines)
        - [Font Manager](#font-manager)

## Contextual Spacing

Bricks 2.0 introducesContextual spacingto give you full control over vertical spacing (margin) between elements like headings, paragraphs, and lists within embedded content.

Contextual spacing automatically applies to elements within:

- Rich text element
- Post content element (source: WordPress)
- WooCommerce embedded content (excluding Checkout)

Out-of-the-box, Bricks tries to apply various top margins (margin-block-start) to elements like headings and paragraphs depending on their context.

`margin-block-start`

If you want to override these defaults, you had to manually remove browser spacing, undo Bricks’ built-in styles, and then define your own margins.

Contextual spacing simplifies this process. You can now reset easily reset those margins and visually define custom spacing rules underTheme Styles→Contextual Spacing.

Whether you are styling embedded content, working with dynamic layouts, or creating utility-based wrappers, this feature gives you consistent and flexible control over spacing.

### How to use contextual spacing

You can enable Contextual spacing inside the builder underSettings → Theme Styles → Contextual Spacing.

Remove default margins: Lets you select the HTML tags from which you want to remove the default margins (i.e. Heading, Paragraph, Lists, etc.). This creates a clean starting point for spacing that fits your layout needs, without interference from inherited or default styles

Contextual spacing:Only applies margins when an element is preceded by another. This prevents extra spacing at the very top while maintaining consistent spacing between elements.

### Settings overview

`h1`

`h6`

`p`

`ul`

`blockquote`

`.contextual-spacing`

### Additional target elements

Use theAdditional target elementsrepeater to extend Contextual spacing to more than headings and paragraphs.

You can choose from predefined elements:

- Unordered list (ul)
- Ordered list (ol)
- List item (li)
- Figure (figure)
- Blockquote (blockquote)

Or enter your own custom selectors like.my-class,code, ordiv.

`.my-class`

`code`

`div`

For each, you can set:

- Top and bottom margin (margin-block)
- Start and end padding (padding-inline)

`margin-block`

`padding-inline`

This gives you spacing consistency across all types of content.

### Apply to more content areas

By default, Contextual spacing only targets Rich Text, Post Content, and WooCommerce content. But you can easily extend it by definingAdditional selectorsto apply Contextual spacing to any wrapper of your choice, such as.contextual-spacing, .brxe-shortcode.

`.contextual-spacing, .brxe-shortcode`

Add these utility classes to wrappers (i.e. Container, Div, Block elements) that hold a mix of content elements, and Bricks will apply your Contextual spacing settings to them.

#### Why not apply spacing to all headings and paragraphs by default?

In most Bricks layouts, especially when usingHeadingandBasic textelements in combination with other elements, spacing is typically handled using thegapproperty between containers.

Because of that, applying a single spacing rule to all headings and paragraphs wouldn’t make sense in every context.

Contextual spacing gives you the flexibility to apply spacing only where it’s needed, using selectors and utility classes.

### Example use case 1: Embedded post content

You’re building a single post template using aPost Contentelement (source: WordPress).Before enabling Contextual spacing, the post displays the default spacing added by Bricks.

WhenRemove default marginsis enabled, Bricks removes both its own default spacing and the browser’s default margins. You can then define your own spacing values using the Contextual spacing controls.

When you enableRemove default margins, then set spacing values. For example:

- Heading:2rem
- Paragraph:1.25rem
- Fallback:1rem

`2rem`

`1.25rem`

`1rem`

Bricks then applies spacing only between elements where needed. The first element inside the post has no margin above it, but elements that follow each other are spaced consistently.

Result:Clean layout, no spacing at the top, full control over vertical rhythm.

### Example use case 2: Mixed content layout

You’ve created a custom template that includes a container with the following elements:

- AHeadingelement
- ABasic textelement (with aptag)
- AnImageelement (with afiguretag)
- APost Contentelement (source: WordPress)

`p`

`figure`

Because these use different systems for spacing, the result may feel inconsistent.

To unify the layout:

1. Under Theme Styles > Contextual Spacing > EnableRemove default margins
2. Set spacing values. For example:Heading:2remParagraph:1.25remFallback:1rem
3. Heading:2rem
4. Paragraph:1.25rem
5. Fallback:1rem
6. Add a global class like.contextual-spacingto the container
7. Enter.contextual-spacingunderAdditional selectors

- Heading:2rem
- Paragraph:1.25rem
- Fallback:1rem

`2rem`

`1.25rem`

`1rem`

`.contextual-spacing`

`.contextual-spacing`

Result: All elements within that wrapper now follow your contextual spacing rules.

###### Bricks CSS: Compatibility guidelines

###### Font Manager

