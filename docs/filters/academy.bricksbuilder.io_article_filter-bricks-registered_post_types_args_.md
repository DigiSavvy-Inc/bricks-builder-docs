---
title: "Filter: bricks/registered_post_types_args – Bricks Academy"
url: https://academy.bricksbuilder.io/article/filter-bricks-registered_post_types_args/
date: 2025-05-01T12:03:16.897195
status: success
---

# Filter: bricks/registered_post_types_args – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/filter-bricks-registered_post_types_args/](https://academy.bricksbuilder.io/article/filter-bricks-registered_post_types_args/)*

## Table of Contents

- [Filter: bricks/registered_post_types_args](#filter-bricksregisteredposttypesargs)
        - [Filter: bricks/screen_conditions/scores](#filter-bricksscreenconditionsscores)
        - [Filter: bricks/content/html_after_begin](#filter-brickscontenthtmlafterbegin)

## Filter: bricks/registered_post_types_args

Available since version 1.6, this filter allows you to customise the post type args that are used to query the post type as shown in the Bricks settings & the builder (e.g. Query control post types, etc.)

```
add_filter( 'bricks/registered_post_types_args', function( $args ) {
  // Default: Return only public post types
  // $args['public'] = true;

  // Custom: Return all registered post types
  unset( $args['public'] );

  // Available arguments: https://developer.wordpress.org/reference/functions/get_post_types/#comment-2184
  return $args;
} );
```

`add_filter( 'bricks/registered_post_types_args', function( $args ) {
  // Default: Return only public post types
  // $args['public'] = true;

  // Custom: Return all registered post types
  unset( $args['public'] );

  // Available arguments: https://developer.wordpress.org/reference/functions/get_post_types/#comment-2184
  return $args;
} );`

###### Filter: bricks/screen_conditions/scores

###### Filter: bricks/content/html_after_begin

