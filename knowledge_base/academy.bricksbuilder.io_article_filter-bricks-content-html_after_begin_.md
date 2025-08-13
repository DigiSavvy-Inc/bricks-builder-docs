---
title: "Filter: bricks/content/html_after_begin – Bricks Academy"
url: https://academy.bricksbuilder.io/article/filter-bricks-content-html_after_begin/
date: 2025-02-27T15:29:56.483388
status: success
---

# Filter: bricks/content/html_after_begin – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/filter-bricks-content-html_after_begin/](https://academy.bricksbuilder.io/article/filter-bricks-content-html_after_begin/)*

## Table of Contents

- [Filter: bricks/content/html_after_begin](#filter-brickscontenthtmlafterbegin)
        - [Filter: bricks/registered_post_types_args](#filter-bricksregisteredposttypesargs)
        - [Filter: bricks/content/html_before_end](#filter-brickscontenthtmlbeforeend)

## Filter: bricks/content/html_after_begin

Available since version 1.6, this filter allows you to customize or insert HTML strings aftermaintag, before rendering bricks data.

`main`

```
add_filter( 'bricks/content/html_after_begin', function( $html_after_begin, $bricks_data, $attributes, $tag ) {

    if ( $tag !== 'main' ) {
      return $html_after_begin;
    }
    
    // Insert custom div after the main tag
    $my_additional_html = '<div class="my_notification">This is my notification</div>';

    return $html_after_begin . $my_additional_html;
}, 10, 4 );
```

`add_filter( 'bricks/content/html_after_begin', function( $html_after_begin, $bricks_data, $attributes, $tag ) {

    if ( $tag !== 'main' ) {
      return $html_after_begin;
    }
    
    // Insert custom div after the main tag
    $my_additional_html = '<div class="my_notification">This is my notification</div>';

    return $html_after_begin . $my_additional_html;
}, 10, 4 );`

###### Filter: bricks/registered_post_types_args

###### Filter: bricks/content/html_before_end

