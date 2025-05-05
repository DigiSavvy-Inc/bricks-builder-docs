---
title: "Filter: bricks/is_layout_element – Bricks Academy"
url: https://academy.bricksbuilder.io/article/filter-bricks-is_layout_element/
date: 2025-05-01T12:02:53.691003
status: success
---

# Filter: bricks/is_layout_element – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/filter-bricks-is_layout_element/](https://academy.bricksbuilder.io/article/filter-bricks-is_layout_element/)*

## Table of Contents

- [Filter: bricks/is_layout_element](#filter-bricksislayoutelement)
        - [Filter: bricks/dynamic_data/post_terms_links](#filter-bricksdynamicdataposttermslinks)
        - [Filter: bricks/content/attributes](#filter-brickscontentattributes)

## Filter: bricks/is_layout_element

Allows to define your custom elements as a layout element, so they are recognised like the section, container, block, div elements and use the same controls like query loop, flex controls, shape divider, etc.

```
add_filter( 'bricks/is_layout_element', function( $layout_element_names ) {
    // Mark your custom element "custom_box" as a layout element
    $layout_element_names[] = 'custom_box';

    return $layout_element_names;
} );
```

`add_filter( 'bricks/is_layout_element', function( $layout_element_names ) {
    // Mark your custom element "custom_box" as a layout element
    $layout_element_names[] = 'custom_box';

    return $layout_element_names;
} );`

###### Filter: bricks/dynamic_data/post_terms_links

###### Filter: bricks/content/attributes

