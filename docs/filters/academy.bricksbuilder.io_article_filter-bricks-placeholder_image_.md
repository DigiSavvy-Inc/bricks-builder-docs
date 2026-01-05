---
title: "Filter: bricks/placeholder_image – Bricks Academy"
url: https://academy.bricksbuilder.io/article/filter-bricks-placeholder_image/
date: 2026-01-05T11:08:23.246762
status: success
---

# Filter: bricks/placeholder_image – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/filter-bricks-placeholder_image/](https://academy.bricksbuilder.io/article/filter-bricks-placeholder_image/)*

## Table of Contents

- [Filter: bricks/placeholder_image](#filter-bricksplaceholderimage)
  - [Parameters](#parameters)
        - [Filter: bricks/maintenance/should_apply](#filter-bricksmaintenanceshouldapply)
        - [Filter: bricks/filter_element/populated_options](#filter-bricksfilterelementpopulatedoptions)

## Filter: bricks/placeholder_image

Thebricks/placeholder_imagefilter allows you to override the default placeholder image used in Bricks. This can be useful when you want to display a custom placeholder for elements when performing template import or pasting elements from another website.(@since 2.0)

`bricks/placeholder_image`

`(@since 2.0)`

### Parameters

- $image(string)– The default placeholder image path or URL.
- $is_svg(bool)– Whether the placeholder should be an SVG. Leave as is.
- $format(string)– Can be'url'or'path'depending on the context Bricks needs it for. Leave as is.

`$image`

`$is_svg`

`$format`

`'url'`

`'path'`

```
add_filter( 'bricks/placeholder_image', function( $image, $is_svg, $format ) {
  // Custom placeholder images (SVG and non-SVG file required)
  // SVG file: /uploads/2025/04/my-placeholder.svg
  // Non-SVG file: /uploads/2025/04/my-placeholder-img.png
  $relative_path = $is_svg ? '2025/04/my-placeholder.svg' : '2025/04/my-placeholder-img.png';
  $upload_dir    = wp_get_upload_dir();

  if ( $format === 'path' ) {
    // Return absolute path to the image
    $image = $upload_dir['basedir'] . '/' . $relative_path;
  } else {
    // Return full URL to the image
    $image = $upload_dir['baseurl'] . '/' . $relative_path;
  }

  return $image;
}, 10, 3 );
```

`add_filter( 'bricks/placeholder_image', function( $image, $is_svg, $format ) {
  // Custom placeholder images (SVG and non-SVG file required)
  // SVG file: /uploads/2025/04/my-placeholder.svg
  // Non-SVG file: /uploads/2025/04/my-placeholder-img.png
  $relative_path = $is_svg ? '2025/04/my-placeholder.svg' : '2025/04/my-placeholder-img.png';
  $upload_dir    = wp_get_upload_dir();

  if ( $format === 'path' ) {
    // Return absolute path to the image
    $image = $upload_dir['basedir'] . '/' . $relative_path;
  } else {
    // Return full URL to the image
    $image = $upload_dir['baseurl'] . '/' . $relative_path;
  }

  return $image;
}, 10, 3 );`

###### Filter: bricks/maintenance/should_apply

###### Filter: bricks/filter_element/populated_options

