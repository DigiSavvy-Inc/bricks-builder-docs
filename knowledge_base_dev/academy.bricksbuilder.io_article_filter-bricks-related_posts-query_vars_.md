---
title: "Filter: bricks/related_posts/query_vars – Bricks Academy"
url: https://academy.bricksbuilder.io/article/filter-bricks-related_posts-query_vars/
date: 2025-02-27T15:34:59.693523
status: success
---

# Filter: bricks/related_posts/query_vars – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/filter-bricks-related_posts-query_vars/](https://academy.bricksbuilder.io/article/filter-bricks-related_posts-query_vars/)*

## Table of Contents

- [Filter: bricks/related_posts/query_vars](#filter-bricksrelatedpostsqueryvars)
        - [Filter: bricks/dynamic_data/exclude_tags](#filter-bricksdynamicdataexcludetags)
        - [Filter: bricks/dynamic_data/read_more](#filter-bricksdynamicdatareadmore)

## Filter: bricks/related_posts/query_vars

Since Bricks 1.3.5 you may manipulate therelated postselement query vars before the query is performed like so:

```
add_filter( 'bricks/related_posts/query_vars', function( $query_vars, $settings, $element_id ) {
    $query_vars['post_type'] = [ 'post', 'project' ];

    return $query_vars;
}, 10, 3 );
```

`add_filter( 'bricks/related_posts/query_vars', function( $query_vars, $settings, $element_id ) {
    $query_vars['post_type'] = [ 'post', 'project' ];

    return $query_vars;
}, 10, 3 );`

The filter callback receives two arguments:

- $query_varsis an associative array used to feed theWP_Queryclass
- $settingsis an associative array containing the element settings set in the builder
- $element_idis a string containing the element ID

`$query_vars`

`$settings`

`$element_id`

###### Filter: bricks/dynamic_data/exclude_tags

###### Filter: bricks/dynamic_data/read_more

