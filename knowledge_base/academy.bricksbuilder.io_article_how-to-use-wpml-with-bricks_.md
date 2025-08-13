---
title: "How to use WPML with Bricks – Bricks Academy"
url: https://academy.bricksbuilder.io/article/how-to-use-wpml-with-bricks/
date: 2025-02-27T15:31:49.516666
status: success
---

# How to use WPML with Bricks – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/how-to-use-wpml-with-bricks/](https://academy.bricksbuilder.io/article/how-to-use-wpml-with-bricks/)*

## Table of Contents

- [How to use WPML with Bricks](#how-to-use-wpml-with-bricks)
  - [Setting up the environment](#setting-up-the-environment)
  - [Translation Options with WPML](#translation-options-with-wpml)
  - [Translating website content](#translating-website-content)
    - [Page & posts translation:](#page--posts-translation)
    - [Template translation:](#template-translation)
    - [Example: Translating an archive template:](#example-translating-an-archive-template)
  - [Language switcher & menu translation](#language-switcher--menu-translation)
  - [Sync Bricks data across translated pages](#sync-bricks-data-across-translated-pages)
    - [Step 1: Edit your original page with Bricks](#step-1-edit-your-original-page-with-bricks)
    - [Step 2: Save your changes](#step-2-save-your-changes)
    - [Step 3: Edit with WordPress](#step-3-edit-with-wordpress)
    - [Step 4: Update translation in the “Languages” panel](#step-4-update-translation-in-the-languages-panel)
  - [Editing translated content with Bricks](#editing-translated-content-with-bricks)
  - [Additional resources](#additional-resources)
  - [Fancy trying out WPML?](#fancy-trying-out-wpml)
        - [How to get your Instagram Access Token](#how-to-get-your-instagram-access-token)
        - [Save Form Submissions](#save-form-submissions)

## How to use WPML with Bricks

WPML is a WordPress plugin known for its role in facilitating the creation of multilingual websites.

Coupling it with Bricks (@since 1.9.1) allows not only for the manual translation of posts, pages, and various content types into numerous languages but also offers automatic translation features, significantly broadening your website’s reach and accessibility.

`@since 1.9.1`

Once you’ve established a page in your primary language with Bricks, WPML enables you to easily translate the content into any language you wish to add to your website, be it manually or automatically.

This documentation will guide you through the process of translating your Bricks website using WPML.

### Setting up the environment

Before translating, set up your environment with the necessary plugins:

1. Bricks setup:This guide will illustrate the translation process using a simple Bricks website. This website has main pages like Home and Blog, and templates including a header and an “All Archives” template, which has atemplate conditionto apply to all archives and the blog page.
2. This guide will illustrate the translation process using a simple Bricks website. This website has main pages like Home and Blog, and templates including a header and an “All Archives” template, which has atemplate conditionto apply to all archives and the blog page.

- This guide will illustrate the translation process using a simple Bricks website. This website has main pages like Home and Blog, and templates including a header and an “All Archives” template, which has atemplate conditionto apply to all archives and the blog page.

1. WPML plugin installation:You can use theOTGS installerto install the requiredWPML Multilingual CMSandWPML String Translationplugins.
2. You can use theOTGS installerto install the requiredWPML Multilingual CMSandWPML String Translationplugins.

- You can use theOTGS installerto install the requiredWPML Multilingual CMSandWPML String Translationplugins.

1. Language Configuration:You can configure your website’s languages and other settings throughthe WPML setup wizard.
2. You can configure your website’s languages and other settings throughthe WPML setup wizard.

- You can configure your website’s languages and other settings throughthe WPML setup wizard.

### Translation Options with WPML

WPML offers different ways to translate your content:

1. Advanced Translation Editor:Manual Translation: A method where each page & string is translated individually. This guide focuses on this approach.Automatic Translation: A method that allows for automatic content translation, with an option for later edits.
2. Manual Translation: A method where each page & string is translated individually. This guide focuses on this approach.
3. Automatic Translation: A method that allows for automatic content translation, with an option for later edits.
4. String Translation:An additional feature for translating strings, such as widgets and admin texts.
5. An additional feature for translating strings, such as widgets and admin texts.
6. Edit with Bricks:Post-translation, modifications to content and design for different languages can be done directly with Bricks, if necessary.
7. Post-translation, modifications to content and design for different languages can be done directly with Bricks, if necessary.
8. Additional Resources:For extensive details, refer to the officialWPML documentation.
9. For extensive details, refer to the officialWPML documentation.

- Manual Translation: A method where each page & string is translated individually. This guide focuses on this approach.
- Automatic Translation: A method that allows for automatic content translation, with an option for later edits.

- An additional feature for translating strings, such as widgets and admin texts.

- Post-translation, modifications to content and design for different languages can be done directly with Bricks, if necessary.

- For extensive details, refer to the officialWPML documentation.

### Translating website content

Translate your website content using WPML and Bricks through the following steps:

#### Page & posts translation:

Use the WPML Advanced Translation Editor to create translations for each page in the desired languages.For comprehensive guidance on the various methods to translate pages and posts created by page builders like Bricks, refer toWPML’s official documentationabout this topic.

#### Template translation:

Translating templates follows the same process as translating WordPress pages & posts. Your template settings & type will be automatically duplicated to the translated post.

If the translation of templates is not automatically enabled when you activate WPML, pleaserefer to the WPML documentationon how to enable translation for custom post types, and ensure that it is enabled for “bricks_template”.

#### Example: Translating an archive template:

We have set up a simple archive template, which is applied to both the “Blog” page and its translated version, “Blogue”.

Each blog page will only display blog posts of that particular language (using only one template):

### Language switcher & menu translation

1. Language switcherBricks provides a “Language switcher” element for WPML, which you can add anywhere on your site. You can customize the language switcher from the WordPress dashboard under WPML > Languages > Custom language switchers.
2. Bricks provides a “Language switcher” element for WPML, which you can add anywhere on your site. You can customize the language switcher from the WordPress dashboard under WPML > Languages > Custom language switchers.

- Bricks provides a “Language switcher” element for WPML, which you can add anywhere on your site. You can customize the language switcher from the WordPress dashboard under WPML > Languages > Custom language switchers.

1. WPML menu translation:Consult WPML documentation for guidance ontranslating WordPress menus.
2. Consult WPML documentation for guidance ontranslating WordPress menus.

- Consult WPML documentation for guidance ontranslating WordPress menus.

### Sync Bricks data across translated pages

After translating a page, you might want to modify the original page. Those changes you perform with Bricks in your original page are not applied to the secondary language pages.

But Bricks and WPML make it seamless to sync your design changes across translated pages without affecting the translated text. Here’s how you can do it:

#### Step 1: Edit your original page with Bricks

Open the page in the primary language in the builder. Make the necessary design changes (edit layout, change styles, etc.)

#### Step 2: Save your changes

Once done, save your changes.

#### Step 3: Edit with WordPress

Close the builder by clicking “Edit with WordPress” to edit the page in WordPress.

#### Step 4: Update translation in the “Languages” panel

In the WordPress editor, navigate to the “Languages” panel. Typically found in the right sidebar or the document settings panel.

Here, you will find an option to edit or update the translation. Click the icon to open the “Advanced Translations Editor” as shown in this screenshot:

Translate any untranslated strings inside the Advanced Translation Editor, then click the “Complete” button at the bottom of the screen. Your new design changes are now synced with this translated page without affecting the translated text.

### Editing translated content with Bricks

You can also access and edit the translated content directly with Bricks for specific language design or content modifications.

### Additional resources

Consult the following official WPML documentation for further guidance:

1. Getting Started with WPML.
2. WPML FAQ.
3. Translating Content Created with Page Builders.
4. Translating External Links.

### Fancy trying out WPML?

If you found this post insightful and you’re considering giving WPML a try, we encourage you to useour affiliate link.

Note: The link we’ve provided is an affiliate link. This means we may earn a small commission if you decide to make a purchase through it. This comes at no extra cost to you, and it assists us in further innovating and refining our offerings.

###### How to get your Instagram Access Token

###### Save Form Submissions

