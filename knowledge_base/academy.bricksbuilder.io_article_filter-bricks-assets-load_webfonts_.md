---
title: "Filter: bricks/assets/load_webfonts – Bricks Academy"
url: https://academy.bricksbuilder.io/article/filter-bricks-assets-load_webfonts/
date: 2025-02-27T15:28:53.843790
status: success
---

# Filter: bricks/assets/load_webfonts – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/filter-bricks-assets-load_webfonts/](https://academy.bricksbuilder.io/article/filter-bricks-assets-load_webfonts/)*

## Table of Contents

- [Filter: bricks/assets/load_webfonts](#filter-bricksassetsloadwebfonts)
        - [Filter: bricks/code/disallow_keywords](#filter-brickscodedisallowkeywords)
        - [Filter: bricks/setup/control_options](#filter-brickssetupcontroloptions)

## Filter: bricks/assets/load_webfonts

Bricks 1.4 introduces the possibility to “Disable Google Fonts”. Either via the Bricks settings under “Performance” or programmatically using the filter as explained below:

With the filterbricks/assets/load_webfontsyou’ll be able to prevent Google Fonts to load in the frontend by returningfalse:

`bricks/assets/load_webfonts`

`false`

```
// Prevent Google Fonts loading
add_filter( 'bricks/assets/load_webfonts', '__return_false' );
```

`// Prevent Google Fonts loading
add_filter( 'bricks/assets/load_webfonts', '__return_false' );`

If you use this filter to remove the embed of Google Fonts but you still like to use Google Fonts, just head to theGoogle Fonts websiteand download the fonts you need. Then, add them manually to your website, using theCustom Fontsscreen.

###### Filter: bricks/code/disallow_keywords

###### Filter: bricks/setup/control_options

