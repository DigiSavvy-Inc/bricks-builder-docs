---
title: "An Intro To Templates – Bricks Academy"
url: https://academy.bricksbuilder.io/article/an-intro-to-templates/
date: 2025-02-27T15:31:58.303905
status: success
---

# An Intro To Templates – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/an-intro-to-templates/](https://academy.bricksbuilder.io/article/an-intro-to-templates/)*

## Table of Contents

- [An Intro To Templates](#an-intro-to-templates)
  - [Pre-Designed Community Templates](#pre-designed-community-templates)
  - [My Templates](#my-templates)
  - [Template Conditions](#template-conditions)
    - [Inject Section templates via hooks](#inject-section-templates-via-hooks)
  - [Template Types](#template-types)
  - [Template Bundles & Template Tags](#template-bundles--template-tags)
        - [Template Library](#template-library)

## An Intro To Templates

Templates are a central feature of Bricks. There are different template types. At the very least, you usually create a header, footer, and blog post template.

A template can contain a single section (your website header, a hero section, etc.) or the entire page content (a single blog post layout, archive pages, search results page, error page, etc.).

You can create your own templates or browse dozens of pre-designed templates from theTemplate Libraryby clicking the Templates (folder) icon in the builder toolbar.

Add a screenshot for your template by setting the featured image.

### Pre-Designed Community Templates

Browse our ever-growing collection of pre-designed templates right from within the builder.

Access the Community Templates by clicking the “folder” icon in the builder’s top toolbar. Then, under “Source,” select “Community Templates”. You’ll now see a list of all pre-designed templates:

Insert the template of your choice with a single click and tweak it from there. All community template images are royalty-free and can be used in your and your client’s projects.

TIP:When you start with Bricks, inspecting a template is a great way to learn how a certain layout is structured.

### My Templates

You can view, create, import, and export your own templates by clicking the Templates (folder) icon in the builder toolbar or directly from the WordPress dashboard:

This also provides a great overview of where on your site a template appears (Template Conditions), theTemplate Type, plus any template metadata you’ve added (Templates Bundle,Template Tags) to better organize your templates.

Let’s quickly go over those template-specific terms:

### Template Conditions

Template conditions determine where on your site a template appears.

For example, anArchivetemplate will be used on all author and date archive pages (see screenshot below). TheSingle Blog Posttemplate is responsible for all your posts. Both are set as such via template conditions.

If no template condition is set, Bricks will use published templates of certain Template Type, such as header and footer templates on the front end of your website.

View the table below to see whichTemplate Typesare picked up by default.

To set template conditions for the template you are editing, click theSettings(gear) icon in the builder toolbar, then go toTemplate Settings → Template Conditions:

TIP:To disable the use of default templates, go toBricks → Settingsand select theDisable Default Templatessetting.

#### Inject Section templates via hooks

Want to render a template at a specific WordPress hook? Starting at Bricks 1.9.1, you can inject any template of type “Section” via any WordPress hook.

All you need to do when editing your section template is to select your template condition (i.e., the entire website) and enter the WordPress action hook name under “Hook: Name“. Your section template will now be rendered wherever this action hook is triggered.

You can optionally also set a “Hook: Priority” (default is 10).

`bricks_before_header`

### Template Types

Setting a template type is required for any template.

Assigning the most suitable template type helps you easily filter large template libraries, and it allows Bricks to determine if a certain template should be shown on the front end of your website in case no conditions are set. This is if you haven’t disabled this option as described in the tip above.

IMPORTANT:Section templates do NOT sync/are updated between pages. Please set the template type to show a certain template at a specific area of your site.  “Single” & “Section” templates are unique and not used anywhere by default.

### Template Bundles & Template Tags

These two Bricks template taxonomies can be used to organize and group your templates together. They are 100% optional.

For example, Our Community Templates useTemplate Bundlesto group individual templates of the same website design (Milo, Sizzle, Rank, etc.) together. Feel free to use template bundles in any other way.

Template Tagsare simple tags. The “My Templates” screenshot above uses template tags such as “Dark” and “Light”. Again, they are completely optional but often very useful. Especially as your template library grows over time.

###### Template Library

