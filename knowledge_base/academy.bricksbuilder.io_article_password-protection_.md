---
title: "Password Protection – Bricks Academy"
url: https://academy.bricksbuilder.io/article/password-protection/
date: 2025-02-27T15:31:12.716258
status: success
---

# Password Protection – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/password-protection/](https://academy.bricksbuilder.io/article/password-protection/)*

## Table of Contents

- [Password Protection](#password-protection)
  - [How to set up password protection](#how-to-set-up-password-protection)
  - [Password source options](#password-source-options)
    - [Template password](#template-password)
    - [Post password](#post-password)
    - [Template & post password](#template--post-password)
    - [Password protection filters:](#password-protection-filters)
        - [Breadcrumbs Element](#breadcrumbs-element)
        - [Masonry Layout](#masonry-layout)

## Password Protection

Bricks 1.11.1 introduces a Bricks-native Password Protection feature, giving you a simple yet powerful way to secure content across your website without needing extra plugins.

Whether you want to lock down individual pages, posts, broader areas like custom post types, or even the entire website, you can create custom templates that control access with ease.

Customize the password entry experience, schedule when protection is active, and manage everything directly within Bricks.

This new feature is currently in its experimental phase!We encourage you to test it thoroughly, especially with any caching solutions you use. Your feedback is valuable and will help us refine and improve this feature.

### How to set up password protection

1. Enable this experimental feature underBricks > Settings > General > Password Protection
2. Create a password protection templateFrom the WordPress dashboard, navigate toBricks > Templatesand create a new template.UnderTemplate type, selectPassword protection.
3. From the WordPress dashboard, navigate toBricks > Templatesand create a new template.
4. UnderTemplate type, selectPassword protection.
5. Configure password protection settingsClickEdit in Bricksto customize the template.To access the password protection settings, go toSettings > Template settings > Password protection.Available settings include:Password source:Select how passwords are managed. Options areTemplate password,Post password, orTemplate & post password. See details on each method in thepassword source optionssection below.Password:Set the password for template-wide protection. This field is only available if thePassword sourceis set toTemplate passwordorTemplate & post password.Disable header.Disable footer.Disable popups.Allow logged-in users to bypass.Schedule:Schedule when the password protection is active.Start date:Set the date and time when protection begins.End date:Set the date and time when protection ends.
6. ClickEdit in Bricksto customize the template.
7. To access the password protection settings, go toSettings > Template settings > Password protection.
8. Available settings include:Password source:Select how passwords are managed. Options areTemplate password,Post password, orTemplate & post password. See details on each method in thepassword source optionssection below.Password:Set the password for template-wide protection. This field is only available if thePassword sourceis set toTemplate passwordorTemplate & post password.Disable header.Disable footer.Disable popups.Allow logged-in users to bypass.Schedule:Schedule when the password protection is active.Start date:Set the date and time when protection begins.End date:Set the date and time when protection ends.
9. Password source:Select how passwords are managed. Options areTemplate password,Post password, orTemplate & post password. See details on each method in thepassword source optionssection below.
10. Password:Set the password for template-wide protection. This field is only available if thePassword sourceis set toTemplate passwordorTemplate & post password.
11. Disable header.
12. Disable footer.
13. Disable popups.
14. Allow logged-in users to bypass.
15. Schedule:Schedule when the password protection is active.Start date:Set the date and time when protection begins.End date:Set the date and time when protection ends.
16. Start date:Set the date and time when protection begins.
17. End date:Set the date and time when protection ends.

`Bricks > Settings > General > Password Protection`

- From the WordPress dashboard, navigate toBricks > Templatesand create a new template.
- UnderTemplate type, selectPassword protection.

`Bricks > Templates`

- ClickEdit in Bricksto customize the template.
- To access the password protection settings, go toSettings > Template settings > Password protection.
- Available settings include:Password source:Select how passwords are managed. Options areTemplate password,Post password, orTemplate & post password. See details on each method in thepassword source optionssection below.Password:Set the password for template-wide protection. This field is only available if thePassword sourceis set toTemplate passwordorTemplate & post password.Disable header.Disable footer.Disable popups.Allow logged-in users to bypass.Schedule:Schedule when the password protection is active.Start date:Set the date and time when protection begins.End date:Set the date and time when protection ends.
- Password source:Select how passwords are managed. Options areTemplate password,Post password, orTemplate & post password. See details on each method in thepassword source optionssection below.
- Password:Set the password for template-wide protection. This field is only available if thePassword sourceis set toTemplate passwordorTemplate & post password.
- Disable header.
- Disable footer.
- Disable popups.
- Allow logged-in users to bypass.
- Schedule:Schedule when the password protection is active.Start date:Set the date and time when protection begins.End date:Set the date and time when protection ends.
- Start date:Set the date and time when protection begins.
- End date:Set the date and time when protection ends.

`Settings > Template settings > Password protection`

- Password source:Select how passwords are managed. Options areTemplate password,Post password, orTemplate & post password. See details on each method in thepassword source optionssection below.
- Password:Set the password for template-wide protection. This field is only available if thePassword sourceis set toTemplate passwordorTemplate & post password.
- Disable header.
- Disable footer.
- Disable popups.
- Allow logged-in users to bypass.
- Schedule:Schedule when the password protection is active.Start date:Set the date and time when protection begins.End date:Set the date and time when protection ends.
- Start date:Set the date and time when protection begins.
- End date:Set the date and time when protection ends.

- Start date:Set the date and time when protection begins.
- End date:Set the date and time when protection ends.

1. Set template conditionsSetthe template conditionsunderSettings > Template settings > Conditionsto define where this template applies.For more dynamic control, use thebricks/password_protection/is_activefilter to customize when the template should be active or bypassed.
2. Setthe template conditionsunderSettings > Template settings > Conditionsto define where this template applies.
3. For more dynamic control, use thebricks/password_protection/is_activefilter to customize when the template should be active or bypassed.

- Setthe template conditionsunderSettings > Template settings > Conditionsto define where this template applies.
- For more dynamic control, use thebricks/password_protection/is_activefilter to customize when the template should be active or bypassed.

`Settings > Template settings > Conditions`

`bricks/password_protection/is_active`

1. Add form element for unlockingAdd aForm Elementto the password protection template.Add anUnlock password protectionform action. This action will allow users to unlock the protected content by entering the correct password.
2. Add aForm Elementto the password protection template.
3. Add anUnlock password protectionform action. This action will allow users to unlock the protected content by entering the correct password.

- Add aForm Elementto the password protection template.
- Add anUnlock password protectionform action. This action will allow users to unlock the protected content by entering the correct password.

### Password source options

The behavior of the password protection feature depends on the selectedpassword sourceoption. Below are details on how each option works and instructions for setup:

#### Template password

SelectingTemplate passwordapplies the password set in the template settings to all pages or posts that meet the template conditions. No further configuration is needed on individual posts. Simply:

- Set the password inSettings > Template settings > Password protection > Password.
- Define the template conditions underSettings > Template settings > Conditionsto specify where this template will apply.

`Settings > Template settings > Password protection > Password`

`Settings > Template settings > Conditions`

For any content matching these conditions, the password form will be automatically rendered, restricting access to those pages.

#### Post password

WhenPost passwordis selected, this template customizes the default WordPress password protection form but requires individual post-level password settings.

To protect content using thePost passwordmethod:

1. Enable password protection on each post or page through the WordPress editor.
2. Set a password directly on the individual post or page (or through quick edit).
3. The template conditions will control where the custom password form appearance applies, but protection is managed at the post level.

#### Template & post password

TheTemplate & post passwordoption uses the template password by default. However, if an individual post password is set, it will take precedence.

Setup process:

1. Enter a password inPassword protection > Password.
2. Define template conditions as needed to apply the password protection across relevant content.
3. For any posts with an individual password set, that password will override the template password.

This setup provides flexibility by allowing individual content to have unique passwords while maintaining general protection for all content under the template.

#### Password protection filters:

- https://academy.bricksbuilder.io/article/filter-bricks-password_protection-cookie-expires/
- https://academy.bricksbuilder.io/article/filter-bricks-password_protection-is_active/

###### Breadcrumbs Element

###### Masonry Layout

