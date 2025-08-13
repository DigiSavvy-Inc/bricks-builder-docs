---
title: "Filter: bricks/auth/custom_redirect_url – Bricks Academy"
url: https://academy.bricksbuilder.io/article/filter-bricks-auth-custom_redirect_url/
date: 2025-02-27T15:35:16.826869
status: success
---

# Filter: bricks/auth/custom_redirect_url – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/filter-bricks-auth-custom_redirect_url/](https://academy.bricksbuilder.io/article/filter-bricks-auth-custom_redirect_url/)*

## Table of Contents

- [Filter: bricks/auth/custom_redirect_url](#filter-bricksauthcustomredirecturl)
  - [Example Usage:](#example-usage)
        - [Filter: bricks/search_form/home_url](#filter-brickssearchformhomeurl)
        - [Filter: bricks/auth/custom_login_redirect](#filter-bricksauthcustomloginredirect)

## Filter: bricks/auth/custom_redirect_url

This filter is distinct from other authentication-related filters in that it provides a broad scope for customizing redirections during authentication processes. Unlike specific filters forlogin,registration,lost password, orreset password pages, this filter applies to any authentication-related URL.

Functionality:

This filter allows overriding the default redirect URL based on custom conditions across various authentication scenarios. It offers flexibility to redirect users to different pages depending on the context or specific requirements of the authentication process.

### Example Usage:

```
add_filter( 'bricks/auth/custom_redirect_url', function( $custom_redirect_url, $current_url_path ) {
    if ( /* custom condition based on $current_url_path */ ) {
        return 'https://example.com/custom-redirect';
    }
    return $custom_redirect_url;
}, 10, 2 );
```

`add_filter( 'bricks/auth/custom_redirect_url', function( $custom_redirect_url, $current_url_path ) {
    if ( /* custom condition based on $current_url_path */ ) {
        return 'https://example.com/custom-redirect';
    }
    return $custom_redirect_url;
}, 10, 2 );`

In this example, the redirection URL changes based on the current URL path, allowing for a dynamic and contextual redirection strategy.

Parameters:

- $custom_redirect_url(string|null): The initial redirect URL.
- $current_url_path(string): The current URL path being accessed.

`$custom_redirect_url`

`$current_url_path`

Return:

- (string|null): The URL to redirect to, or null to follow default logic.

###### Filter: bricks/search_form/home_url

###### Filter: bricks/auth/custom_login_redirect

