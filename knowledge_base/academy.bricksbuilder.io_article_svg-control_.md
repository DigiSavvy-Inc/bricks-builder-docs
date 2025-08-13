---
title: "SVG Control – Bricks Academy"
url: https://academy.bricksbuilder.io/article/svg-control/
date: 2025-02-27T15:29:24.022002
status: success
---

# SVG Control – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/svg-control/](https://academy.bricksbuilder.io/article/svg-control/)*

## Table of Contents

- [SVG Control](#svg-control)
    - [Resources](#resources)
        - [Slider Control](#slider-control)
        - [Text Control](#text-control)

## SVG Control

The SVG control lets you select an SVG (Scalable Vector Graphic) file from the media library. The selected SVG returns an array with the following keys:

- id(media library item ID)
- filename
- url

`id`

`filename`

`url`

We recommend rendering the SVG inline as shown in the code example below. This way you can easily customize it via CSS.

```
class Prefix_Element_Svg extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleSvg'] = [
      'tab' => 'content',
      'type' => 'svg',
    ];
  }

  // Render element HTML
  public function render() {
    if ( isset( $this->settings['exampleSvg']['url'] ) ) {
      echo file_get_contents( esc_url( $this->settings['exampleSvg']['url'] ) );
    } else {
      esc_html_e( 'No SVG selected.', 'bricks' );
    }
  }
}
```

`class Prefix_Element_Svg extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleSvg'] = [
      'tab' => 'content',
      'type' => 'svg',
    ];
  }

  // Render element HTML
  public function render() {
    if ( isset( $this->settings['exampleSvg']['url'] ) ) {
      echo file_get_contents( esc_url( $this->settings['exampleSvg']['url'] ) );
    } else {
      esc_html_e( 'No SVG selected.', 'bricks' );
    }
  }
}`

#### Resources

- https://developer.mozilla.org/en-US/docs/Web/SVG/Element/svg
- https://css-tricks.com/using-svg/

###### Slider Control

###### Text Control

