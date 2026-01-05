---
title: "Image Control – Bricks Academy"
url: https://academy.bricksbuilder.io/article/image-control/
date: 2026-01-05T11:07:39.176490
status: success
---

# Image Control – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/image-control/](https://academy.bricksbuilder.io/article/image-control/)*

## Table of Contents

- [Image Control](#image-control)
        - [Textarea Control](#textarea-control)
        - [Color Control](#color-control)

## Image Control

The image control lets you select a single image from your media library. Once an image has been selected you can choose the image size.

You can either use the returned imageidandsizeto render an image on your page or as abackground-imagevia the CSS control property. See the code example below.

`id`

`size`

`background-image`

TIP:Select the smallest possible image size in which the image still looks crisp. This helps to reduce the loading time of your website and is great for SEO, as loading times are an important ranking factor for search engines.

```
class Prefix_Element_Image extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleImage'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Image', 'bricks' ),
      'type' => 'image',
      // Use the selected image as a background image
      // 'css' => [
      //   [
      //     'property' => 'background-image',
      //     'selector' => '.bricks-video-overlay-image',
      //   ],
      // ],
    ];
  }

  // Render element HTML
  public function render() {
    // Dump 'exampleImage' settings on the screen
    // var_dump( $this->settings['exampleImage'] );    

    if ( isset( $this->settings['exampleImage'] ) ) {
      // Render <img> tag by prodiving image 'id' and 'size'
      // 
      echo wp_get_attachment_image(
        $this->settings['exampleImage']['id'],
        $this->settings['exampleImage']['size'],
        false,
        [] // Image attributes
      );
    } else {
      esc_html_e( 'No image selected.', 'bricks' );
    }
  }
}
```

`class Prefix_Element_Image extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleImage'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Image', 'bricks' ),
      'type' => 'image',
      // Use the selected image as a background image
      // 'css' => [
      //   [
      //     'property' => 'background-image',
      //     'selector' => '.bricks-video-overlay-image',
      //   ],
      // ],
    ];
  }

  // Render element HTML
  public function render() {
    // Dump 'exampleImage' settings on the screen
    // var_dump( $this->settings['exampleImage'] );    

    if ( isset( $this->settings['exampleImage'] ) ) {
      // Render <img> tag by prodiving image 'id' and 'size'
      // 
      echo wp_get_attachment_image(
        $this->settings['exampleImage']['id'],
        $this->settings['exampleImage']['size'],
        false,
        [] // Image attributes
      );
    } else {
      esc_html_e( 'No image selected.', 'bricks' );
    }
  }
}`

###### Textarea Control

###### Color Control

