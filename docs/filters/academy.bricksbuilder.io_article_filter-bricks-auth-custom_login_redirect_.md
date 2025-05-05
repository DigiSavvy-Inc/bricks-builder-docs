---
title: "Filter: bricks/auth/custom_login_redirect – Bricks Academy"
url: https://academy.bricksbuilder.io/article/filter-bricks-auth-custom_login_redirect/
date: 2025-05-01T12:03:21.706981
status: success
---

# Filter: bricks/auth/custom_login_redirect – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/filter-bricks-auth-custom_login_redirect/](https://academy.bricksbuilder.io/article/filter-bricks-auth-custom_login_redirect/)*

## Table of Contents

- [Filter: bricks/auth/custom_login_redirect](#filter-bricksauthcustomloginredirect)
  - [Example Usage:](#example-usage)
        - [Filter: bricks/auth/custom_redirect_url](#filter-bricksauthcustomredirecturl)
        - [Filter: bricks/auth/custom_lost_password_redirect](#filter-bricksauthcustomlostpasswordredirect)

## Filter: bricks/auth/custom_login_redirect

This filter allows customization of the redirect page ID for the login page.

### Example Usage:

```
add_filter( 'bricks/auth/custom_login_redirect', function( $selected_login_page_id ) {
    return /* New login page ID */;
});
```

`add_filter( 'bricks/auth/custom_login_redirect', function( $selected_login_page_id ) {
    return /* New login page ID */;
});`

Parameters:

- $selected_login_page_id(int|false): The ID of the custom login page if set; otherwise,false.

`$selected_login_page_id`

`false`

Return:

- (int|false): The custom page ID for login redirection, orfalseif no custom page is designated.

`false`

###### Filter: bricks/auth/custom_redirect_url

###### Filter: bricks/auth/custom_lost_password_redirect

