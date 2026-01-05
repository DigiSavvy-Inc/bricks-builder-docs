---
title: "Element Controls – Bricks Academy"
url: https://academy.bricksbuilder.io/article/element-controls/
date: 2026-01-05T11:07:30.300923
status: success
---

# Element Controls – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/element-controls/](https://academy.bricksbuilder.io/article/element-controls/)*

## Table of Contents

- [Element Controls](#element-controls)
    - [Universal control arguments](#universal-control-arguments)
    - [Controls Types](#controls-types)
        - [Audio Control](#audio-control)

## Element Controls

Element controls allow the user to change the content and appearance of an element. You can define the controls of an element with the set_controls() method in yourelement PHP class.

Example element class with control parameters for controltestColor:

`testColor`

```
class Prefix_Element_Test extends \Bricks\Element {
  public function set_controls() {
    $this->controls['testColor'] = [
      'tab' => 'content',
      'group' => 'settings',
      'label' => esc_html__( 'Text color', 'bricks' ),
      'type' => 'color',
      'inline' => true,
      'small' => true,
      'css' => [
        [
          'property' => 'color',
          'selector' => '.content',
          'important' => true, // Optional
        ],
      ],
      'default' => [
        'rgb' => 'rgba(158, 158, 158, .8)',
        'hex' => '#9e9e9e',
      ],
      'pasteStyles' => false,
      'description' => esc_html__( 'Define the content color.', 'bricks' ),
      'required' => ['showText', '!=', ''],
    ];
  }
}

```

The following control parameters are available for all control types. To dive deeper into the arguments of a specific control type select the control from the list at the bottom.

#### Universal control arguments

`content`

`style`

`content`

`esc_html__( 'Color', 'bricks' ),`

`property`

`selector`

Parameter #1: control IDParameter #2: comparison operator:=,!=,>=,<=Parameter #3: setting value

`=`

`!=`

`>=`

`<=`

Example:'required' => ['layout', '=', ['list', 'grid']],Required condition: Show this control if setting value of controllayoutequals=eitherlistorgrid.

`'required' => ['layout', '=', ['list', 'grid']],`

`layout`

`=`

`list`

`grid`

#### Controls Types

###### Audio Control

