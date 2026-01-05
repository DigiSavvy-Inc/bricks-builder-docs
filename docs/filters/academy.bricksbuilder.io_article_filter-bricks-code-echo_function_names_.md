---
title: "Filter: bricks/code/echo_function_names – Bricks Academy"
url: https://academy.bricksbuilder.io/article/filter-bricks-code-echo_function_names/
date: 2026-01-05T11:07:25.578620
status: success
---

# Filter: bricks/code/echo_function_names – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/filter-bricks-code-echo_function_names/](https://academy.bricksbuilder.io/article/filter-bricks-code-echo_function_names/)*

## Table of Contents

- [Filter: bricks/code/echo_function_names](#filter-brickscodeechofunctionnames)
  - [Using patterns (regex) to simplify echo function calls](#using-patterns-regex-to-simplify-echo-function-calls)
  - [Check function names against your own custom logic](#check-function-names-against-your-own-custom-logic)
        - [Filter: bricks/code/allow_execution](#filter-brickscodeallowexecution)
        - [Filter: bricks/code/disable_execution](#filter-brickscodedisableexecution)

## Filter: bricks/code/echo_function_names

Starting at Bricks 1.9.7, you must explicitly allow any function names you want to call via Bricks’ dynamic data echo tag using the new bricks/code/echo_function_names filter. You can add this to your Bricks child theme or the code snippet plugin of your choice.

```
add_filter( 'bricks/code/echo_function_names', function() {
  return [
    'my_custom_function',
    'another_custom_function',
  ];
} );
```

`add_filter( 'bricks/code/echo_function_names', function() {
  return [
    'my_custom_function',
    'another_custom_function',
  ];
} );`

To use echo functions, you must first enable “Code execution” for the appropriate user role or user in your WordPress dashboard under “Bricks – Settings – Custom code” (see the screenshot below).

Make sure to only enable code execution for users & user roles you trust 100%.

You can get a list of all functions on your site called through theechotag as part of the “Code review” results. Here’s how:

`echo`

1. Go toBricks > Settings > Custom code
2. Click the “Start: Code review” button
3. Once finished, select “Echo tags” from the dropdown.
4. Copy the code snippet under “Echo: Function names” and paste it into thefunctions.phpfile of your Bricks child name. Make sure to remove any unknown or unwanted function names from the array.

`Bricks > Settings > Custom code`

`functions.php`

### Using patterns (regex) to simplify echo function calls

Bricks 1.9.8 offers greater flexibility when it comes to echo function calls.

While you can still return an array with the exact function names, you can also return an array that contains specific regex checks. We identify those regex calls by the@prefix.

`@`

If your function name matches any of those regex checks, it can be called through theechotag.

`echo`

Example: Allow calling any functions that start withbrx_:

`brx_`

```
add_filter( 'bricks/code/echo_function_names', function($function_name) {
  return [
    '@^brx_', // Allow all functions that start with "brx_"
  ];
} );
```

`add_filter( 'bricks/code/echo_function_names', function($function_name) {
  return [
    '@^brx_', // Allow all functions that start with "brx_"
  ];
} );`

### Check function names against your own custom logic

Instead of returning an array, you can also perform any custom check against the function name itself or any other logic you want to run. The filter receives the function name ($function_name) as an argument to assist in making more dynamic decisions. Returning a boolean (trueorfalse)

`$function_name`

`true`

`false`

Example: Allow function execution based on function name prefix

```
add_filter('bricks/code/echo_function_names', function($function_name) {
  // Only allow functions that start with "custom_"
  return strpos($function_name, 'custom_') === 0;
});
```

`add_filter('bricks/code/echo_function_names', function($function_name) {
  // Only allow functions that start with "custom_"
  return strpos($function_name, 'custom_') === 0;
});`

This example uses a straightforward check to determine if the function starts withcustom_. If so, it returnstrue, allowing the function to be executed; otherwise, it returnsfalse.

`custom_`

`true`

`false`

Example: Run any function when development mode is enabled

```
add_filter( 'bricks/code/echo_function_names', function($function_name) {
  return defined( 'WP_DEVELOPMENT_MODE' ) ? WP_DEVELOPMENT_MODE : false;
} );
```

`add_filter( 'bricks/code/echo_function_names', function($function_name) {
  return defined( 'WP_DEVELOPMENT_MODE' ) ? WP_DEVELOPMENT_MODE : false;
} );`

TheWP_DEVELOPMENT_MODEPHP constant has been available in WordPress core since version 6.3. We use it just as an example. You can use any custom PHP constant of your choice by defining it in your child theme’s functions.php file.

`WP_DEVELOPMENT_MODE`

Example: Run function if the current user can edit posts

```
add_filter( 'bricks/code/echo_function_names', function($function_name) {
  return current_user_can( 'edit_posts' );
} );
```

`add_filter( 'bricks/code/echo_function_names', function($function_name) {
  return current_user_can( 'edit_posts' );
} );`

###### Filter: bricks/code/allow_execution

###### Filter: bricks/code/disable_execution

