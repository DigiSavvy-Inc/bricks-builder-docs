---
title: "Filter: bricks/form/action/{form_action} – Bricks Academy"
url: https://academy.bricksbuilder.io/article/filter-bricks-form-action-form_action/
date: 2025-05-01T12:03:11.501846
status: success
---

# Filter: bricks/form/action/{form_action} – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/filter-bricks-form-action-form_action/](https://academy.bricksbuilder.io/article/filter-bricks-form-action-form_action/)*

## Table of Contents

- [Filter: bricks/form/action/{form_action}](#filter-bricksformactionformaction)
  - [Example usage](#example-usage)
  - [Parameters:](#parameters)
        - [Filter: bricks/use_duplicate_content](#filter-bricksuseduplicatecontent)
        - [Filter: bricks/maintenance/should_apply](#filter-bricksmaintenanceshouldapply)

## Filter: bricks/form/action/{form_action}

Thebricks/form/action/{form_action}filter is triggered when a custom action (one that is not reserved by Bricks) is selected in a form. It allows developers to define custom logic for handling such actions dynamically.

`bricks/form/action/{form_action}`

Bricks provides several reserved actions out of the box, including:

- email
- redirect
- mailchimp
- sendgrid
- login
- registration
- lost-password
- reset-password
- custom

If the user’s selected action is not in this list, thebricks/form/action/{form_action}filter is triggered.

`bricks/form/action/{form_action}`

### Example usage

Here’s how you can handle a custom action calledslack-notification:

`slack-notification`

```
// Handle the Slack notification action
add_action(
    'bricks/form/action/slack-notification',
    function ( $form ) {
        $settings = $form->get_settings();
        $fields   = $form->get_fields();

        // Implement Slack notification logic
    }
);
```

`// Handle the Slack notification action
add_action(
    'bricks/form/action/slack-notification',
    function ( $form ) {
        $settings = $form->get_settings();
        $fields   = $form->get_fields();

        // Implement Slack notification logic
    }
);`

### Parameters:

- $form(\Bricks\Integrations\Form\Init): The current form instance, providing access to settings and submitted fields.

`$form`

###### Filter: bricks/use_duplicate_content

###### Filter: bricks/maintenance/should_apply

