---
title: "Filter: bricks/elements/{element_name}/controls – Bricks Academy"
url: https://academy.bricksbuilder.io/article/filter-bricks-elements-element_name-controls/
date: 2025-02-27T15:35:19.179878
status: success
---

# Filter: bricks/elements/{element_name}/controls – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/filter-bricks-elements-element_name-controls/](https://academy.bricksbuilder.io/article/filter-bricks-elements-element_name-controls/)*

## Table of Contents

- [Filter: bricks/elements/{element_name}/controls](#filter-brickselementselementnamecontrols)
        - [Filter: bricks/dynamic_data/post_terms_separator](#filter-bricksdynamicdataposttermsseparator)
        - [Filter: bricks/posts/query_vars](#filter-brickspostsqueryvars)

## Filter: bricks/elements/{element_name}/controls

Since Bricks 1.3.2 it is possible to add custom controls to any element like so:

```
add_filter( 'bricks/elements/posts/controls', function( $controls ) {
    $controls['ignoreStickyPosts'] = [
        'tab'      => 'content',
        'group'    => 'query',
        'label'    => esc_html__( 'Ignore Sticky Posts', 'my_plugin' ),
        'type'     => 'checkbox'
    ];

    return $controls;
} );
```

`add_filter( 'bricks/elements/posts/controls', function( $controls ) {
    $controls['ignoreStickyPosts'] = [
        'tab'      => 'content',
        'group'    => 'query',
        'label'    => esc_html__( 'Ignore Sticky Posts', 'my_plugin' ),
        'type'     => 'checkbox'
    ];

    return $controls;
} );`

Note: the above example adds a new checkbox to thepostselement, using the filterbricks/elements/posts/controls. To learn about other Bricks controls visit theTopic: Controls.

`bricks/elements/posts/controls`

You might also be interested in the filterbricks/posts/query_varsto manipulate the posts element query.

`bricks/posts/query_vars`

###### Filter: bricks/dynamic_data/post_terms_separator

###### Filter: bricks/posts/query_vars

