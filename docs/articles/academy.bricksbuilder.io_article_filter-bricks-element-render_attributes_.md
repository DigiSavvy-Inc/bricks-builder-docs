---
title: "Filter: bricks/element/render_attributes – Bricks Academy"
url: https://academy.bricksbuilder.io/article/filter-bricks-element-render_attributes/
date: 2025-05-01T12:02:43.708201
status: success
---

# Filter: bricks/element/render_attributes – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/filter-bricks-element-render_attributes/](https://academy.bricksbuilder.io/article/filter-bricks-element-render_attributes/)*

## Table of Contents

- [Filter: bricks/element/render_attributes](#filter-brickselementrenderattributes)
        - [Filter: bricks/dynamic_data/read_more](#filter-bricksdynamicdatareadmore)
        - [Filter: bricks/posts/merge_query](#filter-brickspostsmergequery)

## Filter: bricks/element/render_attributes

Starting with Bricks 1.3.7 you may manipulate the HTMLattributes of a given element using the following filter:

```
add_filter( 'bricks/element/render_attributes', function( $attributes, $key, $element ) {
    if ( isset( $element->settings['my_setting'] ) 
       && $element->settings['my_setting'] == 'xpto' ) {
        $attributes[ $key ]['data-xpto'] = 'my data';
    }
    
    return $attributes;
}, 10, 3 );
```

`add_filter( 'bricks/element/render_attributes', function( $attributes, $key, $element ) {
    if ( isset( $element->settings['my_setting'] ) 
       && $element->settings['my_setting'] == 'xpto' ) {
        $attributes[ $key ]['data-xpto'] = 'my data';
    }
    
    return $attributes;
}, 10, 3 );`

The filter callback receives 3 arguments:

- $attributes– an associative array of the element attributes, grouped by the $key identifier
- $key– the HTML element identifier to render attributes for
- $element– the Bricks element object (since Bricks 1.5)

`$attributes`

`$key`

`$element`

Since Bricks 1.4, if you need to get access to the$is_frontendvalue (whether the element is rendering in the frontend or in the builder), please use the global functionbricks_is_frontend().

`$is_frontend`

`bricks_is_frontend()`

Since Bricks 1.5, the$settingsand$namearguments are deprecated. You may use the callback 3rd argument to get those:$element->settingsand$element->name.

`$settings`

`$name`

`$element->settings`

`$element->name`

###### Filter: bricks/dynamic_data/read_more

###### Filter: bricks/posts/merge_query

