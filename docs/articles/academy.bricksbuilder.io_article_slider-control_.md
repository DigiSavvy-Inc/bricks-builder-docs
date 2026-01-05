---
title: "Slider Control – Bricks Academy"
url: https://academy.bricksbuilder.io/article/slider-control/
date: 2026-01-05T11:08:29.516434
status: success
---

# Slider Control – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/slider-control/](https://academy.bricksbuilder.io/article/slider-control/)*

## Table of Contents

- [Slider Control](#slider-control)
    - [Resources](#resources)
        - [Typography Control](#typography-control)
        - [Select Control](#select-control)

## Slider Control

The slider control shows a draggable range input field. Default units arepx,emandrem. You can set the following control parameters:

`px`

`em`

`rem`

- units (array with custom units andmin,max,stepattributes)
- unitless (set tofalsefor plain number)

`min`

`max`

`step`

`false`

```
class Prefix_Element_Slider extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleSliderFontSize'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Font size', 'bricks' ),
      'type' => 'slider',
      'css' => [
        [
          'property' => 'font-size',
        ],
      ],
      'units' => [
        'px' => [
          'min' => 1,
          'max' => 50,
          'step' => 1,
        ],
        'em' => [
          'min' => 1,
          'max' => 20,
          'step' => 0.1,
        ],
      ],
      'default' => '30px',
      'description' => esc_html__( 'Slider adjusts font size via CSS.', 'bricks' ),
    ];
  }

  // Render element HTML
  public function render() {
    echo '<h3>' . get_bloginfo( 'name' ) . '</h3>';
  }
}
```

`class Prefix_Element_Slider extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleSliderFontSize'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Font size', 'bricks' ),
      'type' => 'slider',
      'css' => [
        [
          'property' => 'font-size',
        ],
      ],
      'units' => [
        'px' => [
          'min' => 1,
          'max' => 50,
          'step' => 1,
        ],
        'em' => [
          'min' => 1,
          'max' => 20,
          'step' => 0.1,
        ],
      ],
      'default' => '30px',
      'description' => esc_html__( 'Slider adjusts font size via CSS.', 'bricks' ),
    ];
  }

  // Render element HTML
  public function render() {
    echo '<h3>' . get_bloginfo( 'name' ) . '</h3>';
  }
}`

#### Resources

- https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/range

###### Typography Control

###### Select Control

