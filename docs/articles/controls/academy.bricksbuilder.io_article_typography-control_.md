---
title: "Typography Control – Bricks Academy"
url: https://academy.bricksbuilder.io/article/typography-control/
date: 2025-05-01T12:03:20.028476
status: success
---

# Typography Control – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/typography-control/](https://academy.bricksbuilder.io/article/typography-control/)*

## Table of Contents

- [Typography Control](#typography-control)
        - [Text Shadow Control](#text-shadow-control)
        - [Apply Control](#apply-control)

## Typography Control

The typography control provides the following CSS properties:

- color
- font-size
- text-align
- text-transform
- font-family
- font-weight
- font-style
- line-height
- letter-spacing
- text-shadow
- text-decoration

Use theexcludeparameter to hide specific typography properties. Setpopupto false to show control inline.

`exclude`

`popup`

```
class Prefix_Element_Typography extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleTypography'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Typography', 'bricks' ),
      'type' => 'typography',
      'css' => [
        [
          'property' => 'typography',
          'selector' => '.prefix-typography',
        ],
      ],
      'inline' => true,
      // 'exclude' => [
      //   'font-family',
      //   'font-weight',
      //   'text-align',
      //   'text-transform',
      //   'font-size',
      //   'line-height',
      //   'letter-spacing',
      //   'color',
      //   'text-shadow',
      // ],
      // 'popup' => false, // Default: true
    ];
  }

  // Render element HTML
  public function render() {
    echo '<h3 class="prefix-typography">' . get_bloginfo( 'name' ) . '</h3>';
  }
}
```

`class Prefix_Element_Typography extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleTypography'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Typography', 'bricks' ),
      'type' => 'typography',
      'css' => [
        [
          'property' => 'typography',
          'selector' => '.prefix-typography',
        ],
      ],
      'inline' => true,
      // 'exclude' => [
      //   'font-family',
      //   'font-weight',
      //   'text-align',
      //   'text-transform',
      //   'font-size',
      //   'line-height',
      //   'letter-spacing',
      //   'color',
      //   'text-shadow',
      // ],
      // 'popup' => false, // Default: true
    ];
  }

  // Render element HTML
  public function render() {
    echo '<h3 class="prefix-typography">' . get_bloginfo( 'name' ) . '</h3>';
  }
}`

###### Text Shadow Control

###### Apply Control

