---
title: "Text Control – Bricks Academy"
url: https://academy.bricksbuilder.io/article/text-control/
date: 2025-02-27T15:28:44.222245
status: success
---

# Text Control – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/text-control/](https://academy.bricksbuilder.io/article/text-control/)*

## Table of Contents

- [Text Control](#text-control)
    - [Resources](#resources)
        - [SVG Control](#svg-control)
        - [Textarea Control](#textarea-control)

## Text Control

The text control displays a text input field. You can set the following parameters:

- spellcheck: true/false. (Default: false)
- trigger: ‘keyup’/’enter’. (Default: keyup)
- inlineEditing: Set to true to enable

`spellcheck`

`trigger`

`inlineEditing`

```
class Prefix_Element_Text extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleText'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Text', 'bricks' ),
      'type' => 'text',
      'spellcheck' => true, // Default: false
      // 'trigger' => 'enter', // Default: 'enter'
      'inlineEditing' => true,
      'default' => 'Here goes your text ..',
    ];
  }

  // Render element HTML
  public function render() {
    if ( isset( $this->settings['exampleText'] ) ) {
      echo $this->settings['exampleText'];
    } else {
      esc_html_e( 'No text provided.', 'bricks' );
    }
  }
}
```

`class Prefix_Element_Text extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleText'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Text', 'bricks' ),
      'type' => 'text',
      'spellcheck' => true, // Default: false
      // 'trigger' => 'enter', // Default: 'enter'
      'inlineEditing' => true,
      'default' => 'Here goes your text ..',
    ];
  }

  // Render element HTML
  public function render() {
    if ( isset( $this->settings['exampleText'] ) ) {
      echo $this->settings['exampleText'];
    } else {
      esc_html_e( 'No text provided.', 'bricks' );
    }
  }
}`

#### Resources

- https://developer.mozilla.org/en-US/docs/Web/SVG/Element/svg
- https://css-tricks.com/using-svg/

###### SVG Control

###### Textarea Control

