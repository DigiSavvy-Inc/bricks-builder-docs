---
title: "Filter: bricks/posts/merge_query – Bricks Academy"
url: https://academy.bricksbuilder.io/article/filter-bricks-posts-merge_query/
date: 2025-02-27T15:28:11.802264
status: success
---

# Filter: bricks/posts/merge_query – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/filter-bricks-posts-merge_query/](https://academy.bricksbuilder.io/article/filter-bricks-posts-merge_query/)*

## Table of Contents

- [Filter: bricks/posts/merge_query](#filter-brickspostsmergequery)
  - [How to find the element ID?](#how-to-find-the-element-id)
        - [Filter: bricks/element/render_attributes](#filter-brickselementrenderattributes)
        - [Filter: bricks/code/disallow_keywords](#filter-brickscodedisallowkeywords)

## Filter: bricks/posts/merge_query

Since Bricks 1.3.7 you’ll be able to decide if a certain element query should be merged with the WordPress main query, in the archive or search templates, using the following filter:

```
add_filter( 'bricks/posts/merge_query', function( $merge, $element_id ) {
  if ( $element_id === 'wghgco' ) {
    return false;
  }

  return $merge;
}, 10, 2 );
```

`add_filter( 'bricks/posts/merge_query', function( $merge, $element_id ) {
  if ( $element_id === 'wghgco' ) {
    return false;
  }

  return $merge;
}, 10, 2 );`

The filter callback receives two arguments:

- $mergeis a boolean variable indicating whether the query should be merged or not (default: true)
- $element_idis a string containing the element ID

`$merge`

`$element_id`

This is triggered for all the Bricks elements containing one internal WP_Query query like the Posts and the Carousel element, or any other element where the Query Loop is enabled (Container, Slider, Accordion).

Starting from Bricks 1.7, you can achieve the same result by utilizing the “Disable Query Merge” option in theQuery Loop, without the need for a PHP filter. Use this filter for more advanced situations.

### How to find the element ID?

Each element in Bricks has a unique ID. You may find the element ID when editing the element and looking into the Global CSS classes input. By default, it shows the element HTML ID (e.g.#bricks-element-wghgco). For the purpose of this filter, we only need the last portion of the string, the six-character long element ID (e.g.wghgco).

`#bricks-element-wghgco`

`wghgco`

###### Filter: bricks/element/render_attributes

###### Filter: bricks/code/disallow_keywords

