---
title: "Filter: bricks/users/query_vars – Bricks Academy"
url: https://academy.bricksbuilder.io/article/filter-bricks-users-query_vars/
date: 2025-02-27T15:30:07.609935
status: success
---

# Filter: bricks/users/query_vars – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/filter-bricks-users-query_vars/](https://academy.bricksbuilder.io/article/filter-bricks-users-query_vars/)*

## Table of Contents

- [Filter: bricks/users/query_vars](#filter-bricksusersqueryvars)
        - [Filter: bricks/terms/query_vars](#filter-brickstermsqueryvars)
        - [Filter: bricks/element/set_root_attributes](#filter-brickselementsetrootattributes)

## Filter: bricks/users/query_vars

Bricks users query variables can be manipulated before the query runs like so:

```
add_filter( 'bricks/users/query_vars', function( $query_vars, $settings, $element_id, $element_name ) {
    $query_vars['exclude'] = [ 2, 5 ]; // Exclude users id 2 and 5

    return $query_vars;
}, 10, 4 );
```

`add_filter( 'bricks/users/query_vars', function( $query_vars, $settings, $element_id, $element_name ) {
    $query_vars['exclude'] = [ 2, 5 ]; // Exclude users id 2 and 5

    return $query_vars;
}, 10, 4 );`

The filter callback receives three arguments:

- $query_varsan associative array used to feed theWP_User_Queryclass
- $settingsan associative array containing the element settings set in the builder
- $element_idis a string containing the unique element ID
- $element_nameis a string containing the element name (@since 1.11.1)

`$query_vars`

`$settings`

`$element_id`

`$element_name`

`@since 1.11.1`

###### Filter: bricks/terms/query_vars

###### Filter: bricks/element/set_root_attributes

