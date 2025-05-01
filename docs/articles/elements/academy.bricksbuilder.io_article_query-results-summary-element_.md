---
title: "Query Results Summary Element – Bricks Academy"
url: https://academy.bricksbuilder.io/article/query-results-summary-element/
date: 2025-05-01T12:03:36.283754
status: success
---

# Query Results Summary Element – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/query-results-summary-element/](https://academy.bricksbuilder.io/article/query-results-summary-element/)*

## Table of Contents

- [Query Results Summary Element](#query-results-summary-element)
  - [Controls](#controls)
      - [Query](#query)
      - [Format](#format)
      - [Text: One Result](#text-one-result)
      - [Text: No Results](#text-no-results)
  - [Compatibility](#compatibility)
        - [Global class import manager](#global-class-import-manager)
        - [Map Element](#map-element)

## Query Results Summary Element

The Query Results Summary element, introduced in version 1.12.2, allows you to display a dynamic count of results within a query, helping users understand which items they are currently viewing in relation to the total number of results. This is particularly useful for search results, archive pages, and paginated lists where users navigate through multiple pages of content. It can be found in the elements panel under the “Query” category.

Note:If a third-party plugin disables Bricks Query history via thebricks/query/force_runhook, the results summary may display incorrect information.

`bricks/query/force_run`

### Controls

##### Query

Select thetarget queryfor which the summary should be displayed.

##### Format

Customize the summary text using placeholders:

- %start%– The index of the first item on the current page.
- %end%– The index of the last item on the current page.
- %total%– The total number of results.

`%start%`

`%end%`

`%total%`

Default format:Results: %start% - %end% of %total% posts

`Results: %start% - %end% of %total% posts`

Example output: Results: 1 – 5 of 14 posts

##### Text: One Result

Define a custom message when the query returns exactlyoneresult to handle singular/plural differences.

Default text: One post found

##### Text: No Results

Specify a custom message when the query returnszeroresults.

Default text: No posts found

### Compatibility

TheQuery Results Summaryelement works seamlessly with Bricks’ native AJAX actions, including:

- AJAX Pagination
- Load More
- Infinite Scroll
- Query Filters

This ensures that the summary updates dynamically as users interact with query-based elements on the page.

Example:

###### Global class import manager

###### Map Element

