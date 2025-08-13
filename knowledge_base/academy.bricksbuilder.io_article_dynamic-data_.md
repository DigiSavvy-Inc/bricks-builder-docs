---
title: "Dynamic Data – Bricks Academy"
url: https://academy.bricksbuilder.io/article/dynamic-data/
date: 2025-02-27T15:30:27.388061
status: success
---

# Dynamic Data – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/dynamic-data/](https://academy.bricksbuilder.io/article/dynamic-data/)*

## Table of Contents

- [Dynamic Data](#dynamic-data)
  - [How to insert dynamic data](#how-to-insert-dynamic-data)
  - [Custom Fields Integrations](#custom-fields-integrations)
    - [Advanced Custom Fields](#advanced-custom-fields)
    - [Meta Box](#meta-box)
    - [Crocoblock JetEngine](#crocoblock-jetengine)
  - [Standard WordPress data](#standard-wordpress-data)
    - [Post fields](#post-fields)
    - [Taxonomies](#taxonomies)
    - [Terms](#terms)
    - [Author Fields](#author-fields)
    - [Current Date fields](#current-date-fields)
    - [Query fields](#query-fields)
    - [Site & Archive fields](#site--archive-fields)
    - [User profile fields](#user-profile-fields)
    - [Native WordPress custom fields](#native-wordpress-custom-fields)
    - [Advanced: echo](#advanced-echo)
    - [Advanced: do_action](#advanced-doaction)
    - [WooCommerce](#woocommerce)
  - [Filters](#filters)
        - [Examples of :array_value filter](#examples-of-arrayvalue-filter)
  - [Key-value pair arguments](#key-value-pair-arguments)
    - [Available arguments:](#available-arguments)
  - [Bricks hooks related to Dynamic Data](#bricks-hooks-related-to-dynamic-data)
        - [Builder Access](#builder-access)
        - [SVG Uploads](#svg-uploads)

## Dynamic Data

Use dynamic data to render all sorts of data from your WordPress database with Bricks.

For example: Featured image, post title, post date, author name, categories, tags, site title, all of your custom fields, etc.

You’ll most likely use dynamic data when creating templates in Bricks. Such as your blog post template, and custom post type templates (e.g. single property listing).

### How to insert dynamic data

The dynamic data picker for text shows up when typing a “{” onto the canvas. You can also click the “bolt” icon in the settings panel to reveal it:

Dynamic data for non-text settings such as images, videos, etc. is available from the “Select dynamic data” dropdown menu in the panel settings.

Below you can see an Advanced Custom Fields gallery (named “Gallery”) rendered inside the Bricks image gallery element:

All dynamic data tags are available in all elements that support dynamic data. This means that you may insert a gallery field (like an ACF gallery field type) inside a text element and it will be rendered as a set ofimgtags (using the filter:image), like so:

`img`

`:image`

### Custom Fields Integrations

You can render much more than just standard dynamic WordPress data. Bricks supports the most popular custom fields plugins such as:

- Advanced Custom Fields
- Meta box
- Crocoblock (JetEngine)(Not support WooCommerce Product Data / Variation Meta Box)
- Pods
- CMB2
- Toolset

This allows you to design templates for even the most complex custom post type layouts and data requirements.

#### Advanced Custom Fields

Bricks integrates with all the ACF and ACF Pro fields, including Flexible Content and Nested Groups.

The fields will be listed in the Dynamic Data dropdown inside of the Bricks builder so you can use them while building your pages and templates with Bricks.

The Relationship (including thebidirectionalimplementation) and the Repeater field types are also available inside the Query Loop builder, so you could loop through the output of these fields while rendering the sub-fields as dynamic data.

The ACF field type “True / False” is great for conditional checks inside the element conditions. By default, the localized “True / False” label is returned. When using it in your element conditions, make sure to apply the:valuefilter. To check for false, you can compare against== 0. Or== 1to check for true.

`:value`

`== 0`

`== 1`

The following dynamic data can be used together withElement conditionseffectively.

`{acf_get_row_layout}`

#### Meta Box

Bricks is compatible with the Meta Box Post Types, Taxonomies, Custom Fields, and Relationships. Regarding the Custom Fields, Bricks will list the fields inside the builder in the Dynamic Data dropdown. According to the custom field contents, these tags will be rendered properly in the front end.

The Group field (when cloneable) and the Relationships will also be available inside the Query Loop builder. You can iterate through these values and render the sub-fields as dynamic data.

It is also possible to build nested non-clone-able Group fields in Bricks Query Loop.

#### Crocoblock JetEngine

Bricks is compatible with Crocoblock JetEngine Post Types, Meta Boxes (Custom fields), Taxonomies, Relations, and Options pages.

Custom Content Types(CCT) has been supported since April 2024 by the JetEngine plugin, not Bricks itself. For any CCT questions, please get in touch with the JetEngine support directly.

Bricks integration with the JetEngine plugin makes the custom fields available as dynamic data inside the Bricks builder.

Bricks also integrates with the JetEngine Relations and Repeaters to feed the Bricks builder query loop.

### Standard WordPress data

By default, you may use the following dynamic data tags.

#### Post fields

The following fields are related to the posts or custom post types.

`{post_title}`

`{post_id}`

`{post_url}`

`{post_slug}`

`{post_type}`

`{post_date}`

`{post_modified}`

`{post_time}`

`{post_comments_count}`

`{post_content}`

`{post_excerpt}`

`{read_more}`

`{featured_image}`

These fields support the followingdynamic data filters:

`{post_title:link}`

`{post_title:link:3}`

`{post_title:link:newTab}`

`{post_date:human_time_diff}`

`{post_excerpt:55}`

`{post_excerpt:format:10}`

`{featured_image:medium_large}`

`{featured_image:large:link}`

#### Taxonomies

The following dynamic data tags render a list of the taxonomy terms assigned to a post. A link to the term archive wraps each term:

`{post_terms_category}`

`{post_terms_post_tag}`

`{post_terms_my_taxonomy_slug}`

`{post_terms_category:plain}`

If you already use a link around your element, you can disable the terms’ links output using thebricks/dynamic_data/post_terms_linksfilter.

`bricks/dynamic_data/post_terms_links`

#### Terms

The following dynamic data tags render data related to taxonomy terms.

`{term_id}`

`{term_name}`

`{term_slug}`

`{term_count}`

`{term_taxonomy_slug}`

`{term_url}`

`{term_description}`

`{term_meta:my_term_meta_key}`

#### Author Fields

`{author_id}`

`{author_name}`

`{author_bio}`

`{author_email}`

`{author_website}`

`{author_archive_url}`

`{author_avatar}`

`{author_meta:meta_key}`

These fields support dynamic data filters like the following:

`{author_bio:20}`

`{author_name:link}`

`{author_email:link}`

`{author_website:link}`

`{author_avatar:200}`

#### Current Date fields

You can render the current date through dynamic data.

`{current_date}`

`{current_wp_date}`

You may specify a different date format using the PHP date format, for example:

`{current_date:Y}`

`{current_date:Ymd}`

`{current_date:Y-m-d}`

`{current_date:Y.m.d}`

`{current_date:Y/m/d}`

`{current_date:Y m d}`

`{current_date:g:i A}`

`{current_date:timestamp}`

#### Query fields

`{query_results_count}`

`{query_results_count:quer34}`

{query_results_count:quer34}only works if the target query is 1 level deep. You wouldn’t be able to get the correct count if the target query located in a >= 2 level deep nested query.

`{query_results_count:quer34}`

#### Site & Archive fields

`{site_title}`

`{site_tagline}`

`{site_url}`

`{site_login}`

`{site_login:3}`

`{site_logout}`

`{site_logout:3}`

`{archive_title}`

`{archive_title:context}`

`{archive_description}`

You can get dynamic data from the URL parameters like so:

`{url_parameter:my_key}`

`my_key`

#### User profile fields

`{wp_user_id}`

`{wp_user_login}`

`{wp_user_email}`

`{wp_user_url}`

`{wp_user_author_url}`

`{wp_user_role}`

`:value`

`{wp_user_registered_date}`

`{wp_user_nicename}`

`{wp_user_description}`

`{wp_user_first_name}`

`{wp_user_last_name}`

`{wp_user_display_name}`

`{wp_user_picture}`

`{wp_user_meta:my_user_meta_key}`

#### Native WordPress custom fields

To render your own custom field entries, you have to prefix them withcf_.

`cf_`

If your custom field name isphone_number, you’d use{cf_phone_number}to render this custom field on the front end.

`phone_number`

`{cf_phone_number}`

Yourphone_numbercustom field entry should also be available in the dynamic data picker dropdown under “Custom fields”.

`phone_number`

#### Advanced: echo

Starting at Bricks 1.9.7, you have to explicitly allow any function names that you want to call via Bricks’ dynamic dataechotag using the newbricks/code/echo_function_namesfilter. Which you can add to your Bricks child theme or the code snippet plugin of your choice. You can find more information in this article:https://academy.bricksbuilder.io/article/filter-bricks-code-echo_function_names/

`echo`

`bricks/code/echo_function_names`

Bricks 1.4 introduces theechotag to render the output of any PHP function:

`echo`

`{echo:my_custom_function}`

`my_custom_function()`

`{echo:get_the_date('Y-m-d', 55)}`

`Y-m-d`

Please note that theechotag does not support double quotes, and the custom PHP function shouldreturnthe value (do notechothe value inside of the custom function).

`echo`

`return`

`echo`

#### Advanced: do_action

Thedo_actiontag enables developers and other plugins to integrate with your template designs seamlessly. With this tag, you can place action hooks such as{do_action:my_custom_hook}anywhere.

`do_action`

`{do_action:my_custom_hook}`

For example, you can insert the{do_action:woocommerce_after_single_product}in your WooCommerce single product template, allowing other plugins to hook into it. This enhances the flexibility of your template design.

`{do_action:woocommerce_after_single_product}`

It is important to note that thedo_actiontag does not support passing arguments to the action. If theadd_action()function expects additional arguments, an error in PHP will occur. Thedo_actiononly runs on the front end of the website, not inside the builder.

`do_action`

`add_action()`

`do_action`

#### WooCommerce

When the WooCommerce plugin is installed and active, you’ll get access to an extra set of Dynamic Data tags related to the products and orders. Please refer to theWooCommerce builderarticle for more details.

### Filters

You can change the output of certain dynamic data tags by using the following filters:

- :numeric value– When used on a text field, it trims the content to the number of words specified (e.g.Use dynamic data to render all sorts of data from…). When used with an avatar field likeauthor_avatarit specifies the width/height of the avatar image
- :contextor:prefix– Add context to the archive title
- :image– Outputs the field as an image tag,e.g.<img src="https://..." />
- :link– Output the field as an anchor tag,e.g.<a href="https://...">value</a>
- :newTab– Sets the link to open in a new tab
- :tel– The URL of the anchor will be formatted as a telephone number,e.g.<a href="tel:+123456789">+123456789</a>
- :text value– Depending on the context, it could mean the following:User or term custom field meta keyThe URL parameter keyPost terms separatorDate formatImage size slug (e.g., thumbnail or full)The echo tag function name
- User or term custom field meta key
- The URL parameter key
- Post terms separator
- Date format
- Image size slug (e.g., thumbnail or full)
- The echo tag function name
- :value– Outputs the value instead of the label. Useful for comparing choices field types like MetaBox checkbox list, etc. inside element conditions, or with ACF choice fields (set the return type to “Both (Array)”) such as Select, Checkbox, Radio Button, and Button Group. ACF field types that supporting this filter: True/False, User, Taxonomy, Image, Gallery, Post Object, Relationship (@since 1.12) MetaBox field types that supporting this filter: File Input, File, File Upload, File Advanced, Video, Image, Image Advanced, Image Upload, Single Image, Image Select Taxonomy, Taxonomy Advanced, Post, User (@since 1.12)
- :raw– Skip parsing dynamic data tag
- :url– Return URL from post ID. Useful to return URL forfilefield, etc.
- :format– Keep HTML format or show empty Star rating forWooCommerce dynamic data
- :plain– Removes HTML tags usingwp_strip_all_tags, which can be helpful when you need to extract plain text from a dynamic tag result. For example, you may want to remove links from a post term dynamic tag.
- :array_value|{KEY}– Returns the value of a specific array key within a dynamic tag result. It can be particularly useful for custom fields such as ACF Google Map and ACF Link types. The filter can also be applied to an echo dynamic tag. In cases where the value is a nested array, Bricks will flatten it as a JSON string to allow for seamless output without any errors. It’s important to note that this filter should only be used when you are certain that the dynamic tag result is an array. Another important point to keep in mind is that if the specified array key does not exist, this filter will return an empty string.Examples
- :timestamp– Convert the date or time related dynamic data to timestamp value.

`:numeric value`

`Use dynamic data to render all sorts of data from…`

`author_avatar`

`:context`

`:prefix`

`:image `

`<img src="https://..." />`

`:link`

`<a href="https://...">value</a>`

`:newTab`

`:tel`

`<a href="tel:+123456789">+123456789</a>`

`:text value `

- User or term custom field meta key
- The URL parameter key
- Post terms separator
- Date format
- Image size slug (e.g., thumbnail or full)
- The echo tag function name

`:value`

`@since 1.12`

`@since 1.12`

`:raw`

`:url`

`file`

`:format`

`:plain`

`wp_strip_all_tags`

`:array_value|{KEY}`

`:timestamp`

###### Examples of :array_value filter

`{acf_place_map:array_value|lat}`

`$value['lat']`

`{acf_place_map:array_value|post_code}`

`$value['post_code']`

`{acf_ext_link:array_value|title}`

`$value['title']`

`{je_football-team_logo:array_value|id}`

`$value['id']`

`{mb_testimonials_user_image:array_value|name}`

`$value['name']`

`{echo:custom_function:array_value|hello}`

`$value['hello']`

`custom_function()`

### Key-value pair arguments

This feature allows for greater flexibility and customization in displaying dynamic content. The general syntax for using key-value pair arguments is:{dynamic_data_tag @key:value}.

`{dynamic_data_tag @key:value}`

- Wrap text with spaces in single quotes.
- The value can include other dynamic data tags (e.g.,{acf_text_field @fallback:'No content was found for Dynamic Data'}).

`{acf_text_field @fallback:'No content was found for Dynamic Data'}`

#### Available arguments:

@fallback– Provides fallback text if the dynamic data tag doesn’t return any data. This argument can be used with any dynamic data tag (@since 1.10).

`@fallback`

`@since 1.10`

- Example:{acf_text_field @fallback:'This is the fallback text!'}. Ifacf_text_fieldis empty, “This is the fallback text!” will be displayed.

`{acf_text_field @fallback:'This is the fallback text!'}`

`acf_text_field`

@fallback-image– Used for image dynamic data tags. It accepts either an attachment ID or a URL.

`@fallback-image`

- Examples:{acf_image @fallback-image:554}or{acf_image @fallback-image:'https://example.com/placeholder.png'}. Ifacf_imageis not available, the specified image (by attachment ID or URL) will be displayed.

`{acf_image @fallback-image:554}`

`{acf_image @fallback-image:'https://example.com/placeholder.png'}`

`acf_image`

@sanitize– Available@since 1.11.1it allows you to control the sanitization method applied to all dynamic tags within a “text” context. By default, all dynamic tags are sanitized usingwp_kses_post, which helps secure output by stripping unwanted HTML and scripts.

`@sanitize`

`@since 1.11.1`

`wp_kses_post`

This argument is particularly useful if you have a shortcode outputting JavaScript—such as a form shortcode from plugins—stored within a custom field. In earlier versions, this JavaScript would be sanitized, preventing the form from functioning when the field is output via{acf_custom_field}.

`{acf_custom_field}`

Examples:

- {acf_my_wysiwyg @sanitize:false}– Disables sanitization, allowing scripts to be output if stored in the custom field.Use carefully, ensuring that the content is safe for output without sanitization.
- {acf_my_wysiwyg @sanitize:sanitize_email}– Appliessanitize_emailto themy_wysiwygfield. If the value doesn’t pass as a valid email, it returns empty.
- {acf_my_wysiwyg @sanitize:sanitize_email @fallback:'abc@gmail.com'}– Appliessanitize_emailto themy_wysiwygfield. If the result is empty, it falls back to'abc@gmail.com'.

`{acf_my_wysiwyg @sanitize:false}`

`{acf_my_wysiwyg @sanitize:sanitize_email}`

`sanitize_email`

`my_wysiwyg`

`{acf_my_wysiwyg @sanitize:sanitize_email @fallback:'abc@gmail.com'}`

`sanitize_email`

`my_wysiwyg`

`'abc@gmail.com'`

Note:The@sanitizeargument only accepts methods listed in theWordPress Sanitizing API,falseorwp_kses. If using@sanitize:false, be cautious, as this will output the field content without sanitization.

`@sanitize`

`false`

`wp_kses`

`@sanitize:false`

### Bricks hooks related to Dynamic Data

bricks/dynamic_data/exclude_tags– exclude a list of tags from the Bricks dynamic data logic

`bricks/dynamic_data/exclude_tags`

bricks/dynamic_data/replace_nonexistent_tags– Disable the default Bricks behavior of replacing the non-existent dynamic data tags with an empty string

`bricks/dynamic_data/replace_nonexistent_tags`

###### Builder Access

###### SVG Uploads

