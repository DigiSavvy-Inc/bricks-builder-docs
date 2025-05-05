---
title: "Filter: bricks/builder/image_size_options – Bricks Academy"
url: https://academy.bricksbuilder.io/article/filter-bricks-builder-image_size_options/
date: 2025-05-01T12:03:07.055683
status: success
---

# Filter: bricks/builder/image_size_options – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/filter-bricks-builder-image_size_options/](https://academy.bricksbuilder.io/article/filter-bricks-builder-image_size_options/)*

## Table of Contents

- [Filter: bricks/builder/image_size_options](#filter-bricksbuilderimagesizeoptions)
        - [Filter: bricks/auth/custom_reset_password_redirect](#filter-bricksauthcustomresetpasswordredirect)
        - [Filter: bricks/code/allow_execution](#filter-brickscodeallowexecution)

## Filter: bricks/builder/image_size_options

Thebricks/builder/image_sizeshook gives developers the ability to customize image size options in the builder.

`bricks/builder/image_sizes`

By default, when working within a query loop and using dynamic data for image sources, Bricks Builder displays all the registered WordPress image sizes.

This hook allows you to modify this list if you know that certain sizes are not being used, helping you streamline your image size options to fit your needs.

```
/**
 * $image_sizes Multidimensional array (key: image size name)
 */
add_filter( 'bricks/builder/image_size_options', function( $image_sizes ) {
  // Unset thumbnail, 1536x1536, 2048x2048
  unset( $image_sizes['thumbnail'] );
  unset( $image_sizes['1536x1536'] );
  unset( $image_sizes['2048x2048'] );

  return $image_sizes;
});
```

`/**
 * $image_sizes Multidimensional array (key: image size name)
 */
add_filter( 'bricks/builder/image_size_options', function( $image_sizes ) {
  // Unset thumbnail, 1536x1536, 2048x2048
  unset( $image_sizes['thumbnail'] );
  unset( $image_sizes['1536x1536'] );
  unset( $image_sizes['2048x2048'] );

  return $image_sizes;
});`

###### Filter: bricks/auth/custom_reset_password_redirect

###### Filter: bricks/code/allow_execution

