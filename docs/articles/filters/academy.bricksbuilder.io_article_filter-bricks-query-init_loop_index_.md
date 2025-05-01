---
title: "Filter: bricks/query/init_loop_index – Bricks Academy"
url: https://academy.bricksbuilder.io/article/filter-bricks-query-init_loop_index/
date: 2025-02-27T15:35:20.447878
status: success
---

# Filter: bricks/query/init_loop_index – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/filter-bricks-query-init_loop_index/](https://academy.bricksbuilder.io/article/filter-bricks-query-init_loop_index/)*

## Table of Contents

- [Filter: bricks/query/init_loop_index](#filter-bricksqueryinitloopindex)
    - [When to Use](#when-to-use)
        - [Filter: bricks/allowed_html_tags](#filter-bricksallowedhtmltags)
        - [Filter: bricks/get_element_data/maybe_from_post_id](#filter-bricksgetelementdatamaybefrompostid)

## Filter: bricks/query/init_loop_index

Thebricks/query/init_loop_indexfilter, available@since 1.11, allows you to modify the initial loop index when using various query types in Bricks Builder. This filter is especially useful in cases such as infinite scroll or paginated queries, where setting the correct loop index is crucial for displaying content seamlessly across multiple pages especially when using dynamic backgound images or colors. Without this hook, the generated dynamic CSS might be applied on the incorrect element when performing infinite scroll or paginate actions.

`bricks/query/init_loop_index`

`@since 1.11`

#### When to Use

This filter is particularly useful when creating a custom query type using thebricks/setup/control_optionshook. You can implement your own logic for handling pagination and adjust the initial loop index accordingly.

```
add_filter( 'bricks/query/init_loop_index', function ( $initial_index, $object_type, $query ) {
  // Check if the object type is 'my_custom_query'
  if ( $object_type !== 'my_custom_query' ) {
    return $initial_index;
  }

  // Add your custom logic to modify the initial loop index
  // Example: Calculate based on custom logic
  // $initial_index = custom_logic_to_calculate_index();

  return $initial_index;
}, 10, 3 );

```

`add_filter( 'bricks/query/init_loop_index', function ( $initial_index, $object_type, $query ) {
  // Check if the object type is 'my_custom_query'
  if ( $object_type !== 'my_custom_query' ) {
    return $initial_index;
  }

  // Add your custom logic to modify the initial loop index
  // Example: Calculate based on custom logic
  // $initial_index = custom_logic_to_calculate_index();

  return $initial_index;
}, 10, 3 );
`

###### Filter: bricks/allowed_html_tags

###### Filter: bricks/get_element_data/maybe_from_post_id

