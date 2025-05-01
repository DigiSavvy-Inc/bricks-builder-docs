---
title: "Text Transform Control – Bricks Academy"
url: https://academy.bricksbuilder.io/article/text-transform-control/
date: 2025-05-01T12:02:45.041395
status: success
---

# Text Transform Control – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/text-transform-control/](https://academy.bricksbuilder.io/article/text-transform-control/)*

## Table of Contents

- [Text Transform Control](#text-transform-control)
        - [Text Decoration Control](#text-decoration-control)

## Text Transform Control

Use thetext-transformcontrol to allow users to set the text-transform CSS property like so:

```
public function set_controls() {
  $this->controls['textTransform'] = [ // Setting key
    'tab' => 'content',
    'label' => esc_html__( 'Text transform', 'bricks' ),
    'type' => 'text-transform',
    'css' => [
      [
        'property' => 'text-transform',
        'selector' => '.text-wrapper',
      ],
    ],
  ];
}
```

`public function set_controls() {
  $this->controls['textTransform'] = [ // Setting key
    'tab' => 'content',
    'label' => esc_html__( 'Text transform', 'bricks' ),
    'type' => 'text-transform',
    'css' => [
      [
        'property' => 'text-transform',
        'selector' => '.text-wrapper',
      ],
    ],
  ];
}`

###### Text Decoration Control

