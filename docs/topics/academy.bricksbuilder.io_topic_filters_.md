---
title: "Filters (Developer) – Bricks Academy"
url: https://academy.bricksbuilder.io/topic/filters/
date: 2026-01-05T11:08:00.032084
status: success
---

# Filters (Developer) – Bricks Academy

*Source: [https://academy.bricksbuilder.io/topic/filters/](https://academy.bricksbuilder.io/topic/filters/)*

## Table of Contents

  - [What  would you like to know?](#what--would-you-like-to-know)
- [Topic: Filters (Developer)](#topic-filters-developer)
  - [Filter: bricks/builder/i18n](#filter-bricksbuilderi18n)
  - [Filter: bricks/builder/save_messages](#filter-bricksbuildersavemessages)
  - [Filter: bricks/builder/map_styles](#filter-bricksbuildermapstyles)
  - [Filter: bricks/builder/color_palette](#filter-bricksbuildercolorpalette)
  - [Filter: bricks/builder/standard_fonts](#filter-bricksbuilderstandardfonts)
  - [Filter: bricks/builder/elements](#filter-bricksbuilderelements)
  - [Filter: bricks/dynamic_data/post_terms_separator](#filter-bricksdynamicdataposttermsseparator)
  - [Filter: bricks/elements/{element_name}/controls](#filter-brickselementselementnamecontrols)
  - [Filter: bricks/posts/query_vars](#filter-brickspostsqueryvars)
  - [Filter: bricks/dynamic_data/replace_nonexistent_tags](#filter-bricksdynamicdatareplacenonexistenttags)
  - [Filter: bricks/dynamic_data/exclude_tags](#filter-bricksdynamicdataexcludetags)
  - [Filter: bricks/related_posts/query_vars](#filter-bricksrelatedpostsqueryvars)
  - [Filter: bricks/dynamic_data/read_more](#filter-bricksdynamicdatareadmore)
  - [Filter: bricks/element/render_attributes](#filter-brickselementrenderattributes)
  - [Filter: bricks/posts/merge_query](#filter-brickspostsmergequery)
  - [Filter: bricks/code/disallow_keywords](#filter-brickscodedisallowkeywords)
  - [Filter: bricks/code/allow_execution](#filter-brickscodeallowexecution)
  - [Filter: bricks/assets/load_webfonts](#filter-bricksassetsloadwebfonts)
  - [Filter: bricks/setup/control_options](#filter-brickssetupcontroloptions)
  - [Filter: bricks/query/run](#filter-bricksqueryrun)
  - [Filter: bricks/terms/query_vars](#filter-brickstermsqueryvars)
  - [Filter: bricks/users/query_vars](#filter-bricksusersqueryvars)
  - [Filter: bricks/query/loop_object](#filter-bricksqueryloopobject)
  - [Filter: bricks/elements/{element_name}/control_groups](#filter-brickselementselementnamecontrolgroups)
  - [Filter: bricks/element/render](#filter-brickselementrender)
  - [Filter: bricks/element/set_root_attributes](#filter-brickselementsetrootattributes)
  - [Filter: bricks/element/settings](#filter-brickselementsettings)
  - [Filter: bricks/link_css_selectors](#filter-brickslinkcssselectors)
  - [Filter: bricks/is_layout_element](#filter-bricksislayoutelement)
  - [Filter: bricks/content/attributes](#filter-brickscontentattributes)
  - [Filter: bricks/header/attributes](#filter-bricksheaderattributes)
  - [Filter: bricks/footer/attributes](#filter-bricksfooterattributes)
  - [Filter: bricks/dynamic_data/post_terms_links](#filter-bricksdynamicdataposttermslinks)
  - [Filter: bricks/body/attributes](#filter-bricksbodyattributes)
  - [Filter: bricks/comments/timestamp](#filter-brickscommentstimestamp)
  - [Filter: builder/settings/{type}/controls_data](#filter-buildersettingstypecontrolsdata)
  - [Filter: bricks/screen_conditions/scores](#filter-bricksscreenconditionsscores)
  - [Filter: bricks/registered_post_types_args](#filter-bricksregisteredposttypesargs)
  - [Filter: bricks/content/html_after_begin](#filter-brickscontenthtmlafterbegin)
  - [Filter: bricks/content/html_before_end](#filter-brickscontenthtmlbeforeend)
  - [Filter: bricks/query/loop_object_id](#filter-bricksqueryloopobjectid)
  - [Filter: bricks/query/loop_object_type](#filter-bricksqueryloopobjecttype)
  - [Filter: bricks/query/no_results_content](#filter-bricksquerynoresultscontent)
  - [Filter: bricks/default_page_title](#filter-bricksdefaultpagetitle)
  - [Filter: bricks/query/result](#filter-bricksqueryresult)
  - [Filter: bricks/query/result_count](#filter-bricksqueryresultcount)
  - [Filter: bricks/active_templates](#filter-bricksactivetemplates)
  - [Filter: bricks/frontend/render_data](#filter-bricksfrontendrenderdata)
  - [Filter: bricks/query/result_max_num_pages](#filter-bricksqueryresultmaxnumpages)
  - [Filter: bricks/query/force_run](#filter-bricksqueryforcerun)
  - [Filter: bricks/assets/generate_css_from_element](#filter-bricksassetsgeneratecssfromelement)
  - [Filter: bricks/search_form/home_url](#filter-brickssearchformhomeurl)
  - [Filter: bricks/builder/image_size_options](#filter-bricksbuilderimagesizeoptions)
  - [Filter: bricks/auth/custom_redirect_url](#filter-bricksauthcustomredirecturl)
  - [Filter: bricks/auth/custom_login_redirect](#filter-bricksauthcustomloginredirect)
  - [Filter: bricks/auth/custom_lost_password_redirect](#filter-bricksauthcustomlostpasswordredirect)
  - [Filter: bricks/auth/custom_registration_redirect](#filter-bricksauthcustomregistrationredirect)
  - [Filter: bricks/auth/custom_reset_password_redirect](#filter-bricksauthcustomresetpasswordredirect)
  - [Filter: bricks/code/echo_function_names](#filter-brickscodeechofunctionnames)
  - [Filter: bricks/nav_menu/menu](#filter-bricksnavmenumenu)
  - [Filter: bricks/code/disable_execution](#filter-brickscodedisableexecution)
  - [Filter: bricks/allowed_html_tags](#filter-bricksallowedhtmltags)
  - [Filter: bricks/get_element_data/maybe_from_post_id](#filter-bricksgetelementdatamaybefrompostid)
  - [Filter: bricks/query/init_loop_index](#filter-bricksqueryinitloopindex)
  - [Filter: bricks/builder/codemirror_config](#filter-bricksbuildercodemirrorconfig)
  - [Filter: bricks/render_query_loop_trail](#filter-bricksrenderquerylooptrail)
  - [Filter: bricks/password_protection/cookie_expires](#filter-brickspasswordprotectioncookieexpires)
  - [Filter: bricks/password_protection/is_active](#filter-brickspasswordprotectionisactive)
  - [Filter: bricks/content/tag](#filter-brickscontenttag)
  - [Filter: bricks/use_duplicate_content](#filter-bricksuseduplicatecontent)
  - [Filter: bricks/form/action/{form_action}](#filter-bricksformactionformaction)
  - [Filter: bricks/maintenance/should_apply](#filter-bricksmaintenanceshouldapply)
  - [Filter: bricks/frontend/render_element](#filter-bricksfrontendrenderelement)
  - [Filter: bricks/placeholder_image](#filter-bricksplaceholderimage)
  - [Filter: bricks/filter_element/populated_options](#filter-bricksfilterelementpopulatedoptions)
  - [Filter: bricks/form/create_post/meta_value](#filter-bricksformcreatepostmetavalue)
  - [Filter: bricks/form/update_post/meta_value](#filter-bricksformupdatepostmetavalue)
  - [Filter: bricks/pagination/total_pages](#filter-brickspaginationtotalpages)
  - [Filter: bricks/pagination/current_page](#filter-brickspaginationcurrentpage)
  - [Filter: bricks/pagination/custom_logic](#filter-brickspaginationcustomlogic)
  - [Filter: bricks/form/file_directory](#filter-bricksformfiledirectory)

### What  would you like to know?

## Topic: Filters (Developer)

- Filter: bricks/builder/i18nPlace and customize the following filter to add translatable string to the builder. add_filter( 'bricks/builder/i18n', function( $i18n ) { //… ...Continue reading ›
- Filter: bricks/builder/save_messagesPlace and customize the following filter to display different save message every time you manually save your progress when editing… ...Continue reading ›
- Filter: bricks/builder/map_stylesThis filter allows you to define your own custom map styles for the Map element. The example below shows how… ...Continue reading ›
- Filter: bricks/builder/color_palettePlace and customize the following filter to display a different default color palette for the color control. add_filter( 'bricks/builder/color_palette', function(… ...Continue reading ›
- Filter: bricks/builder/standard_fontsPlace and customize the following filter to display a different set of web-safe fonts in the typography control. add_filter( 'bricks/builder/standard_fonts',… ...Continue reading ›
- Filter: bricks/builder/elementsDetermine which elements to use in Bricks by out-commenting the ones you don't want to use. There is a full… ...Continue reading ›
- Filter: bricks/dynamic_data/post_terms_separatorProgrammatically set the post term separator like so: ...Continue reading ›
- Filter: bricks/elements/{element_name}/controlsSince Bricks 1.3.2 it is possible to add custom controls to any element like so: Note: the above example adds… ...Continue reading ›
- Filter: bricks/posts/query_varsSince Bricks 1.3.2 you may manipulate the posts, products, or Query Loop elements query vars before the query is performed… ...Continue reading ›
- Filter: bricks/dynamic_data/replace_nonexistent_tagsDynamic data tags are strings with a special syntax wrapped by curly brackets. Sometimes this syntax has conflicts with other… ...Continue reading ›
- Filter: bricks/dynamic_data/exclude_tagsDynamic data tags are strings with a special syntax wrapped by curly brackets. Sometimes this syntax has conflicts with other… ...Continue reading ›
- Filter: bricks/related_posts/query_varsSince Bricks 1.3.5 you may manipulate the related posts element query vars before the query is performed like so: The filter callback… ...Continue reading ›
- Filter: bricks/dynamic_data/read_moreIf you use the dynamic data tagRead moreyou'll get an anchor tag (link) to the post with the label… ...Continue reading ›
- Filter: bricks/element/render_attributesStarting with Bricks 1.3.7 you may manipulate the HTML attributes of a given element using the following filter: The filter… ...Continue reading ›
- Filter: bricks/posts/merge_querySince Bricks 1.3.7 you'll be able to decide if a certain element query should be merged with the WordPress main… ...Continue reading ›
- Filter: bricks/code/disallow_keywordsThis filter introduces another level of security when using the Code element to run code. With the filter bricks/code/disallow_keywords you'll… ...Continue reading ›
- Filter: bricks/code/allow_executionAn alternative to the Disable code execution setting under Bricks > Settings > Builder Access. You can use this PHP… ...Continue reading ›
- Filter: bricks/assets/load_webfontsBricks 1.4 introduces the possibility to "Disable Google Fonts". Either via the Bricks settings under "Performance" or programmatically using the… ...Continue reading ›
- Filter: bricks/setup/control_optionsBricks offers a WordPress filter to add or remove control options. The control options are used throughout Bricks and allow… ...Continue reading ›
- Filter: bricks/query/runThe Bricks Query Loop supports 3 types of queries by default (Posts, Terms and Users). But it can be extended… ...Continue reading ›
- Filter: bricks/terms/query_varsBricks terms query variables can be manipulated before the query runs like so: The filter callback receives three arguments: Example… ...Continue reading ›
- Filter: bricks/users/query_varsBricks users query variables can be manipulated before the query runs like so: The filter callback receives three arguments: ...Continue reading ›
- Filter: bricks/query/loop_objectThe Bricks Query Loop supports 3 types of queries by default (Posts, Terms, and Users). But it can be extended… ...Continue reading ›
- Filter: bricks/elements/{element_name}/control_groupsSince Bricks 1.4 it is possible to add custom control groups to a specific element like so: Note: the above… ...Continue reading ›
- Filter: bricks/element/renderBricks 1.5 introduces the new bricks/element/render filter. This filter enables you to implement your own conditional display logic programmatically. This… ...Continue reading ›
- Filter: bricks/element/set_root_attributesBricks 1.4 with its improved & slimmer DOM structure now requires to add the element ID, root classes, and other… ...Continue reading ›
- Filter: bricks/element/settingsBricks 1.5 adds the possibility to change the element settings before it is rendered. This allows you to change a… ...Continue reading ›
- Filter: bricks/link_css_selectorsUse this filter in your child theme to overwrite/extend the CSS selectors the "Theme Styles > Link" settings are applied… ...Continue reading ›
- Filter: bricks/is_layout_elementAllows to define your custom elements as a layout element, so they are recognised like the section, container, block, div… ...Continue reading ›
- Filter: bricks/content/attributesProgrammatically add HTML attributes to the main tag. ...Continue reading ›
- Filter: bricks/header/attributesProgrammatically add HTML attributes to the header tag. ...Continue reading ›
- Filter: bricks/footer/attributesProgrammatically add HTML attributes to the footer tag. ...Continue reading ›
- Filter: bricks/dynamic_data/post_terms_linksWhen rendering the terms assigned to a post using the dynamic data tag {post_terms_my_taxonomy}, Bricks wraps each term with a… ...Continue reading ›
- Filter: bricks/body/attributesFilter to add HTML attributes to the body tag (@since 1.5). ...Continue reading ›
- Filter: bricks/comments/timestampWhen using the Bricks Post Comments element, the comment default timestamp text will show the time difference since it was… ...Continue reading ›
- Filter: builder/settings/{type}/controls_dataThis filter allows you to add new controls to the Page Settings or Template Settings panels in the builder. To… ...Continue reading ›
- Filter: bricks/screen_conditions/scoresBricks selects the template & theme style for a specific page according to the conditions you've defined. Internally this is… ...Continue reading ›
- Filter: bricks/registered_post_types_argsAvailable since version 1.6, this filter allows you to customise the post type args that are used to query the… ...Continue reading ›
- Filter: bricks/content/html_after_beginAvailable since version 1.6, this filter allows you to customize or insert HTML strings after main tag, before rendering bricks… ...Continue reading ›
- Filter: bricks/content/html_before_endAvailable since version 1.6, this filter allows you to customize or insert HTML strings before closing main tag. ...Continue reading ›
- Filter: bricks/query/loop_object_idBricks will use \Bricks\Query::get_loop_object_id() to retrieve the looping iteration's object ID. This static function is used in many places. Especially… ...Continue reading ›
- Filter: bricks/query/loop_object_typeBricks will use \Bricks\Query::get_loop_object_type() to retrieve the looping iteration's object type. This static function is used in many places. It… ...Continue reading ›
- Filter: bricks/query/no_results_contentYou can programmatically change the query loop "no results content" using this filter. ...Continue reading ›
- Filter: bricks/default_page_titleSince 1.8, Bricks automatically adds default page titles to all non-Bricks pages. However, if you wish to customize or remove… ...Continue reading ›
- Filter: bricks/query/resultAvailable since 1.8, this filter lets you customize the query results and implement additional logic. Like modifying the post, term,… ...Continue reading ›
- Filter: bricks/query/result_countThis filter allows you to modify the query result count (@since 1.8). ...Continue reading ›
- Filter: bricks/active_templatesModify the templates applied on a page programmatically (@since 1.8.4) This is an alternative to setting an active template via… ...Continue reading ›
- Filter: bricks/frontend/render_dataThe filter allows you to modify the rendered content for different areas like header, content, and footer before it's displayed… ...Continue reading ›
- Filter: bricks/query/result_max_num_pagesThis filter allows you to modify the query result maximum number of pages (@since 1.9.1). This value is used for… ...Continue reading ›
- Filter: bricks/query/force_runBricks has enhanced query performance in 1.9.1. Now, each unique query is executed only once per page load, and subsequently,… ...Continue reading ›
- Filter: bricks/assets/generate_css_from_elementThis filter allows you to include your custom query loop supported element to generate the children styles in Bricks. (@since… ...Continue reading ›
- Filter: bricks/search_form/home_urlThe bricks/search_form/home_url filter allows developers to customize the action URL of the search form within the Bricks theme. This filter… ...Continue reading ›
- Filter: bricks/builder/image_size_optionsThe bricks/builder/image_sizes hook gives developers the ability to customize image size options in the builder. By default, when working within… ...Continue reading ›
- Filter: bricks/auth/custom_redirect_urlThis filter is distinct from other authentication-related filters in that it provides a broad scope for customizing redirections during authentication… ...Continue reading ›
- Filter: bricks/auth/custom_login_redirectThis filter allows customization of the redirect page ID for the login page. Example Usage: Parameters: Return: ...Continue reading ›
- Filter: bricks/auth/custom_lost_password_redirectThis filter enables the modification of the redirect page ID for the lost password page. Example Usage: Parameters: Return: ...Continue reading ›
- Filter: bricks/auth/custom_registration_redirectThis filter allows for the customization of the redirect page ID for the registration page. Example Usage: Parameters: Return: ...Continue reading ›
- Filter: bricks/auth/custom_reset_password_redirectThis filter provides a way to change the redirect page ID for the reset password page. Example Usage: Parameters: Return: ...Continue reading ›
- Filter: bricks/code/echo_function_namesStarting at Bricks 1.9.7, you must explicitly allow any function names you want to call via Bricks' dynamic data echo… ...Continue reading ›
- Filter: bricks/nav_menu/menuThe bricks/nav_menu/menu filter allows you to modify the navigation menu dynamically in Bricks Builder based on your conditions. In the… ...Continue reading ›
- Filter: bricks/code/disable_executionThis PHP filter allows you to disable code execution within the Bricks builder programmatically. It takes precedence over the bricks/code/allow_execution… ...Continue reading ›
- Filter: bricks/allowed_html_tagsStarting at version 1.10.2 Bricks restricts the allowed HTML tags to the WordPress core logic for wp_kses_allowed_html( 'post' ). This… ...Continue reading ›
- Filter: bricks/get_element_data/maybe_from_post_idThe bricks/get_element_data/maybe_from_post_id filter, available @since 1.11, allows you to specify an additional post ID from which to retrieve element data.… ...Continue reading ›
- Filter: bricks/query/init_loop_indexThe bricks/query/init_loop_index filter, available @since 1.11, allows you to modify the initial loop index when using various query types in… ...Continue reading ›
- Filter: bricks/builder/codemirror_configUse this filter to customize the configuration of CodeMirror 5, the code editor used within the builder. CodeMirror 5 is… ...Continue reading ›
- Filter: bricks/render_query_loop_trailThe bricks/render_query_loop_trail (@since 1.11.1) filter controls the output of the query loop trail node in Bricks. This node is automatically… ...Continue reading ›
- Filter: bricks/password_protection/cookie_expiresAdjust the expiration time for the password cookie used by the password protection template. By default, when a password is… ...Continue reading ›
- Filter: bricks/password_protection/is_activeUse this filter to add custom rules that determine whether a password protection template should be active. By default, the… ...Continue reading ›
- Filter: bricks/content/tagThe bricks/content/tag (@since 1.11.1) filter lets you set the HTML tag for the #brx-content node that your Bricks content data… ...Continue reading ›
- Filter: bricks/use_duplicate_contentDuplicate content is available for all users with the edit_post capability. Use this feature to duplicate any post or page… ...Continue reading ›
- Filter: bricks/form/action/{form_action}The bricks/form/action/{form_action} filter is triggered when a custom action (one that is not reserved by Bricks) is selected in a… ...Continue reading ›
- Filter: bricks/maintenance/should_applyUse this filter (@since 2.0) to override whether maintenance mode should be enforced for the current request. By default, Bricks… ...Continue reading ›
- Filter: bricks/frontend/render_elementThe bricks/frontend/render_element filter allows you to modify the HTML output of any element in Bricks on the frontend. This powerful… ...Continue reading ›
- Filter: bricks/placeholder_imageThe bricks/placeholder_image filter allows you to override the default placeholder image used in Bricks. This can be useful when you… ...Continue reading ›
- Filter: bricks/filter_element/populated_optionsThe bricks/filter_element/populated_options PHP filter allows you to modify the populated options of Filter - Select, Filter - Radio, and Filter… ...Continue reading ›
- Filter: bricks/form/create_post/meta_valueThis filter is used within the Create post form action in Bricks. It allows developers to alter the meta values… ...Continue reading ›
- Filter: bricks/form/update_post/meta_valueThis filter is part of the Update post form action in Bricks. It enables developers to customize the meta values… ...Continue reading ›
- Filter: bricks/pagination/total_pagesThe bricks/pagination/total_pages filter allows you to modify the total number of pages used in the pagination logic of Bricks Builder.… ...Continue reading ›
- Filter: bricks/pagination/current_pageThe bricks/pagination/current_page filter allows you to modify the current page number used in the pagination logic of Bricks Builder. In… ...Continue reading ›
- Filter: bricks/pagination/custom_logicThe bricks/pagination/custom_logic filter allows you to implement custom pagination logic in Bricks Builder based on specific query settings. @since 2.2… ...Continue reading ›
- Filter: bricks/form/file_directoryThis filter allows you to modify the directory where your uploaded form files are stored when the Save File setting… ...Continue reading ›
-

### Filter: bricks/builder/i18n

Place and customize the following filter to add translatable string to the builder. add_filter( 'bricks/builder/i18n', function( $i18n ) { //… ...

### Filter: bricks/builder/save_messages

Place and customize the following filter to display different save message every time you manually save your progress when editing… ...

### Filter: bricks/builder/map_styles

This filter allows you to define your own custom map styles for the Map element. The example below shows how… ...

### Filter: bricks/builder/color_palette

Place and customize the following filter to display a different default color palette for the color control. add_filter( 'bricks/builder/color_palette', function(… ...

### Filter: bricks/builder/standard_fonts

Place and customize the following filter to display a different set of web-safe fonts in the typography control. add_filter( 'bricks/builder/standard_fonts',… ...

### Filter: bricks/builder/elements

Determine which elements to use in Bricks by out-commenting the ones you don't want to use. There is a full… ...

### Filter: bricks/dynamic_data/post_terms_separator

Programmatically set the post term separator like so: ...

### Filter: bricks/elements/{element_name}/controls

Since Bricks 1.3.2 it is possible to add custom controls to any element like so: Note: the above example adds… ...

### Filter: bricks/posts/query_vars

Since Bricks 1.3.2 you may manipulate the posts, products, or Query Loop elements query vars before the query is performed… ...

### Filter: bricks/dynamic_data/replace_nonexistent_tags

Dynamic data tags are strings with a special syntax wrapped by curly brackets. Sometimes this syntax has conflicts with other… ...

### Filter: bricks/dynamic_data/exclude_tags

Dynamic data tags are strings with a special syntax wrapped by curly brackets. Sometimes this syntax has conflicts with other… ...

### Filter: bricks/related_posts/query_vars

Since Bricks 1.3.5 you may manipulate the related posts element query vars before the query is performed like so: The filter callback… ...

### Filter: bricks/dynamic_data/read_more

If you use the dynamic data tagRead moreyou'll get an anchor tag (link) to the post with the label… ...

### Filter: bricks/element/render_attributes

Starting with Bricks 1.3.7 you may manipulate the HTML attributes of a given element using the following filter: The filter… ...

### Filter: bricks/posts/merge_query

Since Bricks 1.3.7 you'll be able to decide if a certain element query should be merged with the WordPress main… ...

### Filter: bricks/code/disallow_keywords

This filter introduces another level of security when using the Code element to run code. With the filter bricks/code/disallow_keywords you'll… ...

### Filter: bricks/code/allow_execution

An alternative to the Disable code execution setting under Bricks > Settings > Builder Access. You can use this PHP… ...

### Filter: bricks/assets/load_webfonts

Bricks 1.4 introduces the possibility to "Disable Google Fonts". Either via the Bricks settings under "Performance" or programmatically using the… ...

### Filter: bricks/setup/control_options

Bricks offers a WordPress filter to add or remove control options. The control options are used throughout Bricks and allow… ...

### Filter: bricks/query/run

The Bricks Query Loop supports 3 types of queries by default (Posts, Terms and Users). But it can be extended… ...

### Filter: bricks/terms/query_vars

Bricks terms query variables can be manipulated before the query runs like so: The filter callback receives three arguments: Example… ...

### Filter: bricks/users/query_vars

Bricks users query variables can be manipulated before the query runs like so: The filter callback receives three arguments: ...

### Filter: bricks/query/loop_object

The Bricks Query Loop supports 3 types of queries by default (Posts, Terms, and Users). But it can be extended… ...

### Filter: bricks/elements/{element_name}/control_groups

Since Bricks 1.4 it is possible to add custom control groups to a specific element like so: Note: the above… ...

### Filter: bricks/element/render

Bricks 1.5 introduces the new bricks/element/render filter. This filter enables you to implement your own conditional display logic programmatically. This… ...

### Filter: bricks/element/set_root_attributes

Bricks 1.4 with its improved & slimmer DOM structure now requires to add the element ID, root classes, and other… ...

### Filter: bricks/element/settings

Bricks 1.5 adds the possibility to change the element settings before it is rendered. This allows you to change a… ...

### Filter: bricks/link_css_selectors

Use this filter in your child theme to overwrite/extend the CSS selectors the "Theme Styles > Link" settings are applied… ...

### Filter: bricks/is_layout_element

Allows to define your custom elements as a layout element, so they are recognised like the section, container, block, div… ...

### Filter: bricks/content/attributes

Programmatically add HTML attributes to the main tag. ...

### Filter: bricks/header/attributes

Programmatically add HTML attributes to the header tag. ...

### Filter: bricks/footer/attributes

Programmatically add HTML attributes to the footer tag. ...

### Filter: bricks/dynamic_data/post_terms_links

When rendering the terms assigned to a post using the dynamic data tag {post_terms_my_taxonomy}, Bricks wraps each term with a… ...

### Filter: bricks/body/attributes

Filter to add HTML attributes to the body tag (@since 1.5). ...

### Filter: bricks/comments/timestamp

When using the Bricks Post Comments element, the comment default timestamp text will show the time difference since it was… ...

### Filter: builder/settings/{type}/controls_data

This filter allows you to add new controls to the Page Settings or Template Settings panels in the builder. To… ...

### Filter: bricks/screen_conditions/scores

Bricks selects the template & theme style for a specific page according to the conditions you've defined. Internally this is… ...

### Filter: bricks/registered_post_types_args

Available since version 1.6, this filter allows you to customise the post type args that are used to query the… ...

### Filter: bricks/content/html_after_begin

Available since version 1.6, this filter allows you to customize or insert HTML strings after main tag, before rendering bricks… ...

### Filter: bricks/content/html_before_end

Available since version 1.6, this filter allows you to customize or insert HTML strings before closing main tag. ...

### Filter: bricks/query/loop_object_id

Bricks will use \Bricks\Query::get_loop_object_id() to retrieve the looping iteration's object ID. This static function is used in many places. Especially… ...

### Filter: bricks/query/loop_object_type

Bricks will use \Bricks\Query::get_loop_object_type() to retrieve the looping iteration's object type. This static function is used in many places. It… ...

### Filter: bricks/query/no_results_content

You can programmatically change the query loop "no results content" using this filter. ...

### Filter: bricks/default_page_title

Since 1.8, Bricks automatically adds default page titles to all non-Bricks pages. However, if you wish to customize or remove… ...

### Filter: bricks/query/result

Available since 1.8, this filter lets you customize the query results and implement additional logic. Like modifying the post, term,… ...

### Filter: bricks/query/result_count

This filter allows you to modify the query result count (@since 1.8). ...

### Filter: bricks/active_templates

Modify the templates applied on a page programmatically (@since 1.8.4) This is an alternative to setting an active template via… ...

### Filter: bricks/frontend/render_data

The filter allows you to modify the rendered content for different areas like header, content, and footer before it's displayed… ...

### Filter: bricks/query/result_max_num_pages

This filter allows you to modify the query result maximum number of pages (@since 1.9.1). This value is used for… ...

### Filter: bricks/query/force_run

Bricks has enhanced query performance in 1.9.1. Now, each unique query is executed only once per page load, and subsequently,… ...

### Filter: bricks/assets/generate_css_from_element

This filter allows you to include your custom query loop supported element to generate the children styles in Bricks. (@since… ...

### Filter: bricks/search_form/home_url

The bricks/search_form/home_url filter allows developers to customize the action URL of the search form within the Bricks theme. This filter… ...

### Filter: bricks/builder/image_size_options

The bricks/builder/image_sizes hook gives developers the ability to customize image size options in the builder. By default, when working within… ...

### Filter: bricks/auth/custom_redirect_url

This filter is distinct from other authentication-related filters in that it provides a broad scope for customizing redirections during authentication… ...

### Filter: bricks/auth/custom_login_redirect

This filter allows customization of the redirect page ID for the login page. Example Usage: Parameters: Return: ...

### Filter: bricks/auth/custom_lost_password_redirect

This filter enables the modification of the redirect page ID for the lost password page. Example Usage: Parameters: Return: ...

### Filter: bricks/auth/custom_registration_redirect

This filter allows for the customization of the redirect page ID for the registration page. Example Usage: Parameters: Return: ...

### Filter: bricks/auth/custom_reset_password_redirect

This filter provides a way to change the redirect page ID for the reset password page. Example Usage: Parameters: Return: ...

### Filter: bricks/code/echo_function_names

Starting at Bricks 1.9.7, you must explicitly allow any function names you want to call via Bricks' dynamic data echo… ...

### Filter: bricks/nav_menu/menu

The bricks/nav_menu/menu filter allows you to modify the navigation menu dynamically in Bricks Builder based on your conditions. In the… ...

### Filter: bricks/code/disable_execution

This PHP filter allows you to disable code execution within the Bricks builder programmatically. It takes precedence over the bricks/code/allow_execution… ...

### Filter: bricks/allowed_html_tags

Starting at version 1.10.2 Bricks restricts the allowed HTML tags to the WordPress core logic for wp_kses_allowed_html( 'post' ). This… ...

### Filter: bricks/get_element_data/maybe_from_post_id

The bricks/get_element_data/maybe_from_post_id filter, available @since 1.11, allows you to specify an additional post ID from which to retrieve element data.… ...

### Filter: bricks/query/init_loop_index

The bricks/query/init_loop_index filter, available @since 1.11, allows you to modify the initial loop index when using various query types in… ...

### Filter: bricks/builder/codemirror_config

Use this filter to customize the configuration of CodeMirror 5, the code editor used within the builder. CodeMirror 5 is… ...

### Filter: bricks/render_query_loop_trail

The bricks/render_query_loop_trail (@since 1.11.1) filter controls the output of the query loop trail node in Bricks. This node is automatically… ...

### Filter: bricks/password_protection/cookie_expires

Adjust the expiration time for the password cookie used by the password protection template. By default, when a password is… ...

### Filter: bricks/password_protection/is_active

Use this filter to add custom rules that determine whether a password protection template should be active. By default, the… ...

### Filter: bricks/content/tag

The bricks/content/tag (@since 1.11.1) filter lets you set the HTML tag for the #brx-content node that your Bricks content data… ...

### Filter: bricks/use_duplicate_content

Duplicate content is available for all users with the edit_post capability. Use this feature to duplicate any post or page… ...

### Filter: bricks/form/action/{form_action}

The bricks/form/action/{form_action} filter is triggered when a custom action (one that is not reserved by Bricks) is selected in a… ...

### Filter: bricks/maintenance/should_apply

Use this filter (@since 2.0) to override whether maintenance mode should be enforced for the current request. By default, Bricks… ...

### Filter: bricks/frontend/render_element

The bricks/frontend/render_element filter allows you to modify the HTML output of any element in Bricks on the frontend. This powerful… ...

### Filter: bricks/placeholder_image

The bricks/placeholder_image filter allows you to override the default placeholder image used in Bricks. This can be useful when you… ...

### Filter: bricks/filter_element/populated_options

The bricks/filter_element/populated_options PHP filter allows you to modify the populated options of Filter - Select, Filter - Radio, and Filter… ...

### Filter: bricks/form/create_post/meta_value

This filter is used within the Create post form action in Bricks. It allows developers to alter the meta values… ...

### Filter: bricks/form/update_post/meta_value

This filter is part of the Update post form action in Bricks. It enables developers to customize the meta values… ...

### Filter: bricks/pagination/total_pages

The bricks/pagination/total_pages filter allows you to modify the total number of pages used in the pagination logic of Bricks Builder.… ...

### Filter: bricks/pagination/current_page

The bricks/pagination/current_page filter allows you to modify the current page number used in the pagination logic of Bricks Builder. In… ...

### Filter: bricks/pagination/custom_logic

The bricks/pagination/custom_logic filter allows you to implement custom pagination logic in Bricks Builder based on specific query settings. @since 2.2… ...

### Filter: bricks/form/file_directory

This filter allows you to modify the directory where your uploaded form files are stored when the Save File setting… ...

