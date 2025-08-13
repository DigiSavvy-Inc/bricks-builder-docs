---
title: "Nestable Slider: Customization via JavaScript – Bricks Academy"
url: https://academy.bricksbuilder.io/article/nestable-slider-instance/
date: 2025-02-27T15:31:13.937435
status: success
---

# Nestable Slider: Customization via JavaScript – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/nestable-slider-instance/](https://academy.bricksbuilder.io/article/nestable-slider-instance/)*

## Table of Contents

- [Nestable Slider: Customization via JavaScript](#nestable-slider-customization-via-javascript)
  - [Update Nestable Slider options via JavaScript](#update-nestable-slider-options-via-javascript)
  - [Custom navigation arrows outside the slider](#custom-navigation-arrows-outside-the-slider)
        - [Bricks CLI](#bricks-cli)
        - [How to add a custom animation in interaction](#how-to-add-a-custom-animation-in-interaction)

## Nestable Slider: Customization via JavaScript

Bricks introduced the Nestable Slider in version 1.5, utilizing theSplideJSlibrary.

This article is intended for developers, walking you through how to access and customize the Splide instance.

All initialized Splide instances are stored and can be accessed throughwindow.bricksData.splideInstances.

`window.bricksData.splideInstances`

You must first identify the Nestable Slider element’s unique ID to retrieve the appropriate instance from the variable. You can find this ID within the builder when editing this element or through your browsers’ developer tools.

According to the example above, I can access my Splide Instance throughwindow.bricksData.splideInstances['rrbqsp']

`window.bricksData.splideInstances['rrbqsp']`

If you have assigned a custom CSS ID to the Slider, please note that this ID is not the same as the element ID. In such cases, you should obtain the correct element ID through your browser’s developer tools.

### Update Nestable Slider options via JavaScript

Objective: UpdatenoDragoption for all Nestable Sliders on the current page.

`noDrag`

```
<script>
document.addEventListener('DOMContentLoaded', (event) => {
  // Define a function to update the no-drag option for all splide instances on the page
  const updateNoDragOption = () => {
    for( const splideId in window.bricksData.splideInstances ) {
      const splideInstance = window.bricksData.splideInstances[splideId]
      if ( splideInstance ) {
        // Tell Splide that any elements with .no-drag class is not draggable
        splideInstance.options = { noDrag : '.no-drag' }
      }
    }
  }
  
  // Need some delay for Bricks to init the sliders
  setTimeout(updateNoDragOption, 250)
})
</script>
```

`<script>
document.addEventListener('DOMContentLoaded', (event) => {
  // Define a function to update the no-drag option for all splide instances on the page
  const updateNoDragOption = () => {
    for( const splideId in window.bricksData.splideInstances ) {
      const splideInstance = window.bricksData.splideInstances[splideId]
      if ( splideInstance ) {
        // Tell Splide that any elements with .no-drag class is not draggable
        splideInstance.options = { noDrag : '.no-drag' }
      }
    }
  }
  
  // Need some delay for Bricks to init the sliders
  setTimeout(updateNoDragOption, 250)
})
</script>`

### Custom navigation arrows outside the slider

Objective: Implement custom navigation buttons located outside of the Nestable Slider.

Please set unique classes for your buttons. We assigned themy-prevandmy-nextCSS classes in our example.

`my-prev`

`my-next`

Next, place a Code element and write some simple JavaScript. Remember to turnONthe Execute code checkbox. (Arrows for the Slider remainedOFF)

```
<script>
document.addEventListener('DOMContentLoaded', (event) => {
  // Give some times for Bricks to init the sliders
  setTimeout(() => {
    // Please replace rrbqsp to your Slider element ID !!NOT CSS ID!!
    const mySlider = window.bricksData?.splideInstances['rrbqsp'] || false
    // Please replace the button classes to suit your scenario
    const myPrevBtn = document.querySelector('.my-prev')
    const myNextBtn = document.querySelector('.my-next')

    if (mySlider && myPrevBtn && myNextBtn) {
      // Add click event handlers for your custom buttons
      myPrevBtn.addEventListener('click', function () {
        mySlider.go('-1') // go() function by SplideJS
      })
      myNextBtn.addEventListener('click', function () {
        mySlider.go('+1') // go() function by SplideJS
      })
    }
  }, 250)
})
</script>

```

`<script>
document.addEventListener('DOMContentLoaded', (event) => {
  // Give some times for Bricks to init the sliders
  setTimeout(() => {
    // Please replace rrbqsp to your Slider element ID !!NOT CSS ID!!
    const mySlider = window.bricksData?.splideInstances['rrbqsp'] || false
    // Please replace the button classes to suit your scenario
    const myPrevBtn = document.querySelector('.my-prev')
    const myNextBtn = document.querySelector('.my-next')

    if (mySlider && myPrevBtn && myNextBtn) {
      // Add click event handlers for your custom buttons
      myPrevBtn.addEventListener('click', function () {
        mySlider.go('-1') // go() function by SplideJS
      })
      myNextBtn.addEventListener('click', function () {
        mySlider.go('+1') // go() function by SplideJS
      })
    }
  }, 250)
})
</script>
`

###### Bricks CLI

###### How to add a custom animation in interaction

