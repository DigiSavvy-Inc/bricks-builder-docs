---
title: "Theme Styles – Bricks Academy"
url: https://academy.bricksbuilder.io/article/theme-styles/
date: 2025-02-27T15:31:22.525860
status: success
---

# Theme Styles – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/theme-styles/](https://academy.bricksbuilder.io/article/theme-styles/)*

## Table of Contents

- [Theme Styles](#theme-styles)
  - [Conditions](#conditions)
    - [Exclude condition](#exclude-condition)
  - [Export](#export)
  - [Import](#import)
  - [Style Hierarchy](#style-hierarchy)
        - [Save & Publish](#save--publish)
        - [Page Settings](#page-settings)

## Theme Styles

Adjust the default styling of your site layout, elements, colors, links, typography, etc. throughout your site via Theme Styles for a consistent and easy-to-maintain design system for your entire site.

Access the Theme Styles by clicking theSettings(gear) icon in the builder toolbar. Then go toTheme Styles.

To create your own Theme Style, click theCreate(plus) icon and provide a name.

Apply any styling changes you want in the control groups below (like setting your fonts under “Typography”, etc.).

### Conditions

Open theConditionscontrol group to tell Bricks where on your site this theme style should be used.

To apply a theme style to your entire website open theConditionscontrol group, clickAdd Condition, and selectEntire Website.

You can set as many theme style conditions as you want.

Let’s say you want to apply a Theme Style to two specific landing pages and your home page. You simply add a condition, click on Individual, and select your two landing pages. Then you add another condition and selectFront page.

These are the available control groups:

- CONDITIONS
- GENERAL
- COLORS
- CONTENT
- LINKS
- TYPOGRAPHY
- ELEMENT – SECTION
- ELEMENT – CONTAINER
- ELEMENT – BLOCK
- ELEMENT – DIV
- ELEMENT – ACCORDION
- ELEMENT – ALERT
- ELEMENT – BUTTON
- ELEMENT – CAROUSEL
- ELEMENT – CODE
- ELEMENT – COUNTER
- ELEMENT – DIVIDER
- ELEMENT – FORM
- ELEMENT – HEADING
- ELEMENT – ICON BOX
- ELEMENT – IMAGE
- ELEMENT – IMAGE GALLERY
- ELEMENT – LIST
- ELEMENT – NAV MENU
- ELEMENT – POST CONTENT
- ELEMENT – META DATA
- ELEMENT – POST NAVIGATION
- ELEMENT – RELATED POSTS
- ELEMENT – TAXONOMY
- ELEMENT – POST TITLE
- ELEMENT – PRICING TABLES
- ELEMENT – PROGRESS BAR
- ELEMENT – SEARCH
- ELEMENT – SIDEBAR
- ELEMENT – SLIDER
- ELEMENT – ICON LIST
- ELEMENT – SVG
- ELEMENT – TABS
- ELEMENT – TEAM MEMBERS
- ELEMENT – TESTIMONIALS
- ELEMENT – TEXT
- ELEMENT – VIDEO
- ELEMENT – WORDPRESS
- WOOCOMMERCE – BUTTON

#### Exclude condition

Since Bricks 1.3.6 you’ll be able to set exclude conditions for any theme style. To exclude a specific condition you need to toggle the exclude control. Excluding a certain condition will let Bricks know that if the condition applies in a certain scenario, then that theme style won’t be used.

### Export

1. Inside the builder go toSettings > Theme styles
2. Select the theme style you wish to export
3. Click theEdit(pencil) icon
4. Click theExport(download) icon
5. Download the generated JSON file to your computer

`Settings > Theme styles`

### Import

1. Inside the builder go toSettings > Theme styles
2. Click theCreate(plus) icon
3. Click theImport(upload) icon
4. Select the theme style JSON file from your computer, and upload it

`Settings > Theme styles`

If a theme style with the same name already exists in your installation, the import will fail. This is to prevent any theme styles with identical names.

### Style Hierarchy

Bricks automatically applies the most specific styles to your site. Theme Styles are preceded by page settings (as they are more specific). And page settings are preceded by elements settings on an individual page. This allows you to easily mix and match styles to your exact requirements.

###### Save & Publish

###### Page Settings

