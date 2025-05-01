---
title: "Filter: bricks/builder/standard_fonts – Bricks Academy"
url: https://academy.bricksbuilder.io/article/filter-standard-fonts/
date: 2025-05-01T12:03:23.804655
status: success
---

# Filter: bricks/builder/standard_fonts – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/filter-standard-fonts/](https://academy.bricksbuilder.io/article/filter-standard-fonts/)*

## Table of Contents

- [Filter: bricks/builder/standard_fonts](#filter-bricksbuilderstandardfonts)
        - [Filter: bricks/builder/save_messages](#filter-bricksbuildersavemessages)
        - [Filter: bricks/builder/elements](#filter-bricksbuilderelements)

## Filter: bricks/builder/standard_fonts

Place and customize the following filter to display a different set of web-safe fonts in the typography control.

```
add_filter( 'bricks/builder/standard_fonts', function( $standard_fonts ) {
  // Option #1: Add individual standard font
  $standard_fonts[] = 'Verdana';

  // Option #2: Replace all standard fonts
  $standard_fonts = [
    'Georgia',
    'Times New Roman',
    'Verdana',
  ];

  return $standard_fonts;
} );
```

###### Filter: bricks/builder/save_messages

###### Filter: bricks/builder/elements

