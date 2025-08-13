---
title: "Filter: bricks/element/set_root_attributes – Bricks Academy"
url: https://academy.bricksbuilder.io/article/filter-bricks-set_root_attributes/
date: 2025-02-27T15:29:35.100563
status: success
---

# Filter: bricks/element/set_root_attributes – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/filter-bricks-set_root_attributes/](https://academy.bricksbuilder.io/article/filter-bricks-set_root_attributes/)*

## Table of Contents

- [Filter: bricks/element/set_root_attributes](#filter-brickselementsetrootattributes)
        - [Filter: bricks/users/query_vars](#filter-bricksusersqueryvars)
        - [Filter: bricks/elements/{element_name}/control_groups](#filter-brickselementselementnamecontrolgroups)

## Filter: bricks/element/set_root_attributes

Bricks 1.4 with its improved & slimmer DOM structure now requires to add the element ID, root classes, and other element root HTML attributes directly inside therender()function. You can programmatically manipulate the returns element root attributes like so:

`render()`

```
add_filter( 'bricks/element/set_root_attributes', function( $attributes, $element ) {
    // Add CSS class 'heading-bg' to every heading element
    if ( $element->name === 'heading' ) {
        $attributes['class'][] = 'heading-bg'; 
    }

    return $attributes;
}, 10, 2 );
```

`add_filter( 'bricks/element/set_root_attributes', function( $attributes, $element ) {
    // Add CSS class 'heading-bg' to every heading element
    if ( $element->name === 'heading' ) {
        $attributes['class'][] = 'heading-bg'; 
    }

    return $attributes;
}, 10, 2 );`

The filter callback receives 2 arguments:

- $attributes– an associative array of the element root attributes, grouped by the attribute name (e.g. “class”, “data-animation”, …)
- $element– the Bricks elementobject

`$attributes`

`$element`

NOTE: This filter doesn’t work in builder & already possible withbricks/element/render_attributes

###### Filter: bricks/users/query_vars

###### Filter: bricks/elements/{element_name}/control_groups

