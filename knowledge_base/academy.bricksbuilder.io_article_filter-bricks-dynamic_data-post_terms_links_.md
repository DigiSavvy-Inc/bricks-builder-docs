---
title: "Filter: bricks/dynamic_data/post_terms_links – Bricks Academy"
url: https://academy.bricksbuilder.io/article/filter-bricks-dynamic_data-post_terms_links/
date: 2025-02-27T15:28:38.142221
status: success
---

# Filter: bricks/dynamic_data/post_terms_links – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/filter-bricks-dynamic_data-post_terms_links/](https://academy.bricksbuilder.io/article/filter-bricks-dynamic_data-post_terms_links/)*

## Table of Contents

- [Filter: bricks/dynamic_data/post_terms_links](#filter-bricksdynamicdataposttermslinks)
        - [Filter: bricks/link_css_selectors](#filter-brickslinkcssselectors)
        - [Filter: bricks/is_layout_element](#filter-bricksislayoutelement)

## Filter: bricks/dynamic_data/post_terms_links

When rendering the terms assigned to a post using the dynamic data tag{post_terms_my_taxonomy}, Bricks wraps each term with a link to the term archive page. To disable this default behavior, you may hook into thebricks/dynamic_data/post_terms_linksfilter, like so:

`bricks/dynamic_data/post_terms_links`

```
// Disable links for all the {post_terms_my_taxonomy} tags
add_filter( 'bricks/dynamic_data/post_terms_links', '__return_false' );
```

`// Disable links for all the {post_terms_my_taxonomy} tags
add_filter( 'bricks/dynamic_data/post_terms_links', '__return_false' );`

or, for a specific taxonomy:

```
add_filter( 'bricks/dynamic_data/post_terms_links', function( $has_links, $post, $taxonomy) {
  // Disable links for my_custom_tax taxonomy
  return $taxonomy !== 'my_custom_tax'; 
}, 10, 3);
```

`add_filter( 'bricks/dynamic_data/post_terms_links', function( $has_links, $post, $taxonomy) {
  // Disable links for my_custom_tax taxonomy
  return $taxonomy !== 'my_custom_tax'; 
}, 10, 3);`

###### Filter: bricks/link_css_selectors

###### Filter: bricks/is_layout_element

