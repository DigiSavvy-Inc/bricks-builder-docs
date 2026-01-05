---
title: "Icon Control – Bricks Academy"
url: https://academy.bricksbuilder.io/article/icon-control/
date: 2026-01-05T11:07:52.206550
status: success
---

# Icon Control – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/icon-control/](https://academy.bricksbuilder.io/article/icon-control/)*

## Table of Contents

- [Icon Control](#icon-control)
        - [Query Control](#query-control)
        - [Audio Control](#audio-control)

## Icon Control

The icon control lets you select and output icons from the following icon font libraries:

- Fontawesome 6
- Ionicons 4
- Themify

The user can also select individually uploaded SVG files if you’ve enabled “SVG Uploads” underBricks > Settingsin your WordPress dashboard, and custom icon sets since Bricks 2.0.

`Bricks > Settings`

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

###### Query Control

###### Audio Control

