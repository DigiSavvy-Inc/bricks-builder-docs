---
title: "Code Control – Bricks Academy"
url: https://academy.bricksbuilder.io/article/code-control/
date: 2026-01-05T11:07:35.915093
status: success
---

# Code Control – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/code-control/](https://academy.bricksbuilder.io/article/code-control/)*

## Table of Contents

- [Code Control](#code-control)
        - [Query Control](#query-control)
        - [Audio Control](#audio-control)

## Code Control

The code control embeds a code editor utilizing the amazing CodeMirror library. Users for which you’ve enabled “Code Execution” in the Bricks settings, will be able to execute PHP, HTML, CSS, and JavaScript.

```
class Prefix_Element_Code extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleHtml'] = [
      'tab' => 'content',
      'label' => esc_html__( 'HTML', 'bricks' ),
      'type' => 'code',
      'mode' => 'php',
      'default' => '<h4>Example H4 HTML title</h4>',
    ];
  }

  // Render element HTML
  public function render() {
    echo isset( $this->settings['exampleHtml'] ) ? $this->settings['exampleHtml'] : esc_html__( 'No HTML provided.', 'bricks' );
  }
}
```

`class Prefix_Element_Code extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleHtml'] = [
      'tab' => 'content',
      'label' => esc_html__( 'HTML', 'bricks' ),
      'type' => 'code',
      'mode' => 'php',
      'default' => '<h4>Example H4 HTML title</h4>',
    ];
  }

  // Render element HTML
  public function render() {
    echo isset( $this->settings['exampleHtml'] ) ? $this->settings['exampleHtml'] : esc_html__( 'No HTML provided.', 'bricks' );
  }
}`

You don’t need to define your own element CSS and JS controls. Those are already available when editing the element under the Style tab “CSS” control group.

###### Query Control

###### Audio Control

