---
title: "Align Items Control (Flexbox) – Bricks Academy"
url: https://academy.bricksbuilder.io/article/align-items-control/
date: 2025-02-27T15:29:10.693776
status: success
---

# Align Items Control (Flexbox) – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/align-items-control/](https://academy.bricksbuilder.io/article/align-items-control/)*

## Table of Contents

- [Align Items Control (Flexbox)](#align-items-control-flexbox)
        - [Apply Control](#apply-control)
        - [Justify Content Control (Flexbox)](#justify-content-control-flexbox)

## Align Items Control (Flexbox)

Use the align-items control to allow users to set thealign-itemsCSS property (alignment along thecross-axis) of your CSS flexbox layout.

`align-items`

There is also ajustify-contentcontrol to allow users to set the alignment along the main axis of your CSS flexbox layout:

`justify-content`

```
public function set_controls() {
  $this->controls['alignItems'] = [ // Setting key
    'tab'   => 'content',
    'label' => esc_html__( 'Align items', 'bricks' ),
    'type'  => 'align-items',
    'css'   => [
      [
        'property' => 'align-items',
        'selector' => '.flexbox-wrapper',
      ],
    ],
    // 'isHorizontal' => false,
    // 'exclude' => [
      // 'flex-start',
      // 'center',
      // 'flex-end',
      // 'space-between',
      // 'space-around',
      // 'space-evenly',
    // ],
  ];
}
```

`public function set_controls() {
  $this->controls['alignItems'] = [ // Setting key
    'tab'   => 'content',
    'label' => esc_html__( 'Align items', 'bricks' ),
    'type'  => 'align-items',
    'css'   => [
      [
        'property' => 'align-items',
        'selector' => '.flexbox-wrapper',
      ],
    ],
    // 'isHorizontal' => false,
    // 'exclude' => [
      // 'flex-start',
      // 'center',
      // 'flex-end',
      // 'space-between',
      // 'space-around',
      // 'space-evenly',
    // ],
  ];
}`

###### Apply Control

###### Justify Content Control (Flexbox)

