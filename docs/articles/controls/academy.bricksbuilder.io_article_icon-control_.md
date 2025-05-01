---
title: "Icon Control – Bricks Academy"
url: https://academy.bricksbuilder.io/article/icon-control/
date: 2025-05-01T12:03:03.944624
status: success
---

# Icon Control – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/icon-control/](https://academy.bricksbuilder.io/article/icon-control/)*

## Table of Contents

- [Icon Control](#icon-control)
        - [Gradient Control](#gradient-control)
        - [Image Control](#image-control)

## Icon Control

The icon control lets you select and output icons from the following icon font libraries:

- Fontawesome 6
- Ionicons 4
- Themify

The user can also select individually uploaded SVG files if you’ve enabled “SVG Uploads” under “Bricks > Settings” in your WordPress dashboard.

```
class Prefix_Element_Icon extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleIcon'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Icon', 'bricks' ),
      'type' => 'icon',
      'default' => [
        'library' => 'themify', // fontawesome/ionicons/themify
        'icon' => 'ti-star',    // Example: Themify icon class
      ],
      'css' => [
        [
          'selector' => '.icon-svg', // Use to target SVG file
        ],
      ],
    ];
  }

  // Render element HTML
  public function render() {
    // Set icon 'class' attribute
    if ( isset( $this->settings['exampleIcon'] ) ) {
      Helpers::render_control_icon( $settings['exampleIcon'], ['test-class', 'test-class-2'] );
    }
  }
}
```

`class Prefix_Element_Icon extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleIcon'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Icon', 'bricks' ),
      'type' => 'icon',
      'default' => [
        'library' => 'themify', // fontawesome/ionicons/themify
        'icon' => 'ti-star',    // Example: Themify icon class
      ],
      'css' => [
        [
          'selector' => '.icon-svg', // Use to target SVG file
        ],
      ],
    ];
  }

  // Render element HTML
  public function render() {
    // Set icon 'class' attribute
    if ( isset( $this->settings['exampleIcon'] ) ) {
      Helpers::render_control_icon( $settings['exampleIcon'], ['test-class', 'test-class-2'] );
    }
  }
}`

###### Gradient Control

###### Image Control

