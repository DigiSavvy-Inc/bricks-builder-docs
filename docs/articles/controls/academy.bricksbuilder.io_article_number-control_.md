---
title: "Number Control – Bricks Academy"
url: https://academy.bricksbuilder.io/article/number-control/
date: 2025-05-01T12:03:03.625433
status: success
---

# Number Control – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/number-control/](https://academy.bricksbuilder.io/article/number-control/)*

## Table of Contents

- [Number Control](#number-control)
        - [Link Control](#link-control)
        - [Query Control](#query-control)

## Number Control

The number control represents a simple number input field. It has the following custom properties:

- units (optional: boolean or array)
- unit (string:px,em,remetc.)
- min (number)
- step (Default: 1) (Custom: ‘0.1’ etc.)

`px`

`em`

`rem`

Use it to render a number to the page or set thecsscontrol property to target a specific CSS style.

`css`

```
class Prefix_Element_Number extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleNumber'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Number', 'bricks' ),
      'type' => 'number',
      'min' => 0,
      'step' => '0.1', // Default: 1
      'inline' => true,
      'default' => 123,
    ];

    $this->controls['examplePadding'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Padding in px', 'bricks' ),
      'type' => 'number',
      'unit' => 'px',
      'inline' => true,
      'css' => [
        [
          'property' => 'padding',
        ],
      ],
      'default' => 33,
    ];
  }

  // Render element HTML
  public function render() {
    if ( isset( $this->settings['exampleNumber'] ) ) {
      echo esc_html__( 'Number: ', 'bricks' ) . $this->settings['exampleNumber'];
    } else {
      esc_html_e( 'No number provided.', 'bricks' );
    }
  }
}
```

`class Prefix_Element_Number extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleNumber'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Number', 'bricks' ),
      'type' => 'number',
      'min' => 0,
      'step' => '0.1', // Default: 1
      'inline' => true,
      'default' => 123,
    ];

    $this->controls['examplePadding'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Padding in px', 'bricks' ),
      'type' => 'number',
      'unit' => 'px',
      'inline' => true,
      'css' => [
        [
          'property' => 'padding',
        ],
      ],
      'default' => 33,
    ];
  }

  // Render element HTML
  public function render() {
    if ( isset( $this->settings['exampleNumber'] ) ) {
      echo esc_html__( 'Number: ', 'bricks' ) . $this->settings['exampleNumber'];
    } else {
      esc_html_e( 'No number provided.', 'bricks' );
    }
  }
}`

###### Link Control

###### Query Control

