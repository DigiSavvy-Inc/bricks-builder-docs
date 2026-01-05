---
title: "Command Palette – Bricks Academy"
url: https://academy.bricksbuilder.io/article/command-palette/
date: 2026-01-05T11:09:09.705955
status: success
---

# Command Palette – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/command-palette/](https://academy.bricksbuilder.io/article/command-palette/)*

## Table of Contents

- [Command Palette](#command-palette)
  - [How to launch It](#how-to-launch-it)
  - [Scope:Builder](#scopebuilder)
  - [Scope:Post Types](#scopepost-types)
  - [Scope:Elements](#scopeelements)
    - [Insert single element](#insert-single-element)
    - [Insert element structure](#insert-element-structure)
    - [Supported operators](#supported-operators)
    - [Element structure example](#element-structure-example)
    - [Quick element insertion](#quick-element-insertion)
    - [Save element structures](#save-element-structures)
  - [Keyboard shortcuts](#keyboard-shortcuts)
  - [Notes](#notes)
        - [Icon Manager](#icon-manager)
        - [Query Data from APIs](#query-data-from-apis)

## Command Palette

Bricks 2.0 introduces theCommand Palette, a powerful new feature that gives you instant keyboard-driven access to core functionality inside the builder.

### How to launch It

Click the command⌘icon in the builder toolbar or use theCMD/CTRL + Kkeyboard shortcut to open the Command Palette, which appears as an overlay, allowing you to type and filter commands across three distinct scopes.

`⌘`

`CMD/CTRL + K`

### Scope:Builder

Navigate to key parts of the builder from a growing list of targets such as classes, variables, templates, theme styles, settings, etc.

### Scope:Post Types

This scope lets browse all registered post types, create new posts or duplicate any existing post.

The scope auto-selects the post type that you are currently editing. So if are editing a Bricks template the “Template (Bricks)” post type will be selected. If you edit a “Page”, then “Page” is selected and so on.

### Scope:Elements

The “Elements” scope will dramatically speed up your workflow by allowing you to insert multiple elements with specific structure in a single action.

By mastering the Emmet-like syntax, you can create complex layouts in seconds rather than minutes, making your design process significantly more efficient.

With practice, this feature becomes second nature and an essential part of your Bricks Builder toolkit, especially for quickly creating common page structures and element combinations that you use frequently, which you can also save for instant access to use whenever needed.

#### Insert single element

To insert a single element simple type its name, such as “Section”, thenARROW-navigate to it in the elements list, and insert it by pressingENTERor just click on the element name.

`ARROW`

`ENTER`

#### Insert element structure

Each element starts with an@symbol.

The element name that the command bar requires is displayed in square brackets in the results list:

`@text-link`

#### Supported operators

Use the following opeators to define nested structure, siblings or a multiplier.

`@`

`@heading`

`>`

`+`

#### Element structure example

@section * 2 > @heading + @text + @buttonThis creates the following structure(two times because of the multiplier:* 2):

`@section * 2 > @heading + @text + @button`

`* 2`

- Section└Container├Heading├Text└Button

`Section`

`Container`

`Heading`

`Text`

`Button`

#### Quick element insertion

After selecting an element from the search results, its name is added to your query with the@prefix, allowing you to quickly build complex queries:

`@`

1. Type@to activate insertion mode
2. Select an element (e.g., “section”)
3. Type>for a child element
4. Continue building your structure
5. Click your element structtureClick the “Insert” button that appears next to your queryPressCMD/CTRL + ENTER
6. Click the “Insert” button that appears next to your query
7. PressCMD/CTRL + ENTER

`@`

`>`

- Click the “Insert” button that appears next to your query
- PressCMD/CTRL + ENTER

`CMD/CTRL + ENTER`

#### Save element structures

Instead of typing out your favorite structures by hand every time can just save them by clicking the “Save” button next to the command bar. Your structures are stored inlocalStorage, so every user on your site can have it own set of their favorite structures.

`localStorage`

To delete a structure, mouseover the structure item in the list, and click the “Delete” icon.

### Keyboard shortcuts

`CMD/CTRL + K`

`ESC`

`TAB > ENTER`

`#`

`/`

`+`

`@`

`/0-9`

`ARROW UP/DOWN`

### Notes

Bricks remembers your last selected scope, even after builder reload (stored in your localStorage).

The “Pages” panel has been deprecated as all its functionality is now available in the Command Palette.

The “Docs” icon disappeared from the toolbar as well, but is still accessible from the “Builder” scope.

###### Icon Manager

###### Query Data from APIs

