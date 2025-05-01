---
title: "Custom Authentication Pages – Bricks Academy"
url: https://academy.bricksbuilder.io/article/custom-authentication-pages/
date: 2025-05-01T12:03:29.204735
status: success
---

# Custom Authentication Pages – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/custom-authentication-pages/](https://academy.bricksbuilder.io/article/custom-authentication-pages/)*

## Table of Contents

- [Custom Authentication Pages](#custom-authentication-pages)
  - [How to set custom authentication pages](#how-to-set-custom-authentication-pages)
  - [Setting up your custom pages](#setting-up-your-custom-pages)
  - [WordPress authentication page access](#wordpress-authentication-page-access)
  - [Bypassing custom login (since 1.9.4):](#bypassing-custom-login-since-194)
        - [Save Form Submissions](#save-form-submissions)
        - [Scroll Snap](#scroll-snap)

## Custom Authentication Pages

Since Bricks 1.9.2, you can create custom pages for the various authentication processes, effectively substituting the standard WordPress authentication pages.

### How to set custom authentication pages

1. Navigate to the WordPress dashboard
2. Navigate toBricks>Settings>General
3. Scroll down toCustom authentication pages

Here, you can choose a custom page for the following processes:

- Login
- Registration
- Lost Password
- Reset Password

### Setting up your custom pages

When creating these custom pages, it’s essential to use the “Form” element on those pages with the appropriate authentication actions set under the “Actions” control group of your form.

For detailed information on setting up form actions and other features of the Form Element, please refer to theForm elementarticle.

For instance, for a login page, you should have a form that includes fields for username/email and password, with the “User Login” action set.

### WordPress authentication page access

As of Bricks 1.11, you have control over what happens when someone visits a default WordPress authentication URL (such aswp-login.php), provided custom authentication pages are set.

`wp-login.php`

To manage this:

1. Navigate toBricks>Settings>General>Custom authentication pages.
2. UnderWordPress authentication page access, select one of the following options:Redirect to custom authentication page (default): The user will be redirected to the corresponding custom authentication page you’ve set.Error page: Visitors will be redirected to the 404 error page, effectively blocking access to the default WordPress login page.Home URL: Redirects visitors to your homepage.Redirect to specific page: Allows you to choose a specific page on your site to redirect visitors to.
3. Redirect to custom authentication page (default): The user will be redirected to the corresponding custom authentication page you’ve set.
4. Error page: Visitors will be redirected to the 404 error page, effectively blocking access to the default WordPress login page.
5. Home URL: Redirects visitors to your homepage.
6. Redirect to specific page: Allows you to choose a specific page on your site to redirect visitors to.

- Redirect to custom authentication page (default): The user will be redirected to the corresponding custom authentication page you’ve set.
- Error page: Visitors will be redirected to the 404 error page, effectively blocking access to the default WordPress login page.
- Home URL: Redirects visitors to your homepage.
- Redirect to specific page: Allows you to choose a specific page on your site to redirect visitors to.

This feature is particularly useful if you want to prevent access to the default WordPress login page (wp-login.php) entirely. For example, combining this with the bypass disabling feature (below) will fully restrict access to the default authentication URLs.

`wp-login.php`

### Bypassing custom login (since 1.9.4):

By default, when visiting any authentication page on your site, you can access the default WordPress login page by addingbrx_use_wp_loginas a URL parameter (e.g., https://example.com/wp-login.php?brx_use_wp_login=1). This feature allows users to bypass the custom login page if needed.

`brx_use_wp_login`

In Bricks settings, you have the optionto disable this feature:

- Navigate to Bricks > Settings > General > Custom authentication pages.
- Check theDisable custom authentication page bypasssetting to force the use of your custom authentication pages, preventing access to the default WordPress login page through the URL parameter.

###### Save Form Submissions

###### Scroll Snap

