---
title: "Filter: bricks/password_protection/is_active – Bricks Academy"
url: https://academy.bricksbuilder.io/article/filter-bricks-password_protection-is_active/
date: 2025-02-27T15:35:43.512466
status: success
---

# Filter: bricks/password_protection/is_active – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/filter-bricks-password_protection-is_active/](https://academy.bricksbuilder.io/article/filter-bricks-password_protection-is_active/)*

## Table of Contents

- [Filter: bricks/password_protection/is_active](#filter-brickspasswordprotectionisactive)
  - [Example Usage:](#example-usage)
        - [Filter: bricks/get_element_data/maybe_from_post_id](#filter-bricksgetelementdatamaybefrompostid)
        - [Filter: bricks/password_protection/cookie_expires](#filter-brickspasswordprotectioncookieexpires)

## Filter: bricks/password_protection/is_active

Use this filter to add custom rules that determine whether apassword protection templateshould be active. By default, the template’s visibility is controlled by settings such as logged-in status, valid password cookies, and scheduling through the password protection template settings in the builder. This filter allows you to extend those checks, adding more dynamic criteria once the default settings have been applied.

### Example Usage:

```
add_filter( 'bricks/password_protection/is_active', function( $is_active, $template_id, $settings ) {
    // Bypass password protection for users with the 'manage_options' capability
    if ( current_user_can( 'manage_options' ) ) {
        return false;
    }

    // Maintain default logic for other cases
    return $is_active;
}, 10, 3 );
```

`add_filter( 'bricks/password_protection/is_active', function( $is_active, $template_id, $settings ) {
    // Bypass password protection for users with the 'manage_options' capability
    if ( current_user_can( 'manage_options' ) ) {
        return false;
    }

    // Maintain default logic for other cases
    return $is_active;
}, 10, 3 );`

In this example, any user with themanage_optionscapability (typically administrators) will bypass the password protection, while other users will follow the default settings.

`manage_options`

Parameters:

- $is_active(bool): The initial status of whether the password protection is active.
- $template_id(int): The ID of the password protection template.
- $settings(array): The template settings.

`$is_active`

`$template_id`

`$settings`

Return:

- (bool):trueto keep the template active,falseto disable it.

`true`

`false`

###### Filter: bricks/get_element_data/maybe_from_post_id

###### Filter: bricks/password_protection/cookie_expires

