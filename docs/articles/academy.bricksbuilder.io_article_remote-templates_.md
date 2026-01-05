---
title: "Remote Templates – Bricks Academy"
url: https://academy.bricksbuilder.io/article/remote-templates/
date: 2026-01-05T11:09:44.788712
status: success
---

# Remote Templates – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/remote-templates/](https://academy.bricksbuilder.io/article/remote-templates/)*

## Table of Contents

- [Remote Templates](#remote-templates)
  - [Step 1: Enable My Templates Access](#step-1-enable-my-templates-access)
  - [Step 2: Remote Templates Settings](#step-2-remote-templates-settings)
        - [Template Settings](#template-settings)
        - [Wireframe Templates](#wireframe-templates)

## Remote Templates

Remote templates allow you to view & insert templates of another Bricks installation. Avoiding the constant template export from one site and then importing them on another site.

Public access to your templates is disabled by default. Follow the steps below to make your templates easily available as a remote template source.

### Step 1: Enable My Templates Access

First, you have to enable template access on the site whose templates you want to browse and insert.

In your WordPress dashboard, go toBricks → Settings → Templatesand enable theMy Templates Accesscheckbox. With this setting enabled, your template library is accessible to anyone who knows your site URL.

It is recommended to restrict access by whitelisting URLs and/or password protection:

Use theWhitelist URLssetting to provide template access only to the specified URLs.

Set a password underPassword Protectionto restrict template access to people who know the correct password.

Since Bricks 1.9.4, you can add unlimited remote template URLs!Click the “Add” button to add another template URL. To remove a previously added remote source, clear the URL and password input fields and save your settings.

Please ensure thepermalink structureof this WordPress website (Settings > Permalinks) is set to something other thanPlain.

### Step 2: Remote Templates Settings

Log into the site you want to browse and insert templates from.

Go toBricks → Settings → Templatesand paste the URL of the Bricks site you want to retrieve templates from into theRemote Templates URLfield.

If you’ve set password protection on the other website, make sure to enter the password underRemote Templates Password.

Then clickSave Settings, open the builder, and then open the template library.

You should now see the remote template URLs added to the templateSOURCEdropdown, as illustrated in the following screenshot:

`SOURCE`

Since version 1.9.4, Bricks pulls in the latest template data every time you view a remote template source instead of storing it in your database. Guaranteeing you that you always work with the latest remote template data without having to worry about refreshing the remote templates every time.

###### Template Settings

###### Wireframe Templates

