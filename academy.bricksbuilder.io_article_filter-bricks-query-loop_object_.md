---
title: "Filter: bricks/query/loop_object – Bricks Academy"
url: https://academy.bricksbuilder.io/article/filter-bricks-query-loop_object/
date: 2025-02-27T15:34:52.538050
status: success
---

# Filter: bricks/query/loop_object – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/filter-bricks-query-loop_object/](https://academy.bricksbuilder.io/article/filter-bricks-query-loop_object/)*

## Table of Contents

- [Filter: bricks/query/loop_object](#filter-bricksqueryloopobject)
        - [Filter: bricks/query/run](#filter-bricksqueryrun)
        - [Filter: bricks/terms/query_vars](#filter-brickstermsqueryvars)

## Filter: bricks/query/loop_object

The BricksQuery Loopsupports 3 types of queries by default (Posts, Terms, and Users). But it can be extended to supportany other query. While iterating through the query results, the iteration object could be manipulated using thebricks/query/loop_objectlike so:

`bricks/query/loop_object`

```
add_filter( 'bricks/query/loop_object', function( $loop_object, $loop_key, $query_obj ) {
    if ( $query_obj->object_type !== 'my_query_type' ) {
	return $loop_object;
    }

    // Perform some logic, for example:
    // global $post;
    // $post = get_post( $loop_object );
    // setup_postdata( $post );
    
    return $loop_object;
}, 10, 3 );
```

`add_filter( 'bricks/query/loop_object', function( $loop_object, $loop_key, $query_obj ) {
    if ( $query_obj->object_type !== 'my_query_type' ) {
	return $loop_object;
    }

    // Perform some logic, for example:
    // global $post;
    // $post = get_post( $loop_object );
    // setup_postdata( $post );
    
    return $loop_object;
}, 10, 3 );`

The filter callback receives two arguments:

- $loop_objectis the current loop iteration value (from the results array)
- $loop_keyis the current loop iteration key (from the results array)
- $query_objis an instance of the\Bricks\Queryclass object

`$loop_object`

`$loop_key`

`$query_obj`

`\Bricks\Query`

Related hooks:

- To add a query type to the Query control usebricks/setup/control_options
- To perform the custom query type and output the results usebricks/query/run

`bricks/setup/control_options`

`bricks/query/run`

###### Filter: bricks/query/run

###### Filter: bricks/terms/query_vars

