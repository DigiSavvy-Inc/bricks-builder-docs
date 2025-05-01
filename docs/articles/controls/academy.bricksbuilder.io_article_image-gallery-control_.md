---
title: "Image Gallery Control – Bricks Academy"
url: https://academy.bricksbuilder.io/article/image-gallery-control/
date: 2025-05-01T12:02:45.356525
status: success
---

# Image Gallery Control – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/image-gallery-control/](https://academy.bricksbuilder.io/article/image-gallery-control/)*

## Table of Contents

- [Image Gallery Control](#image-gallery-control)
        - [Image Control](#image-control)
        - [Info Control](#info-control)

## Image Gallery Control

The image gallery control lets you select multiple images from your media library. Once images have been selected you can choose the image size.

Your selected images are stored in an array, which you have to loop through (see code example below). Use theidandsizeof each image to render it on your page.

`id`

`size`

Tip #1:Hold down theSHIFTkey in order to select multiple image in your media library.

Tip #2:Select the smallest possible image size in which the image still looks crisp. This helps to reduce the loading time of your website and is great for SEO, as loading times are an important ranking factor for search engines.

```
class Prefix_Element_Image extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleImageGallery'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Image gallery', 'bricks' ),
      'type' => 'image-gallery',
    ];
  }

  // Render element HTML
  public function render() {
    if ( isset( $this->settings['exampleImageGallery'] ) ) {
      foreach( $this->settings['exampleImageGallery'] as $index => $image ) {
        echo wp_get_attachment_image(
          $image['id'],
          $image['size'],
          false,
          ['class' => 'css-filter']
        );
      }
    } else {
      esc_html_e( 'No image(s) selected.', 'bricks' );
    }
  }
}
```

`class Prefix_Element_Image extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleImageGallery'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Image gallery', 'bricks' ),
      'type' => 'image-gallery',
    ];
  }

  // Render element HTML
  public function render() {
    if ( isset( $this->settings['exampleImageGallery'] ) ) {
      foreach( $this->settings['exampleImageGallery'] as $index => $image ) {
        echo wp_get_attachment_image(
          $image['id'],
          $image['size'],
          false,
          ['class' => 'css-filter']
        );
      }
    } else {
      esc_html_e( 'No image(s) selected.', 'bricks' );
    }
  }
}`

###### Image Control

###### Info Control

