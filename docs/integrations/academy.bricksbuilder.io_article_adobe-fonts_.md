---
title: "Integration: Adobe Fonts – Bricks Academy"
url: https://academy.bricksbuilder.io/article/adobe-fonts/
date: 2026-01-05T11:09:10.375031
status: success
---

# Integration: Adobe Fonts – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/adobe-fonts/](https://academy.bricksbuilder.io/article/adobe-fonts/)*

## Table of Contents

- [Integration: Adobe Fonts](#integration-adobe-fonts)
  - [How to use Adobe Fonts with Bricks](#how-to-use-adobe-fonts-with-bricks)
  - [Variable fonts](#variable-fonts)
        - [CSS Grid Layout](#css-grid-layout)
        - [Menu Builder](#menu-builder)

## Integration: Adobe Fonts

### How to use Adobe Fonts with Bricks

All you need to do is provide Bricks with your Adobe Fonts “Project ID”.

First, visit the “web projects” section inside your Adobe Fonts account:https://fonts.adobe.com/my_fonts#web_projects-section

Each of your web projects contains a unique “Project ID”.

Copy the project ID of the web project whose fonts you want to use on your Bricks site.

Next, inside your WordPress dashboard, go toBricks > Settings > API keysand paste the project ID into the “Adobe fonts (Project ID)” input field. Then save your settings.

`Bricks > Settings > API keys`

Next to the project ID input, a “Sync fonts” button should now be visible. Click it to fetch the Adobe fonts of this project. A success message should appear & the “Published Adobe fonts” counter should reflect the number of published fonts.

Those fonts are now available inside the builder in anyfont-familydropdown:

`font-family`

NOTE: Bricks recognizes when you use an Adobe font that is also available as a Google font. Bricks will load only the Adobe font to prevent loading this font from Google as well.

### Variable fonts

Bricks also provides a newfont-variation-settings. This CSS property allows you to control the four-letter axis names of a variable Adobe font. Such as thewght,wdth,slnt, andital.

`font-variation-settings`

`wght`

`wdth`

`slnt`

`ital`

For more information about the specifics please visithttps://developer.mozilla.org/en-US/docs/Web/CSS/font-variation-settings

You can view available variable Adobe fonts by selecting “Variable Fonts” under “Font technology onhttps://fonts.adobe.com/fonts.

NOTE: This newfont-variation-settingsis also available forcustom fonts. Google fonts currently only support thewghtaxis in Bricks. We are working on full variable font support with Google fonts as well.

`font-variation-settings`

`wght`

###### CSS Grid Layout

###### Menu Builder

