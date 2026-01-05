---
title: "Text Decoration Control – Bricks Academy"
url: https://academy.bricksbuilder.io/article/text-decoration-control/
date: 2026-01-05T11:08:26.050728
status: success
---

# Text Decoration Control – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/text-decoration-control/](https://academy.bricksbuilder.io/article/text-decoration-control/)*

## Table of Contents

- [Text Decoration Control](#text-decoration-control)
        - [Text Align Control](#text-align-control)
        - [Text Transform Control](#text-transform-control)

## Text Decoration Control

Use thetext-decorationcontrol to allow users to set the text-decoration CSS property like so:

```
public function set_controls() {
  $this->controls['textDecoration'] = [ // Setting key
    'tab' => 'content',
    'label' => esc_html__( 'Text decoration', 'bricks' ),
    'type' => 'text-decoration',
    'css' => [
      [
        'property' => 'text-decoration',
        'selector' => '.text-wrapper',
      ],
    ],
  ];
}
```

`public function set_controls() {
  $this->controls['textDecoration'] = [ // Setting key
    'tab' => 'content',
    'label' => esc_html__( 'Text decoration', 'bricks' ),
    'type' => 'text-decoration',
    'css' => [
      [
        'property' => 'text-decoration',
        'selector' => '.text-wrapper',
      ],
    ],
  ];
}`

###### Text Align Control

###### Text Transform Control

