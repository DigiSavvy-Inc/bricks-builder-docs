---
title: "Code review – Bricks Academy"
url: https://academy.bricksbuilder.io/article/code-review/
date: 2025-05-01T12:03:42.445172
status: success
---

# Code review – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/code-review/](https://academy.bricksbuilder.io/article/code-review/)*

## Table of Contents

- [Code review](#code-review)
  - [Core functionalities](#core-functionalities)
  - [Advantages of centralized code monitoring](#advantages-of-centralized-code-monitoring)
        - [Code signatures](#code-signatures)
        - [Global Variables Manager](#global-variables-manager)

## Code review

With the implementation of code signatures in Bricks 1.9.7 providing a robust mechanism to safeguard code authenticity, another new key feature to further improve the security management of your Bricks site is the “Code review”.

The “Code review” gives you a thorough overview of all custom and executable PHP code added to your site through Bricks.

We recommend performing a code review every time before generating code signatures globally via the Bricks settings.

You can access and start a “Code review” underBricks > Settings > Custom codeby clicking the “Start: Code review” button.

`Bricks > Settings > Custom code`

### Core functionalities

Review executable code & functions:The code review displays all instances of executable code in Code elements, SVG elements (source: code), Query editor instances, and all functions called throughecho:tags.

`echo:`

Quickly locate code:View and edit the specific page or template where each code instance is located, along with the element’s ID, and if contains a valid, invalid or no code signature. And the user who last signed the code.

Lists all echo function names in use:At the bottom of the code review results, you’ll find a code snippet for the new Bricks filterbricks/code/echo_function_names, which you can copy & paste into your Bricks child themefunctions.phpfile in order to use those functions in your dynamicechotag. For more details about using theechotag in Bricks 1.9.7+, please visithttps://academy.bricksbuilder.io/article/filter-bricks-code-echo_function_names/

`bricks/code/echo_function_names`

`functions.php`

`echo`

`echo`

### Advantages of centralized code monitoring

- Centralized code oversight:Offering one page to review all the Bricks-added PHP code on your site, this feature makes it easy to ensure that all code added through Bricks elements to your website is legitimate and safe.
- Proactive security:The new code review feature empowers you to identify and rectify potential exploitations preemptively by providing an overview of all code elements.

###### Code signatures

###### Global Variables Manager

