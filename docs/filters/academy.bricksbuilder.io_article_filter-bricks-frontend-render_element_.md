---
title: "Filter: bricks/frontend/render_element – Bricks Academy"
url: https://academy.bricksbuilder.io/article/filter-bricks-frontend-render_element/
date: 2025-05-01T12:02:42.731585
status: success
---

# Filter: bricks/frontend/render_element – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/filter-bricks-frontend-render_element/](https://academy.bricksbuilder.io/article/filter-bricks-frontend-render_element/)*

## Table of Contents

- [Filter: bricks/frontend/render_element](#filter-bricksfrontendrenderelement)
        - [Filter: bricks/content/tag](#filter-brickscontenttag)
        - [Filter: bricks/use_duplicate_content](#filter-bricksuseduplicatecontent)

## Filter: bricks/frontend/render_element

Thebricks/frontend/render_elementfilter allows you to modify the HTML output of any element in Bricks on the frontend. This powerful hook can be used for a variety of customization tasks, such as adding comments, modifying content, or dynamically adjusting HTML. (@since 1.x)

`bricks/frontend/render_element`

```
add_filter( 'bricks/frontend/render_element', function( $html, $element ) {
    // Do not modify the HTML in the builder
    if (
        bricks_is_builder_main() ||
        bricks_is_builder_iframe() ||
        bricks_is_builder_call()
    ) {
        return $html;
    }

    // Add comments before and after an element with a specific ID
    if ( $element->id === 'regxve' ) {
        $html = '<!-- Start of the element -->' . $html . '<!-- End of the element -->';
    }

    // Modify the content of a Basic Text element
    if ( $element->id === 'wtktgp' ) {
        // Replace "|" with ">>" in the HTML
        $html = str_replace( '|', '>>', $html );
    }

    return $html;
}, 10, 2 );

```

`add_filter( 'bricks/frontend/render_element', function( $html, $element ) {
    // Do not modify the HTML in the builder
    if (
        bricks_is_builder_main() ||
        bricks_is_builder_iframe() ||
        bricks_is_builder_call()
    ) {
        return $html;
    }

    // Add comments before and after an element with a specific ID
    if ( $element->id === 'regxve' ) {
        $html = '<!-- Start of the element -->' . $html . '<!-- End of the element -->';
    }

    // Modify the content of a Basic Text element
    if ( $element->id === 'wtktgp' ) {
        // Replace "|" with ">>" in the HTML
        $html = str_replace( '|', '>>', $html );
    }

    return $html;
}, 10, 2 );
`

###### Filter: bricks/content/tag

###### Filter: bricks/use_duplicate_content

