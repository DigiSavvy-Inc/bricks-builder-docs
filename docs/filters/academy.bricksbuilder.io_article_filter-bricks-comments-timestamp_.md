---
title: "Filter: bricks/comments/timestamp – Bricks Academy"
url: https://academy.bricksbuilder.io/article/filter-bricks-comments-timestamp/
date: 2026-01-05T11:07:39.816229
status: success
---

# Filter: bricks/comments/timestamp – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/filter-bricks-comments-timestamp/](https://academy.bricksbuilder.io/article/filter-bricks-comments-timestamp/)*

## Table of Contents

- [Filter: bricks/comments/timestamp](#filter-brickscommentstimestamp)
        - [Filter: bricks/body/attributes](#filter-bricksbodyattributes)
        - [Filter: builder/settings/{type}/controls_data](#filter-buildersettingstypecontrolsdata)

## Filter: bricks/comments/timestamp

When using the Bricks Post Comments element, the comment default timestamp text will show the time difference since it was published in a human-readable format such as “1 hour ago” or “2 days ago”.

Since Bricks 1.5.1, you’ll be able to customize the comment timestamp text, like so:

```
add_filter( 'bricks/comments/timestamp', function( $timestamp, $comment ) {
  // Return the WordPress default comment timestamp
  return sprintf( __( '%1$s at %2$s' ),
    get_comment_date( '', $comment ),
    get_comment_time()
  );
}, 10, 2 );
```

`add_filter( 'bricks/comments/timestamp', function( $timestamp, $comment ) {
  // Return the WordPress default comment timestamp
  return sprintf( __( '%1$s at %2$s' ),
    get_comment_date( '', $comment ),
    get_comment_time()
  );
}, 10, 2 );`

###### Filter: bricks/body/attributes

###### Filter: builder/settings/{type}/controls_data

