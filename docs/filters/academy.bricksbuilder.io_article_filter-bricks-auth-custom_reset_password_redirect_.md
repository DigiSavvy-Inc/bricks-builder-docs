---
title: "Filter: bricks/auth/custom_reset_password_redirect – Bricks Academy"
url: https://academy.bricksbuilder.io/article/filter-bricks-auth-custom_reset_password_redirect/
date: 2026-01-05T11:07:46.624070
status: success
---

# Filter: bricks/auth/custom_reset_password_redirect – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/filter-bricks-auth-custom_reset_password_redirect/](https://academy.bricksbuilder.io/article/filter-bricks-auth-custom_reset_password_redirect/)*

## Table of Contents

- [Filter: bricks/auth/custom_reset_password_redirect](#filter-bricksauthcustomresetpasswordredirect)
  - [Example Usage:](#example-usage)
        - [Filter: bricks/auth/custom_registration_redirect](#filter-bricksauthcustomregistrationredirect)
        - [Filter: bricks/builder/image_size_options](#filter-bricksbuilderimagesizeoptions)

## Filter: bricks/auth/custom_reset_password_redirect

This filter provides a way to change the redirect page ID for the reset password page.

### Example Usage:

```
add_filter( 'bricks/auth/custom_reset_password_redirect', function( $selected_reset_password_page_id ) {
    return /* New reset password page ID */;
});
```

`add_filter( 'bricks/auth/custom_reset_password_redirect', function( $selected_reset_password_page_id ) {
    return /* New reset password page ID */;
});`

Parameters:

- $selected_reset_password_page_id(int|false): The ID of the custom reset password page if set; otherwise,false.

`$selected_reset_password_page_id`

`false`

Return:

- (int|false): The custom page ID for reset password redirection, orfalseif no custom page is specified.

`false`

###### Filter: bricks/auth/custom_registration_redirect

###### Filter: bricks/builder/image_size_options

