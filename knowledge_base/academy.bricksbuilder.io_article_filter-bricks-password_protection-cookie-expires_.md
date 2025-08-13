---
title: "Filter: bricks/password_protection/cookie_expires – Bricks Academy"
url: https://academy.bricksbuilder.io/article/filter-bricks-password_protection-cookie-expires/
date: 2025-02-27T15:27:58.745327
status: success
---

# Filter: bricks/password_protection/cookie_expires – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/filter-bricks-password_protection-cookie-expires/](https://academy.bricksbuilder.io/article/filter-bricks-password_protection-cookie-expires/)*

## Table of Contents

- [Filter: bricks/password_protection/cookie_expires](#filter-brickspasswordprotectioncookieexpires)
  - [Example Usage:](#example-usage)
        - [Filter: bricks/password_protection/is_active](#filter-brickspasswordprotectionisactive)
        - [Filter: bricks/builder/codemirror_config](#filter-bricksbuildercodemirrorconfig)

## Filter: bricks/password_protection/cookie_expires

Adjust the expiration time for the password cookie used bythe password protection template. By default, when a password is set in the template settings, the cookie expires after10 days. This filter allows you to customize how long the cookie remains valid.

### Example Usage:

```
add_filter( 'bricks/password_protection/cookie_expires', function( $expire ) {
    // Set cookie expiration to 1 hour (3600 seconds)
    return time() + 3600;
} );
```

`add_filter( 'bricks/password_protection/cookie_expires', function( $expire ) {
    // Set cookie expiration to 1 hour (3600 seconds)
    return time() + 3600;
} );`

In this example, the password cookie will expire after 1 hour, requiring users to re-enter the password if they revisit the page after that time.

Parameters:

- $expire(int): The default expiration timestamp for the password cookie, which is set to10 days.

`$expire`

Return:

- (int): The Unix timestamp for when the cookie should expire.

###### Filter: bricks/password_protection/is_active

###### Filter: bricks/builder/codemirror_config

