---
title: "Filter: bricks/terms/query_vars – Bricks Academy"
url: https://academy.bricksbuilder.io/article/filter-bricks-terms-query_vars/
date: 2026-01-05T11:08:23.885615
status: success
---

# Filter: bricks/terms/query_vars – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/filter-bricks-terms-query_vars/](https://academy.bricksbuilder.io/article/filter-bricks-terms-query_vars/)*

## Table of Contents

- [Filter: bricks/terms/query_vars](#filter-brickstermsqueryvars)
  - [Example 1: Exclude the current term from the query](#example-1-exclude-the-current-term-from-the-query)
  - [Example 2: Get terms assigned to a post](#example-2-get-terms-assigned-to-a-post)
        - [Filter: bricks/query/loop_object](#filter-bricksqueryloopobject)
        - [Filter: bricks/users/query_vars](#filter-bricksusersqueryvars)

## Filter: bricks/terms/query_vars

Bricks terms query variables can be manipulated before the query runs like so:

```
add_filter( 'bricks/terms/query_vars', function( $query_vars, $settings, $element_id, $element_name ) {
    $query_vars['exclude'] = 23; // Exclude term id 23

    return $query_vars;
}, 10, 4 );
```

`add_filter( 'bricks/terms/query_vars', function( $query_vars, $settings, $element_id, $element_name ) {
    $query_vars['exclude'] = 23; // Exclude term id 23

    return $query_vars;
}, 10, 4 );`

The filter callback receives three arguments:

- $query_varsan associative array used to feed theWP_Term_Queryclass
- $settingsan associative array containing the element settings set in the builder
- $element_idis a string containing the unique element ID
- $element_nameis a string containing the element name (@since 1.11.1)

`$query_vars`

`$settings`

`$element_id`

`$element_name`

`@since 1.11.1`

### Example 1: Exclude the current term from the query

Inside a term archive page, to exclude the current term from the query:

```
// Exclude current term from the terms query loop on term archive pages.
add_filter( 'bricks/terms/query_vars', function( $query_vars, $settings, $element_id, $element_name ) {
    if ( $element_id !== 'uxtkgn' ) {
        return $query_vars;
    }

    $query_vars['exclude'] = get_queried_object_id();

    return $query_vars;
}, 10, 4 );
```

`// Exclude current term from the terms query loop on term archive pages.
add_filter( 'bricks/terms/query_vars', function( $query_vars, $settings, $element_id, $element_name ) {
    if ( $element_id !== 'uxtkgn' ) {
        return $query_vars;
    }

    $query_vars['exclude'] = get_queried_object_id();

    return $query_vars;
}, 10, 4 );`

whereuxtkgnis the Bricks ID of the element on which query loop is enabled.

`uxtkgn`

### Example 2: Get terms assigned to a post

In this example, we would like to get only the terms assigned to a specific post ID (the same as the WordPress functionwp_get_object_terms()output):

`wp_get_object_terms()`

```
add_filter( 'bricks/terms/query_vars', function( $query_vars, $settings, $element_id, $element_name ) {
    if ( $element_id !== 'mjvhur' ) {
        return $query_vars;
    }

    $query_vars['object_ids'] = get_the_ID();

    return $query_vars;
}, 10, 4 );
```

`add_filter( 'bricks/terms/query_vars', function( $query_vars, $settings, $element_id, $element_name ) {
    if ( $element_id !== 'mjvhur' ) {
        return $query_vars;
    }

    $query_vars['object_ids'] = get_the_ID();

    return $query_vars;
}, 10, 4 );`

###### Filter: bricks/query/loop_object

###### Filter: bricks/users/query_vars

