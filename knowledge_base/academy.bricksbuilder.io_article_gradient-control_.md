---
title: "Gradient Control – Bricks Academy"
url: https://academy.bricksbuilder.io/article/gradient-control/
date: 2025-02-27T15:30:03.878763
status: success
---

# Gradient Control – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/gradient-control/](https://academy.bricksbuilder.io/article/gradient-control/)*

## Table of Contents

- [Gradient Control](#gradient-control)
        - [Filters Control](#filters-control)
        - [Icon Control](#icon-control)

## Gradient Control

The gradient control lets you define an unlimited number of gradients that you can apply to text, background, and as an overlay.

You can set the CSS selector in the control, adjust the angle between 0 and 360°, and set a color stop for each color.

```
class Prefix_Element_Gradient extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleGradient'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Gradient', 'bricks' ),
      'type' => 'gradient',
      'css' => [
        [
          'property' => 'background-image',
        ],
      ],
    ];
  }

  // Render element HTML
  public function render() {
    echo get_bloginfo( 'name' );
  }
}
```

`class Prefix_Element_Gradient extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleGradient'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Gradient', 'bricks' ),
      'type' => 'gradient',
      'css' => [
        [
          'property' => 'background-image',
        ],
      ],
    ];
  }

  // Render element HTML
  public function render() {
    echo get_bloginfo( 'name' );
  }
}`

All sections, rows, columns, and elements already have aCSS Gradientcontrol under the Style tab Gradient / Overlay group.

###### Filters Control

###### Icon Control

