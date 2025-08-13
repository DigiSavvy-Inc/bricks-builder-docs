---
title: "Cascade layer – Bricks Academy"
url: https://academy.bricksbuilder.io/article/cascade-layer/
date: 2025-02-27T15:30:46.913555
status: success
---

# Cascade layer – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/cascade-layer/](https://academy.bricksbuilder.io/article/cascade-layer/)*

## Table of Contents

- [Cascade layer](#cascade-layer)
  - [How it works](#how-it-works)
    - [The problem: Selector specificity](#the-problem-selector-specificity)
    - [The solution: Cascade layers](#the-solution-cascade-layers)
    - [The role ofbricks.reset](#the-role-ofbricksreset)
  - [Why this matters](#why-this-matters)
  - [What does this mean for you](#what-does-this-mean-for-you)
  - [Resources](#resources)
        - [Components](#components)
        - [Global class import manager](#global-class-import-manager)

## Cascade layer

The specificity of default Bricks styles has always been a balancing act. While we aim to keep these styles as non-intrusive as possible, providing a blank canvas for users to build upon, achieving this solely through selector specificity has its limitations. In some cases, it’s been challenging for users to override specific selectors, even when desired.

Bricks 1.12 introduces a promising solution to this longstanding issue throughCSS cascade layers, which as of December 2024 reach an impressive 96% browser support and “Widely available” Baseline.

You can enable the new, experimentalWrap Bricks default styles in @layerfeature underBricks settings > Performance > Cascade layer.

`Wrap Bricks default styles in @layer`

When enabled, this feature leverages cascade layers to define how Bricks’ default styles interact with other styles on the page.

### How it works

This feature introducestwo cascade layers:

- bricks.reset(a lower-priority layer): This sublayer is empty, providing a safety net for advanced users. Bricks itself does not apply any styles in this layer.
- bricks: This layer contains all of Bricks’ default styles, making them easier to override using un-layered styles or styles in higher-priority user-defined layers.

`bricks.reset`

`bricks`

Here’s an example to illustrate the problem and the solution:

#### The problem: Selector specificity

In the default Bricks styles, a common pattern might look like this:

```
[class*="brxe-"] {
    max-width: 100%;
}
```

`[class*="brxe-"] {
    max-width: 100%;
}`

If you tried to override this with a general element selector, such as:

```
div {
    max-width: 400px;
}
```

`div {
    max-width: 400px;
}`

…the override wouldn’t work because the attribute selector[class*="brxe-"]has a higher specificity then thediv.

`[class*="brxe-"]`

`div`

One potential workaround could be wrapping Bricks’ attribute selectors in:where()to reduce specificity:

`:where()`

```
:where([class*="brxe-"]) {
    max-width: 100%;
}
```

`:where([class*="brxe-"]) {
    max-width: 100%;
}`

However, this approach would require wrapping every selector, which is not only complex but also impractical at scale.

#### The solution: Cascade layers

With cascade layers, we can simply define the default styles within a layer namedbricks.

`bricks`

Styles outside this layer (un-layered) or in a higher-priority layer automatically precede the default Bricks styles.

Here’s how the layers are structured:

```
@layer bricks.reset;

@layer bricks {
    [class*="brxe-"] {
        max-width: 100%;
    }
    /* Other default Bricks styles */
}
```

`@layer bricks.reset;

@layer bricks {
    [class*="brxe-"] {
        max-width: 100%;
    }
    /* Other default Bricks styles */
}`

Now, when you add your own styles outside thebrickslayer, like this:

`bricks`

```
div {
    max-width: 400px;
}
```

`div {
    max-width: 400px;
}`

…they will precede the default Bricks styles because un-layered styles and higher-priority layers take precedence, regardless of the selector.

#### The role ofbricks.reset

`bricks.reset`

Thebricks.resetsublayer ensures flexibility when overriding default Bricks styles.

`bricks.reset`

Normally, styles in thebrickslayer are easy to override, but if a default style uses!important, the cascade order flips, making it harder to override with un-layered styles or higher-priority layers. You can learn more about this behaviourhere.

`bricks`

`!important`

Thebricks.resetlayer, being lower priority, provides a fallback for safely defining custom styles in these rare cases. While we aim to avoid using!importantin our default styles unless absolutely required, this sublayer is there as a safeguard.

`bricks.reset`

`!important`

### Why this matters

By moving default Bricks styles into a dedicated cascade layer, we ensure:

1. Easier overrides: Un-layered or higher-priority layered styles can override the default Bricks styles without battling selector specificity.
2. Simplified maintenance: Instead of manually tweaking every selector’s specificity, cascade layers offer a clean, scalable solution.

This experimental feature reflects our commitment to modern web standards and making Bricks as intuitive and developer-friendly as possible.

### What does this mean for you

We encourage you to try this feature by enabling it on a staging clone of your website. This will help you check if it causes any issues with your custom styles. For those who have already experienced specificity challenges, this feature can also demonstrate how it makes overriding Bricks’ default styles easier and allows for cleaner custom CSS.

Our goal is to make this the default behavior for Bricks in the future, so your feedback is invaluable. Let us know how it works for you via email orthe forumto help us refine and improve this solution.

### Resources

- Kevin Powell’s YouTube video on cascade layers:A look at CSS Cascade Layers
- In-depth guide on CSS cascade layers:CSS-Tricks: Cascade Layers Guide

###### Components

###### Global class import manager

