---
title: "Filter: bricks/allowed_html_tags – Bricks Academy"
url: https://academy.bricksbuilder.io/article/filter-bricks-allowed_html_tags/
date: 2026-01-05T11:07:20.896962
status: success
---

# Filter: bricks/allowed_html_tags – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/filter-bricks-allowed_html_tags/](https://academy.bricksbuilder.io/article/filter-bricks-allowed_html_tags/)*

## Table of Contents

- [Filter: bricks/allowed_html_tags](#filter-bricksallowedhtmltags)
        - [Filter: bricks/pagination/total_pages](#filter-brickspaginationtotalpages)
        - [Filter: bricks/query/init_loop_index](#filter-bricksqueryinitloopindex)

## Filter: bricks/allowed_html_tags

Starting at version1.10.2Bricks restricts the allowed HTML tags to the WordPress core logic forwp_kses_allowed_html( 'post' ).

`1.10.2`

`wp_kses_allowed_html( 'post' )`

This results in the following HTML tags being allowed out-of-the-box:

address, a, abbr, acronym, area, article, aside, audio, b, bdo, big, blockquote, br, button, caption, cite, code, col, colgroup, del, dd, dfn, details, div, dl, dt, em, fieldset, figure, figcaption, font, footer, h1, h2, h3, h4, h5, h6, header, hgroup, hr, i, img, ins, kbd, label, legend, li, main, map, mark, menu, nav, object, p, pre, q, rb, rp, rt, rtc, ruby, s, samp, span, section, small, strike, strong, sub, summary, sup, table, tbody, td, textarea, tfoot, th, thead, title, tr, track, tt, u, ul, ol, var, video

For example, setting the “Custom tag” on a “Block” element toformis not allowed by default, and will throw the following error in the builder:

`form`

Using the new filter as shown in the code snippet below, theformtag is added to the list of allowed HTML tags and can be used without throwing any errors.

`form`

```

add_filter( 'bricks/allowed_html_tags', function( $allowed_html_tags ) {
    // Define the additional tags to be added (e.g. 'form' & 'select')
    $additional_tags = ['form', 'select'];

    // Merge additional tags with the existing allowed tags
    return array_merge( $allowed_html_tags, $additional_tags );
} );
```

`
add_filter( 'bricks/allowed_html_tags', function( $allowed_html_tags ) {
    // Define the additional tags to be added (e.g. 'form' & 'select')
    $additional_tags = ['form', 'select'];

    // Merge additional tags with the existing allowed tags
    return array_merge( $allowed_html_tags, $additional_tags );
} );`

Only allow HTML tags that are considered safe, as anyone with builder access can use them!

###### Filter: bricks/pagination/total_pages

###### Filter: bricks/query/init_loop_index

