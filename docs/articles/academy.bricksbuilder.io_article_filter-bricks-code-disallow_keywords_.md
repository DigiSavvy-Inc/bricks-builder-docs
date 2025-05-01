---
title: "Filter: bricks/code/disallow_keywords – Bricks Academy"
url: https://academy.bricksbuilder.io/article/filter-bricks-code-disallow_keywords/
date: 2025-05-01T12:03:27.215507
status: success
---

# Filter: bricks/code/disallow_keywords – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/filter-bricks-code-disallow_keywords/](https://academy.bricksbuilder.io/article/filter-bricks-code-disallow_keywords/)*

## Table of Contents

- [Filter: bricks/code/disallow_keywords](#filter-brickscodedisallowkeywords)
        - [Filter: bricks/posts/merge_query](#filter-brickspostsmergequery)
        - [Filter: bricks/assets/load_webfonts](#filter-bricksassetsloadwebfonts)

## Filter: bricks/code/disallow_keywords

This filter introduces another level of security when using the Code element to run code.

With the filterbricks/code/disallow_keywordsyou’ll be able to prevent the code execution if specifickeywords are found in the code, thus reducing the risk of using this element. To addkeywords to this check, use the following example:

`bricks/code/disallow_keywords`

```
add_filter( 'bricks/code/disallow_keywords', function( $keywords ) {
  $keywords[] = 'wpdb';
  
  return $keywords;
} );
```

`add_filter( 'bricks/code/disallow_keywords', function( $keywords ) {
  $keywords[] = 'wpdb';
  
  return $keywords;
} );`

###### Filter: bricks/posts/merge_query

###### Filter: bricks/assets/load_webfonts

