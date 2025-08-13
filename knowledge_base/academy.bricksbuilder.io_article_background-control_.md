---
title: "Background Control – Bricks Academy"
url: https://academy.bricksbuilder.io/article/background-control/
date: 2025-02-27T15:27:50.444839
status: success
---

# Background Control – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/background-control/](https://academy.bricksbuilder.io/article/background-control/)*

## Table of Contents

- [Background Control](#background-control)
        - [Audio Control](#audio-control)
        - [Border Control](#border-control)

## Background Control

The background control lets you set the following background properties:

- Background color
- Background image
- Background video (requiresbricksBackgroundVideoInitscript. See code example below)

`bricksBackgroundVideoInit`

There are various settings for the background image and video. You can exclude color/image/video settings via theexcludeparameter.

`exclude`

As the background control serves most likely as a CSS setting the following example shows you how to set thecssparameter to apply it to the elements’.prefix-test-wrapperHTML.

`css`

`.prefix-test-wrapper`

Adding a background video requires you to load thebricksBackgroundVideoInitscript and use theBricksFrontend::get_element_background_video_wrapper()method to render it.

`bricksBackgroundVideoInit`

`BricksFrontend::get_element_background_video_wrapper()`

When you just want to set a background color better use thecolor control. The background control is handier when using a background image or video on top of the color.

```
class Prefix_Element_Background extends \Bricks\Element {
  // Required for background video
  public $scripts = ['bricksBackgroundVideoInit'];

  // Set builder controls
  public function set_controls() {
    $this->controls['exampleBackground'] = [ // Setting key
      'tab' => 'content',
      'label' => esc_html__( 'Background', 'bricks' ),
      'type' => 'background',
      'css' => [
        [
          'property' => 'background',
          'selector' => '.prefix-background-wrapper',
        ],
      ],
      'exclude' => [
        // 'color',
        // 'image',
        // 'parallax',
        // 'attachment',
        // 'position',
        // 'positionX',
        // 'positionY',
        // 'repeat',
        // 'size',
        // 'custom',
        // 'videoUrl',
        // 'videoScale',
      ],
      'inline' => true,
      'small' => true,
      'default' => [
        'color' => [
          'rgb' => 'rgba(255, 255, 255, .5)',
          'hex' => '#ffffff',
        ],
      ],
    ];
  }

  // Render element HTML
  public function render() {
    echo '<div class="prefix-background-wrapper">';

    // Background video
    echo BricksFrontend::get_element_background_video_wrapper( 
      ['settings' => $settings], 
      'exampleBackground' // Setting key
    );

    echo get_bloginfo( 'name' );

    echo '</div>';
  }
}
```

`class Prefix_Element_Background extends \Bricks\Element {
  // Required for background video
  public $scripts = ['bricksBackgroundVideoInit'];

  // Set builder controls
  public function set_controls() {
    $this->controls['exampleBackground'] = [ // Setting key
      'tab' => 'content',
      'label' => esc_html__( 'Background', 'bricks' ),
      'type' => 'background',
      'css' => [
        [
          'property' => 'background',
          'selector' => '.prefix-background-wrapper',
        ],
      ],
      'exclude' => [
        // 'color',
        // 'image',
        // 'parallax',
        // 'attachment',
        // 'position',
        // 'positionX',
        // 'positionY',
        // 'repeat',
        // 'size',
        // 'custom',
        // 'videoUrl',
        // 'videoScale',
      ],
      'inline' => true,
      'small' => true,
      'default' => [
        'color' => [
          'rgb' => 'rgba(255, 255, 255, .5)',
          'hex' => '#ffffff',
        ],
      ],
    ];
  }

  // Render element HTML
  public function render() {
    echo '<div class="prefix-background-wrapper">';

    // Background video
    echo BricksFrontend::get_element_background_video_wrapper( 
      ['settings' => $settings], 
      'exampleBackground' // Setting key
    );

    echo get_bloginfo( 'name' );

    echo '</div>';
  }
}`

###### Audio Control

###### Border Control

