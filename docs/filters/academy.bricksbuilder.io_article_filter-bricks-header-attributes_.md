---
title: "Filter: bricks/header/attributes – Bricks Academy"
url: https://academy.bricksbuilder.io/article/filter-bricks-header-attributes/
date: 2026-01-05T11:07:59.224593
status: success
---

# Filter: bricks/header/attributes – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/filter-bricks-header-attributes/](https://academy.bricksbuilder.io/article/filter-bricks-header-attributes/)*

## Table of Contents

- [Filter: bricks/header/attributes](#filter-bricksheaderattributes)
        - [Filter: bricks/content/attributes](#filter-brickscontentattributes)
        - [Filter: bricks/footer/attributes](#filter-bricksfooterattributes)

## Filter: bricks/header/attributes

Programmatically add HTML attributes to theheadertag.

`header`

```
add_filter( 'bricks/header/attributes', function( $attributes ) {
  // Add custom class to header
  if ( isset( $attributes['class'] ) && is_array( $attributes['class'] ) ) { 
    $attributes['class'][] = 'my-header-class';
  } else {
    $attributes['class'] = ['my-header-class'];
  }

  // Add 'data-is-header' HTML attribute to header with value 'y'
  $attributes['data-is-header'] = 'y';

  return $attributes;
} );
```

`add_filter( 'bricks/header/attributes', function( $attributes ) {
  // Add custom class to header
  if ( isset( $attributes['class'] ) && is_array( $attributes['class'] ) ) { 
    $attributes['class'][] = 'my-header-class';
  } else {
    $attributes['class'] = ['my-header-class'];
  }

  // Add 'data-is-header' HTML attribute to header with value 'y'
  $attributes['data-is-header'] = 'y';

  return $attributes;
} );`

- https://academy.bricksbuilder.io/article/filter-bricks-content-attributes/
- https://academy.bricksbuilder.io/article/filter-bricks-footer-attributes/

###### Filter: bricks/content/attributes

###### Filter: bricks/footer/attributes

