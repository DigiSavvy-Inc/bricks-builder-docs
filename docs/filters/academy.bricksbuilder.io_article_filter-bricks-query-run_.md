---
title: "Filter: bricks/query/run – Bricks Academy"
url: https://academy.bricksbuilder.io/article/filter-bricks-query-run/
date: 2025-05-01T12:03:24.770269
status: success
---

# Filter: bricks/query/run – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/filter-bricks-query-run/](https://academy.bricksbuilder.io/article/filter-bricks-query-run/)*

## Table of Contents

- [Filter: bricks/query/run](#filter-bricksqueryrun)
        - [Filter: bricks/setup/control_options](#filter-brickssetupcontroloptions)
        - [Filter: bricks/query/loop_object](#filter-bricksqueryloopobject)

## Filter: bricks/query/run

The BricksQuery Loopsupports 3 types of queries by default (Posts, Terms and Users). But it can be extended to support any other query. To return a custom query result, Bricks can be extended using the WP filterbricks/query/runlike so:

`bricks/query/run`

```
add_filter( 'bricks/query/run', function( $results, $query_obj ) {
    if ( $query_obj->object_type !== 'my_query_type' ) {
	return $results;
    }

    // Perform the query
    // Assign the results to $results (array)
    
    return $results;
}, 10, 2 );
```

`add_filter( 'bricks/query/run', function( $results, $query_obj ) {
    if ( $query_obj->object_type !== 'my_query_type' ) {
	return $results;
    }

    // Perform the query
    // Assign the results to $results (array)
    
    return $results;
}, 10, 2 );`

The filter callback receives two arguments:

- $resultsis the results array (empty by default). The loop will iterate through this array.
- $query_objis an instance of the\Bricks\Queryclass object

`$results`

`$query_obj`

`\Bricks\Query`

Note: This hook should be used to add different types of query results. If you want to alter the posts, terms, or users query, use the following hooks:

- Posts:bricks/posts/query_vars
- Terms:bricks/terms/query_vars
- Users:bricks/users/query_vars

`bricks/posts/query_vars`

Related hooks:

- To add a query type to the Query control usebricks/setup/control_options
- To manage the object on every loop iteration usebricks/query/loop_object

`bricks/setup/control_options`

`bricks/query/loop_object`

###### Filter: bricks/setup/control_options

###### Filter: bricks/query/loop_object

