---
title: "Function: bricks_render_dynamic_data – Bricks Academy"
url: https://academy.bricksbuilder.io/article/function-bricks_render_dynamic_data/
date: 2025-02-27T15:28:15.491409
status: success
---

# Function: bricks_render_dynamic_data – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/function-bricks_render_dynamic_data/](https://academy.bricksbuilder.io/article/function-bricks_render_dynamic_data/)*

## Table of Contents

- [Function: bricks_render_dynamic_data](#function-bricksrenderdynamicdata)
    - [Parameters:](#parameters)
    - [Return:](#return)

## Function: bricks_render_dynamic_data

This helper function will render the dynamic data tags inside of a content string (@since 1.5.5).

```
echo bricks_render_dynamic_data( $content, $post_id, $context ); 
```

`echo bricks_render_dynamic_data( $content, $post_id, $context ); `

#### Parameters:

- $content– a string containing dynamic data tags (required)
- $post_id– the post id if needed (default: current post id)
- $context– the context where the data is used after rendered:text,link,image,media(default:text)

`$content`

`$post_id`

`$context`

#### Return:

The string after replacing the dynamic data tags with their content.

Example:

```
echo bricks_render_dynamic_data('My Post Title: {post_title}'); 
```

`echo bricks_render_dynamic_data('My Post Title: {post_title}'); `

