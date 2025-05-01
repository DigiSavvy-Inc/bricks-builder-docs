---
title: "Checkbox Control – Bricks Academy"
url: https://academy.bricksbuilder.io/article/checkbox-control/
date: 2025-05-01T12:03:04.942507
status: success
---

# Checkbox Control – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/checkbox-control/](https://academy.bricksbuilder.io/article/checkbox-control/)*

## Table of Contents

- [Checkbox Control](#checkbox-control)
        - [Box Shadow Control](#box-shadow-control)
        - [Code Control](#code-control)

## Checkbox Control

The checkbox control is a simple on/off switch. If enabled it outputs a boolean value oftrue. Disabled it returnsfalse. You can use it to conditionally show/hide other content settings as we illustrate in the following code example:

`true`

`false`

```
class Prefix_Element_Checkbox extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleCheckbox'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Show site title', 'bricks' ),
      'type' => 'checkbox',
      'inline' => true,
      'small' => true,
      'default' => true, // Default: false
    ];
  }

  // Render element HTML
  public function render() {
    // Show site title if setting checkbox 'exampleCheckbox' is checked
    if ( isset( $this->settings['exampleCheckbox'] ) ) {
      echo get_bloginfo( 'name' );
    }
  }
}
```

###### Box Shadow Control

###### Code Control

