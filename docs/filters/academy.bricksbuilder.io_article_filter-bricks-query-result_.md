---
title: "Filter: bricks/query/result – Bricks Academy"
url: https://academy.bricksbuilder.io/article/filter-bricks-query-result/
date: 2025-05-01T12:02:50.112739
status: success
---

# Filter: bricks/query/result – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/filter-bricks-query-result/](https://academy.bricksbuilder.io/article/filter-bricks-query-result/)*

## Table of Contents

- [Filter: bricks/query/result](#filter-bricksqueryresult)
        - [Filter: bricks/default_page_title](#filter-bricksdefaultpagetitle)
        - [Filter: bricks/query/result_count](#filter-bricksqueryresultcount)

## Filter: bricks/query/result

Available since 1.8, this filter lets you customize the query results and implement additional logic. Like modifying the post, term, or user object type. Which was previously not editable through thebricks/query/runfilter.

`bricks/query/run`

```
// Use this filter to rearrange it by post title (PHP way instead of query orderby)
add_filter( 'bricks/query/result', function( $result, $query_obj ){
  // Return: Element ID is not "djvsvi", nor is it a post query
  if ( $query_obj->element_id !== 'djvsvi' || $query_obj->object_type !== 'post' ) {
    return $result;
  }

  // Sort by post title (descending)
  // Result is WP_Query object with posts
  if ( $result->have_posts() ) {
    $posts = $result->posts;
    
    usort( $posts, function( $a, $b ) {
      return strcmp( $b->post_title, $a->post_title );
    });

    $result->posts = $posts;
  }

  return $result;
}, 10, 2 );
```

`// Use this filter to rearrange it by post title (PHP way instead of query orderby)
add_filter( 'bricks/query/result', function( $result, $query_obj ){
  // Return: Element ID is not "djvsvi", nor is it a post query
  if ( $query_obj->element_id !== 'djvsvi' || $query_obj->object_type !== 'post' ) {
    return $result;
  }

  // Sort by post title (descending)
  // Result is WP_Query object with posts
  if ( $result->have_posts() ) {
    $posts = $result->posts;
    
    usort( $posts, function( $a, $b ) {
      return strcmp( $b->post_title, $a->post_title );
    });

    $result->posts = $posts;
  }

  return $result;
}, 10, 2 );`

###### Filter: bricks/default_page_title

###### Filter: bricks/query/result_count

