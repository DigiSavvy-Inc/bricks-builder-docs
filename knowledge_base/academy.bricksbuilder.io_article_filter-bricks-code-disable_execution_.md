---
title: "Filter: bricks/code/disable_execution – Bricks Academy"
url: https://academy.bricksbuilder.io/article/filter-bricks-code-disable_execution/
date: 2025-02-27T15:28:56.307008
status: success
---

# Filter: bricks/code/disable_execution – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/filter-bricks-code-disable_execution/](https://academy.bricksbuilder.io/article/filter-bricks-code-disable_execution/)*

## Table of Contents

- [Filter: bricks/code/disable_execution](#filter-brickscodedisableexecution)
        - [Filter: bricks/code/echo_function_names](#filter-brickscodeechofunctionnames)
        - [Filter: bricks/nav_menu/menu](#filter-bricksnavmenumenu)

## Filter: bricks/code/disable_execution

This PHP filter allows you to disable code execution within the Bricks builder programmatically.

It takes precedence over thebricks/code/allow_executionfilter and any settings configured inBricks > Settings > Custom code > Code execution.

`bricks/code/allow_execution`

`Bricks > Settings > Custom code > Code execution`

```
add_filter( 'bricks/code/disable_execution', function( $disable ) {
  // Returning true disables code execution programmatically
  return true;
} );
```

`add_filter( 'bricks/code/disable_execution', function( $disable ) {
  // Returning true disables code execution programmatically
  return true;
} );`

Use this filter to enforce stricter security by disabling code execution, regardless of other configurations on your site.

###### Filter: bricks/code/echo_function_names

###### Filter: bricks/nav_menu/menu

