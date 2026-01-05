---
title: "Repeater Control – Bricks Academy"
url: https://academy.bricksbuilder.io/article/repeater-control/
date: 2026-01-05T11:07:29.651199
status: success
---

# Repeater Control – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/repeater-control/](https://academy.bricksbuilder.io/article/repeater-control/)*

## Table of Contents

- [Repeater Control](#repeater-control)
        - [Typography Control](#typography-control)
        - [Filters Control](#filters-control)

## Repeater Control

The repeater control lets you create repeatable fields. Fields can be cloned, deleted, and sorted via Drag & Drop. Use thefieldsargument to set up the field controls.

`fields`

```
class Prefix_Element_Posts extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleRepeater'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Repeater', 'bricks' ),
      'type' => 'repeater',
      'titleProperty' => 'title', // Default 'title'
      'default' => [
        [
          'title' => 'Design',
          'description' => 'Here goes the description for repeater item.',
        ],
        [
          'title' => 'Code',
          'description' => 'Here goes the description for repeater item.',
        ],
        [
          'title' => 'Launch',
          'description' => 'Here goes the description for repeater item.',
        ],
      ],
      'placeholder' => esc_html__( 'Title placeholder', 'bricks' ),
      'fields' => [
        'title' => [
          'label' => esc_html__( 'Title', 'bricks' ),
          'type' => 'text',
        ],
        'description' => [
          'label' => esc_html__( 'Description', 'bricks' ),
          'type' => 'textarea',
        ],
      ],
    ];
  }

  // Render element HTML
  public function render() {
    $items = $this->settings['exampleRepeater'];

    if ( count( $items ) ) {
      foreach ( $items as $item ) {
        echo '<h4>' . $item['title'] . '</h4>';
        echo '<p>' . $item['description'] . '</p>';
      }
    } else {
      esc_html_e( 'No items defined.', 'bricks' );
    }
  }
}
```

`class Prefix_Element_Posts extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleRepeater'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Repeater', 'bricks' ),
      'type' => 'repeater',
      'titleProperty' => 'title', // Default 'title'
      'default' => [
        [
          'title' => 'Design',
          'description' => 'Here goes the description for repeater item.',
        ],
        [
          'title' => 'Code',
          'description' => 'Here goes the description for repeater item.',
        ],
        [
          'title' => 'Launch',
          'description' => 'Here goes the description for repeater item.',
        ],
      ],
      'placeholder' => esc_html__( 'Title placeholder', 'bricks' ),
      'fields' => [
        'title' => [
          'label' => esc_html__( 'Title', 'bricks' ),
          'type' => 'text',
        ],
        'description' => [
          'label' => esc_html__( 'Description', 'bricks' ),
          'type' => 'textarea',
        ],
      ],
    ];
  }

  // Render element HTML
  public function render() {
    $items = $this->settings['exampleRepeater'];

    if ( count( $items ) ) {
      foreach ( $items as $item ) {
        echo '<h4>' . $item['title'] . '</h4>';
        echo '<p>' . $item['description'] . '</p>';
      }
    } else {
      esc_html_e( 'No items defined.', 'bricks' );
    }
  }
}`

###### Typography Control

###### Filters Control

