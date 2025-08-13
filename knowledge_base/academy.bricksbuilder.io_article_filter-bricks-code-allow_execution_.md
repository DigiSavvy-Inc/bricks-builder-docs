---
title: "Filter: bricks/code/allow_execution – Bricks Academy"
url: https://academy.bricksbuilder.io/article/filter-bricks-code-allow_execution/
date: 2025-02-27T15:30:11.263950
status: success
---

# Filter: bricks/code/allow_execution – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/filter-bricks-code-allow_execution/](https://academy.bricksbuilder.io/article/filter-bricks-code-allow_execution/)*

## Table of Contents

- [Filter: bricks/code/allow_execution](#filter-brickscodeallowexecution)
        - [Filter: bricks/builder/image_size_options](#filter-bricksbuilderimagesizeoptions)
        - [Filter: bricks/code/echo_function_names](#filter-brickscodeechofunctionnames)

## Filter: bricks/code/allow_execution

An alternative to theDisable code executionsetting underBricks > Settings > Builder Access. You can use this PHP filter to disable/enable code execution programmatically.

`Bricks > Settings > Builder Access`

```
add_filter( 'bricks/code/allow_execution', function( $allow ) {
  // Only allows to return false to disable code execution programmatically
  return false;
} );
```

`add_filter( 'bricks/code/allow_execution', function( $allow ) {
  // Only allows to return false to disable code execution programmatically
  return false;
} );`

###### Filter: bricks/builder/image_size_options

###### Filter: bricks/code/echo_function_names

