---
title: "Border Control – Bricks Academy"
url: https://academy.bricksbuilder.io/article/border-control/
date: 2026-01-05T11:07:53.529687
status: success
---

# Border Control – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/border-control/](https://academy.bricksbuilder.io/article/border-control/)*

## Table of Contents

- [Border Control](#border-control)
        - [Query Control](#query-control)
        - [Audio Control](#audio-control)

## Border Control

The border control lets you set the following border properties:

- Border width (top/right/bottom/left)
- Background style (top/right/bottom/left)
- Background color (none/solid/double/dotted/dashed)
- Border radius (top/right/bottom/left)

The example below illustrates how to apply a border via thecssparameter and how to set border defaults.

`css`

```
class Builder_Element_Prefix_Test extends \Bricks\Element {
  public function set_controls() {
    $this->controls['titleBorder'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Title border', 'bricks' ),
      'type' => 'border',
      'css' => [
        [
          'property' => 'border',
          'selector' => '.prefix-test-title',
        ],
      ],
      'inline' => true,
      'small' => true,
      'default' => [
        'width' => [
          'top' => 1,
          'right' => 0,
          'bottom' => 0,
          'left' => 0,
        ],
        'style' => 'solid',
        'color' => [
          'hex' => '#ffff00',
        ],
        'radius' => [
          'top' => 1,
          'right' => 1,
          'bottom' => 1,
          'left' => 1,
        ],
      ],


    ];
  }
}
```

`class Builder_Element_Prefix_Test extends \Bricks\Element {
  public function set_controls() {
    $this->controls['titleBorder'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Title border', 'bricks' ),
      'type' => 'border',
      'css' => [
        [
          'property' => 'border',
          'selector' => '.prefix-test-title',
        ],
      ],
      'inline' => true,
      'small' => true,
      'default' => [
        'width' => [
          'top' => 1,
          'right' => 0,
          'bottom' => 0,
          'left' => 0,
        ],
        'style' => 'solid',
        'color' => [
          'hex' => '#ffff00',
        ],
        'radius' => [
          'top' => 1,
          'right' => 1,
          'bottom' => 1,
          'left' => 1,
        ],
      ],


    ];
  }
}`

###### Query Control

###### Audio Control

