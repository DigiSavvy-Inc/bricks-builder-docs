---
title: "Filter: bricks/body/attributes – Bricks Academy"
url: https://academy.bricksbuilder.io/article/filter-bricks-body-attributes/
date: 2025-02-27T15:28:04.661939
status: success
---

# Filter: bricks/body/attributes – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/filter-bricks-body-attributes/](https://academy.bricksbuilder.io/article/filter-bricks-body-attributes/)*

## Table of Contents

- [Filter: bricks/body/attributes](#filter-bricksbodyattributes)
        - [Filter: bricks/footer/attributes](#filter-bricksfooterattributes)
        - [Filter: bricks/comments/timestamp](#filter-brickscommentstimestamp)

## Filter: bricks/body/attributes

Filter to add HTML attributes to thebodytag (@since 1.5).

`body`

```
add_filter( 'bricks/body/attributes', function( $attributes ) {
  // Add 'data-is-body' HTML attribute to footer with value 'y'
  $attributes['data-is-body'] = 'y';

  return $attributes;
} );
```

`add_filter( 'bricks/body/attributes', function( $attributes ) {
  // Add 'data-is-body' HTML attribute to footer with value 'y'
  $attributes['data-is-body'] = 'y';

  return $attributes;
} );`

###### Filter: bricks/footer/attributes

###### Filter: bricks/comments/timestamp

