---
title: "Filter: bricks/query/no_results_content – Bricks Academy"
url: https://academy.bricksbuilder.io/article/filter-bricks-query-no_results_content/
date: 2025-02-27T15:32:05.531727
status: success
---

# Filter: bricks/query/no_results_content – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/filter-bricks-query-no_results_content/](https://academy.bricksbuilder.io/article/filter-bricks-query-no_results_content/)*

## Table of Contents

- [Filter: bricks/query/no_results_content](#filter-bricksquerynoresultscontent)
        - [Filter: bricks/query/loop_object_type](#filter-bricksqueryloopobjecttype)
        - [Filter: bricks/default_page_title](#filter-bricksdefaultpagetitle)

## Filter: bricks/query/no_results_content

You can programmatically change the query loop “no results content” using this filter.

```
add_filter( 'bricks/query/no_results_content', function( $content, $settings, $element_id ) {

  // Check if the query element id is the one you want
  if( $element_id !== 'srixvr' ) return $content;

  // Use a bricks section template as the no results content
  $content = do_shortcode('[bricks_template id="3981"]');

  return $content;
}, 10, 3 );
```

`add_filter( 'bricks/query/no_results_content', function( $content, $settings, $element_id ) {

  // Check if the query element id is the one you want
  if( $element_id !== 'srixvr' ) return $content;

  // Use a bricks section template as the no results content
  $content = do_shortcode('[bricks_template id="3981"]');

  return $content;
}, 10, 3 );`

###### Filter: bricks/query/loop_object_type

###### Filter: bricks/default_page_title

