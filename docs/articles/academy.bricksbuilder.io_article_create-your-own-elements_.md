---
title: "Create Your Own Elements – Bricks Academy"
url: https://academy.bricksbuilder.io/article/create-your-own-elements/
date: 2025-05-01T12:02:54.013031
status: success
---

# Create Your Own Elements – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/create-your-own-elements/](https://academy.bricksbuilder.io/article/create-your-own-elements/)*

## Table of Contents

- [Create Your Own Elements](#create-your-own-elements)
  - [Blank element class](#blank-element-class)
  - [Load and register your element](#load-and-register-your-element)
        - [Child Theme](#child-theme)
        - [Nestable Elements (API)](#nestable-elements-api)

## Create Your Own Elements

The Brickschild theme, which you can download from yourBricks accountincludes a simple custom element for demonstration purposes. The article below explains in more detail how to create your own elements programmatically.

Creating your own elements with Bricks follows a pattern similar to how you create WordPress widgets. You start by extending theBricks\Elementclass and populate the required properties and methods for your element.

`Bricks\Element`

First, create a new fileelement-test.phpin the root folder of your Bricks child theme.

`element-test.php`

### Blank element class

```
<?php 
// element-test.php
if ( ! defined( 'ABSPATH' ) ) exit; // Exit if accessed directly

class Prefix_Element_Test extends \Bricks\Element {
  // Element properties
  public $category     = '';
  public $name         = '';
  public $icon         = '';
  public $css_selector = '';
  public $scripts      = [];
  public $nestable     = false; // true || @since 1.5

  // Methods: Builder-specific
  public function get_label() {}
  public function get_keywords() {}
  public function set_control_groups() {}
  public function set_controls() {}

  // Methods: Frontend-specific
  public function enqueue_scripts() {}
  public function render() {}
}

```

Let’s walk through the element builder properties and methods:

`general`

`media`

`prefix-element-test`

- Fontawesome 6(i.e. “fas fa-anchor”)
- Ionicons 4(i.e. “ion-md-alarm”)
- Themify Icons(i.e. “ti-bolt-alt”)

`.bricks-element-wrapper`

`true`

`public $scripts = ['bricksCounter'];`

`prefixElementTest`

- title– Localized control group title

- tab– Set to either “content” or “style”

`wp_enqueue_script( 'prefix-element-test', get_template_directory_uri() . '/js/custom.js', ['jquery'], '1.0', true );`

`$this->set_attribute() `

`$this->render_attribute()`

`$key`

`$attribute`

`$value`

`$this->set_attribute()`

`$this->render_dynamic_data_tag(...)`

`$tag`

`{post_title}`

`$this->render_dynamic_data(...)`

Let’s populate our element properties and methods with some data:

```
<?php // element-test.phpif ( ! defined( 'ABSPATH' ) ) exit; // Exit if accessed directlyclass Prefix_Element_Test extends \Bricks\Element {  // Element properties  public $category     = 'general'; // Use predefined element category 'general'  public $name         = 'prefix-test'; // Make sure to prefix your elements  public $icon         = 'ti-bolt-alt'; // Themify icon font class  public $css_selector = '.prefix-test-wrapper'; // Default CSS selector  public $scripts      = ['prefixElementTest']; // Script(s) run when element is rendered on frontend or updated in builder  // Return localised element label  public function get_label() {    return esc_html__( 'Test element', 'bricks' );  }  // Set builder control groups  public function set_control_groups() {    $this->control_groups['text'] = [ // Unique group identifier (lowercase, no spaces)      'title' => esc_html__( 'Text', 'bricks' ), // Localized control group title      'tab' => 'content', // Set to either "content" or "style"    ];    $this->control_groups['settings'] = [      'title' => esc_html__( 'Settings', 'bricks' ),      'tab' => 'content',    ];  }   // Set builder controls  public function set_controls() {    $this->controls['content'] = [ // Unique control identifier (lowercase, no spaces)      'tab' => 'content', // Control tab: content/style      'group' => 'text', // Show under control group      'label' => esc_html__( 'Content', 'bricks' ), // Control label      'type' => 'text', // Control type       'default' => esc_html__( 'Content goes here ..', 'bricks' ), // Default setting    ];        $this->controls['type'] = [      'tab' => 'content',      'group' => 'settings',      'label' => esc_html__( 'Type', 'bricks' ),      'type' => 'select',      'options' => [        'info' => esc_html__( 'Info', 'bricks' ),        'success' => esc_html__( 'Success', 'bricks' ),        'warning' => esc_html__( 'Warning', 'bricks' ),        'danger' => esc_html__( 'Danger', 'bricks' ),        'muted' => esc_html__( 'Muted', 'bricks' ),      ],      'inline' => true,      'clearable' => false,      'pasteStyles' => false,      'default' => 'info',    ];  }  // Enqueue element styles and scripts  public function enqueue_scripts() {    wp_enqueue_script( 'prefix-test-script' );  }  // Render element HTML  public function render() {    // Set element attributes    $root_classes[] = 'prefix-test-wrapper';    if ( ! empty( $this->settings['type'] ) ) {      $root_classes[] = "color-{$this->settings['type']}";    }    // Add 'class' attribute to element root tag    $this->set_attribute( '_root', 'class', $root_classes );    // Render element HTML    // '_root' attribute is required (contains element ID, class, etc.)    echo "<div {$this->render_attributes( '_root' )}>"; // Element root attributes      if ( ! empty( $this->settings['content'] ) ) {        echo "<div>{$this->settings['content']}</div>";      }    echo '</div>';  }}
```

You can view all element controls over at:https://academy.bricksbuilder.io/topic/controls/

All element settings are stored in$this->settings. To view of element settings you can print them on the screen like so:var_dump( $this->settings );in therender()function.

`$this->settings`

`var_dump( $this->settings );`

`render()`

### Load and register your element

After creating your custom element you need to load and register your element. Open upfunctions.phpof your Bricks child theme and copy & paste the following code:

`functions.php`

```
/**
 * Register custom elements
 */
add_action( 'init', function() {
  $element_files = [
    __DIR__ . '/element-test.php',
  ];

  foreach ( $element_files as $file ) {
    \Bricks\Elements::register_element( $file );
  }
}, 11 );

```

Theregister_elementmethod accepts 3 arguments:

`register_element`

- $file(required): The full path to the custom element PHP file in the server
- $name(optional): A string containing the name of the custom element (e.g.:prefix-element-test)
- $element_class(optional): A string containing the class name of the element (e.g.:Prefix_Element_Test) which should derive from the Bricks element class (\Bricks\Element)

`$file`

`$name`

`prefix-element-test`

`$element_class`

`Prefix_Element_Test`

`\Bricks\Element`

Note:Using the$nameand$element_classarguments will improve the loading performance.

`$name`

`$element_class`

###### Child Theme

###### Nestable Elements (API)

