---
title: "Editor Control – Bricks Academy"
url: https://academy.bricksbuilder.io/article/editor-control/
date: 2025-02-27T15:28:09.413998
status: success
---

# Editor Control – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/editor-control/](https://academy.bricksbuilder.io/article/editor-control/)*

## Table of Contents

- [Editor Control](#editor-control)
        - [Dimensions Control](#dimensions-control)
        - [Filters Control](#filters-control)

## Editor Control

The editor control provides the default WordPress editor. To directly edit content in the builder preview set theinlineEditingproperties. See the code example below:

`inlineEditing`

```
class Prefix_Element_Editor extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleEditor'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Text editor', 'bricks' ),
      'type' => 'editor',
      'inlineEditing' => [
        'selector' => '.text-editor', // Mount inline editor to this CSS selector
        'toolbar' => true, // Enable/disable inline editing toolbar
      ],
      'default' => esc_html__( 'Here goes the content ..', 'bricks' ),
    ];
  }

  // Render element HTML
  public function render() {
    if ( isset( $this->settings['exampleEditor'] ) ) {
      echo '<div class="text-editor">' . $this->settings['exampleEditor'] . '</div>';
    }
  }
}
```

`class Prefix_Element_Editor extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleEditor'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Text editor', 'bricks' ),
      'type' => 'editor',
      'inlineEditing' => [
        'selector' => '.text-editor', // Mount inline editor to this CSS selector
        'toolbar' => true, // Enable/disable inline editing toolbar
      ],
      'default' => esc_html__( 'Here goes the content ..', 'bricks' ),
    ];
  }

  // Render element HTML
  public function render() {
    if ( isset( $this->settings['exampleEditor'] ) ) {
      echo '<div class="text-editor">' . $this->settings['exampleEditor'] . '</div>';
    }
  }
}`

###### Dimensions Control

###### Filters Control

