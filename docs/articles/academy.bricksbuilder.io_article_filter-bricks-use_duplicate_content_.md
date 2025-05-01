---
title: "Filter: bricks/use_duplicate_content – Bricks Academy"
url: https://academy.bricksbuilder.io/article/filter-bricks-use_duplicate_content/
date: 2025-05-01T12:03:05.603608
status: success
---

# Filter: bricks/use_duplicate_content – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/filter-bricks-use_duplicate_content/](https://academy.bricksbuilder.io/article/filter-bricks-use_duplicate_content/)*

## Table of Contents

- [Filter: bricks/use_duplicate_content](#filter-bricksuseduplicatecontent)
  - [Parameters](#parameters)
  - [Return Value](#return-value)
  - [Example Usage](#example-usage)
        - [Filter: bricks/frontend/render_element](#filter-bricksfrontendrenderelement)
        - [Filter: bricks/form/action/{form_action}](#filter-bricksformactionformaction)

## Filter: bricks/use_duplicate_content

Duplicate content is available for all users with theedit_postcapability. Use this feature to duplicate any post or page containing Bricks data to ensure Bricks IDs are not duplicated. The duplicate option is also available for posts without Bricks data, allowing you to duplicate standard posts without the need for a third-party plugin.

`edit_post`

InBricks > Settings, you can configure the duplicate content behavior:

Enable: Duplicate content is available for all posts.Disable globally: Duplicate content is disabled for all posts.Disable for WordPress Data: Duplicate content is disabled for posts that do not use Bricks data.

Thisbricks/use_duplicate_contenthook provides an additional layer of customization, enabling you to implement more complex logic based on your specific requirements.(@since 1.12)

`bricks/use_duplicate_content`

`(@since 1.12)`

### Parameters

$use(bool)

`$use`

- The current decision on whether duplicate content is allowed. Default is based on settings and user capabilities.

$post_id(int)

`$post_id`

- The ID of the post being checked.

$setting(string)

`$setting`

- The value in Bricks > Settings. Which can beenable,disabled_all, ordisable_wp

`enable`

`disabled_all`

`disable_wp`

### Return Value

This filter expects a boolean value:

- trueto allow duplicate content for the particular post.
- falseto disallow duplicate content for the particular post.

`true`

`false`

### Example Usage

Follow setting logic + ensure the user is admin

```
add_filter( 'bricks/use_duplicate_content', function( $use, $post_id, $settings ) {
  // Only allow if current has user administrative privileges
  $has_admin_cap = current_user_can( 'manage_options' );

  // Fulfilled the condition
  return $use && $has_admin_cap;
}, 10, 3 );
```

`add_filter( 'bricks/use_duplicate_content', function( $use, $post_id, $settings ) {
  // Only allow if current has user administrative privileges
  $has_admin_cap = current_user_can( 'manage_options' );

  // Fulfilled the condition
  return $use && $has_admin_cap;
}, 10, 3 );`

Follow setting logic + exclude post type for ACF or MB

```
add_filter( 'bricks/use_duplicate_content', function( $use, $post_id, $settings ) {
  // Check if the post type is 'acf-field-group' or 'mb-post-type
  $post_type = get_post_type( $post_id );
  $exclude_post_types = [ 'acf-field-group', 'mb-post-type' ];

  // Fulfilled the condition
  return $use && ! in_array( $post_type, $exclude_post_types, true );
}, 10, 3 );
```

`add_filter( 'bricks/use_duplicate_content', function( $use, $post_id, $settings ) {
  // Check if the post type is 'acf-field-group' or 'mb-post-type
  $post_type = get_post_type( $post_id );
  $exclude_post_types = [ 'acf-field-group', 'mb-post-type' ];

  // Fulfilled the condition
  return $use && ! in_array( $post_type, $exclude_post_types, true );
}, 10, 3 );`

###### Filter: bricks/frontend/render_element

###### Filter: bricks/form/action/{form_action}

