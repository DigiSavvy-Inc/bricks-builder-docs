---
title: "Filter: bricks/builder/i18n – Bricks Academy"
url: https://academy.bricksbuilder.io/article/filter-bricks-i18n/
date: 2025-02-27T15:36:03.199857
status: success
---

# Filter: bricks/builder/i18n – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/filter-bricks-i18n/](https://academy.bricksbuilder.io/article/filter-bricks-i18n/)*

## Table of Contents

- [Filter: bricks/builder/i18n](#filter-bricksbuilderi18n)
        - [Filter: bricks/builder/color_palette](#filter-bricksbuildercolorpalette)
        - [Filter: bricks/builder/map_styles](#filter-bricksbuildermapstyles)

## Filter: bricks/builder/i18n

Place and customize the following filter to add translatable string to the builder.

```
add_filter( 'bricks/builder/i18n', function( $i18n ) {
  // Example: Provide translatable string for element category 'custom'
  $i18n['custom'] = esc_html__( 'Custom', 'bricks' );

  return $i18n;
} );
```

###### Filter: bricks/builder/color_palette

###### Filter: bricks/builder/map_styles

