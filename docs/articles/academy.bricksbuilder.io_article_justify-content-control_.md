---
title: "Justify Content Control (Flexbox) – Bricks Academy"
url: https://academy.bricksbuilder.io/article/justify-content-control/
date: 2026-01-05T11:07:21.538176
status: success
---

# Justify Content Control (Flexbox) – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/justify-content-control/](https://academy.bricksbuilder.io/article/justify-content-control/)*

## Table of Contents

- [Justify Content Control (Flexbox)](#justify-content-control-flexbox)
        - [Align Items Control (Flexbox)](#align-items-control-flexbox)
        - [Direction Control (Flexbox)](#direction-control-flexbox)

## Justify Content Control (Flexbox)

Use the justify-content control to allow users to set thejustify-contentCSS property (alignment along themain-axis) of your CSS flexbox layout.

`justify-content`

There is also aalign-itemscontrol to allow users to set the alignment along the cross axis of your CSS flexbox layout:

`align-items`

```
public function set_controls() {
  $this->controls['justifyContent'] = [
    'tab'   => 'content',
    'label' => esc_html__( 'Justify content', 'bricks' ),
    'type'  => 'justify-content',
    'css'   => [
      [
        'property' => 'justify-content',
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
  $this->controls['justifyContent'] = [
    'tab'   => 'content',
    'label' => esc_html__( 'Justify content', 'bricks' ),
    'type'  => 'justify-content',
    'css'   => [
      [
        'property' => 'justify-content',
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

###### Align Items Control (Flexbox)

###### Direction Control (Flexbox)

