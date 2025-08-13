---
title: "Filter: bricks/content/attributes – Bricks Academy"
url: https://academy.bricksbuilder.io/article/filter-bricks-content-attributes/
date: 2025-02-27T15:29:51.602100
status: success
---

# Filter: bricks/content/attributes – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/filter-bricks-content-attributes/](https://academy.bricksbuilder.io/article/filter-bricks-content-attributes/)*

## Table of Contents

- [Filter: bricks/content/attributes](#filter-brickscontentattributes)
        - [Filter: bricks/is_layout_element](#filter-bricksislayoutelement)
        - [Filter: bricks/header/attributes](#filter-bricksheaderattributes)

## Filter: bricks/content/attributes

Programmatically add HTML attributes to themaintag.

`main`

```
add_filter( 'bricks/content/attributes', function( $attributes ) {
  // Add 'data-is-content' HTML attribute to main with value 'y'
  $attributes['data-is-content'] = 'y';
  return $attributes;
} );
```

`add_filter( 'bricks/content/attributes', function( $attributes ) {
  // Add 'data-is-content' HTML attribute to main with value 'y'
  $attributes['data-is-content'] = 'y';
  return $attributes;
} );`

- https://academy.bricksbuilder.io/article/filter-bricks-header-attributes/
- https://academy.bricksbuilder.io/article/filter-bricks-header-attributes/

###### Filter: bricks/is_layout_element

###### Filter: bricks/header/attributes

