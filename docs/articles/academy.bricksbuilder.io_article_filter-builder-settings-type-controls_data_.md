---
title: "Filter: builder/settings/{type}/controls_data – Bricks Academy"
url: https://academy.bricksbuilder.io/article/filter-builder-settings-type-controls_data/
date: 2025-05-01T12:03:11.822022
status: success
---

# Filter: builder/settings/{type}/controls_data – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/filter-builder-settings-type-controls_data/](https://academy.bricksbuilder.io/article/filter-builder-settings-type-controls_data/)*

## Table of Contents

- [Filter: builder/settings/{type}/controls_data](#filter-buildersettingstypecontrolsdata)
        - [Filter: bricks/comments/timestamp](#filter-brickscommentstimestamp)
        - [Filter: bricks/screen_conditions/scores](#filter-bricksscreenconditionsscores)

## Filter: builder/settings/{type}/controls_data

This filter allows you to add new controls to the Page Settings or Template Settings panels in the builder.

To manage theTemplate Settingscontrols use thebuilder/settings/template/controls_datahook like so:

`builder/settings/template/controls_data`

```
add_filter( 'builder/settings/template/controls_data', function( $data ) {
  // Do something
 
  return $data;
} );
```

`add_filter( 'builder/settings/template/controls_data', function( $data ) {
  // Do something
 
  return $data;
} );`

To manage thePage Settingscontrols use thebuilder/settings/page/controls_datahook like so:

`builder/settings/page/controls_data`

```
add_filter( 'builder/settings/page/controls_data', function( $data ) {
  // Do something
 
  return $data;
} );
```

`add_filter( 'builder/settings/page/controls_data', function( $data ) {
  // Do something
 
  return $data;
} );`

Example: Add a control to select the user roles in the author archive template type template condition

```
add_filter( 'builder/settings/template/controls_data', function( $data ) {
  // Get all the site user roles
  $all_roles = wp_roles()->roles;

  $roles = [];

  foreach ( $all_roles as $role => $role_data ) {
    $roles[ $role ] = $role_data['name'];
  }

  // Add control to select the user roles for an author archive template type
  $data['controls']['templateConditions']['fields']['archiveAuthorRoles'] = [
    'type'        => 'select',
    'label'       => esc_html__( 'Author roles', 'bricks' ),
    'options'     => $roles,
    'multiple'    => true,
    'placeholder' => esc_html__( 'Select role', 'bricks' ),
    'description' => esc_html__( 'Leave empty to apply template to all roles.', 'bricks' ),
    'required'    => [ 'archiveType', '=', 'author' ],
  ];

  return $data;
} );
```

`add_filter( 'builder/settings/template/controls_data', function( $data ) {
  // Get all the site user roles
  $all_roles = wp_roles()->roles;

  $roles = [];

  foreach ( $all_roles as $role => $role_data ) {
    $roles[ $role ] = $role_data['name'];
  }

  // Add control to select the user roles for an author archive template type
  $data['controls']['templateConditions']['fields']['archiveAuthorRoles'] = [
    'type'        => 'select',
    'label'       => esc_html__( 'Author roles', 'bricks' ),
    'options'     => $roles,
    'multiple'    => true,
    'placeholder' => esc_html__( 'Select role', 'bricks' ),
    'description' => esc_html__( 'Leave empty to apply template to all roles.', 'bricks' ),
    'required'    => [ 'archiveType', '=', 'author' ],
  ];

  return $data;
} );`

###### Filter: bricks/comments/timestamp

###### Filter: bricks/screen_conditions/scores

