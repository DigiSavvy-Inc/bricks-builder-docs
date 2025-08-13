---
title: "Filter: bricks/search_form/home_url – Bricks Academy"
url: https://academy.bricksbuilder.io/article/filter-bricks-search_form-home_url/
date: 2025-02-27T15:29:27.656306
status: success
---

# Filter: bricks/search_form/home_url – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/filter-bricks-search_form-home_url/](https://academy.bricksbuilder.io/article/filter-bricks-search_form-home_url/)*

## Table of Contents

- [Filter: bricks/search_form/home_url](#filter-brickssearchformhomeurl)
    - [Example Usage:](#example-usage)
    - [Parameters:](#parameters)
    - [Return:](#return)
        - [Filter: bricks/query/force_run](#filter-bricksqueryforcerun)
        - [Filter: bricks/auth/custom_redirect_url](#filter-bricksauthcustomredirecturl)

## Filter: bricks/search_form/home_url

Thebricks/search_form/home_urlfilter allows developers to customize the action URL of the search form within the Bricks theme. This filter provides the flexibility to redirect search queries to a different URL than the default WordPress home URL.

`bricks/search_form/home_url`

By using this filter, developers can integrate custom search solutions or direct the search form submissions to a specific page, enhancing the search functionality tailored to specific needs.

#### Example Usage:

```
add_filter( 'bricks/search_form/home_url', function( $home_url ) {    // Custom logic to determine the action URL    $custom_action_url = 'https://example.com/custom-search-page/'; 
    return $custom_action_url;});
```

`add_filter( 'bricks/search_form/home_url', function( $home_url ) {    // Custom logic to determine the action URL    $custom_action_url = 'https://example.com/custom-search-page/'; 
    return $custom_action_url;});`

`add_filter( 'bricks/search_form/home_url', function( $home_url ) {`

`    // Custom logic to determine the action URL`

`    $custom_action_url = 'https://example.com/custom-search-page/'; `

`    return $custom_action_url;`

`});`

In this simple example, the search form action URL is changed to a custom page. This is particularly useful for websites with specialized search requirements or for integrating with external search platforms.

#### Parameters:

- $home_url(string): The default URL to which the search form points, typically the home URL.

`$home_url`

#### Return:

- (string): The modified URL for the search form action.

###### Filter: bricks/query/force_run

###### Filter: bricks/auth/custom_redirect_url

