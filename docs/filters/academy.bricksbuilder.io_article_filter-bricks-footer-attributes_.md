---
title: "Filter: bricks/footer/attributes – Bricks Academy"
url: https://academy.bricksbuilder.io/article/filter-bricks-footer-attributes/
date: 2025-05-01T12:02:56.164701
status: success
---

# Filter: bricks/footer/attributes – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/filter-bricks-footer-attributes/](https://academy.bricksbuilder.io/article/filter-bricks-footer-attributes/)*

## Table of Contents

- [Filter: bricks/footer/attributes](#filter-bricksfooterattributes)
        - [Filter: bricks/header/attributes](#filter-bricksheaderattributes)
        - [Filter: bricks/body/attributes](#filter-bricksbodyattributes)

## Filter: bricks/footer/attributes

Programmatically add HTML attributes to thefootertag.

`footer`

```
add_filter( 'bricks/footer/attributes', function( $attributes ) {
  // Add 'data-is-footer' HTML attribute to footer with value 'y'
  $attributes['data-is-footer'] = 'y';

  return $attributes;
} );
```

`add_filter( 'bricks/footer/attributes', function( $attributes ) {
  // Add 'data-is-footer' HTML attribute to footer with value 'y'
  $attributes['data-is-footer'] = 'y';

  return $attributes;
} );`

- https://academy.bricksbuilder.io/article/filter-bricks-header-attributes/
- https://academy.bricksbuilder.io/article/filter-bricks-content-attributes/

###### Filter: bricks/header/attributes

###### Filter: bricks/body/attributes

