---
title: "Filter: bricks/link_css_selectors – Bricks Academy"
url: https://academy.bricksbuilder.io/article/filter-bricks-link_css_selectors/
date: 2025-05-01T12:03:24.125744
status: success
---

# Filter: bricks/link_css_selectors – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/filter-bricks-link_css_selectors/](https://academy.bricksbuilder.io/article/filter-bricks-link_css_selectors/)*

## Table of Contents

- [Filter: bricks/link_css_selectors](#filter-brickslinkcssselectors)
        - [Filter: bricks/element/settings](#filter-brickselementsettings)
        - [Filter: bricks/dynamic_data/post_terms_links](#filter-bricksdynamicdataposttermslinks)

## Filter: bricks/link_css_selectors

Use this filter in your child theme to overwrite/extend the CSS selectors the “Theme Styles > Link” settings are applied to like this (since Bricks 1.10 also available in the builder):

```
add_filter( 'bricks/link_css_selectors', function( $link_css_selectors ) {
    // Add CSS link styles to .my-custom-element a
    $link_css_selectors[] = '.my-custom-element a';
    
    // OR return new list of CSS link selectors
    // $link_css_selectors = ['.link-wrapper a', '.link-wrapper-2 a'];

    return $link_css_selectors; // Array of selectors link styles are applied to
} );
```

`add_filter( 'bricks/link_css_selectors', function( $link_css_selectors ) {
    // Add CSS link styles to .my-custom-element a
    $link_css_selectors[] = '.my-custom-element a';
    
    // OR return new list of CSS link selectors
    // $link_css_selectors = ['.link-wrapper a', '.link-wrapper-2 a'];

    return $link_css_selectors; // Array of selectors link styles are applied to
} );`

If the theme styles link styles do not apply to your custom selectors, force the regeneration of the theme styles by changing and saving the link color, the padding, or the text decoration, for example. Your new selectors will then be available.

###### Filter: bricks/element/settings

###### Filter: bricks/dynamic_data/post_terms_links

