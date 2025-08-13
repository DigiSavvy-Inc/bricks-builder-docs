---
title: "Filter: bricks/content/html_before_end – Bricks Academy"
url: https://academy.bricksbuilder.io/article/filter-bricks-content-html_before_end/
date: 2025-02-27T15:29:47.948819
status: success
---

# Filter: bricks/content/html_before_end – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/filter-bricks-content-html_before_end/](https://academy.bricksbuilder.io/article/filter-bricks-content-html_before_end/)*

## Table of Contents

- [Filter: bricks/content/html_before_end](#filter-brickscontenthtmlbeforeend)
        - [Filter: bricks/content/html_after_begin](#filter-brickscontenthtmlafterbegin)
        - [Filter: bricks/query/loop_object_id](#filter-bricksqueryloopobjectid)

## Filter: bricks/content/html_before_end

Available since version 1.6, this filter allows you to customize or insert HTML strings before closingmaintag.

`main`

```
add_filter( 'bricks/content/html_before_end', function( $html_after_begin, $bricks_data, $attributes, $tag ) {

    if ( $tag !== 'main' ) {
      return $html_after_begin;
    }

    // Insert custom popup HTML
    $my_popup_html = '<div class="my_popup">This is my popup</div>';

    return $html_after_begin . $my_popup_html;
}, 10, 4 );
```

`add_filter( 'bricks/content/html_before_end', function( $html_after_begin, $bricks_data, $attributes, $tag ) {

    if ( $tag !== 'main' ) {
      return $html_after_begin;
    }

    // Insert custom popup HTML
    $my_popup_html = '<div class="my_popup">This is my popup</div>';

    return $html_after_begin . $my_popup_html;
}, 10, 4 );`

###### Filter: bricks/content/html_after_begin

###### Filter: bricks/query/loop_object_id

