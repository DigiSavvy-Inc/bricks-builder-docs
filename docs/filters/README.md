# Bricks Builder Filters

This directory contains documentation for all the filters available in Bricks Builder. Filters allow developers to modify the behavior of Bricks Builder without having to modify the core code.

## What are filters?

Filters are WordPress hooks that allow you to modify data during execution. In the context of Bricks Builder, filters can be used to customize various aspects of the theme's behavior, from modifying element attributes to changing query parameters.

## How to use filters

To use a filter, you'll need to add a function that hooks into the filter using the `add_filter()` WordPress function. For example:

```php
add_filter('bricks/builder/color_palette', function($palette) {
    // Modify the palette array
    return $palette;
});
```

## Available Filters

Browse through the files in this directory to find documentation for specific filters.