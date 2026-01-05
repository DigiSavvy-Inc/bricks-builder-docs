---
title: "How to use Polylang with Bricks – Bricks Academy"
url: https://academy.bricksbuilder.io/article/polylang/
date: 2026-01-05T11:09:37.811710
status: success
---

# How to use Polylang with Bricks – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/polylang/](https://academy.bricksbuilder.io/article/polylang/)*

## Table of Contents

- [How to use Polylang with Bricks](#how-to-use-polylang-with-bricks)
  - [Setting up Polylang with Bricks](#setting-up-polylang-with-bricks)
  - [Translating posts & pages](#translating-posts--pages)
  - [Translating components](#translating-components)
  - [Translating templates](#translating-templates)
  - [Using templates conditions](#using-templates-conditions)
  - [Managing multilingual menus](#managing-multilingual-menus)
  - [The language switcher](#the-language-switcher)
  - [Troubleshooting common Polylang issues](#troubleshooting-common-polylang-issues)
    - [1. Templates don’t show after Polylang activation](#1-templates-dont-show-after-polylang-activation)
    - [2. Untranslated templates do not appear](#2-untranslated-templates-do-not-appear)
    - [3. Incorrect language in menus](#3-incorrect-language-in-menus)
    - [4. Incorrect language query results in Archive or Search template](#4-incorrect-language-query-results-in-archive-or-search-template)
  - [Additional resources](#additional-resources)
        - [Menu Builder](#menu-builder)
        - [How to get your Instagram Access Token](#how-to-get-your-instagram-access-token)

## How to use Polylang with Bricks

Polylang is a WordPress plugin designed to simplify the creation of multilingual websites.

With Polylang, you can write posts, custom post types, pages, create categories, and post tags in multiple languages.

In combination, Bricks and Polylang facilitate the design and management of multilingual websites.

After creating a page in your default language with Bricks, you can use Polylang to translate the page into any other language your website supports.

### Setting up Polylang with Bricks

Assuming you have Bricks installed and activated on your WordPress site, the next step is to set up Polylang. This guide applies to both the free version of Polylang and Polylang Pro.

To set up Polylang with Bricks, follow the steps below:

1. In your WordPress dashboard, go toPlugins > Add New.
2. Type “Polylang” into the search bar and press Enter.
3. You’ll see the Polylang plugin in the search results. Click onInstall Now.
4. After the installation is complete, clickActivate.
5. Once activated, a newLanguagesmenu item appears on your WordPress dashboard. Visit it, and add the languages you want to support on your website.

`Plugins > Add New`

`Install Now`

`Activate`

`Languages`

Remember to set the default language and add other languages as needed.

After adding languages and assigning any current posts/pages to their appropriate language, you can start translating your pages and posts with Polylang.

For Polylang Pro users, the installation process is slightly different as the plugin needs to be downloaded from the Polylang website and uploaded to your WordPress site. You can refer to the official Polylang documentation for detailed instructions on installing Polylang Pro.

For detailed instructions on configuring Polylang’s settings, please refer to theofficial Polylang documentation.

### Translating posts & pages

Translating your pages and posts using Polylang and Bricks is a straightforward process. Here are the steps:

1. In your WordPress dashboard, navigate to the page or post you want to translate.
2. On the right-hand side, you’ll see a “Languages” meta box (added by Polylang). This box displays your default language and other languages you’ve added.
3. Under each language, you’ll see a “+” button. Click this button to create a new translation for the selected language.

1. This action will create a new page or post draft. You can now use Bricks to design your page or write your post in the new language.
2. Once you’re done, click “Publish”. The translated page or post will automatically be linked to the original one.

Note:Polylang Pro users have the advantage of the “Clone” feature, which allows you to copy the entire content and settings of a page or post into a new translation. This can significantly speed up the translation process, especially for complex layouts.

For users of the free version of Polylang, theYoast Duplicate Postplugin can be a good alternative. It allows you to duplicate a post or page, which you can then edit with the translation.

Make sure to enable the duplicator for the “My templates” post type underSettings > Duplicate post > Permissions.Assign the duplicate page to the correct language and link it back to the page you’ve cloned it from.

`Settings > Duplicate post > Permissions`

Please ensure you check theofficial Polylang documentationfor detailed instructions.

### Translating components

Since Bricks 2.2-beta, you can now translate components with Polylang. All component strings are registered automatically, and you can translate them directly from the WordPress dashboard.

To translate component strings:

1. Go toLanguages > Translations.
2. Search for the component string you want to translate.
3. Add translations for each language your site supports and save.

Make sure the admin language selector in the top admin bar is set toShow all languages.

### Translating templates

Translating templates in Bricks with the help of Polylang is a slightly distinct process compared to translating standard pages or posts. This is mainly because the translation of Bricks templates is not enabled by default in Polylang (as existing templates without a language set are not rendered on the front end).

Here is a step-by-step process to enable it:

1. In your WordPress dashboard, navigate toLanguages > Settingsto visit theCustom post types and Taxonomiestab.

`Languages > Settings`

`Custom post types and Taxonomies`

1. Enable theMy Templates (bricks_template)checkbox enables translation for your Bricks templates.

`My Templates (bricks_template)`

1. Next, go toBricks > Templatesin your WordPress dashboard.
2. Choose the template you want to translate and assign a language to it in the “Languages” meta box.

`Bricks > Templates`

1. Once the language is set, you can initiate the translation process as you would do with a standard post or page by clicking the “+” button for the desired language in the Languages meta box.

1. The newly translated template will be created in draft mode. At this point, you can modify the content and adapt it to the new language using Bricks.

Note:Setting a language for your current templates is a prerequisite before you can translate them.

Important:Duplicating the template for each language you wish to translate it into is essential. If a Bricks page uses a template that has not been translated into the page’s language, that template will not be visible on the page in that language. Hence, ensure that all the templates used on your pages are translated for each supported language.

### Using templates conditions

Bricks templates havetemplate conditionsthat define where a particular template is rendered on your website. While these conditions offer flexibility, using them with Polylang introduces complexities due to how Polylang handles languages as WordPress taxonomy terms.

Although you can select language terms in Bricks conditions, it’s generally not recommended because of potential unexpected bugs. This is due to Polylang creating distinct posts or pages for each language, which are separate entities linked by the plugin.

Due to backward compatibility, these language terms are available in the conditionals but may not behave as expected.

Instead, it’s advisable to directly translate the templates as covered in theTranslating templatessection. This involves duplicating each template for every language you want to support and translating the content within those templates. This method ensures consistent results when showing the correct template per language and avoids potential confusion and inconsistencies.

### Managing multilingual menus

Polylang’s method for handling menu translations involves creating a separate menu for each language. To do so, you should follow these steps:

1. Go toAppearance > Menusin your WordPress dashboard.
2. ClickCreate a new menu.
3. Give your menu a name, ideally including the language for easy identification.
4. Choose the display location for this menu, then clickCreate Menu.
5. (Optional)Use the admin language option in the admin bar at the top of the screen to match the menu language. This ensures the pages listed are in the selected language, helping you add the correct content.
6. Start adding the pages, posts, categories, or custom links this menu will contain.
7. Repeat these steps for each language your website supports.

`Appearance > Menus`

`Create a new menu`

`Create Menu`

Keep in mind that Polylang changes the language of the content on your site, not individual menu items, so you’ll need to create separate menus for each language. Additionally, when translating a page or template (e.g., a header template with a Nav element), be sure to edit the navigation element in the translated template to select the correct menu for that language. This ensures that each language version of the header template displays the appropriate menu.

For more details, please refer to the Polylang documentation:https://polylang.pro/doc/create-menus/.

### The language switcher

Bricks provides a dedicated “Language switcher” element for Polylang, which you can add anywhere on your site and customize without leaving the builder.

To replace default Polylang flags with custom ones, please refer to the Polylang documentation on this topichere.

You can also add the language switcher to your WordPress menu by adding the “Language switcher” under Appearance > Menus like this:

### Troubleshooting common Polylang issues

When integrating Polylang with Bricks, you might encounter some common issues. Here are a few possible problems and suggested solutions:

#### 1. Templates don’t show after Polylang activation

If you have Bricks templates that don’t appear after activating Polylang, this might be due to language settings. Ensure each of your templates is assigned a language. This setting is found on the right side of the WordPress editor page under “Languages”. Remember to update your template after assigning a language.

#### 2. Untranslated templates do not appear

When an untranslated Bricks template doesn’t appear, it might be due to a language discrepancy between the page and the template. If a Bricks page uses a template that isn’t translated into that page’s language, the template won’t show. To fix this, translate your templates into all languages your pages use.

#### 3. Incorrect language in menus

If a menu appears in the wrong language, double-check that you’ve assigned the correct language to each of your menus, as per theManaging multilingual menussection above. Remember, Polylang requires a separate menu for each language on your site.

#### 4. Incorrect language query results in Archive or Search template

Please ensure all archive or search templates have enabledIs main queryon the main query loop.

### Additional resources

To learn more about Polylang and its various features, you can refer to the following resources from Polylang’s official documentation:

1. Getting Started with Polylang: This guide covers the basics of setting up and using Polylang on your WordPress site.
2. Polylang FAQ: Here you’ll find answers to commonly asked questions about using Polylang.
3. Polylang advanced: This section provides more advanced Polylang guides.

These resources can provide additional insights and answers to more specific or complex issues you might encounter when using Polylang.

###### Menu Builder

###### How to get your Instagram Access Token

