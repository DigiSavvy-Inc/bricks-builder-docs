---
title: "Custom Code – Bricks Academy"
url: https://academy.bricksbuilder.io/article/custom-code/
date: 2026-01-05T11:08:45.571821
status: success
---

# Custom Code – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/custom-code/](https://academy.bricksbuilder.io/article/custom-code/)*

## Table of Contents

- [Custom Code](#custom-code)
  - [Global CSS & JavaScript](#global-css--javascript)
  - [Page-SpecificCSS & JavaScript](#page-specificcss--javascript)
  - [Element-Specific Custom CSS](#element-specific-custom-css)
    - [CSS code completion via Emmet](#css-code-completion-via-emmet)
  - [Code Element (PHP, HTML, CSS, JS)](#code-element-php-html-css-js)
    - [How to add PHP & HTML code to your element](#how-to-add-php--html-code-to-your-element)
    - [HTML Code Completion via Emmet](#html-code-completion-via-emmet)
        - [Custom Fonts](#custom-fonts)
        - [Gradients & Overlays](#gradients--overlays)

## Custom Code

Bricks allows you to add your own custom code (CSS, JavaScript, HTML, PHP) to various parts of your website.

### Global CSS & JavaScript

You can add your ownCustom CSS&Custom JavaScriptglobally from your WordPress dashboard underBricks > Settings > Custom Code.

Custom scripts (JavaScript) can be added in three different (document) locations:

- Header scripts: Adds your scripts right before the closing </head> tag. This is where you want to copy & paste tracking scripts, etc.
- Body (header) scripts: Adds your scripts right after the opening <body> tag.
- Body (footer) scripts: Adds your scripts right before the closing </body> tag.

### Page-SpecificCSS & JavaScript

To apply custom CSS & JavaScript to a specific page, edit this page with Bricks. Go toSettings > Page Settings > Custom Code. There, you can add your custom CSS & JS that should only be applied to the page you are currently editing.

### Element-Specific Custom CSS

Extend the styles of any element and global class by adding your own custom CSS to it.

First, edit the element to which you want to add your own custom CSS.

Under the “Style” tab, open the “CSS” control group.

There, you can find theCustom CSScode editor.

Use the%root%placeholder to target the element or global class you are currently editing. Bricks automatically converts this%root%placeholder to your element ID or global class.

`%root%`

`%root%`

Keyboard shortcode to insert%root%is “r + TAB”.

`%root%`

The screenshot on the right illustrates how to add a 1px width red border to an element.

#### CSS code completion via Emmet

You can use CSS abbreviations to write your CSS even faster. Instead of writingmargin: 10px, simply typem10and press the TAB key.

`margin: 10px`

`m10`

https://docs.emmet.io/css-abbreviations/

### Code Element (PHP, HTML, CSS, JS)

The “Code” element allows you to execute your own code (PHP, HTML, CSS & JS) anywhere on any page.

By default, the code added to the Code element is displayed as a code snippet.

In order to execute your code, you need to first enable“Code Execution”for the appropriate user role or user in your WordPress dashboard under “Bricks – Settings – Custom code” (see the screenshot below).

Make sure to only enable code execution for users & user roles you trust 100%.

#### How to add PHP & HTML code to your element

Once you’ve enabled code execution you can start adding the “Code” element wherever you want to execute your code.

You’d usually execute PHP & HMTL code, as CSS & JS can be added much easier via the solutions outlined above.

Once you’ve added the Code element to your page, you can add your custom code to it (as shown in the screenshot ).

To run/execute the code, enable the “Execute Code” setting. Otherwise, the code just shows as a code snippet.

Click the “Sign code” icon at the top-right of the code editor (or CMD/CTRL + R) once you’ve finished editing your executable code.

#### HTML Code Completion via Emmet

You can use abbreviations to generate your HTML structures much faster via a familiar CSS-based syntax.

Abbreviation:#header(+ TAB key)

`#header`

Generates:<div id="header"></div>Abbreviation:h$[title=item$]{Header $}*3

`<div id="header"></div>`

`h$[title=item$]{Header $}*3`

Generates:

```
<h1 title="item1">Header 1</h1>
<h2 title="item2">Header 2</h2>
<h3 title="item3">Header 3</h3>
```

`<h1 title="item1">Header 1</h1>
<h2 title="item2">Header 2</h2>
<h3 title="item3">Header 3</h3>`

https://docs.emmet.io/cheat-sheet/

###### Custom Fonts

###### Gradients & Overlays

