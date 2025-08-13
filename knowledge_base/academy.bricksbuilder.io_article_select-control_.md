---
title: "Select Control – Bricks Academy"
url: https://academy.bricksbuilder.io/article/select-control/
date: 2025-02-27T15:28:03.489313
status: success
---

# Select Control – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/select-control/](https://academy.bricksbuilder.io/article/select-control/)*

## Table of Contents

- [Select Control](#select-control)
        - [Repeater Control](#repeater-control)
        - [Slider Control](#slider-control)

## Select Control

The select control lets you select an option from a dropdown. It can be used to render content or CSS styling. Use the options array to populate the dropdown with your own options. The option key should be all lowercase, with no spaces.

```
class Prefix_Element_Posts extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    // Example content 
    $this->controls['exampleSelectTitleTag'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Title tag', 'bricks' ),
      'type' => 'select',
      'options' => [
        'h1' => 'H1',
        'h2' => 'H2',
        'h3' => 'H3',
        'h4' => 'H4',
        'h5' => 'H5',
        'h6' => 'H6',
      ],
      'inline' => true,
      'placeholder' => esc_html__( 'Select tag', 'bricks' ),
      'multiple' => true, 
      'searchable' => true,
      'clearable' => true,
      'default' => 'h3',
    ];

    // Example CSS
    $this->controls['exampleSelectTextAlign'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Text align', 'bricks' ),
      'type' => 'select',
      'options' => [
        'right' => esc_html__( 'Right', 'bricks' ),
        'center' => esc_html__( 'Center', 'bricks' ),
        'left' => esc_html__( 'Left', 'bricks' ),
      ],
      'inline' => true,
      'css' => [
        [
          'property' => 'text-align',
          'selector' => '.prefix-title',
        ],
      ],
      'placeholder' => esc_html__( 'Select', 'bricks' ),
      'default' => 'center', // Option key
    ];
  }

  // Render element HTML
  public function render() {
    $title_tag = isset( $this->settings['exampleSelectTitleTag'] ) ? $this->settings['exampleSelectTitleTag'] : 'h5';
    echo '<' . $title_tag . ' class="prefix-title">' . get_bloginfo( 'name' ) . '</' . $title_tag . '>';
  }
}
```

`class Prefix_Element_Posts extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    // Example content 
    $this->controls['exampleSelectTitleTag'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Title tag', 'bricks' ),
      'type' => 'select',
      'options' => [
        'h1' => 'H1',
        'h2' => 'H2',
        'h3' => 'H3',
        'h4' => 'H4',
        'h5' => 'H5',
        'h6' => 'H6',
      ],
      'inline' => true,
      'placeholder' => esc_html__( 'Select tag', 'bricks' ),
      'multiple' => true, 
      'searchable' => true,
      'clearable' => true,
      'default' => 'h3',
    ];

    // Example CSS
    $this->controls['exampleSelectTextAlign'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Text align', 'bricks' ),
      'type' => 'select',
      'options' => [
        'right' => esc_html__( 'Right', 'bricks' ),
        'center' => esc_html__( 'Center', 'bricks' ),
        'left' => esc_html__( 'Left', 'bricks' ),
      ],
      'inline' => true,
      'css' => [
        [
          'property' => 'text-align',
          'selector' => '.prefix-title',
        ],
      ],
      'placeholder' => esc_html__( 'Select', 'bricks' ),
      'default' => 'center', // Option key
    ];
  }

  // Render element HTML
  public function render() {
    $title_tag = isset( $this->settings['exampleSelectTitleTag'] ) ? $this->settings['exampleSelectTitleTag'] : 'h5';
    echo '<' . $title_tag . ' class="prefix-title">' . get_bloginfo( 'name' ) . '</' . $title_tag . '>';
  }
}`

###### Repeater Control

###### Slider Control

