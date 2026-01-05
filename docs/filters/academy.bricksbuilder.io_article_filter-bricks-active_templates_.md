---
title: "Filter: bricks/active_templates – Bricks Academy"
url: https://academy.bricksbuilder.io/article/filter-bricks-active_templates/
date: 2026-01-05T11:07:42.526292
status: success
---

# Filter: bricks/active_templates – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/filter-bricks-active_templates/](https://academy.bricksbuilder.io/article/filter-bricks-active_templates/)*

## Table of Contents

- [Filter: bricks/active_templates](#filter-bricksactivetemplates)
  - [Example: Do not use the Single template if the post has been edited with Bricks](#example-do-not-use-the-single-template-if-the-post-has-been-edited-with-bricks)
  - [Example: Change a single template based on a custom field](#example-change-a-single-template-based-on-a-custom-field)
  - [Example: Disable active template in the builder](#example-disable-active-template-in-the-builder)
    - [Explanation:](#explanation)
        - [Filter: bricks/query/result_count](#filter-bricksqueryresultcount)
        - [Filter: bricks/form/file_directory](#filter-bricksformfiledirectory)

## Filter: bricks/active_templates

Modify the templates applied on a page programmatically (@since 1.8.4)

`@since 1.8.4`

This is an alternative to setting an active template via thebricks/screen_conditions/scoresfilter.

Please note that this filter is executed afterbricks/screen_conditions/scores

`bricks/screen_conditions/scores`

### Example: Do not use the Single template if the post has been edited with Bricks

In this example, we want to exclude the single post from utilizing a template if it contains Bricks data (Edit with Bricks).

```
add_filter( 'bricks/active_templates', 'set_my_active_templates', 10, 3 );
function set_my_active_templates( $active_templates, $post_id, $content_type ) {
  // Return if single post $content_type is not 'content'
  if ( $content_type !== 'content' ) {
    return $active_templates;
  }

  // Return: Current post type is not 'post'
  $post_type = get_post_type( $post_id );

  if ( $post_type !== 'post' ) {
    return $active_templates;
  }

  /**
   * $active_templates is an array with different important keys
   * 
   * $active_templates['header'] is the header template ID, set it to 0 if do not want to use any template
   * $active_templates['content'] is the content template ID, set it to current post ID if do not want to use any template
   * $active_templates['footer'] is the footer template ID, set it to 0 if do not want to use any template
   * 
   * $active_templates['search'] is the search template ID, will only be used if $content_type is 'search'
   * $active_templates['archive'] is the archive template ID, will only be used if $content_type is 'archive'
   * $active_templates['error] is the error template ID, will only be used if $content_type is 'error'
  */

  // Check if the current post has Bricks data, return value is an array
  $bricks_data = \Bricks\Database::get_data( $post_id, 'content' );

  if ( count( $bricks_data ) > 0 ) {
    // Has Bricks data: Don't use any template, set the $active_templates['content'] to current post ID
    $active_templates['content'] = $post_id;

    // To disable header & footer (e.g. landing page) set $active_templates['header'] & $active_templates['footer'] to 0
    $active_templates['header'] = 0;
    $active_templates['footer'] = 0;
  }

  return $active_templates;
}
```

`add_filter( 'bricks/active_templates', 'set_my_active_templates', 10, 3 );
function set_my_active_templates( $active_templates, $post_id, $content_type ) {
  // Return if single post $content_type is not 'content'
  if ( $content_type !== 'content' ) {
    return $active_templates;
  }

  // Return: Current post type is not 'post'
  $post_type = get_post_type( $post_id );

  if ( $post_type !== 'post' ) {
    return $active_templates;
  }

  /**
   * $active_templates is an array with different important keys
   * 
   * $active_templates['header'] is the header template ID, set it to 0 if do not want to use any template
   * $active_templates['content'] is the content template ID, set it to current post ID if do not want to use any template
   * $active_templates['footer'] is the footer template ID, set it to 0 if do not want to use any template
   * 
   * $active_templates['search'] is the search template ID, will only be used if $content_type is 'search'
   * $active_templates['archive'] is the archive template ID, will only be used if $content_type is 'archive'
   * $active_templates['error] is the error template ID, will only be used if $content_type is 'error'
  */

  // Check if the current post has Bricks data, return value is an array
  $bricks_data = \Bricks\Database::get_data( $post_id, 'content' );

  if ( count( $bricks_data ) > 0 ) {
    // Has Bricks data: Don't use any template, set the $active_templates['content'] to current post ID
    $active_templates['content'] = $post_id;

    // To disable header & footer (e.g. landing page) set $active_templates['header'] & $active_templates['footer'] to 0
    $active_templates['header'] = 0;
    $active_templates['footer'] = 0;
  }

  return $active_templates;
}`

### Example: Change a single template based on a custom field

There is a scenario like having multiple single templates for a custom post type. Using this filter, you can decide which template to apply based on a custom field.

```
add_filter( 'bricks/active_templates', 'set_active_templates_by_custom_field', 10, 3 );

function set_active_templates_by_custom_field( $active_templates, $post_id, $content_type ) {
  // Return if single post $content_type is not 'content'
  if ( $content_type !== 'content' ) {
    return $active_templates;
  }

  // Return: Current post type is not 'project'
  $post_type = get_post_type( $post_id );

  if ( $post_type !== 'project' ) {
    return $active_templates;
  }

  // Get the custom field value from Metabox
  $value = absint( rwmb_meta( 'use_template_id' ) );

  // Value not empty: Set $active_templates['content'] to the value
  if ( $value > 0 ) {
    $active_templates['content'] = $value;
    // If single template, the page settings will be used, so no need to set header and footer
  }

  return $active_templates;
}
```

`add_filter( 'bricks/active_templates', 'set_active_templates_by_custom_field', 10, 3 );

function set_active_templates_by_custom_field( $active_templates, $post_id, $content_type ) {
  // Return if single post $content_type is not 'content'
  if ( $content_type !== 'content' ) {
    return $active_templates;
  }

  // Return: Current post type is not 'project'
  $post_type = get_post_type( $post_id );

  if ( $post_type !== 'project' ) {
    return $active_templates;
  }

  // Get the custom field value from Metabox
  $value = absint( rwmb_meta( 'use_template_id' ) );

  // Value not empty: Set $active_templates['content'] to the value
  if ( $value > 0 ) {
    $active_templates['content'] = $value;
    // If single template, the page settings will be used, so no need to set header and footer
  }

  return $active_templates;
}`

### Example: Disable active template in the builder

Since Bricks 1.12, templates applied to a page are now also displayed in the Builder. Previously, only thePost Contentelement was visible, making it difficult to style surrounding elements. If you prefer the old behavior and want to disable the applied templateonly inside the builder, you can use this filter:

```
add_filter( 'bricks/active_templates', 'disable_template_in_builder', 10, 3 );

function disable_template_in_builder( $active_templates, $post_id, $content_type ) {
  // Only run my logic in the Builder
  if ( bricks_is_builder() ) {
    $active_templates['content'] = 0;
  }

  return $active_templates;
}
```

`add_filter( 'bricks/active_templates', 'disable_template_in_builder', 10, 3 );

function disable_template_in_builder( $active_templates, $post_id, $content_type ) {
  // Only run my logic in the Builder
  if ( bricks_is_builder() ) {
    $active_templates['content'] = 0;
  }

  return $active_templates;
}`

#### Explanation:

- This function runs only when Bricks is inBuilder mode(bricks_is_builder()).
- It prevents the active single template from applying inside the Builder by setting$active_templates['content'] = 0.
- The frontend remains unaffected; the template is still used when viewing the post/page normally.
- This effectively disables the newouter Post Content elements visibilityintroduced inBricks 1.12, restoring the previous Builder behavior.

`bricks_is_builder()`

`$active_templates['content'] = 0`

###### Filter: bricks/query/result_count

###### Filter: bricks/form/file_directory

