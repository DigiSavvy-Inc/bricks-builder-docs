---
title: "Filter: bricks/query/result_max_num_pages – Bricks Academy"
url: https://academy.bricksbuilder.io/article/filter-bricks-query-result_max_num_pages/
date: 2025-02-27T15:36:06.800159
status: success
---

# Filter: bricks/query/result_max_num_pages – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/filter-bricks-query-result_max_num_pages/](https://academy.bricksbuilder.io/article/filter-bricks-query-result_max_num_pages/)*

## Table of Contents

- [Filter: bricks/query/result_max_num_pages](#filter-bricksqueryresultmaxnumpages)
        - [Filter: bricks/frontend/render_data](#filter-bricksfrontendrenderdata)
        - [Filter: bricks/assets/generate_css_from_element](#filter-bricksassetsgeneratecssfromelement)

## Filter: bricks/query/result_max_num_pages

This filter allows you to modify the query result maximum number of pages (@since 1.9.1). This value is used for the Pagination element as well.

```
add_filter( 'bricks/query/result_max_num_pages', function( $max_num_pages, $query_obj ) {
  // Return: Element ID is not "lbsijo", nor is it a post query
  if( $query_obj->element_id !== 'lbsijo' || $query_obj->object_type !== 'post' ) {
    return $max_num_pages;
  }

  // Perform your logic here
  // Use $query_obj->query_result to access the query result
  $max_num_pages = 3;
  return $max_num_pages;
}, 10, 2 );
```

`add_filter( 'bricks/query/result_max_num_pages', function( $max_num_pages, $query_obj ) {
  // Return: Element ID is not "lbsijo", nor is it a post query
  if( $query_obj->element_id !== 'lbsijo' || $query_obj->object_type !== 'post' ) {
    return $max_num_pages;
  }

  // Perform your logic here
  // Use $query_obj->query_result to access the query result
  $max_num_pages = 3;
  return $max_num_pages;
}, 10, 2 );`

###### Filter: bricks/frontend/render_data

###### Filter: bricks/assets/generate_css_from_element

