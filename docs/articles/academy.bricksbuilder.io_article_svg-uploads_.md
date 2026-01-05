---
title: "SVG Uploads – Bricks Academy"
url: https://academy.bricksbuilder.io/article/svg-uploads/
date: 2026-01-05T11:08:51.983489
status: success
---

# SVG Uploads – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/svg-uploads/](https://academy.bricksbuilder.io/article/svg-uploads/)*

## Table of Contents

- [SVG Uploads](#svg-uploads)
  - [How to enable SVG support](#how-to-enable-svg-support)
  - [Bypass sanitization](#bypass-sanitization)
  - [Sanitizer allowed tags and attributes](#sanitizer-allowed-tags-and-attributes)
        - [Dynamic Data](#dynamic-data)
        - [Container Element](#container-element)

## SVG Uploads

WordPress, by default, does not allow SVG file uploads as this XML-based file format can contain malicious code. It can be especially dangerous when downloaded from unknown/untrusted sources or by untrusted users.

### How to enable SVG support

You can enable SVG uploads on a user role basis underBricks > Settings > SVG Uploads(tab: General). Once enabled Bricks will try to sanitize any SVG file uploads.

It is important to note that no built-in SVG sanitizer has a 100% guarantee to remove all malicious code. You should therefore download SVG files only from trusted sources, and only enable SVG uploads for user roles that you trust to follow this rule.

### Bypass sanitization

Although it is wise to sanitize all the SVG files uploaded to WordPress, there could be a situation where you don’t want to rely on the Bricks SVG sanitizer. To bypass the sanitization logic, Bricks provides the hookbricks/svg/bypass_sanitization, and you could use it like so:

`bricks/svg/bypass_sanitization`

```
add_filter( 'bricks/svg/bypass_sanitization', function( $bypass, $file ) {
  // Perform some logic to decide to bypass or not the sanitization

  return $bypass;
}, 10, 2 );
```

`add_filter( 'bricks/svg/bypass_sanitization', function( $bypass, $file ) {
  // Perform some logic to decide to bypass or not the sanitization

  return $bypass;
}, 10, 2 );`

Filter callback parameters:

- $bypassis a boolean variable (true= bypass)
- $filerepresents a single element of the $_FILES array

`$bypass`

`true`

`$file`

If you just want to bypass the sanitization without conditions you could use this shorthand approach:

```
add_filter( 'bricks/svg/bypass_sanitization', '__return_true' );
```

`add_filter( 'bricks/svg/bypass_sanitization', '__return_true' );`

### Sanitizer allowed tags and attributes

The sanitizer uses a predefined list of allowed tags and attributes. In some edge cases you would like to upload SVG files that contain other tags and attributes and therefore you need to include them in the allowed list. Or, you may want to narrow the allowed tags and attributes for high security reasons. To manage these lists, Bricks has two different filters:

```
add_filter( 'bricks/svg/allowed_tags', function( $tags ) {
    $tags[] = 'filter'; // Allow the "filter" tag

    return $tags;
} );
```

`add_filter( 'bricks/svg/allowed_tags', function( $tags ) {
    $tags[] = 'filter'; // Allow the "filter" tag

    return $tags;
} );`

```
add_filter( 'bricks/svg/allowed_attributes', function( $attributes ) {
    $attributes[] = 'filterUnits'; // Allow the "filterUnits" attribute

    return $attributes;
} );
```

`add_filter( 'bricks/svg/allowed_attributes', function( $attributes ) {
    $attributes[] = 'filterUnits'; // Allow the "filterUnits" attribute

    return $attributes;
} );`

###### Dynamic Data

###### Container Element

