---
title: "Filter: bricks/auth/custom_registration_redirect – Bricks Academy"
url: https://academy.bricksbuilder.io/article/filter-bricks-auth-custom_registration_redirect/
date: 2025-02-27T15:29:36.302126
status: success
---

# Filter: bricks/auth/custom_registration_redirect – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/filter-bricks-auth-custom_registration_redirect/](https://academy.bricksbuilder.io/article/filter-bricks-auth-custom_registration_redirect/)*

## Table of Contents

- [Filter: bricks/auth/custom_registration_redirect](#filter-bricksauthcustomregistrationredirect)
  - [Example Usage:](#example-usage)
        - [Filter: bricks/auth/custom_lost_password_redirect](#filter-bricksauthcustomlostpasswordredirect)
        - [Filter: bricks/auth/custom_reset_password_redirect](#filter-bricksauthcustomresetpasswordredirect)

## Filter: bricks/auth/custom_registration_redirect

This filter allows for the customization of the redirect page ID for the registration page.

### Example Usage:

```
add_filter( 'bricks/auth/custom_registration_redirect', function( $selected_registration_page_id ) {
    return /* New registration page ID */;
});
```

`add_filter( 'bricks/auth/custom_registration_redirect', function( $selected_registration_page_id ) {
    return /* New registration page ID */;
});`

Parameters:

- $selected_registration_page_id(int|false): The ID of the custom registration page if set; otherwise,false.

`$selected_registration_page_id`

`false`

Return:

- (int|false): The custom page ID for registration redirection, orfalseif no custom page is set.

`false`

###### Filter: bricks/auth/custom_lost_password_redirect

###### Filter: bricks/auth/custom_reset_password_redirect

