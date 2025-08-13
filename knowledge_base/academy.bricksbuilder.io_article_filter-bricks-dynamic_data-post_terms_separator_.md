---
title: "Filter: bricks/dynamic_data/post_terms_separator – Bricks Academy"
url: https://academy.bricksbuilder.io/article/filter-bricks-dynamic_data-post_terms_separator/
date: 2025-02-27T15:29:58.866459
status: success
---

# Filter: bricks/dynamic_data/post_terms_separator – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/filter-bricks-dynamic_data-post_terms_separator/](https://academy.bricksbuilder.io/article/filter-bricks-dynamic_data-post_terms_separator/)*

## Table of Contents

- [Filter: bricks/dynamic_data/post_terms_separator](#filter-bricksdynamicdataposttermsseparator)
        - [Filter: bricks/builder/elements](#filter-bricksbuilderelements)
        - [Filter: bricks/elements/{element_name}/controls](#filter-brickselementselementnamecontrols)

## Filter: bricks/dynamic_data/post_terms_separator

Programmatically set the post term separator like so:

```
add_filter( 'bricks/dynamic_data/post_terms_separator', function( $sep, $post, $taxonomy ) {
  return ' : ';
}, 10, 3 );
```

`add_filter( 'bricks/dynamic_data/post_terms_separator', function( $sep, $post, $taxonomy ) {
  return ' : ';
}, 10, 3 );`

###### Filter: bricks/builder/elements

###### Filter: bricks/elements/{element_name}/controls

