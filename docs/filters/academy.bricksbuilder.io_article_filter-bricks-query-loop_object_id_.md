---
title: "Filter: bricks/query/loop_object_id – Bricks Academy"
url: https://academy.bricksbuilder.io/article/filter-bricks-query-loop_object_id/
date: 2026-01-05T11:09:48.251504
status: success
---

# Filter: bricks/query/loop_object_id – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/filter-bricks-query-loop_object_id/](https://academy.bricksbuilder.io/article/filter-bricks-query-loop_object_id/)*

## Table of Contents

- [Filter: bricks/query/loop_object_id](#filter-bricksqueryloopobjectid)
    - [Related hooks:](#related-hooks)
        - [Filter: bricks/content/html_before_end](#filter-brickscontenthtmlbeforeend)
        - [Filter: bricks/query/loop_object_type](#filter-bricksqueryloopobjecttype)

## Filter: bricks/query/loop_object_id

Bricks will use\Bricks\Query::get_loop_object_id()to retrieve the looping iteration’s object ID.

`\Bricks\Query::get_loop_object_id()`

This static function is used in many places. Especially when trying to parse dynamic data.  By default, Bricks uses the looping ID if the looping object is a WP_Post, WP_Term, or WP_User object. This filter allows you to change the ID conditionally.

```
// Change the object_id if the current looping query type is myCustomQueryType
add_filter( 'bricks/query/loop_object_id', function( $object_id, $object, $query_id ) {
    $query_object_type = \Bricks\Query::get_query_object_type( $query_id );
    if ( $query_object_type !== 'myCustomQueryType' ) {
	return $object_id;
    }

    // Set my loop_object_id
    $new_id = my_custom_function_to_transform_the_id( $object_id );
    return $new_id;
}, 10, 3 );
```

`// Change the object_id if the current looping query type is myCustomQueryType
add_filter( 'bricks/query/loop_object_id', function( $object_id, $object, $query_id ) {
    $query_object_type = \Bricks\Query::get_query_object_type( $query_id );
    if ( $query_object_type !== 'myCustomQueryType' ) {
	return $object_id;
    }

    // Set my loop_object_id
    $new_id = my_custom_function_to_transform_the_id( $object_id );
    return $new_id;
}, 10, 3 );`

#### Related hooks:

- bricks/setup/control_options: To add a custom query type to the Query control
- bricks/query/loop_object: To manage the object on every loop iteration

###### Filter: bricks/content/html_before_end

###### Filter: bricks/query/loop_object_type

