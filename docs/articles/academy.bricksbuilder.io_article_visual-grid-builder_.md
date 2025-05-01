---
title: "Visual Grid Builder – Bricks Academy"
url: https://academy.bricksbuilder.io/article/visual-grid-builder/
date: 2025-05-01T12:03:46.002801
status: success
---

# Visual Grid Builder – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/visual-grid-builder/](https://academy.bricksbuilder.io/article/visual-grid-builder/)*

## Table of Contents

- [Visual Grid Builder](#visual-grid-builder)
  - [How it works](#how-it-works)
    - [Activating the Visual Grid Builder](#activating-the-visual-grid-builder)
    - [Styling elements](#styling-elements)
  - [Controls](#controls)
        - [Map Element](#map-element)
        - [Bricks CSS: Compatibility guidelines](#bricks-css-compatibility-guidelines)

## Visual Grid Builder

The newVisual Grid Builderallows you to visually design and manage your grid layouts. The feature becomes is available for any element with thedisplaycontrol set togrid, and allows you to:

`display`

`grid`

- Adjust grid size: Modify the number of columns and rows to fit your design needs.
- Resize and move elements: Easily adjust the size and position of elements within your grid through simple drag and drop.
- Query loop support: Tweak any query loop item inside your grid.
- Breakpoint support: Create different grid layouts for various breakpoints to ensure responsiveness.
- Rename elements: Organize your layout by renaming elements for better identification.
- Edit elements: Hover over any grid item and click the pencil icon to continue editing it in the element panel.
- Reset options: Reset the entire grid or individual elements on the current breakpoint.
- History: Use history buttons to go back and forth between changes.
- Fill grid: Auto-fill any empty grid cells with one click using Block elements.
- ID & class level: Visually design your grid on the element ID or class-level.

### How it works

#### Activating the Visual Grid Builder

Begin by setting thedisplayproperty of your grid layout element togrid. Once once, the Visual Grid Builder icon appears next to thegridvalue.

`display`

`grid`

`grid`

#### Styling elements

The Visual Grid Builder allows you to style both individual elements and elements that are part of a query loop. The approach to styling depends on whether you are working at the class or ID level. Here’s an overview of how this works:

Static elements:

- ID level: When you resize or move a static element, the changes are reflected in theGrid Itemcontrols, specifically updating theGrid ColumnandGrid Rowproperties. This approach is straightforward and directly modifies the element’s grid positioning.
- Class level: If you have defined the grid at the class level, any resizing or movement of the element will save the changes as custom CSS. These custom styles are applied to theCustom CSScontrol of the main element.

`Grid Item`

`Grid Column`

`Grid Row`

`Custom CSS`

Query loop element:

- ID or class level: When working with elements that are part of a query loop, changes to size or position are saved as custom CSS in theCustom CSScontrol of the main element, regardless of whether you are styling at the ID or class level.

`Custom CSS`

Important: It is crucial not to alter the auto-generated CSS styles, as they are essential for maintaining the layout’s integrity. These styles are clearly marked with code comments, making them easy to identify and preserve. After moving or resizing an element, the CSS will automatically update to reflect the new values. If you choose to reset an element, the auto-generated custom CSS will be cleared, reverting the element to its original state.

### Controls

Grid actions:

1. Reset (Grid): Resets all grid styles for the currently selected breakpoint.
2. Breakpoints: Toggle between different breakpoints without leaving the editor.
3. History: Undo or redo actions.

Grid controls:

1. Columns and rows: Adjust the number of columns and rows within the grid.
2. Gap: Modify the gap between grid elements using any valid CSS value, including variables.
3. Use min/max: Toggle to set column or row size tominmax(0, 1fr)for better flexibility.

`minmax(0, 1fr)`

When you open the Visual Grid Builder, it will automatically detect and adjust the column and row controls to match your existing grid configuration.

Grid panel controls:

1. Individual Columns and rows: Precisely control the size of columns and rows.
2. Elements: Edit the elements within the grid.

Sizes aure automatically calculated from your main element settings. For instance,repeat(3, 2fr)is converted to2fr 2fr 2fr. You can also customize sizes using values like1fr,300px, orminmax(0, 1fr)or any other valid value, to adjust the design to your needs.

`repeat(3, 2fr)`

`2fr 2fr 2fr`

`1fr`

`300px`

`minmax(0, 1fr)`

Single element controls:

1. Resize: Click and drag the borders to resize elements.
2. Move: Click and drag within the element to reposition it.
3. Rename: Click on the element label to rename it.
4. Reset: Reset all styling for the element on the current breakpoint.
5. Edit: Close the Visual Grid Builder and select the element in the structure panel for further editing.

You can also view the index of each element, and if an element is part of a query loop, its specific index within the loop will be displayed, starting at 0.

###### Map Element

###### Bricks CSS: Compatibility guidelines

