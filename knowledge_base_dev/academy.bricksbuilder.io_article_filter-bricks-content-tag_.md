---
title: "Filter: bricks/content/tag – Bricks Academy"
url: https://academy.bricksbuilder.io/article/filter-bricks-content-tag/
date: 2025-02-27T15:35:03.437448
status: success
---

# Filter: bricks/content/tag – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/filter-bricks-content-tag/](https://academy.bricksbuilder.io/article/filter-bricks-content-tag/)*

## Table of Contents

- [Filter: bricks/content/tag](#filter-brickscontenttag)
  - [Example Usage:](#example-usage)
        - [Filter: bricks/render_query_loop_trail](#filter-bricksrenderquerylooptrail)
        - [Filter: bricks/use_duplicate_content](#filter-bricksuseduplicatecontent)

## Filter: bricks/content/tag

Thebricks/content/tag(@since 1.11.1) filter lets you set the HTML tag for the#brx-contentnode that your Bricks content data is wrapped in.

`bricks/content/tag`

`#brx-content`

Make sure the HTML tag you return is anallowed HTML tag.

### Example Usage:

```
add_filter( 'bricks/content/tag', function( $tag ) {
    // Set #brx-content tag to 'div' (default: main)
    return 'div';
} );
```

`add_filter( 'bricks/content/tag', function( $tag ) {
    // Set #brx-content tag to 'div' (default: main)
    return 'div';
} );`

Parameters:

- $tag(string): The default HTML tag, which ismain.

`$tag`

`main`

Return:

- (string): The HTML tag you want to render instead of the default.

###### Filter: bricks/render_query_loop_trail

###### Filter: bricks/use_duplicate_content

