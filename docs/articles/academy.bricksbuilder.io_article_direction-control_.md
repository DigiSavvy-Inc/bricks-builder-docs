---
title: "Direction Control (Flexbox) – Bricks Academy"
url: https://academy.bricksbuilder.io/article/direction-control/
date: 2026-01-05T11:07:14.301259
status: success
---

# Direction Control (Flexbox) – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/direction-control/](https://academy.bricksbuilder.io/article/direction-control/)*

## Table of Contents

- [Direction Control (Flexbox)](#direction-control-flexbox)
        - [Justify Content Control (Flexbox)](#justify-content-control-flexbox)
        - [Text Align Control](#text-align-control)

## Direction Control (Flexbox)

Use the direction control to allow users to set theflex-directionCSS property of your CSS flexbox layout.

`flex-direction`

```
public function set_controls() {
  $this->controls['direction'] = [ // Setting key
    'tab'   => 'content',
    'label' => esc_html__( 'Direction', 'bricks' ),
    'type'  => 'direction',
    'css'   => [
      [
        'property' => 'flex-direction',
        'selector' => '.flexbox-wrapper',
        // 'id'       => '', // Leave 'id' empty to apply to .flexbox-wrapper directly (@since 1.5.6)
      ],
    ],
  ];
}
```

`public function set_controls() {
  $this->controls['direction'] = [ // Setting key
    'tab'   => 'content',
    'label' => esc_html__( 'Direction', 'bricks' ),
    'type'  => 'direction',
    'css'   => [
      [
        'property' => 'flex-direction',
        'selector' => '.flexbox-wrapper',
        // 'id'       => '', // Leave 'id' empty to apply to .flexbox-wrapper directly (@since 1.5.6)
      ],
    ],
  ];
}`

###### Justify Content Control (Flexbox)

###### Text Align Control

