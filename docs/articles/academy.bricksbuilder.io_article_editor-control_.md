---
title: "Editor Control – Bricks Academy"
url: https://academy.bricksbuilder.io/article/editor-control/
date: 2026-01-05T11:07:22.268734
status: success
---

# Editor Control – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/editor-control/](https://academy.bricksbuilder.io/article/editor-control/)*

## Table of Contents

- [Editor Control](#editor-control)
        - [Query Control](#query-control)
        - [Audio Control](#audio-control)

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

###### Query Control

###### Audio Control

