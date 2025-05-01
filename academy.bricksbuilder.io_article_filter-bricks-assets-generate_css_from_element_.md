---
title: "Filter: bricks/assets/generate_css_from_element – Bricks Academy"
url: https://academy.bricksbuilder.io/article/filter-bricks-assets-generate_css_from_element/
date: 2025-02-27T15:34:56.095537
status: success
---

# Filter: bricks/assets/generate_css_from_element – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/filter-bricks-assets-generate_css_from_element/](https://academy.bricksbuilder.io/article/filter-bricks-assets-generate_css_from_element/)*

## Table of Contents

- [Filter: bricks/assets/generate_css_from_element](#filter-bricksassetsgeneratecssfromelement)
        - [Filter: bricks/query/result_max_num_pages](#filter-bricksqueryresultmaxnumpages)
        - [Filter: bricks/query/force_run](#filter-bricksqueryforcerun)

## Filter: bricks/assets/generate_css_from_element

This filter allows you to include your custom query loop supported element to generate the children styles in Bricks. (@since 1.9.2)

```
add_filter( 'bricks/assets/generate_css_from_element', function( $element_name, $current_element, $css_type ) {
  // $css_type is a string (e.g. header, footer, content, etc.)
  // Add your custom element name so the looping children styles are generated.
  if ( ! in_array( 'my-custom-element-name', $element_name ) ) {
    $element_name[] = 'my-custom-element-name';
  }

  return $element_name;
}, 10, 3 ); 
```

`add_filter( 'bricks/assets/generate_css_from_element', function( $element_name, $current_element, $css_type ) {
  // $css_type is a string (e.g. header, footer, content, etc.)
  // Add your custom element name so the looping children styles are generated.
  if ( ! in_array( 'my-custom-element-name', $element_name ) ) {
    $element_name[] = 'my-custom-element-name';
  }

  return $element_name;
}, 10, 3 ); `

###### Filter: bricks/query/result_max_num_pages

###### Filter: bricks/query/force_run

