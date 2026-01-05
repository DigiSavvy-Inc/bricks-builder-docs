---
title: "Filter: bricks/query/loop_object_type – Bricks Academy"
url: https://academy.bricksbuilder.io/article/filter-bricks-query-loop_object_type/
date: 2026-01-05T11:09:46.877904
status: success
---

# Filter: bricks/query/loop_object_type – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/filter-bricks-query-loop_object_type/](https://academy.bricksbuilder.io/article/filter-bricks-query-loop_object_type/)*

## Table of Contents

- [Filter: bricks/query/loop_object_type](#filter-bricksqueryloopobjecttype)
        - [Filter: bricks/query/loop_object_id](#filter-bricksqueryloopobjectid)
        - [Filter: bricks/query/no_results_content](#filter-bricksquerynoresultscontent)

## Filter: bricks/query/loop_object_type

Bricks will use\Bricks\Query::get_loop_object_type()to retrieve the looping iteration’s object type. This static function is used in many places. It plays an important role in many conditions. The possible return object_type should be ‘post’, ‘term’, or ‘user’ only.

`\Bricks\Query::get_loop_object_type()`

```
// This is the example when Bricks set the object_type in woo cart query, so inside each iteration, it will be treat as a post/product object_type
add_filter( 'bricks/query/loop_object_type', function( $object_type, $object, $query_id ) {
    $query_object_type = \Bricks\Query::get_query_object_type( $query_id );

    if ( $query_object_type !== 'wooCart' ) {
	return $object_type;
    }

    return 'post';
}, 10, 3 );
```

`// This is the example when Bricks set the object_type in woo cart query, so inside each iteration, it will be treat as a post/product object_type
add_filter( 'bricks/query/loop_object_type', function( $object_type, $object, $query_id ) {
    $query_object_type = \Bricks\Query::get_query_object_type( $query_id );

    if ( $query_object_type !== 'wooCart' ) {
	return $object_type;
    }

    return 'post';
}, 10, 3 );`

###### Filter: bricks/query/loop_object_id

###### Filter: bricks/query/no_results_content

