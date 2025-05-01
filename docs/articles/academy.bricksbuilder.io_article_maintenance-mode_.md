---
title: "Maintenance Mode – Bricks Academy"
url: https://academy.bricksbuilder.io/article/maintenance-mode/
date: 2025-05-01T12:03:34.153083
status: success
---

# Maintenance Mode – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/maintenance-mode/](https://academy.bricksbuilder.io/article/maintenance-mode/)*

## Table of Contents

- [Maintenance Mode](#maintenance-mode)
        - [Scroll Snap](#scroll-snap)
        - [How to set up your Google Maps API key](#how-to-set-up-your-google-maps-api-key)

## Maintenance Mode

Bricks 1.9.4 introduces theMaintenance Modefeature. A straightforward way to manage your site’s availability during updates or construction.

How to enable Maintenance Mode

1. Log in to the WordPress dashboard.
2. Navigate to Bricks > Settings > Maintenance.

Here, you’ll find several settings to configure:

- Mode selection: ChooseDisabled,Maintenance, orComing Soon. “Maintenance” mode (HTTP status code 503) indicates that your site is temporarily unavailable, signaling search engines to come back later. “Coming soon” mode (HTTP status code 200) indicates that your site is available for search engine indexing.
- Template(optional): Assign a custom single template for your maintenance or coming soon mode.Render popups(optional): Enable this setting if you want Bricks popups to be rendered on the maintenance or coming soon template. This isdisabled by default.
- Render popups(optional): Enable this setting if you want Bricks popups to be rendered on the maintenance or coming soon template. This isdisabled by default.
- Bypass maintenance: Customize access settings for different user roles.
- Exclude posts/pages(since 2.0): Select specific pages or posts where Maintenance Mode shouldnotbe applied.

`Disabled`

`Maintenance`

`Coming Soon`

- Render popups(optional): Enable this setting if you want Bricks popups to be rendered on the maintenance or coming soon template. This isdisabled by default.

Configuring role-based access

In the “Bypass maintenance” setting:

1. Select from the dropdown menu:Logged-in usersallows all logged-in users to bypass maintenance mode;Logged-in users with roleprovides a more granular control.
2. IfLogged-in users with roleis selected, checkboxes will appear to enable or disable maintenance mode bypass for specific roles such as Editor, Author, Contributor, etc.

`Logged-in users`

`Logged-in users with role`

`Logged-in users with role`

Individual user access settings

To configure access on an individual user level:

1. From the WordPress dashboard, go to “Users”.
2. Click to edit a specific user’s profile.
3. In the user profile, find and adjust the “Bypass Maintenance” setting. This allows you to enable or disable maintenance mode bypass for that user, overriding the broader role-based settings.

Filters:

- https://academy.bricksbuilder.io/article/filter-bricks-maintenance-should_apply/

###### Scroll Snap

###### How to set up your Google Maps API key

