---
title: "Color Control – Bricks Academy"
url: https://academy.bricksbuilder.io/article/color-control/
date: 2025-05-01T12:02:41.764685
status: success
---

# Color Control – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/color-control/](https://academy.bricksbuilder.io/article/color-control/)*

## Table of Contents

- [Color Control](#color-control)
    - [Color palette filter](#color-palette-filter)
        - [Code Control](#code-control)
        - [Datepicker Control](#datepicker-control)

## Color Control

The color control is a custom-built color picker that you won’t find anywhere else.

It lets you pick and adjust colors inhex,rgbaandhslformat. It also includes a global color palette to save any color for later reuse anywhere else on your site.

`hex`

`rgba`

`hsl`

Define your own default color palette with thebricks/builder/color_palettefilter.

`bricks/builder/color_palette`

You can set the CSSpropertytocolororbackground-coloras illustrated in the example below.

`property`

`color`

`background-color`

```
class Prefix_Element_Color extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    // Text color applied to '.prefix-element-test-title'
    $this->controls['exampleColor'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Title color', 'bricks' ),
      'type' => 'color',
      'inline' => true,
      'css' => [
        [
          'property' => 'color',
          'selector' => '.prefix-element-test-title',
        ]
      ],
      'default' => [
        'hex' => '#3ce77b',
        'rgb' => 'rgba(60, 231, 123, 0.9)',
      ],
    ];

    // Background color applied to '.prefix-element-test-content'
    $this->controls['exampleBackgroundColor'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Background color', 'bricks' ),
      'type' => 'color',
      'inline' => true,
      'css' => [
        [
          'property' => 'background-color',
          'selector' => '.prefix-element-test-content',
        ]
      ],
      'default' => [
        'hex' => '#1ebea5',
        'rgb' => 'rgba(30, 190, 165, 0.8)',
      ],
    ];
  }

  // Render element HTML
  public function render() {
    echo '<h5 class="prefix-element-test-title">' . get_bloginfo( 'name' ) . '</h5>';
    echo '<p class="prefix-element-test-content">Just some bogus text ..</p>';
  }
}

```

`class Prefix_Element_Color extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    // Text color applied to '.prefix-element-test-title'
    $this->controls['exampleColor'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Title color', 'bricks' ),
      'type' => 'color',
      'inline' => true,
      'css' => [
        [
          'property' => 'color',
          'selector' => '.prefix-element-test-title',
        ]
      ],
      'default' => [
        'hex' => '#3ce77b',
        'rgb' => 'rgba(60, 231, 123, 0.9)',
      ],
    ];

    // Background color applied to '.prefix-element-test-content'
    $this->controls['exampleBackgroundColor'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Background color', 'bricks' ),
      'type' => 'color',
      'inline' => true,
      'css' => [
        [
          'property' => 'background-color',
          'selector' => '.prefix-element-test-content',
        ]
      ],
      'default' => [
        'hex' => '#1ebea5',
        'rgb' => 'rgba(30, 190, 165, 0.8)',
      ],
    ];
  }

  // Render element HTML
  public function render() {
    echo '<h5 class="prefix-element-test-title">' . get_bloginfo( 'name' ) . '</h5>';
    echo '<p class="prefix-element-test-content">Just some bogus text ..</p>';
  }
}
`

#### Color palette filter

Add the following PHP code into the funcions.php file of yourchild themeto add your own colors to the default color palette (option #1) or replace all default colors with your own choice of colors (option #2).

```
// functions.php
add_filter( 'bricks/builder/color_palette', function( $colors ) {
  // Option #1: Add individual color
  $colors[] = [
    'hex' => '#3ce77b',
    'rgb' => 'rgba(60, 231, 123, 0.56)',
  ];

  // Option #2: Override entire color palette
  $colors = [
    ['hex' => '#3ce77b'],
    ['hex' => '#f1faee'],
    ['hex' => '#a8dadc'],
    ['hex' => '#457b9d'],
    ['hex' => '#1d3557'],
  ];

  return $colors;
} );
```

`// functions.php
add_filter( 'bricks/builder/color_palette', function( $colors ) {
  // Option #1: Add individual color
  $colors[] = [
    'hex' => '#3ce77b',
    'rgb' => 'rgba(60, 231, 123, 0.56)',
  ];

  // Option #2: Override entire color palette
  $colors = [
    ['hex' => '#3ce77b'],
    ['hex' => '#f1faee'],
    ['hex' => '#a8dadc'],
    ['hex' => '#457b9d'],
    ['hex' => '#1d3557'],
  ];

  return $colors;
} );`

If you have saved any custom colors with the builder you need to reset your global settings in order for your new default colors to take effect.

###### Code Control

###### Datepicker Control

