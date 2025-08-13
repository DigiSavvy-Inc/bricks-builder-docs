---
title: "Action: bricks/generate_css_file – Bricks Academy"
url: https://academy.bricksbuilder.io/article/action-bricks-generate_css_file/
date: 2025-02-27T15:28:51.467231
status: success
---

# Action: bricks/generate_css_file – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/action-bricks-generate_css_file/](https://academy.bricksbuilder.io/article/action-bricks-generate_css_file/)*

## Table of Contents

- [Action: bricks/generate_css_file](#action-bricksgeneratecssfile)
        - [Action: bricks/query/after_loop](#action-bricksqueryafterloop)

## Action: bricks/generate_css_file

If your CSS loading method is set toExternal files, this hook will be triggered when a CSS file is generated in Bricks. Developers can use this hook to trigger other actions related to CSS file generation. It’s useful for instructing a cache plugin to clear the cache when a CSS file is generated. (@since 1.9.5)

`@since 1.9.5`

```
/**
  * $type : 'global-color-palettes' | 'global-elements' | 'theme-styles' | 'global-custom-css' | 'post'
  * $file_name : The generated CSS file name
*/
add_action( 'bricks/generate_css_file', function( $type, $file_name ) {
  error_log( 'Generated CSS file: ' . $type . ' - ' . $file_name );
}, 10, 2 );
```

`/**
  * $type : 'global-color-palettes' | 'global-elements' | 'theme-styles' | 'global-custom-css' | 'post'
  * $file_name : The generated CSS file name
*/
add_action( 'bricks/generate_css_file', function( $type, $file_name ) {
  error_log( 'Generated CSS file: ' . $type . ' - ' . $file_name );
}, 10, 2 );`

Parameters:

- $type(string): Possible stringsglobal-color-palettesglobal-elementstheme-stylesglobal-custom-csspost
- $file_name(string): The generated CSS file name

`$type`

`global-color-palettes`

`global-elements`

`theme-styles`

`global-custom-css`

`post`

`$file_name`

###### Action: bricks/query/after_loop

