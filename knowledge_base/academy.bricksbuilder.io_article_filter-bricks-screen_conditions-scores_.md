---
title: "Filter: bricks/screen_conditions/scores – Bricks Academy"
url: https://academy.bricksbuilder.io/article/filter-bricks-screen_conditions-scores/
date: 2025-02-27T15:29:16.726867
status: success
---

# Filter: bricks/screen_conditions/scores – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/filter-bricks-screen_conditions-scores/](https://academy.bricksbuilder.io/article/filter-bricks-screen_conditions-scores/)*

## Table of Contents

- [Filter: bricks/screen_conditions/scores](#filter-bricksscreenconditionsscores)
        - [Filter: builder/settings/{type}/controls_data](#filter-buildersettingstypecontrolsdata)
        - [Filter: bricks/registered_post_types_args](#filter-bricksregisteredposttypesargs)

## Filter: bricks/screen_conditions/scores

Bricks selects the template & theme style for a specific page according to the conditions you’ve defined.

Internally this is done via a scoring system from 0 to 10. 0 is the least specific. 10 being the most specific (e.g. specific post ID).

For each template/theme style condition that could apply to a certain context, the template/theme style earns a specific score. After analyzing all templates/theme styles, Bricks chooses the one with the highest score.

If you need to add new template conditions using the filterbuilder/settings/template/controls_dataorbricks/theme_styles/controlsfor theme styles, you then need to hook into the scoring logic to score the templates/theme styles based on the custom conditions.

`builder/settings/template/controls_data`

`bricks/theme_styles/controls`

This is where thebricks/screen_conditions/scoresfilter comes in handy, like so:

`bricks/screen_conditions/scores`

```
add_filter( 'bricks/screen_conditions/scores', function( $scores, $condition, $post_id, $preview_type ) {
  // Run custom logic to score the template/theme style $condition
  // $scores[] = 5; 
 
  return $scores;
}, 10, 4 );
```

`add_filter( 'bricks/screen_conditions/scores', function( $scores, $condition, $post_id, $preview_type ) {
  // Run custom logic to score the template/theme style $condition
  // $scores[] = 5; 
 
  return $scores;
}, 10, 4 );`

Example 1: Add the score for a specific author role in an author archive template

After adding the control using thebuilder/settings/template/controls_data(check example 1), we now need to hook inbricks/screen_conditions/scoresto score the template based on the condition, like so:

`builder/settings/template/controls_data`

`bricks/screen_conditions/scores`

```
add_filter( 'bricks/screen_conditions/scores', function( $scores, $condition, $post_id, $preview_type ) {
  if ( is_author() && $condition['main'] === 'archiveType' && isset( $condition['archiveType'] ) && in_array( 'author', $condition['archiveType'] ) && isset( $condition['archiveAuthorRoles'] ) ) { 
    $user = get_queried_object();

    if ( ! empty( $user->roles ) && is_array( $user->roles ) ) {
      foreach ( $user->roles as $role_name ) {
        if ( in_array( $role_name, $condition['archiveAuthorRoles'] ) ) {
          $scores[] = 9;
        }
      }
    }
  }

  return $scores;
}, 10, 4 );
```

`add_filter( 'bricks/screen_conditions/scores', function( $scores, $condition, $post_id, $preview_type ) {
  if ( is_author() && $condition['main'] === 'archiveType' && isset( $condition['archiveType'] ) && in_array( 'author', $condition['archiveType'] ) && isset( $condition['archiveAuthorRoles'] ) ) { 
    $user = get_queried_object();

    if ( ! empty( $user->roles ) && is_array( $user->roles ) ) {
      foreach ( $user->roles as $role_name ) {
        if ( in_array( $role_name, $condition['archiveAuthorRoles'] ) ) {
          $scores[] = 9;
        }
      }
    }
  }

  return $scores;
}, 10, 4 );`

###### Filter: builder/settings/{type}/controls_data

###### Filter: bricks/registered_post_types_args

