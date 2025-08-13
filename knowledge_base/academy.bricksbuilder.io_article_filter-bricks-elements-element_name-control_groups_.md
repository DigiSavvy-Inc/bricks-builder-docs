---
title: "Filter: bricks/elements/{element_name}/control_groups – Bricks Academy"
url: https://academy.bricksbuilder.io/article/filter-bricks-elements-element_name-control_groups/
date: 2025-02-27T15:28:24.731368
status: success
---

# Filter: bricks/elements/{element_name}/control_groups – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/filter-bricks-elements-element_name-control_groups/](https://academy.bricksbuilder.io/article/filter-bricks-elements-element_name-control_groups/)*

## Table of Contents

- [Filter: bricks/elements/{element_name}/control_groups](#filter-brickselementselementnamecontrolgroups)
        - [Filter: bricks/element/set_root_attributes](#filter-brickselementsetrootattributes)
        - [Filter: bricks/element/render](#filter-brickselementrender)

## Filter: bricks/elements/{element_name}/control_groups

Since Bricks 1.4 it is possible to add custom control groups to a specific element like so:

```
add_filter( 'bricks/elements/heading/control_groups', function( $control_groups ) {
    $control_groups['custom_controls'] = [
        'tab'      => 'content', // or 'style'
        'title'    => esc_html__( 'Custom controls', 'my_plugin' ),
    ];

    return $control_groups;
} );
```

`add_filter( 'bricks/elements/heading/control_groups', function( $control_groups ) {
    $control_groups['custom_controls'] = [
        'tab'      => 'content', // or 'style'
        'title'    => esc_html__( 'Custom controls', 'my_plugin' ),
    ];

    return $control_groups;
} );`

Note: the above example adds a new control group with the title “Custom controls” to theheadingelement, using the filterbricks/elements/heading/control_groups. To learn about other Bricks controls visit theTopic: Controls.

`bricks/elements/heading/control_groups`

###### Filter: bricks/element/set_root_attributes

###### Filter: bricks/element/render

