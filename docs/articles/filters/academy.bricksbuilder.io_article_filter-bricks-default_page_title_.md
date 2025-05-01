---
title: "Filter: bricks/default_page_title – Bricks Academy"
url: https://academy.bricksbuilder.io/article/filter-bricks-default_page_title/
date: 2025-02-27T15:35:38.647187
status: success
---

# Filter: bricks/default_page_title – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/filter-bricks-default_page_title/](https://academy.bricksbuilder.io/article/filter-bricks-default_page_title/)*

## Table of Contents

- [Filter: bricks/default_page_title](#filter-bricksdefaultpagetitle)
        - [Filter: bricks/query/no_results_content](#filter-bricksquerynoresultscontent)
        - [Filter: bricks/query/result](#filter-bricksqueryresult)

## Filter: bricks/default_page_title

Since 1.8, Bricks automatically adds default page titles to all non-Bricks pages. However, if you wish to customize or remove this default page title, you can utilize this filter.

Returning an empty string, disables the default page title.

```
add_filter( 'bricks/default_page_title', function( $title, $post_id ) {
  // If slug of current page is 'my-page': Return empty page title
  if ( is_page( 'my-page' ) ) {
    $title = '';
  }

  return $title;
}, 10, 2 );
```

`add_filter( 'bricks/default_page_title', function( $title, $post_id ) {
  // If slug of current page is 'my-page': Return empty page title
  if ( is_page( 'my-page' ) ) {
    $title = '';
  }

  return $title;
}, 10, 2 );`

###### Filter: bricks/query/no_results_content

###### Filter: bricks/query/result

