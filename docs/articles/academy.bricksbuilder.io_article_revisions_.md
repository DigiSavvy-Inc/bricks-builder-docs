---
title: "Revisions – Bricks Academy"
url: https://academy.bricksbuilder.io/article/revisions/
date: 2026-01-05T11:09:24.018859
status: success
---

# Revisions – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/revisions/](https://academy.bricksbuilder.io/article/revisions/)*

## Table of Contents

- [Revisions](#revisions)
  - [Manage the number of Bricks revisions](#manage-the-number-of-bricks-revisions)
        - [Best Practices](#best-practices)
        - [Responsive Editing](#responsive-editing)

## Revisions

Every time you perform a save in the builder, Bricks creates a revision/snapshot of your Bricks elements data (template, page, etc.). Using the official WordPress Revisions API.

You can browse, preview, and apply your revisions inside the builder by clicking theRevisions(clock) icon in the builder toolbar, then going to the “Revisions” tab.

Select any revision in this list to preview it. The canvas should automatically update showing you the selected revision.

ClickApplyto continue editing the selected revision. ClickDiscardto continue editing your current version.

### Manage the number of Bricks revisions

In order to limit the number of Bricks revisions, you may define the constantBRICKS_MAX_REVISIONS_TO_KEEPlike so (insert this code in the Bricks child theme):

`BRICKS_MAX_REVISIONS_TO_KEEP`

```
if ( ! defined( 'BRICKS_MAX_REVISIONS_TO_KEEP' ) ) {
    define( 'BRICKS_MAX_REVISIONS_TO_KEEP', 10 );
}
```

`if ( ! defined( 'BRICKS_MAX_REVISIONS_TO_KEEP' ) ) {
    define( 'BRICKS_MAX_REVISIONS_TO_KEEP', 10 );
}`

By default, Bricks sets the maximum to 100 revisions per post for the Bricks templates and enabled post types.

You may set the following values:

- true: unlimited revisions
- false or 0: do not store any Bricks’ revisions
- value above 0: store up to this number of revisions per post. Old revisions are automatically deleted.

###### Best Practices

###### Responsive Editing

