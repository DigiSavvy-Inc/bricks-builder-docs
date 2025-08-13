---
title: "Query Loop – Bricks Academy"
url: https://academy.bricksbuilder.io/article/query-loop/
date: 2025-02-27T15:31:11.413665
status: success
---

# Query Loop – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/query-loop/](https://academy.bricksbuilder.io/article/query-loop/)*

## Table of Contents

- [Query Loop](#query-loop)
  - [How to create a query loop](#how-to-create-a-query-loop)
  - [Query control](#query-control)
  - [Query editor (PHP)](#query-editor-php)
  - [Posts query](#posts-query)
    - [Enhanced Ordering Options](#enhanced-ordering-options)
    - [Best Practice for Pagination & Order By](#best-practice-for-pagination--order-by)
    - [Example 1: Latest Posts](#example-1-latest-posts)
  - [Media query](#media-query)
    - [Example 2: Media gallery](#example-2-media-gallery)
  - [WooCommerce Products Query](#woocommerce-products-query)
    - [Example 1: WooCommerce Featured Products](#example-1-woocommerce-featured-products)
    - [Example 2: WooCommerce Related Products](#example-2-woocommerce-related-products)
    - [Example 3: WooCommerce Upsells Products](#example-3-woocommerce-upsells-products)
  - [Terms query](#terms-query)
    - [Example 3: Product categories](#example-3-product-categories)
  - [Users query](#users-query)
    - [Example 4:The blog authors](#example-4the-blog-authors)
  - [The Pagination element](#the-pagination-element)
  - [Load more (button)](#load-more-button)
  - [Query loop in Accordions & Sliders](#query-loop-in-accordions--sliders)
  - [Include/Exclude Controls: Dynamic data tag support](#includeexclude-controls-dynamic-data-tag-support)
      - [Supported Field Types](#supported-field-types)
    - [Example 1: Retrieve ACF Relationship Posts by Post Type and Order by Post IDs](#example-1-retrieve-acf-relationship-posts-by-post-type-and-order-by-post-ids)
    - [Example 2: Use Meta Box Image Advanced Field for a Nestable Slider Query Loop](#example-2-use-meta-box-image-advanced-field-for-a-nestable-slider-query-loop)
    - [Example 3: Query ACF Gallery with Random Order](#example-3-query-acf-gallery-with-random-order)
  - [Query loop hooks](#query-loop-hooks)
        - [Builder Mode (Custom)](#builder-mode-custom)
        - [Converter](#converter)

## Query Loop

TheQuery Loopbuilder is available for alllayout elements, Accordion, and Slider elements.

It can also be enabled for the Accordion (Nestable), Tabs (Nestable), and Slider (Nestable).

It lets you query your database (according to your query parameters) and renders the query results you want to show inside the loop (dynamic data).

You can query post types, taxonomy terms, and users. Some typical use cases are:

- Posts: Latest posts, related posts (works for any registered & public post type)
- Terms: Post categories & tags, product categories, etc.
- Users: List blog authors, community members, and team members

### How to create a query loop

Add a “Container” element to the canvas. Enable theUse Query Loopsetting to turn your container into a loop (repeater) item.

Once you’ve enabled theUse Query Loopsetting, you’ll see aQuerycontrol (loop/infinity icon).

Open the query control to set the query parameters for retrieving the content from your database.

This container now serves as your repeater item. All elements inside this container are repeated as often as there are query results.

### Query control

TheQuerycontrol supports three different object types:posts,terms, andusers.

`posts`

`terms`

`users`

- Postsenable aWP_Querytype of query. This is the default query type and should be used when you want to display a loop of posts, pages, media files, or custom post types.
- Termsenable theWP_Term_Query. This should be used when you want to loop through the different terms of a taxonomy. Useful to list all the product categories that contain products.
- Usersenable theWP_User_Query. This should be used when you want to loop through a set of site users. Useful to list the blog authors or a list of team members (as long as they are inserted as site users).

The query controls adapt according to the selected query type.

### Query editor (PHP)

Bricks 1.9.1 introduces a newQuery editorcontrol that lets you write your own queries in PHP for maximum flexibility and querying capabilities.

`Query editor`

The query editor appears after enabling the “Query editor (PHP)” control.

Note: You must enable code execution inBricks settingsto access this feature.

You have toreturn a PHP arraycontaining theWordPress query argumentsyou’d like to use for your query.

As shown in the screenshot above, the query editor supports dynamic data.

### Posts query

Post type: Select one or multiple post types (default: posts)

Order by: Order the results by post ID, author, title, published or modified date, comment count, relevance, menu order, or random (default: published date). (Support multiple values@since 1.11.1)

`@since 1.11.1`

Order: Ascending or Descending (default). (Support multiple values@since 1.11.1)

`@since 1.11.1`

Posts Per Page: The number of posts to show per page (default: WordPress settings → Reading → Blog pages show at most)

Offset: The number of posts to skip.

Ignore Sticky Posts: Turn this on if do not want to move sticky posts to the start of the set.

Disable Query Merge: Turn this on if do not want the query to be auto-merged by Bricks in archive pages, search pages, etc. Usually, you will turn this on for the Query loops in the footer, header, or non-main query. This is the GUI for thebricks/posts/merge_queryfilter.

Child Of: Set the parent ID to return all its children only. (post_parentin WP_Query)

`post_parent`

Include/Exclude: If you want to include or exclude one or multiple posts from the query. You can usedynamic tagon this control too (@since 1.12)

`@since 1.12`

Exclude Current Post: If enabled it will exclude the current post from the loop (useful to build a “related posts” section)

Terms Include/Exclude: Include or Exclude posts that have one or multiple terms.

Taxonomy Query: Add one or multiple taxonomy queries to filter the posts.

Tax Query Relation: Define if the taxonomy queries should be inclusive (OR) or exclusive (AND).

Meta Query: Add one or multiple meta queries to filter the posts based on the custom fields.

Relation: Define if the meta queries should be inclusive (OR) or exclusive (AND).

Random seed TTL: Duration in minutes for which the random seed exists. Set to prevent duplicate post results (only needed & available when using a random order query loop).  Set “0” to turn this feature off.

If you set the TTL to 10 minutes, the query result remains the same for the next 10 minutes. This ensures that no duplicate posts are displayed on different pages or when the infinite scroll is active. (@since 1.7.1)

`@since 1.7.1`

Is main query (Archive, Search): When creating an archive or search template, choose one of the loops as the main query. This will prevent a 404 error from occurring when visitors navigate to different pages. Turn on to designate the main query. Remember to set the correct query on your pagination element as well.However, do not turn on this option for multiple queries on the same page, as only the first one will be set as the archive main query.(@since 1.8)

`(@since 1.8)`

#### Enhanced Ordering Options

Starting with version 1.11.1, theOrder ByandOrdersettings in Bricks Query Loop have been improved to support multiple ordering criteria. This allows you to define complex ordering rules directly within Bricks, eliminating the need for a custom PHP filter that was previously required.

This update is particularly useful in scenarios where you want to order query results by more than one criterion. For example, you can now order bynamein descending order and then byIDin descending order. Bricks will process these criteria sequentially, applying each in the order specified to deliver the desired result.

Example Scenarios:

- Multi-Criteria Ordering: Suppose you have a directory listing and want to display results by popularity first (custom field) and then by date added. With this update, you can set the query to order first by the popularity meta field in descending order and then by date added in ascending order, ensuring that the most popular and newest items appear at the top.
- Custom Order Clauses with Meta Queries: Bricks now supports more complex ordering directly aligned with meta query conditions. For instance, if you’re working with a meta query to order posts byperformance dateandtime, you can define this directly in the order clause. Code example inthis article.

#### Best Practice for Pagination & Order By

When using multiple ordering criteria, it’s recommended to always includeIDas the second ordering criterion to avoid duplicate results across paginated pages. For example, if you’re displaying 5 posts per page and have 15 posts with the sameprice, simply ordering bypricemay cause posts to appear on multiple pages. To avoid this, set the query to order bypricein ascending or descending order, followed byIDin ascending or descending order. This ensures consistent results and resolves potential duplication issues in pagination.

#### Example 1: Latest Posts

In this example, we’ll list the latest four posts (each item shows the featured image, post title, and excerpt) using the Query Loop Builder.

We start by adding a container to the canvas. This container holds our loop and serves as the blueprint for each query item.

Next, we enable the “Use Query Loop” setting to turn our simple container into a query loop.

We add an image element inside our container and set it to “Featured Image” using the Dynamic Data dropdown.

Add another container with a Heading and Text element in the same container.

For the Heading element, we add the{post_title}tag.

`{post_title}`

For the Text element, we add{post_excerpt}tag.

`{post_excerpt}`

You could use the Post Title element or the Post Excerpt element instead if you like.

By default, the query control shows the latest posts. But because we want to restrict the number of posts shown, we need to edit the Query setting and set the Posts Per Page control to 4 to restrict the output to four rows.

### Media query

Bricks 1.5 introduces the possibility to query for media files (the attachment post type). You’ll now find theMedia(attachment) post type in the Posts query type.

`Media`

After selectingMediain the post type control, you’ll get a new control to define the mime type. By default, Bricks automatically queries for images, but you may define other mime types (separated by a comma, e.g.,image/jpeg,image/png,image/gif).

`Media`

To query for the images attached to a post, you may use theChild ofcontrol to specify the post ID. To do it dynamically, you may use dynamic data to fetch the current post id:{post_id}.

`{post_id}`

#### Example 2: Media gallery

The media query opens the possibility of building a custom media gallery using the Query Loop builder. To start, you need to add a Container element, insert a Block element inside it, and finally, an image element inside of the Block.

In the container, you’ll set the flex-wrap towrapand the direction to horizontal (row). In the Block, you must activate the Query Loop and set the Media post type and the number of images you’ll want to get (posts per page). In the Block layout, you must set the width and the height (e.g. 300px).

`wrap`

In the Image, you’ll set the dynamic data as{post_id}– note that the query returns the attachment posts (media files), so the image ID is the post ID. To complete the layout, set the image object-fit tocoverand the height to 300px.

`{post_id}`

`cover`

### WooCommerce Products Query

Since 1.10, Bricks introduced new settings for WooCommerce products query. Once selected Products post type, you will be able to see the WooCommerce section. (Only available if WooCommerce is activated)

#### Example 1: WooCommerce Featured Products

To show latest 10 featured products on your homepage, just set a query loop with below settings.

#### Example 2: WooCommerce Related Products

To show 4 related products on your single product template.

#### Example 3: WooCommerce Upsells Products

To show 3 upsells product in  a single product template.

### Terms query

Taxonomies: Select one or multiple taxonomies to query (default: none).

Order by: Order the results by term ID, term name, term parent, count, or include list.

Order: Ascending (default) or Descending.

Number: The number of terms to show per page. WordPress default is all, but Bricks defaults to the number defined in the WordPress settings → Reading → Blog pages show at most. Use 0 to display all the results.

Offset: The number of terms to skip.

Parent: Parent term ID to retrieve direct-child terms. Set this to 0 to fetch only the terms that have children. Ex.: Given this structure, entering 55 would get only the T-shirts.

Child of: Term ID to retrieve child terms of.  Ex.: Giventhisstructure, entering 55 would get T-shirts and Tees.

Childless: (bool) True to limit results to terms with no children. This parameter has no effect on non-hierarchical taxonomies. Default false.

Disable Query Merge: Turn this on if do not want the query to be auto-merged by Bricks. (@since 1.7.1)

Terms Include/Exclude: Include or Exclude terms from the query

Show empty: Whether to show terms not assigned to any posts.

Meta Query: Add one or multiple meta queries to filter the posts based on the custom fields.

Relation: Define if the meta queries should be inclusive (OR) or exclusive (AND).

No Results: Text to be shown when there are no matching results.

Current post term: Enable to get the terms assigned to the current post only.(@since 1.8.4)Only use in single post context. Only visible if “Type” is set to “Term”. This is the same logic as the example inbricks/terms/query_vars

`(@since 1.8.4)`

#### Example 3: Product categories

In this example, we’ll build a dynamic list of product categories (product category image + a link to the category archive).

The example is based on the WooCommerce plugin and the sample products. We’ll need one container to hold the container loop. Inside the container loop, we’ve added a Basic Text element that contains the Dynamic Data{term_name}tag.

`{term_name}`

After setting the Query to loop through “terms” and selecting the Taxonomy “Product Categories”, you’ll get in the canvas as many containers as the existing categories. Inside the loop, you’ll be able to use several dynamic data tags to fetch the term’s data, such as the term ID, the term name, the term archive URL, the term description, and any term meta.

In this example, we set the loop container background image as the product category thumbnail, using the Dynamic Data dropdown and selecting the Product Category Image tag:

We also set the loop container as a link to the product category archive page (using the Term Archive URL dynamic data tag). You’ll need to set the HTML tag to “a (link)” and the link type to Dynamic Data, which will enable the Dynamic Data dropdown:

### Users query

Roles: Select one or multiple user roles to query (default: any)

Order by: Order the results by user ID, name, username, nicename, login, email, registered date, post count, or include list.

Order: Ascending (default) or Descending.

Number: The number of users to show per page. WordPress defaults to all, but Bricks defaults to the number defined in the WordPress settings > Reading > Blog pages show at most. Use -1 to display all the results.

Offset: The number of users to skip.

Current post author:Enable to query the current post author (@since 1.9.1)

Disable Query Merge: Turn this on if do not want the query to be auto-merged by Bricks. (@since 1.7.1)

Meta Query: Add one or multiple meta queries to filter the posts based on the custom fields.

Relation: Define if the meta queries should be inclusive (OR) or exclusive (AND).

No Results: Text to be shown when there are no matching results.

#### Example 4:The blog authors

In this example, we want to build a section to list all the blog authors.

The blog authors are website users with the role of author. As in the other examples, we’ve used a container to loop through the users. In that container, we’ve set a query of user type, setting roles to “Author” to pull only the website’s authors.

We’ve added an Image and a Basic Text element inside the query loop container.

The image we’ve set to display an ACF Dynamic Data field containing the profile image.

In the Basic Text, we’ve used the Dynamic Data{wp_user_display_name}tag.

`{wp_user_display_name}`

### The Pagination element

The perfect companion to the custom query loop builder. You’ll find the Pagination element under theWordPressgroup of the elements panel.

Having pagination as a separate element offers you the most flexibility to build any layout.

After adding the Pagination element to the canvas, you’ll need to link this pagination element to one of the elements that run a query. To do so, please select the element in theRelated Querycontrol by editing the Pagination element:

Tip: to make it easier to recognize elements, give descriptive element names to the containers that have a query enabled.

### Load more (button)

Besides the infinite scroll, which automatically loads more results as you scroll down the page, you can also give any element (typically the Button) a “Load more” functionality by adding a “Load more” clickinteractionto it like this:

### Query loop in Accordions & Sliders

The Accordion & Slider elements also allow to pull data dynamically through the Query Loop to feed the element parts.

You’ll find a Query Loop control in the Accordion element to configure a query. The query results create as many accordion items as the query results.

You’ll be able to configure the accordion title, subtitle, and content of the “master” accordion item, and this will be used as a template for the dynamic accordion items:

The same happens in the Slider element. If the Query Loop is enabled, you’ll have access to a Query control and a slide item, which will behave as the template for all the slides.

### Include/Exclude Controls: Dynamic data tag support

Starting at version 1.12, Bricks supports dynamic data tags in the “Include” and “Exclude” query loop controls.

This allows you to include or exclude posts dynamically using field values, such as those retrieved from ACF or Meta Box relationship fields.

- Include: Adds IDs to thepost__inparameter.
- Exclude: Adds IDs to thepost__not_inparameter.

`post__in`

`post__not_in`

This enhancement enables you to use dynamic data to retrieve post IDs from custom fields (e.g., ACF or Meta Box), while still combining additional query parameters likemeta queriesortaxonomy queries.

##### Supported Field Types

- ACF:Relationship, Post Object, Gallery
- Meta Box:Relationship, Post, Image Advanced, Image, Image Upload, Single Image

Important: When using dynamic data in the Include field, ensure the selected Post Type matches the field values. For example, if you are using a Gallery field, set the Post Type to Media to ensure the dynamic value aligns correctly.

#### Example 1: Retrieve ACF Relationship Posts by Post Type and Order by Post IDs

Imagine you have an ACF Relationship field that connects to multiple post types. On a specific query, you only want to retrieve the related posts limited to the “Book” post type and have them displayed in the same order as defined in the relationship field.

#### Example 2: Use Meta Box Image Advanced Field for a Nestable Slider Query Loop

Previously, retrieving images saved in theMeta Box Image Advancedfield required using a PHP filter to pass the image IDs into thepost__inparameter. Now, you can achieve this directly within the Query Loop UI.

`post__in`

Simply choose your dynamic field, set thePost TypetoMediaand, if needed, add an additionalMime Typefilter to ensure only the correct image types are included.

Note: Inside the loop, use dynamic tags like{post_id}for the image source and{post_title}to retrieve the image title. Avoid using{featured_image}, as this is not applicable in this context.

`{post_id}`

`{post_title}`

`{featured_image}`

#### Example 3: Query ACF Gallery with Random Order

To display images from anACF Galleryfield in a random order, set the Post Type toMedia. (Add an additional Mime Type filter if necessary to ensure only specific file types are included.) SelectRandom (rand)to randomize the order of the images in the gallery.

Note: Inside the loop, use dynamic tags like{post_id}for the image source and{post_title}to retrieve the image title. Avoid using{featured_image}, as this is not applicable in this context.

`{post_id}`

`{post_title}`

`{featured_image}`

### Query loop hooks

- bricks/query/run(filter)
- bricks/terms/query_vars(filter)
- bricks/users/query_vars(filter)
- bricks/posts/merge_query(filter)
- bricks/posts/query_vars(filter)
- bricks/query/loop_object(filter)
- bricks/query/loop_object_id(filter)
- bricks/query/loop_object_type(filter)
- bricks/query/no_results_content(filter)
- bricks/query/before_loop(action)
- bricks/query/after_loop(action)
- bricks/query/result(filter)
- bricks/query/result_count(filter)
- bricks/query/result_max_num_pages(filter)
- bricks/query/init_loop_index(filter)

###### Builder Mode (Custom)

###### Converter

