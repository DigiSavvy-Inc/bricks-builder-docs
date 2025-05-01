---
title: "Filter: bricks/setup/control_options – Bricks Academy"
url: https://academy.bricksbuilder.io/article/filter-bricks-setup-control_options/
date: 2025-02-27T15:36:04.379925
status: success
---

# Filter: bricks/setup/control_options – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/filter-bricks-setup-control_options/](https://academy.bricksbuilder.io/article/filter-bricks-setup-control_options/)*

## Table of Contents

- [Filter: bricks/setup/control_options](#filter-brickssetupcontroloptions)
        - [Filter: bricks/assets/load_webfonts](#filter-bricksassetsloadwebfonts)
        - [Filter: bricks/query/run](#filter-bricksqueryrun)

## Filter: bricks/setup/control_options

Bricks offers a WordPress filter to add or remove control options. The control options are used throughout Bricks and allow you to manage the options of the:

- Template Types (e.g. Header, Footer, Single, Section…)
- Background position, repeat, attachment or size
- Button sizes
- Button or Heading styles
- Border styles
- Font weight and style
- CSS position
- Query types (e.g. Posts, Terms, Users, ..)
- Query order by, compare, operator and value type
- Image Sizes
- Taxonomies
- User roles

To manage any of these options or add new ones, use the WP hookbricks/setup/control_optionslike so:

`bricks/setup/control_options`

```
add_filter( 'bricks/setup/control_options', function( $control_options ) {
    $control_options['templateTypes']['my_template_type'] = esc_html__( 'My Template Type', 'my-plugin' );

    return $control_options;
} );
```

`add_filter( 'bricks/setup/control_options', function( $control_options ) {
    $control_options['templateTypes']['my_template_type'] = esc_html__( 'My Template Type', 'my-plugin' );

    return $control_options;
} );`

Note: the above example adds a new template type. To learn about other Bricks controls visit theTopic: Controls.

###### Filter: bricks/assets/load_webfonts

###### Filter: bricks/query/run

