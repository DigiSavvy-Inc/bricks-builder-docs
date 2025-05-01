---
title: "Info Control – Bricks Academy"
url: https://academy.bricksbuilder.io/article/info-control/
date: 2025-05-01T12:03:10.845758
status: success
---

# Info Control – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/info-control/](https://academy.bricksbuilder.io/article/info-control/)*

## Table of Contents

- [Info Control](#info-control)
        - [Image Gallery Control](#image-gallery-control)
        - [Link Control](#link-control)

## Info Control

The info control does not affect the HTML or CSS on the frontend. It serves as a builder-only helper controls to provide additional information.

Example below: theAlertelement displays an info control when theTypeis set toCustom.

```
class Prefix_Element_Info extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['type'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Type', 'bricks' ),
      'type' => 'select',
      'options' => [
        'info' => esc_html__( 'Info', 'bricks' ),
        'success' => esc_html__( 'Success', 'bricks' ),
        'warning' => esc_html__( 'Warning', 'bricks' ),
        'danger' => esc_html__( 'Danger', 'bricks' ),
        'muted' => esc_html__( 'Muted', 'bricks' ),
        'custom' => esc_html__( 'Custom', 'bricks' ),
      ],
      'inline' => true,
      'clearable' => false,
      'pasteStyles' => false,
      'default' => 'info',
    ];

    $this->controls['typeInfo'] = [
      'tab' => 'content',
      'content' => esc_html__( 'Customize alert in STYLE tab.', 'bricks' ),
      'type' => 'info',
      'required' => ['type', '=', 'custom'], // Show info control if 'type' = 'custom'
    ];
  }
}
```

`class Prefix_Element_Info extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['type'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Type', 'bricks' ),
      'type' => 'select',
      'options' => [
        'info' => esc_html__( 'Info', 'bricks' ),
        'success' => esc_html__( 'Success', 'bricks' ),
        'warning' => esc_html__( 'Warning', 'bricks' ),
        'danger' => esc_html__( 'Danger', 'bricks' ),
        'muted' => esc_html__( 'Muted', 'bricks' ),
        'custom' => esc_html__( 'Custom', 'bricks' ),
      ],
      'inline' => true,
      'clearable' => false,
      'pasteStyles' => false,
      'default' => 'info',
    ];

    $this->controls['typeInfo'] = [
      'tab' => 'content',
      'content' => esc_html__( 'Customize alert in STYLE tab.', 'bricks' ),
      'type' => 'info',
      'required' => ['type', '=', 'custom'], // Show info control if 'type' = 'custom'
    ];
  }
}`

###### Image Gallery Control

###### Link Control

