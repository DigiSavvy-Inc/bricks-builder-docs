---
title: "Link Control – Bricks Academy"
url: https://academy.bricksbuilder.io/article/link-control/
date: 2026-01-05T11:08:12.580623
status: success
---

# Link Control – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/link-control/](https://academy.bricksbuilder.io/article/link-control/)*

## Table of Contents

- [Link Control](#link-control)
        - [Query Control](#query-control)
        - [Audio Control](#audio-control)

## Link Control

The link control give you the choice of different link types:

- Internal post/page
- External URL
- Popup (image, video)

```
class Prefix_Element_Link extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleLink'] = [
      'tab'         => 'content',
      'label'       => esc_html__( 'Link', 'bricks' ),
      'type'        => 'link',
      'pasteStyles' => false,
      'placeholder' => esc_html__( 'http://yoursite.com', 'bricks' ),
      // 'exclude'     => [
      //  'rel',
      //  'newTab',
      // ],
    ];
  }

  // Render element HTML
  public function render() {
    if ( isset( $this->settings['exampleLink'] ) ) {
      // Set link attributes by passing attribute key and link settings
      $this->set_link_attributes( 'a', $this->settings['exampleLink'] );

      echo '<a ' . $this->render_attributes( 'a' ) . '>' . get_bloginfo( 'name' ) . '</a>';
    } else {
      esc_html_e( 'No link provided.', 'bricks' );
    }
  }
}
```

`class Prefix_Element_Link extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleLink'] = [
      'tab'         => 'content',
      'label'       => esc_html__( 'Link', 'bricks' ),
      'type'        => 'link',
      'pasteStyles' => false,
      'placeholder' => esc_html__( 'http://yoursite.com', 'bricks' ),
      // 'exclude'     => [
      //  'rel',
      //  'newTab',
      // ],
    ];
  }

  // Render element HTML
  public function render() {
    if ( isset( $this->settings['exampleLink'] ) ) {
      // Set link attributes by passing attribute key and link settings
      $this->set_link_attributes( 'a', $this->settings['exampleLink'] );

      echo '<a ' . $this->render_attributes( 'a' ) . '>' . get_bloginfo( 'name' ) . '</a>';
    } else {
      esc_html_e( 'No link provided.', 'bricks' );
    }
  }
}`

###### Query Control

###### Audio Control

