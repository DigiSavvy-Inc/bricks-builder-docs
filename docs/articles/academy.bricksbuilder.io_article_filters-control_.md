---
title: "Filters Control – Bricks Academy"
url: https://academy.bricksbuilder.io/article/filters-control/
date: 2026-01-05T11:08:08.205855
status: success
---

# Filters Control – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/filters-control/](https://academy.bricksbuilder.io/article/filters-control/)*

## Table of Contents

- [Filters Control](#filters-control)
        - [Typography Control](#typography-control)
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

###### Typography Control

###### Gradient Control

