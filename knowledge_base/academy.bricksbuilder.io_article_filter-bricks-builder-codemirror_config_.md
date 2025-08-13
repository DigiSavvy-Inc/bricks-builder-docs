---
title: "Filter: bricks/builder/codemirror_config – Bricks Academy"
url: https://academy.bricksbuilder.io/article/filter-bricks-builder-codemirror_config/
date: 2025-02-27T15:29:40.560552
status: success
---

# Filter: bricks/builder/codemirror_config – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/filter-bricks-builder-codemirror_config/](https://academy.bricksbuilder.io/article/filter-bricks-builder-codemirror_config/)*

## Table of Contents

- [Filter: bricks/builder/codemirror_config](#filter-bricksbuildercodemirrorconfig)
  - [Example Usage:](#example-usage)
        - [Filter: bricks/password_protection/cookie_expires](#filter-brickspasswordprotectioncookieexpires)
        - [Filter: bricks/render_query_loop_trail](#filter-bricksrenderquerylooptrail)

## Filter: bricks/builder/codemirror_config

Use this filter to customize the configuration of CodeMirror 5, the code editor used within the builder. CodeMirror 5 is used in areas such as theCustom CSSsetting for elements and theCode elementsettings, where it provides an interface for editing HTML, CSS, JavaScript, PHP, and more.

You can refer to theCodeMirror 5 configuration documentationfor more details on available options.

### Example Usage:

```
add_filter( 'bricks/builder/codemirror_config', function( $config ) {
    // Disable auto-close brackets
    $config['autoCloseBrackets'] = false;

    // Disable line numbers
    $config['lineNumbers'] = false;

    // Override default tab size
    $config['tabSize'] = 4;

    return $config;
});
```

`add_filter( 'bricks/builder/codemirror_config', function( $config ) {
    // Disable auto-close brackets
    $config['autoCloseBrackets'] = false;

    // Disable line numbers
    $config['lineNumbers'] = false;

    // Override default tab size
    $config['tabSize'] = 4;

    return $config;
});`

In this example, the filter modifies the default CodeMirror configuration to:

- Disableauto-close brackets.
- Disableline numbers.
- Set thetab sizeto 4 spaces.

Parameters:

- $config(array): An empty array by default. Define only the specific configurations you need, which will override the builder’s default settings.

`$config`

Return:

- (array): The custom configuration array, applied alongside or in place of Bricks’ defaults.

###### Filter: bricks/password_protection/cookie_expires

###### Filter: bricks/render_query_loop_trail

