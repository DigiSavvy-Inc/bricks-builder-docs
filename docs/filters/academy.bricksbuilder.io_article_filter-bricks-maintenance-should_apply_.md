---
title: "Filter: bricks/maintenance/should_apply – Bricks Academy"
url: https://academy.bricksbuilder.io/article/filter-bricks-maintenance-should_apply/
date: 2025-05-01T12:03:25.606024
status: success
---

# Filter: bricks/maintenance/should_apply – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/filter-bricks-maintenance-should_apply/](https://academy.bricksbuilder.io/article/filter-bricks-maintenance-should_apply/)*

## Table of Contents

- [Filter: bricks/maintenance/should_apply](#filter-bricksmaintenanceshouldapply)
  - [Parameters:](#parameters)
  - [Return:](#return)
  - [Example Usage:](#example-usage)
    - [Improved version with cookie persistence:](#improved-version-with-cookie-persistence)
        - [Filter: bricks/form/action/{form_action}](#filter-bricksformactionformaction)

## Filter: bricks/maintenance/should_apply

Use this filter to override whether maintenance mode should be enforced for the current request.

By default, Bricks checks if the user is in the admin area or builder, if the current page is the login page, if the user can bypass maintenance, or if the current post is in the excluded list.

This filter runsafterall of those checks have passed, giving you a final opportunity to apply custom logic before showing the maintenance or coming soon page.

### Parameters:

- $apply_maintenance(bool): Whether maintenance mode should apply. Defaults totrueafter all core checks pass.
- $mode(string): The current maintenance mode. Either'maintenance'or'coming_soon'.

`$apply_maintenance`

`true`

`$mode`

`'maintenance'`

`'coming_soon'`

### Return:

- (bool):trueto apply maintenance mode,falseto bypass it.

`(bool)`

`true`

`false`

### Example Usage:

In the following example, anyone with the correctpreview_keyin the URL (e.g.https://domain.com?preview_key=letmein123) will bypass maintenance mode. This is especially useful for sharing a live preview with clients or collaborators without requiring login access.

`preview_key`

`https://domain.com?preview_key=letmein123`

```
add_filter( 'bricks/maintenance/should_apply', function( $apply_maintenance, $mode ) {
    $valid_key = 'letmein123';

    // Bypass maintenance mode if a valid preview key is present in the URL
    if ( isset( $_GET['preview_key'] ) && $_GET['preview_key'] === $valid_key ) {
        return false;
    }

    // Keep default behavior for all other cases
    return $apply_maintenance;
}, 10, 2 );
```

`add_filter( 'bricks/maintenance/should_apply', function( $apply_maintenance, $mode ) {
    $valid_key = 'letmein123';

    // Bypass maintenance mode if a valid preview key is present in the URL
    if ( isset( $_GET['preview_key'] ) && $_GET['preview_key'] === $valid_key ) {
        return false;
    }

    // Keep default behavior for all other cases
    return $apply_maintenance;
}, 10, 2 );`

#### Improved version with cookie persistence:

You can improve this behavior further bypersisting the preview access across page loadsusing a cookie. Otherwise, the user would only bypass maintenance on the first page they visit (where the key is present in the URL), and get blocked again when navigating elsewhere.

```
add_filter( 'bricks/maintenance/should_apply', function( $apply_maintenance, $mode ) {
    $valid_key   = 'letmein123';
    $cookie_name = 'bricks_preview_key';

    // Check preview key in URL
    if ( isset( $_GET['preview_key'] ) && $_GET['preview_key'] === $valid_key ) {
        // Set a cookie for 1 hour
        setcookie( $cookie_name, $valid_key, time() + HOUR_IN_SECONDS, COOKIEPATH, COOKIE_DOMAIN );
        return false;
    }

    // Check cookie on subsequent requests
    if ( isset( $_COOKIE[ $cookie_name ] ) && $_COOKIE[ $cookie_name ] === $valid_key ) {
        return false;
    }

    return $apply_maintenance;
}, 10, 2 );
```

`add_filter( 'bricks/maintenance/should_apply', function( $apply_maintenance, $mode ) {
    $valid_key   = 'letmein123';
    $cookie_name = 'bricks_preview_key';

    // Check preview key in URL
    if ( isset( $_GET['preview_key'] ) && $_GET['preview_key'] === $valid_key ) {
        // Set a cookie for 1 hour
        setcookie( $cookie_name, $valid_key, time() + HOUR_IN_SECONDS, COOKIEPATH, COOKIE_DOMAIN );
        return false;
    }

    // Check cookie on subsequent requests
    if ( isset( $_COOKIE[ $cookie_name ] ) && $_COOKIE[ $cookie_name ] === $valid_key ) {
        return false;
    }

    return $apply_maintenance;
}, 10, 2 );`

###### Filter: bricks/form/action/{form_action}

