---
title: "Text Align Control – Bricks Academy"
url: https://academy.bricksbuilder.io/article/text-align-control/
date: 2025-05-01T12:02:56.811284
status: success
---

# Text Align Control – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/text-align-control/](https://academy.bricksbuilder.io/article/text-align-control/)*

## Table of Contents

- [Text Align Control](#text-align-control)
        - [Direction Control (Flexbox)](#direction-control-flexbox)
        - [Text Decoration Control](#text-decoration-control)

## Text Align Control

Use thetext-aligncontrol to allow users to set the text-align CSS property like so:

```
public function set_controls() {
  $this->controls['textAlign'] = [ // Setting key
    'tab' => 'content',
    'label' => esc_html__( 'Text align', 'bricks' ),
    'type' => 'text-align',
    'css' => [
      [
        'property' => 'text-align',
        'selector' => '.text-wrapper',
      ],
    ],
  ];
}
```

`public function set_controls() {
  $this->controls['textAlign'] = [ // Setting key
    'tab' => 'content',
    'label' => esc_html__( 'Text align', 'bricks' ),
    'type' => 'text-align',
    'css' => [
      [
        'property' => 'text-align',
        'selector' => '.text-wrapper',
      ],
    ],
  ];
}`

###### Direction Control (Flexbox)

###### Text Decoration Control

