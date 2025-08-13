---
title: "Apply Control – Bricks Academy"
url: https://academy.bricksbuilder.io/article/apply-control/
date: 2025-02-27T15:29:08.332043
status: success
---

# Apply Control – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/apply-control/](https://academy.bricksbuilder.io/article/apply-control/)*

## Table of Contents

- [Apply Control](#apply-control)
        - [Typography Control](#typography-control)
        - [Align Items Control (Flexbox)](#align-items-control-flexbox)

## Apply Control

Theapplycontrol saves your settings. You can set thereloadcontrol property totruein order to trigger a builder reload after the “Apply” button has been clicked. We use it in the builder for settings like the template “Populate Content” or the “SEO” page settings.

`apply`

`reload`

```
$this->controls['apply'] = [
  'group' => 'template-preview',
  'type' => 'apply',
  'reload' => true,
  'label' => esc_html__( 'Apply preview', 'bricks' ),
];
```

`$this->controls['apply'] = [
  'group' => 'template-preview',
  'type' => 'apply',
  'reload' => true,
  'label' => esc_html__( 'Apply preview', 'bricks' ),
];`

###### Typography Control

###### Align Items Control (Flexbox)

