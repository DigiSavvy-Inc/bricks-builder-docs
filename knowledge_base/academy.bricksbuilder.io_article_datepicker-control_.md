---
title: "Datepicker Control – Bricks Academy"
url: https://academy.bricksbuilder.io/article/datepicker-control/
date: 2025-02-27T15:28:28.546616
status: success
---

# Datepicker Control – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/datepicker-control/](https://academy.bricksbuilder.io/article/datepicker-control/)*

## Table of Contents

- [Datepicker Control](#datepicker-control)
  - [Properties:](#properties)
    - [Property: options (since 1.9.8)](#property-options-since-198)
    - [Property:enableTime](#propertyenabletime)
    - [Property:altInput](#propertyaltinput)
  - [Example: Countdown element](#example-countdown-element)
        - [Color Control](#color-control)
        - [Dimensions Control](#dimensions-control)

## Datepicker Control

The datepicker control provides a great interface for selecting a specific date and time and outputting it in theformat of your choice.

The Datepicker control leverages the Flatpickr library to offer a robust date selection interface. Since Bricks 1.9.8 anoptionsproperty has been added which allows for further customization.

`options`

### Properties:

#### Property: options (since 1.9.8)

- Type:array (associative)
- Description:Enables customization of the datepicker by passing an associative array of options defined in the Flatpickr library.
- Default values:enableTime:Defaults totrueunless explicitly set through a passed property.altInput:Defaults totrueunless specified otherwise through a passed property.
- enableTime:Defaults totrueunless explicitly set through a passed property.
- altInput:Defaults totrueunless specified otherwise through a passed property.

- enableTime:Defaults totrueunless explicitly set through a passed property.
- altInput:Defaults totrueunless specified otherwise through a passed property.

`true`

`true`

Example usage:

```
$this->controls['date'] = [
  'tab' => 'content',
  'label' => esc_html__('Date', 'bricks'),
  'type' => 'datepicker',
  'options' => [
    'enableTime' => true,  // Enables time selection.
    'time_24hr' => true,   // Displays time picker in 24-hour mode.
    'noCalendar' => true   // Hides the calendar day selection.
  ]
];
```

`$this->controls['date'] = [
  'tab' => 'content',
  'label' => esc_html__('Date', 'bricks'),
  'type' => 'datepicker',
  'options' => [
    'enableTime' => true,  // Enables time selection.
    'time_24hr' => true,   // Displays time picker in 24-hour mode.
    'noCalendar' => true   // Hides the calendar day selection.
  ]
];`

In this example, theoptionsarray is configured to create a time picker that operates in 24-hour format without showing a calendar for day selection. TheenableTimeoption is set to true to ensure time can be selected,time_24hris enabled for 24-hour time format, andnoCalendaris set to true to hide the calendar component. Adjust theoptionsarray as needed to customize the datepicker to meet different requirements.

`options`

`enableTime`

`time_24hr`

`noCalendar`

`options`

For a full list of customizable options available in Flatpickr, please refer to theFlatpickr Options documentation.

#### Property:enableTime

- Type:boolean
- Description:Determines whether time selection is enabled. Overridden if any settings are passed in theoptionsproperty.
- Default:true

`options`

#### Property:altInput

- Type:boolean
- Description:Enables an alternative, more user-friendly input style. Overridden if any settings are passed in theoptionsproperty.
- Default:true

`options`

### Example: Countdown element

```
// Example: Countdown element
class Prefix_Element_Countdown extends \Bricks\Element {
  public $category = 'general';
  public $name     = 'countdown';
  public $icon     = 'ti-timer';
  public $scripts  = ['bricksCountdown'];

  public function get_label() {
    return esc_html__( 'Countdown', 'bricks' );
  }

  public function set_controls() {
    $this->controls['date'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Date', 'bricks' ),
      'type' => 'datepicker',
      'options' => ['enableTime' => true, 'altInput' => true],
      'default' => '2019-01-01 12:00',
    ];

    $this->controls['format'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Format', 'bricks' ),
      'type' => 'text',
      'default' => '%D days %H hours %M minutes %S seconds.',
      'description' => sprintf(
        '%s <a target="_blank" href="http://hilios.github.io/jQuery.countdown/documentation.html#directives">%s</a>.',
        esc_html__( 'For formatting options see', 'bricks' ),
        esc_html__( 'directives', 'bricks' )
      ),
    ];
  }

  public function render() {
    $this->set_attribute( 'wrapper', 'class', 'countdown-wrapper' );

    $countdown_options = [
      'date' => isset( $this->settings['date'] ) ? $this->settings['date'] : '',
      'format' => isset( $this->settings['format'] ) ? $this->settings['format'] : '',
    ];

    $this->set_attribute( 'wrapper', 'data-bricks-countdown-options', wp_json_encode( $countdown_options ) );

    // Render
    if ( ! isset( $this->settings['date'] ) || ! isset( $this->settings['format'] ) ) {
      return $this->render_element_placeholder( [
        'icon-class' => 'ti-timer',
        'text'       => esc_html__( 'No date/format set.', 'bricks' ),
      ] );
    } else {
      echo '<div ' . $this->render_attributes( 'wrapper' ) . '></div>';
    }
  }
}
```

`// Example: Countdown element
class Prefix_Element_Countdown extends \Bricks\Element {
  public $category = 'general';
  public $name     = 'countdown';
  public $icon     = 'ti-timer';
  public $scripts  = ['bricksCountdown'];

  public function get_label() {
    return esc_html__( 'Countdown', 'bricks' );
  }

  public function set_controls() {
    $this->controls['date'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Date', 'bricks' ),
      'type' => 'datepicker',
      'options' => ['enableTime' => true, 'altInput' => true],
      'default' => '2019-01-01 12:00',
    ];

    $this->controls['format'] = [
      'tab' => 'content',
      'label' => esc_html__( 'Format', 'bricks' ),
      'type' => 'text',
      'default' => '%D days %H hours %M minutes %S seconds.',
      'description' => sprintf(
        '%s <a target="_blank" href="http://hilios.github.io/jQuery.countdown/documentation.html#directives">%s</a>.',
        esc_html__( 'For formatting options see', 'bricks' ),
        esc_html__( 'directives', 'bricks' )
      ),
    ];
  }

  public function render() {
    $this->set_attribute( 'wrapper', 'class', 'countdown-wrapper' );

    $countdown_options = [
      'date' => isset( $this->settings['date'] ) ? $this->settings['date'] : '',
      'format' => isset( $this->settings['format'] ) ? $this->settings['format'] : '',
    ];

    $this->set_attribute( 'wrapper', 'data-bricks-countdown-options', wp_json_encode( $countdown_options ) );

    // Render
    if ( ! isset( $this->settings['date'] ) || ! isset( $this->settings['format'] ) ) {
      return $this->render_element_placeholder( [
        'icon-class' => 'ti-timer',
        'text'       => esc_html__( 'No date/format set.', 'bricks' ),
      ] );
    } else {
      echo '<div ' . $this->render_attributes( 'wrapper' ) . '></div>';
    }
  }
}`

###### Color Control

###### Dimensions Control

