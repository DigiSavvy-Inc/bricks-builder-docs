---
title: "Filter: bricks/builder/color_palette – Bricks Academy"
url: https://academy.bricksbuilder.io/article/filter-color-palette/
date: 2025-02-27T15:29:44.275978
status: success
---

# Filter: bricks/builder/color_palette – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/filter-color-palette/](https://academy.bricksbuilder.io/article/filter-color-palette/)*

## Table of Contents

- [Filter: bricks/builder/color_palette](#filter-bricksbuildercolorpalette)
        - [Filter: bricks/builder/i18n](#filter-bricksbuilderi18n)

## Filter: bricks/builder/color_palette

Place and customize the following filter to display a different default color palette for the color control.

```
add_filter( 'bricks/builder/color_palette', function( $colors ) {
  // Option #1: Add an individual color
    $colors[] = [
      'hex' => '#3ce77b',
      'rgb' => 'rgba(60, 231, 123, 0.56)',
    ];

  // Option #2: Override entire color palette
  $colors = [
    ['hex' => '#3ce77b'],
    ['hex' => '#f1faee'],
    ['hex' => '#a8dadc'],
    ['hex' => '#457b9d'],
    ['hex' => '#1d3557'],
  ];

  return $colors;
} );
```

###### Filter: bricks/builder/i18n

