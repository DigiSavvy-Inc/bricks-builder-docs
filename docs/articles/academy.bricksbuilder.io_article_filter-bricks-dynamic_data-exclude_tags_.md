---
title: "Filter: bricks/dynamic_data/exclude_tags – Bricks Academy"
url: https://academy.bricksbuilder.io/article/filter-bricks-dynamic_data-exclude_tags/
date: 2025-05-01T12:03:27.555111
status: success
---

# Filter: bricks/dynamic_data/exclude_tags – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/filter-bricks-dynamic_data-exclude_tags/](https://academy.bricksbuilder.io/article/filter-bricks-dynamic_data-exclude_tags/)*

## Table of Contents

- [Filter: bricks/dynamic_data/exclude_tags](#filter-bricksdynamicdataexcludetags)
        - [Filter: bricks/dynamic_data/replace_nonexistent_tags](#filter-bricksdynamicdatareplacenonexistenttags)
        - [Filter: bricks/related_posts/query_vars](#filter-bricksrelatedpostsqueryvars)

## Filter: bricks/dynamic_data/exclude_tags

Dynamic data tags are strings with a special syntax wrapped by curly brackets. Sometimes this syntax has conflicts with other plugins which cause a specific tag to be removed by the content.

Since Bricks 1.3.5 it is possible to exclude a list of tags from the Bricks dynamic data logic using the following PHP snippet in yourfunctions.phpfile:

`functions.php`

```
add_filter( 'bricks/dynamic_data/exclude_tags', function( $tags ) {
    return [
        'my_specific_tag',
        'my_other_specific_tag'
    ];
});
```

`add_filter( 'bricks/dynamic_data/exclude_tags', function( $tags ) {
    return [
        'my_specific_tag',
        'my_other_specific_tag'
    ];
});`

Adding this code to your child theme will prevent Bricks from replacing these tags with an empty string.

###### Filter: bricks/dynamic_data/replace_nonexistent_tags

###### Filter: bricks/related_posts/query_vars

