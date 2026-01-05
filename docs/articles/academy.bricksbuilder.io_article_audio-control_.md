---
title: "Audio Control – Bricks Academy"
url: https://academy.bricksbuilder.io/article/audio-control/
date: 2026-01-05T11:07:58.569651
status: success
---

# Audio Control – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/audio-control/](https://academy.bricksbuilder.io/article/audio-control/)*

## Table of Contents

- [Audio Control](#audio-control)
    - [Resources](#resources)
        - [Textarea Control](#textarea-control)
        - [Background Control](#background-control)

## Audio Control

The audio control lets you select an audio file from the media library. It also gives you various options to show/hide artist and title, choose between a light/dark theme, autoplay the audio file, etc. It has no custom control parameters.

```
class Prefix_Element_Audio extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['file'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Audio file', 'bricks' ),
      'type' => 'audio',
    ];
  }

  // Render element HTML
  public function render() {
    $settings = $this->settings;

    if ( isset( $settings['file']['url'] ) ) {
      echo wp_audio_shortcode( [
        'src'      => $settings['file']['url'],
        'loop'     => isset( $settings['loop'] ) ? $settings['loop'] : false, 
        'autoplay' => isset( $settings['autoplay'] ) ? $settings['autoplay'] : false, 
        'preload'  => isset( $settings['preload'] ) ? $settings['preload'] : 'none', 
      ] );
    }
  }
}
```

`class Prefix_Element_Audio extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['file'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Audio file', 'bricks' ),
      'type' => 'audio',
    ];
  }

  // Render element HTML
  public function render() {
    $settings = $this->settings;

    if ( isset( $settings['file']['url'] ) ) {
      echo wp_audio_shortcode( [
        'src'      => $settings['file']['url'],
        'loop'     => isset( $settings['loop'] ) ? $settings['loop'] : false, 
        'autoplay' => isset( $settings['autoplay'] ) ? $settings['autoplay'] : false, 
        'preload'  => isset( $settings['preload'] ) ? $settings['preload'] : 'none', 
      ] );
    }
  }
}`

#### Resources

https://codex.wordpress.org/Function_Reference/wp_audio_shortcode

###### Textarea Control

###### Background Control

