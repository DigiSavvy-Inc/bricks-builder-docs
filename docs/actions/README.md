# Bricks Builder Actions

This directory contains documentation for WordPress actions provided by Bricks Builder. Actions allow developers to execute custom code at specific points during the Bricks Builder execution process.

## What are actions?

Actions are WordPress hooks that allow you to execute code at specific points in WordPress and Bricks Builder execution. Unlike filters which modify data, actions are used to trigger functionality.

## How to use actions

To use an action, you'll need to add a function that hooks into the action using the `add_action()` WordPress function. For example:

```php
add_action('bricks_query_before_loop', function($query_obj) {
    // Execute code before query loop
}, 10, 1);
```

## Available Actions

Browse through the files in this directory to find documentation for specific actions.