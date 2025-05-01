---
title: "Filter: bricks/query/result_count – Bricks Academy"
url: https://academy.bricksbuilder.io/article/filter-bricks-query-result_count/
date: 2025-02-27T15:35:54.768562
status: success
---

# Filter: bricks/query/result_count – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/filter-bricks-query-result_count/](https://academy.bricksbuilder.io/article/filter-bricks-query-result_count/)*

## Table of Contents

- [Filter: bricks/query/result_count](#filter-bricksqueryresultcount)
        - [Filter: bricks/query/result](#filter-bricksqueryresult)
        - [Filter: bricks/active_templates](#filter-bricksactivetemplates)

## Filter: bricks/query/result_count

This filter allows you to modify the query result count (@since 1.8).

```
add_filter( 'bricks/query/result_count', function( $result_count, $query_obj ) {
  // Return: Element ID is not "lbsijo", nor is it a post query
  if( $query_obj->element_id !== 'lbsijo' || $query_obj->object_type !== 'post' ) {
    return $result_count;
  }

  // Perform your logic here
  // Use $query_obj->query_result to access the query result
  $new_count = 123;
  return $new_count;
}, 10, 2 );
```

`add_filter( 'bricks/query/result_count', function( $result_count, $query_obj ) {
  // Return: Element ID is not "lbsijo", nor is it a post query
  if( $query_obj->element_id !== 'lbsijo' || $query_obj->object_type !== 'post' ) {
    return $result_count;
  }

  // Perform your logic here
  // Use $query_obj->query_result to access the query result
  $new_count = 123;
  return $new_count;
}, 10, 2 );`

###### Filter: bricks/query/result

###### Filter: bricks/active_templates

