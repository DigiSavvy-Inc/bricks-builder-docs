---
title: "Filter: bricks/auth/custom_lost_password_redirect – Bricks Academy"
url: https://academy.bricksbuilder.io/article/filter-bricks-auth-custom_lost_password_redirect/
date: 2025-02-27T15:35:27.592785
status: success
---

# Filter: bricks/auth/custom_lost_password_redirect – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/filter-bricks-auth-custom_lost_password_redirect/](https://academy.bricksbuilder.io/article/filter-bricks-auth-custom_lost_password_redirect/)*

## Table of Contents

- [Filter: bricks/auth/custom_lost_password_redirect](#filter-bricksauthcustomlostpasswordredirect)
  - [Example Usage:](#example-usage)
        - [Filter: bricks/auth/custom_login_redirect](#filter-bricksauthcustomloginredirect)
        - [Filter: bricks/auth/custom_registration_redirect](#filter-bricksauthcustomregistrationredirect)

## Filter: bricks/auth/custom_lost_password_redirect

This filter enables the modification of the redirect page ID for the lost password page.

### Example Usage:

```
add_filter( 'bricks/auth/custom_lost_password_redirect', function( $selected_lost_password_page_id ) {
    return /* New lost password page ID */;
});
```

`add_filter( 'bricks/auth/custom_lost_password_redirect', function( $selected_lost_password_page_id ) {
    return /* New lost password page ID */;
});`

Parameters:

- $selected_lost_password_page_id(int|false): The ID of the custom lost password page if set, otherwisefalse.

`$selected_lost_password_page_id`

`false`

Return:

- (int|false): The new custom lost password page ID orfalseto indicate no custom page is set.

`false`

###### Filter: bricks/auth/custom_login_redirect

###### Filter: bricks/auth/custom_registration_redirect

