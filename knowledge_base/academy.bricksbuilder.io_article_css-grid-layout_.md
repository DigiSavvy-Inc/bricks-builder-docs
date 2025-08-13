---
title: "CSS Grid Layout – Bricks Academy"
url: https://academy.bricksbuilder.io/article/css-grid-layout/
date: 2025-02-27T15:30:40.815756
status: success
---

# CSS Grid Layout – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/css-grid-layout/](https://academy.bricksbuilder.io/article/css-grid-layout/)*

## Table of Contents

- [CSS Grid Layout](#css-grid-layout)
  - [Creating a grid layout](#creating-a-grid-layout)
  - [Setting up column & row tracks (explicit grid)](#setting-up-column--row-tracks-explicit-grid)
    - [Implicit grid](#implicit-grid)
    - [Min & max grid track sizes](#min--max-grid-track-sizes)
    - [auto-fill & auto-fit keywords](#auto-fill--auto-fit-keywords)
    - [Repeat track sizes](#repeat-track-sizes)
  - [Placing grid items (by line number)](#placing-grid-items-by-line-number)
  - [Notes](#notes)
    - [Additional resources](#additional-resources)
        - [Interactions](#interactions)
        - [Integration: Adobe Fonts](#integration-adobe-fonts)

## CSS Grid Layout

Available since Bricks 1.6.1 CSS grid allows you to create two-dimensional layouts (columns & rows). Whereas CSS flexbox, which Bricks uses as the default layout model, is designed for one-dimensional layouts (either column or row).

### Creating a grid layout

You can turn any layout element (section, container, block, div) into a CSS grid layout by setting theDisplayvalue togrid. This element is yourGrid Container.

`grid`

Every direct child element of your Grid container is aGrid Item, with additional settings forGrid column&Grid rowto place an item it within the grid.

When editing a grid container in the builder a grid overlay becomes visible indicating thegrid cells. Clicking the little four-square element action icon lets to show/hide this overlay.

As you can see in the screenshot above grid items are laid out in rows by default, covering the full width of the grid container. Which in itself doesn’t unlock the true power of CSS grid, until you start …

### Setting up column & row tracks (explicit grid)

Once we’ve created our grid container it is time to define our grid column & rowtracks.

We can do this explicitly via theGrid template columns(grid-template-columns) &Grid template rows(grid-template-rows) settings of our grid container.

`grid-template-columns`

`grid-template-rows`

Let’s explore a few examples together …

grid-template-columns: 200px 1fr 2fr

`grid-template-columns: 200px 1fr 2fr`

Each value of thegrid-template-columnsproperty creates a column track.

`grid-template-columns`

The example above creates a three-column grid layout.

Column 1 has a fixed width of 200px. Column 2 is1fra column 3 is2frwide.

`1fr`

`2fr`

fris a new flexible unit, called the fractional unit, which takes up x parts of the available space.

`fr`

How isfrcalculated?

`fr`

Let’s say our grid container has a width of 1100px (the container’s default width).

We first need to subtract all non-fr values and gaps: So minus the fixed 200px width of column 1 the remaining available width is 900px.

We have 3 fractional units in total (1fr from column 2 plus 2fr from column 3) to allocate the remaining space towards.

Meaning 1fr equals 300px (= 900px / 3). So column 2 is 300px wide (= 1fr x 300px), and column 3 is 600px (= 2fr x 300px) wide.

grid-template-rows: 100px 300px

`grid-template-rows: 100px 300px`

Each value of thegrid-template-rows property creates a row track.

`grid-template-row`

The example above explicitly defines the first two rows. Row 1 is 100px high, and row 2 is 300px high.

As we only explicitly defined the height for the first two rows, the height of any row after row 2 is determined by the height of its content by default. We can change this behaviour by creating an implicit grid …

#### Implicit grid

The grid container automatically generates additional (column & row) tracks for grid items that fall outside of your explicitly defined grid. This is called the implicit grid.

You can define the column & row sizes of this implicit grid via theGrid auto columns(grid-auto-columns) andGrid auto rows(grid-auto-rows) settings of your grid container.

`grid-auto-columns`

`grid-auto-rows`

#### Min & max grid track sizes

TheminmaxCSS function lets you set a minimum and maximum track size.

`minmax`

It accepts two arguments. The first one is the minimum value, and the second one is the maximum value of your grid track.

grid-template-columns: repeat(3, minmax(200px, 1fr))

`grid-template-columns: repeat(3, minmax(200px, 1fr))`

Creates an explicit 3-column grid where each grid item has a min. width of 200px, and a max. width of 1fr.

The problem is this sort of explicit grid is that is it not responsive. It overflows when the viewport is less than 600px wide (3 columns of min. 200px), and the number of columns doesn’t adjust to different breakpoints out of the box.

#### auto-fill & auto-fit keywords

We can use theauto-fillorauto-fitkeywords to address those responsive issues. Allowing us to create responsive grid layouts without media queries.

`auto-fill`

`auto-fit`

So instead of setting an explicit 3 column grid, we use theauto-fillorauto-fitkeyword like this:

`auto-fill`

`auto-fit`

grid-template-columns: repeat(auto-fill, minmax(200px, 1fr))

`grid-template-columns: repeat(auto-fill, minmax(200px, 1fr))`

Which keyword to use depends on the desired behavior.auto-fitexpands grid items to fill the available space. Whileauto-filldoes not (it keeps the available space).

`auto-fit`

`auto-fill`

#### Repeat track sizes

TherepeatCSS function lets you define a repeating track size pattern in a compact format.

It accepts two arguments. The first one is the number of times the track should repeat and the second one is the definition of the tracks.

grid-template-columns: repeat(3, 1fr)Creates an explicit 3-column grid.

`grid-template-columns: repeat(3, 1fr)`

grid-template-rows: 100px repeat(2, 1fr) 200pxCreates an explicit 4-row grid. Where row 1 is 100px high, row 2 & 3 are 1fr each, and row 4 is 200px high.

`grid-template-rows: 100px repeat(2, 1fr) 200px`

### Placing grid items (by line number)

Grid linesmark the start or end of a column or row track. The count starts at 1.

We can use those line numbers to place a grid item onto the grid.

The example below shows an explicit three column grid layout, whose grid items cover three rows.

That means this grid has 4 column lines and 4 row lines.

When inspecting the grid layout of any website by clicking the little bluegridbutton next to the element node in the browser, in this case Chrome, shows you the grid lines as well:

`grid`

In our example above we positionedGrid Item 2via the Grid column (grid-column) and Grid row (grid-row) settings like this, so it takes up two columns and two rows:

`grid-column`

`grid-row`

TheGrid column&Grid rowsettings are available for all grid items (direct children of the grid container).

Syntax: The first value specifies the starting line number. Followed by a forward slash (/). Followed by the second value, which specifies the end line number.

`/`

In our example above we’ve set the Grid column to “2 / 4”. Telling the grid we want Grid Item 2 to start at column line 2 and end at column line 4. The Grid row is set to “1 / 3”, meaning Grid Item 2 starts at row line 1 and ends at row line 3.

We could have achieved the same layout by setting the grid column & Grid row setting to “span 2“.spanis a keyword that tells the grid layout how many columns or rows the item should span.

`span 2`

`span`

### Notes

Named grid areas (grid-template-areas) have to be defined via custom CSS.

`grid-template-areas`

Placing grid items inside a query loop are best done vianth-childcustom CSS.

`nth-child`

This article is meant to provide an overview of CSS grid, and not a complete reference. We recommend following the resources linked below to learn more about CSS grid.

#### Additional resources

- A Complete Guide to CSS Grid(by CSS tricks)
- learncssgrid.com(comprehensive CSS grid overview)
- cssgrid.io(free CSS grid course by Wes Bos)

###### Interactions

###### Integration: Adobe Fonts

