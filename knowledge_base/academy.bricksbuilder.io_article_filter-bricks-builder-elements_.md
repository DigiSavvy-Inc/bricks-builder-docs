---
title: "Filter: bricks/builder/elements – Bricks Academy"
url: https://academy.bricksbuilder.io/article/filter-bricks-builder-elements/
date: 2025-02-27T15:29:07.153034
status: success
---

# Filter: bricks/builder/elements – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/filter-bricks-builder-elements/](https://academy.bricksbuilder.io/article/filter-bricks-builder-elements/)*

## Table of Contents

- [Filter: bricks/builder/elements](#filter-bricksbuilderelements)
        - [Filter: bricks/builder/standard_fonts](#filter-bricksbuilderstandardfonts)
        - [Filter: bricks/dynamic_data/post_terms_separator](#filter-bricksdynamicdataposttermsseparator)

## Filter: bricks/builder/elements

Determine which elements to use in Bricks by out-commenting the ones you don’t want to use. There is a full example and list of all elements in the Bricks child theme that you can customize to your requirements.

```
add_filter( 'bricks/builder/elements', function( $elements ) {
  // See Bricks child theme for a full list of all available elements
  // var_dump( $elements ); // To see all available elements

  return $elements;
} );
```

`add_filter( 'bricks/builder/elements', function( $elements ) {
  // See Bricks child theme for a full list of all available elements
  // var_dump( $elements ); // To see all available elements

  return $elements;
} );`

###### Filter: bricks/builder/standard_fonts

###### Filter: bricks/dynamic_data/post_terms_separator

