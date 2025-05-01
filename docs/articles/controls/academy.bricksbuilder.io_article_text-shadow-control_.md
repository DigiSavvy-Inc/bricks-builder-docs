---
title: "Text Shadow Control – Bricks Academy"
url: https://academy.bricksbuilder.io/article/text-shadow-control/
date: 2025-05-01T12:02:44.029555
status: success
---

# Text Shadow Control – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/text-shadow-control/](https://academy.bricksbuilder.io/article/text-shadow-control/)*

## Table of Contents

- [Text Shadow Control](#text-shadow-control)
    - [Resources](#resources)
        - [Textarea Control](#textarea-control)
        - [Typography Control](#typography-control)

## Text Shadow Control

The text-shadow control displays a popup that lets you set the CSS text-shadow of a specified HTML text element.

```
class Prefix_Element_Textarea extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleTextShadow'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Text Shadow', 'bricks' ),
      'type' => 'text-shadow',
      'css' => [
        [
          'property' => 'text-shadow',
          'selector' => '.prefix-text',
        ],
      ],
      'inline' => true,
    ];
  }

  // Render element HTML
  public function render() {
    echo '<h3 class="prefix-text">' . get_bloginfo( 'name' ) . '</h3>';
  }
}
```

`class Prefix_Element_Textarea extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleTextShadow'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Text Shadow', 'bricks' ),
      'type' => 'text-shadow',
      'css' => [
        [
          'property' => 'text-shadow',
          'selector' => '.prefix-text',
        ],
      ],
      'inline' => true,
    ];
  }

  // Render element HTML
  public function render() {
    echo '<h3 class="prefix-text">' . get_bloginfo( 'name' ) . '</h3>';
  }
}`

#### Resources

https://developer.mozilla.org/en-US/docs/Web/CSS/text-shadow

###### Textarea Control

###### Typography Control

