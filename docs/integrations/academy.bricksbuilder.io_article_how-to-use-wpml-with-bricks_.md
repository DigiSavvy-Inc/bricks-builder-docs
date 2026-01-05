---
title: "How to use WPML with Bricks – Bricks Academy"
url: https://academy.bricksbuilder.io/article/how-to-use-wpml-with-bricks/
date: 2026-01-05T11:09:38.550571
status: success
---

# How to use WPML with Bricks – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/how-to-use-wpml-with-bricks/](https://academy.bricksbuilder.io/article/how-to-use-wpml-with-bricks/)*

## Table of Contents

- [How to use WPML with Bricks](#how-to-use-wpml-with-bricks)
  - [Setting up the environment](#setting-up-the-environment)
  - [Translation options with WPML & Bricks](#translation-options-with-wpml--bricks)
  - [Translating website content](#translating-website-content)
    - [Bulk translation via translation dashboard](#bulk-translation-via-translation-dashboard)
    - [Translating individual pages and posts](#translating-individual-pages-and-posts)
    - [Template translation:](#template-translation)
    - [Example: Translating an archive template:](#example-translating-an-archive-template)
  - [Language switcher & menu translation](#language-switcher--menu-translation)
    - [Language switcher](#language-switcher)
    - [WPML menu translation:](#wpml-menu-translation)
  - [Sync Bricks data across translated pages](#sync-bricks-data-across-translated-pages)
    - [Step 1: Edit your original page with Bricks](#step-1-edit-your-original-page-with-bricks)
    - [Step 2: Save your changes](#step-2-save-your-changes)
    - [Step 3: Edit with WordPress](#step-3-edit-with-wordpress)
    - [Step 4: Update translation in the “Languages” panel](#step-4-update-translation-in-the-languages-panel)
  - [Creating different designs per language](#creating-different-designs-per-language)
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

1. Language Configuration:You can configure your website’s languages and other settings throughthe WPML setup wizard. During this process, WPML will also ask you for context about your website, such as what it’s about and whose it for.
2. You can configure your website’s languages and other settings throughthe WPML setup wizard. During this process, WPML will also ask you for context about your website, such as what it’s about and whose it for.

- You can configure your website’s languages and other settings throughthe WPML setup wizard. During this process, WPML will also ask you for context about your website, such as what it’s about and whose it for.

Using the context that you provide, WPML’s AI translator –PTC (Private Translation Cloud)will create translations that fit your target audience and industry.

### Translation options with WPML & Bricks

WPML offers different ways to translate your Bricks content:

1. Advanced Translation Editor:Automatic (AI) Translation: Instantly translate your content using WPML’s AI-based engine, then optionally review it before publishing.Manual Translation: A method where each page & string is translated individually.
2. Automatic (AI) Translation: Instantly translate your content using WPML’s AI-based engine, then optionally review it before publishing.
3. Manual Translation: A method where each page & string is translated individually.
4. String Translation:Translate theme/plugin strings, widget texts, and other interface strings found under WPML → String Translation.
5. Translate theme/plugin strings, widget texts, and other interface strings found under WPML → String Translation.
6. Edit with Bricks:If needed, post-translation modifications to design or layout can be done in the Bricks builder for each language.
7. If needed, post-translation modifications to design or layout can be done in the Bricks builder for each language.

- Automatic (AI) Translation: Instantly translate your content using WPML’s AI-based engine, then optionally review it before publishing.
- Manual Translation: A method where each page & string is translated individually.

- Translate theme/plugin strings, widget texts, and other interface strings found under WPML → String Translation.

- If needed, post-translation modifications to design or layout can be done in the Bricks builder for each language.

For more in-depth information on each method, refer to the officialWPML documentation.

### Translating website content

Translate your website content using WPML and Bricks through the following steps:

#### Bulk translation via translation dashboard

WPML can translate any content you build with Bricks, including pages, posts, templates, and components.

To translate any Bricks content, start by going toWPML→Translation Dashboard. From here, expand the section with the content you want to translate and select your items.

For example, to translate a page, expand thePagessection and select the page. This will include all Bricks element data and any component instance property values used on that page. To translate Bricks components themselves, expand theBricks componentssection and select the components you want to translate.

Next, selectTranslate automaticallyfor the languages you want to translate into, and click theTranslatebutton to begin. If you look under the table, WPML also shows you how much translating your content costs.

In most cases, your translations will be good to go, but you can always review and make changes using WPML’sAdvanced Translation Editor.

Just visit the translated page you want to edit on the front-end, and clickEdit translationin the top admin bar. This will open the editor, where you can make any changes necessary.

Once you’re done reviewing, you can instantly publish your translations and display them on your website. Remember that you need to switch languages to view your translations.

#### Translating individual pages and posts

WhileTranslation Managementis perfect for translating multiple pages and templates in one go, you may sometimes want to focus on a single page or post—either for fine-tuning the translation or making additional adjustments. In those cases, you can use theWPML Advanced Translation Editordirectly from the page/post edit screen.For comprehensive guidance on the various methods to translate pages and posts created by page builders like Bricks, refer toWPML’s official documentationabout this topic.

#### Template translation:

Translating templates follows the same process as translating WordPress pages & posts. Your template settings & type will be automatically duplicated to the translated post.

If the translation of templates is not automatically enabled when you activate WPML, pleaserefer to the WPML documentationon how to enable translation for custom post types, and ensure that it is enabled for “bricks_template”.

#### Example: Translating an archive template:

We have set up a simple archive template, which is applied to both the “Blog” page and its translated version, “Blogue”.

Each blog page will only display blog posts of that particular language (using only one template):

### Language switcher & menu translation

#### Language switcher

Bricks provides a “Language switcher” element for WPML, which you can add anywhere on your site.

By default, the language switcher comes with a basic preset design. However, you can always customize the switcher to match your website style:

1. Go toWPML→Languages.
2. Scroll down toCustom language switchersand check theEnablebox. This will reveal aCustomizebutton.
3. Click the button to set your custom preferences and save.

Your changes will immediately take effect on your website.

#### WPML menu translation:

Consult WPML documentation for guidance ontranslating WordPress menus.

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

### Creating different designs per language

You can also access and edit the translated content directly with Bricks for specific language design or content modifications. For instance, instead of simply translating the text of your homepage, you can create a completely different layout that appeals to a specific target audience.

To create a different design per language:

1. Use the admin language switcher to change to the language you want to edit.
2. Find the page or template you want to make changes to and open it in Bricks.

1. Make your design changes and save. Your pages will now have different designs when switching languages.

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

