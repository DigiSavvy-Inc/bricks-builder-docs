---
title: "Filter: bricks/builder/save_messages – Bricks Academy"
url: https://academy.bricksbuilder.io/article/filter-save-messages/
date: 2025-02-27T15:28:47.854220
status: success
---

# Filter: bricks/builder/save_messages – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/filter-save-messages/](https://academy.bricksbuilder.io/article/filter-save-messages/)*

## Table of Contents

- [Filter: bricks/builder/save_messages](#filter-bricksbuildersavemessages)
        - [Filter: bricks/builder/map_styles](#filter-bricksbuildermapstyles)
        - [Filter: bricks/builder/standard_fonts](#filter-bricksbuilderstandardfonts)

## Filter: bricks/builder/save_messages

Place and customize the following filter to display different save message every time you manually save your progress when editing with Bricks.

```
add_filter( 'bricks/builder/save_messages', function( $messages ) {
  // Option #1: Append individual save message to existing message collection
    $messages[] = 'Yasss';

  // Option #2: Replace all existing builder save messages
    $messages = [
      'Done',
      'Cool',
      'High five!',
    ];

  return $messages;
} );
```

###### Filter: bricks/builder/map_styles

###### Filter: bricks/builder/standard_fonts

