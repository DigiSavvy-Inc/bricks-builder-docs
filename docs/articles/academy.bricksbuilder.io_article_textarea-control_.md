---
title: "Textarea Control – Bricks Academy"
url: https://academy.bricksbuilder.io/article/textarea-control/
date: 2026-01-05T11:08:02.871789
status: success
---

# Textarea Control – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/textarea-control/](https://academy.bricksbuilder.io/article/textarea-control/)*

## Table of Contents

- [Textarea Control](#textarea-control)
        - [Text Control](#text-control)
        - [Audio Control](#audio-control)

## Textarea Control

The textarea control displays a textarea input field. You can set the following parameters:

- rows(number. Default: 5)
- readonly(true/false. Default: false)
- spellcheck(true/false. Default: false)
- inlineEditing(true to enable)

`rows`

`readonly`

`spellcheck`

`inlineEditing`

```
class Prefix_Element_Textarea extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleTextarea'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Textarea', 'bricks' ),
      'type' => 'textarea',
      // 'readonly' => true, // Default: false
      'rows' => 10, // Default: 5
      'spellcheck' => true, // Default: false
      'inlineEditing' => true,
      'default' => 'Here goes your content ..',
    ];
  }

  // Render element HTML
  public function render() {
    if ( isset( $this->settings['exampleTextarea'] ) ) {
      echo $this->settings['exampleTextarea'];
    } else {
      esc_html_e( 'No text provided.', 'bricks' );
    }
  }
}
```

`class Prefix_Element_Textarea extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleTextarea'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Textarea', 'bricks' ),
      'type' => 'textarea',
      // 'readonly' => true, // Default: false
      'rows' => 10, // Default: 5
      'spellcheck' => true, // Default: false
      'inlineEditing' => true,
      'default' => 'Here goes your content ..',
    ];
  }

  // Render element HTML
  public function render() {
    if ( isset( $this->settings['exampleTextarea'] ) ) {
      echo $this->settings['exampleTextarea'];
    } else {
      esc_html_e( 'No text provided.', 'bricks' );
    }
  }
}`

###### Text Control

###### Audio Control

