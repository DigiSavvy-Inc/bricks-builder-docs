---
title: "Element: Post Content – Bricks Academy"
url: https://academy.bricksbuilder.io/article/element-post-content/
date: 2026-01-05T11:08:51.340389
status: success
---

# Element: Post Content – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/element-post-content/](https://academy.bricksbuilder.io/article/element-post-content/)*

## Table of Contents

- [Element: Post Content](#element-post-content)
  - [How to use the Post Content element](#how-to-use-the-post-content-element)
  - [Fetching Bricks Data with the Post Content element](#fetching-bricks-data-with-the-post-content-element)
  - [Creating different page layouts using the Post Content](#creating-different-page-layouts-using-the-post-content)
        - [Styling Element States & Parts](#styling-element-states--parts)
        - [Builder Mode (Custom)](#builder-mode-custom)

## Element: Post Content

ThePost Contentelement is a placeholder in the builder that tells Bricks to fetch the post content into the layout you’re building.

Since Bricks 1.3.5 you can select the source from which to pull the content:

- WordPress Editor (Gutenberg/Classic editor)
- Bricks Data

TheData Sourcecontrol is only visible when the Post Content element is used in Bricks templates.

If thePost Contentelement is placed in a Page/Post, etc. the WordPress content is fetched by default.

### How to use the Post Content element

Inside the builder, go to the Elements panel and look for thePost Contentelement in the Single elements group or use the element search bar in the panel header. Click or drag the Post Content element onto the canvas.

If the element is inserted when editing a post or page, it will automatically show the WordPress editor content on the canvas unless there is no Page/Post content. That content is also shown on the front end.

This is useful when creating aSingle Post templatein which you want to show the WordPress content (e.g. a single blog post).

### Fetching Bricks Data with the Post Content element

In certain scenarios, you’d like to edit each post with Bricks instead of using the WordPress editor such as when using more complex layouts that aren’t possible with WordPress.

In this case, you need to set theData Sourceto “Bricks” in the Post Content settings:

### Creating different page layouts using the Post Content

When using a Bricks template as your page layout this template is rendered on the frontend instead of the individual page created with Bricks.

If you use thePost Contentelement and set theData Sourceto Bricks, you can design different page templates and still fetch each page content built with Bricks.

A common use case would be to build a page template with two areas: the main area (which is populated with the page content), and a fixed sidebar for all the pages.

To get the Bricks-built content of each page, the Data Source of the Post Content element needs to be set to “Bricks”:

###### Styling Element States & Parts

###### Builder Mode (Custom)

