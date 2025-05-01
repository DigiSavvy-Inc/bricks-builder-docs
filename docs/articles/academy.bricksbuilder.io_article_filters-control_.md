---
title: "Filters Control – Bricks Academy"
url: https://academy.bricksbuilder.io/article/filters-control/
date: 2025-05-01T12:03:13.109606
status: success
---

# Filters Control – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/filters-control/](https://academy.bricksbuilder.io/article/filters-control/)*

## Table of Contents

- [Filters Control](#filters-control)
        - [Editor Control](#editor-control)
        - [Gradient Control](#gradient-control)

## Filters Control

The filters control offers the followingCSS filters:blur,brightness,contrast,hue,invert,opacity,saturation,sepia.

`blur`

`brightness`

`contrast`

`hue`

`invert`

`opacity`

`saturation`

`sepia`

```
class Prefix_Element_Filters extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleFilters'] = [
      'tab' => 'content',
      'label' => esc_html__( 'CSS filters', 'bricks' ),
      'type' => 'filters',
      'inline' => true,
      'css' => [
        [
          'property' => 'filter',
          'selector' => '.css-filter',
        ],
      ],
    ];
  }

  // Render element HTML
  public function render() {
    echo '<div class="css-filter">' . echo get_bloginfo( 'name' ); . '</div>';
  }
}
```

`class Prefix_Element_Filters extends \Bricks\Element {
  // Set builder controls
  public function set_controls() {
    $this->controls['exampleFilters'] = [
      'tab' => 'content',
      'label' => esc_html__( 'CSS filters', 'bricks' ),
      'type' => 'filters',
      'inline' => true,
      'css' => [
        [
          'property' => 'filter',
          'selector' => '.css-filter',
        ],
      ],
    ];
  }

  // Render element HTML
  public function render() {
    echo '<div class="css-filter">' . echo get_bloginfo( 'name' ); . '</div>';
  }
}`

All sections, rows, columns, and elements already have aCSS Filterscontrol under the Style tab CSS group.

###### Editor Control

###### Gradient Control

