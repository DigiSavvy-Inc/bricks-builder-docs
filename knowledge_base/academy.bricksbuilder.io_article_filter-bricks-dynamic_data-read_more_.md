---
title: "Filter: bricks/dynamic_data/read_more – Bricks Academy"
url: https://academy.bricksbuilder.io/article/filter-bricks-dynamic_data-read_more/
date: 2025-02-27T15:29:49.185787
status: success
---

# Filter: bricks/dynamic_data/read_more – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/filter-bricks-dynamic_data-read_more/](https://academy.bricksbuilder.io/article/filter-bricks-dynamic_data-read_more/)*

## Table of Contents

- [Filter: bricks/dynamic_data/read_more](#filter-bricksdynamicdatareadmore)
        - [Filter: bricks/related_posts/query_vars](#filter-bricksrelatedpostsqueryvars)
        - [Filter: bricks/element/render_attributes](#filter-brickselementrenderattributes)

## Filter: bricks/dynamic_data/read_more

If you use the dynamic data tag{read_more}you’ll get an anchor tag (link) to the post with the label “Read more” by default. To change this label use the following code:

`{read_more}`

```
add_filter( 'bricks/dynamic_data/read_more', function( $label, $post ) {
   return 'My New Label';
}, 10, 2 );
```

`add_filter( 'bricks/dynamic_data/read_more', function( $label, $post ) {
   return 'My New Label';
}, 10, 2 );`

Read more aboutDynamic Datain the Bricks academy.

###### Filter: bricks/related_posts/query_vars

###### Filter: bricks/element/render_attributes

