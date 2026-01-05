---
title: "Filter: bricks/nav_menu/menu – Bricks Academy"
url: https://academy.bricksbuilder.io/article/filter-bricks-nav_menu-menu/
date: 2026-01-05T11:08:06.900827
status: success
---

# Filter: bricks/nav_menu/menu – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/filter-bricks-nav_menu-menu/](https://academy.bricksbuilder.io/article/filter-bricks-nav_menu-menu/)*

## Table of Contents

- [Filter: bricks/nav_menu/menu](#filter-bricksnavmenumenu)
        - [Filter: bricks/code/disable_execution](#filter-brickscodedisableexecution)
        - [Filter: bricks/pagination/custom_logic](#filter-brickspaginationcustomlogic)

## Filter: bricks/nav_menu/menu

Thebricks/nav_menu/menufilter allows you to modify the navigation menu dynamically in Bricks Builder based on your conditions.

`bricks/nav_menu/menu`

In the following example, we’ll demonstrate how to change the navigation menu if the user is logged in.

This can be useful for displaying different menus to guests and logged-in users without using multiple Nab Menu elements and Bricks conditions.

Example:Use “My Account Menu” on the “Nav Menu” element (id:kybsde) if the user is logged in.

`kybsde`

You can retrieve the menu ID via the URL parameter after selecting it.

```
add_filter( 'bricks/nav_menu/menu', function( $menu, $post_id, $element ) {
  // Only target this nav menu element
  if( $element['id'] !== 'kdkdge' ) {
    return $menu;
  }

  // If logged-in, use the menu ID 4
  if( is_user_logged_in() ) {
    $menu = 4;
  }

  return $menu;
}, 10, 3 );
```

`add_filter( 'bricks/nav_menu/menu', function( $menu, $post_id, $element ) {
  // Only target this nav menu element
  if( $element['id'] !== 'kdkdge' ) {
    return $menu;
  }

  // If logged-in, use the menu ID 4
  if( is_user_logged_in() ) {
    $menu = 4;
  }

  return $menu;
}, 10, 3 );`

###### Filter: bricks/code/disable_execution

###### Filter: bricks/pagination/custom_logic

