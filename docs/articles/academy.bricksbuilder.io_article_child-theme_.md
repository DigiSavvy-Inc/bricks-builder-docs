---
title: "Child Theme – Bricks Academy"
url: https://academy.bricksbuilder.io/article/child-theme/
date: 2026-01-05T11:07:14.951492
status: success
---

# Child Theme – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/child-theme/](https://academy.bricksbuilder.io/article/child-theme/)*

## Table of Contents

- [Child Theme](#child-theme)
  - [How To Enqueue Scripts (JS) & Styles (CSS)](#how-to-enqueue-scripts-js--styles-css)
        - [Create Your Own Elements](#create-your-own-elements)

## Child Theme

Please do not edit any of the Bricks theme core files directly, as updating the theme will cause all your changes to be lost.

Instead, use the Bricks child theme to make modifications and overwrite files. You can download the Bricks child theme directly from yourBricks account.

Upload this child theme ZIP file (bricks-child.zip) like any other WordPress theme. Go toAppearance → Themesand activateBricks Child Theme. You can add your own styles tostyle.css.

### How To Enqueue Scripts (JS) & Styles (CSS)

In order to load your files only on the front end & the canvas and not in the builder panel (as your custom CSS might affect the builder), you have to check againstbricks_is_builder_main()like this:

`bricks_is_builder_main()`

```
add_action( 'wp_enqueue_scripts', function() {
  // Code & check below enqueues your files on the canvas & frontend, not the builder panel. Otherwise custom CSS might affect builder)
  if ( ! bricks_is_builder_main() ) {
    wp_enqueue_style( 'bricks-child', get_stylesheet_uri(), ['bricks-frontend'], filemtime( get_stylesheet_directory() . '/style.css' ) );
  }
} );
```

`add_action( 'wp_enqueue_scripts', function() {
  // Code & check below enqueues your files on the canvas & frontend, not the builder panel. Otherwise custom CSS might affect builder)
  if ( ! bricks_is_builder_main() ) {
    wp_enqueue_style( 'bricks-child', get_stylesheet_uri(), ['bricks-frontend'], filemtime( get_stylesheet_directory() . '/style.css' ) );
  }
} );`

You can learn more about how a Child Theme works by visiting the official WordPress Codex:https://developer.wordpress.org/themes/advanced-topics/child-themes/

Thefunctions.phpfile of a child theme, unlikestyle.css, does not override thefunctions.phpfile of the parent theme. Instead, it is loaded in addition to the parent theme’sfunctions.php, right before the parent file.

`functions.php`

`style.css`

`functions.php`

`functions.php`

###### Create Your Own Elements

