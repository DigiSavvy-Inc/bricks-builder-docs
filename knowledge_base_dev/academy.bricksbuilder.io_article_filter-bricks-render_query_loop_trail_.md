---
title: "Filter: bricks/render_query_loop_trail – Bricks Academy"
url: https://academy.bricksbuilder.io/article/filter-bricks-render_query_loop_trail/
date: 2025-02-27T15:35:00.859664
status: success
---

# Filter: bricks/render_query_loop_trail – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/filter-bricks-render_query_loop_trail/](https://academy.bricksbuilder.io/article/filter-bricks-render_query_loop_trail/)*

## Table of Contents

- [Filter: bricks/render_query_loop_trail](#filter-bricksrenderquerylooptrail)
        - [Filter: bricks/builder/codemirror_config](#filter-bricksbuildercodemirrorconfig)
        - [Filter: bricks/content/tag](#filter-brickscontenttag)

## Filter: bricks/render_query_loop_trail

Thebricks/render_query_loop_trail(@since 1.11.1) filter controls the output of the query loop trail node in Bricks. This node is automatically added to each query loop and records the loop’s settings, which are then accessed by frontend JavaScript to manage various query-related tasks. Once these settings are read by Bricks, the node is removed from the DOM.

`bricks/render_query_loop_trail`

For some third-party plugins, this node may not be needed—especially if they use custom AJAX endpoints to update query results independently of Bricks. Using this filter, you can control whether or not the query loop trail node is rendered.

```
// Return true = render the query loop trail node
// Return false = skip the query loop trail node
add_filter( 'bricks/render_query_loop_trail', function( $render, $element, $query ) {
  // Do not render query loop trail node if my-custom-param parameter exists
  if ( isset( $_GET['my-custom-param'] ) ) {
    $render = false;
  }

  return $render;
}, 10, 3 );
```

`// Return true = render the query loop trail node
// Return false = skip the query loop trail node
add_filter( 'bricks/render_query_loop_trail', function( $render, $element, $query ) {
  // Do not render query loop trail node if my-custom-param parameter exists
  if ( isset( $_GET['my-custom-param'] ) ) {
    $render = false;
  }

  return $render;
}, 10, 3 );`

In this example, if themy-custom-paramparameter is detected in the URL, the query loop trail node will not be rendered. This can be useful for third-party plugins with custom AJAX endpoints that handle query configurations independently.

`my-custom-param`

###### Filter: bricks/builder/codemirror_config

###### Filter: bricks/content/tag

