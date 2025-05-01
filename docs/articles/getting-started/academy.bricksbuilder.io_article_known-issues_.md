---
title: "Known issues – Bricks Academy"
url: https://academy.bricksbuilder.io/article/known-issues/
date: 2025-05-01T12:03:47.662589
status: success
---

# Known issues – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/known-issues/](https://academy.bricksbuilder.io/article/known-issues/)*

## Table of Contents

- [Known issues](#known-issues)
  - [When I open the builder I don’t see the elements on the canvas](#when-i-open-the-builder-i-dont-see-the-elements-on-the-canvas)
    - [Workarounds](#workarounds)
    - [Method 1) Configuration Rules](#method-1-configuration-rules)
    - [Method 2) Disable Rocket Loader](#method-2-disable-rocket-loader)
    - [Method 3) Disable SiteGround Worker Routes](#method-3-disable-siteground-worker-routes)
  - [Copy/paste elements or styles not working](#copypaste-elements-or-styles-not-working)
    - [Using Firefox](#using-firefox)
  - [Internal server error (500) when trying to edit homepage with Bricks](#internal-server-error-500-when-trying-to-edit-homepage-with-bricks)
  - [My Blog page is not using the posts archive template](#my-blog-page-is-not-using-the-posts-archive-template)
  - [I’m using SVG files in Bricks elements but I cannot change their color](#im-using-svg-files-in-bricks-elements-but-i-cannot-change-their-color)
  - [Custom Fonts not working on the frontend](#custom-fonts-not-working-on-the-frontend)
  - [YouTube background video doesn’t autoplay on mobile](#youtube-background-video-doesnt-autoplay-on-mobile)
  - [Slider doesn’t autoplay / Animation Flickering](#slider-doesnt-autoplay--animation-flickering)
  - [Invalid Post Type / Custom Post Type 404 Errors](#invalid-post-type--custom-post-type-404-errors)
    - [Re-save your permalink settings](#re-save-your-permalink-settings)
    - [Check for slug conflicts](#check-for-slug-conflicts)
  - [Builder changes not saved](#builder-changes-not-saved)
  - [Save button spinning endlessly due to ModSecurity](#save-button-spinning-endlessly-due-to-modsecurity)
  - [Query Filter Indexer: No Progress](#query-filter-indexer-no-progress)
  - [Avoiding Slow Queries in Media/Attachment Dynamic Data](#avoiding-slow-queries-in-mediaattachment-dynamic-data)
  - [Slider doesn’t autoplay / Animations not working](#slider-doesnt-autoplay--animations-not-working)
        - [Understanding The Layout](#understanding-the-layout)
        - [Best Practices](#best-practices)

## Known issues

### When I open the builder I don’t see the elements on the canvas

If you open the builder and you don’t see the elements in the canvas but they are shown in the structure panel, and if you are using Cloudflare, then this is a known problem caused by a conflict between theCloudflare Rocket Loader™ / other performance optimization feature and the Bricks builder JavaScript.

Starting with Bricks 2.0, a newexperimental settinghas been introduced to improve compatibility with Rocket Loader™. Enable it inBricks > Settings > Builderand reload the builder page, your elements should now appear correctly on the canvas.

#### Workarounds

#### Method 1) Configuration Rules

Create a configuration rule for builder mode.

1. Log into the Cloudflaredashboard.
2. Select your account and website.
3. Go to Rules > Configuration Rules.
4. Create a new Rule, give it a name, and choose Custom filter expressionField: URI Query StringOperator: containsValue: bricks=run
5. Field: URI Query String
6. Operator: contains
7. Value: bricks=run
8. Configure “Then the settings are…”:Add Rocket Loader and leave the checkbox empty.
9. Add Rocket Loader and leave the checkbox empty.
10. Leave the other settings empty.
11. Save the rule by clicking “Deploy”.
12. Wait for a few minutes and do a browser hard refresh in Bricks builder. (Clear browser caches)

- Field: URI Query String
- Operator: contains
- Value: bricks=run

- Add Rocket Loader and leave the checkbox empty.

#### Method 2) Disable Rocket Loader

Disable the Rocket Loader™ in the Cloudflare dashboard:

1. Log into the Cloudflaredashboard.
2. Select your account and website.
3. Go to Speed > Optimization.
4. Scroll down until you find Rocket Loader.
5. Turn it off.

#### Method 3) Disable SiteGround Worker Routes

If the above 2 methods do not work and you are using SiteGround hosting, please check and disable the Worker created by SiteGround.

1. Log into the Cloudflare dashboard.
2. Select your account and website.
3. Go to Workers Routes.
4. If sg_worker exists or another suspicious worker is defined without your awareness, you can remove it.

### Copy/paste elements or styles not working

Bricks 1.5.1 uses the Clipboard API to copy and paste elements and styles across different domains.

Copy/paste is only supported for pages served overHTTPS.

#### Using Firefox

Firefox is more restrictive regarding reading from this API, which prevents the paste action, and therefore it requires the user to manually grant permission to use the API.

To do so, please follow these steps in your Firefox browser:

1. Enterabout:configin navigation bar
2. Click “Accept the Risk and Continue”
3. Searchclipboardand setdom.events.asyncClipboard.readTextanddom.events.testing.asyncClipboardtotrue
4. Restart Firefox

`about:config`

`clipboard`

`dom.events.asyncClipboard.readText`

`dom.events.testing.asyncClipboard`

`true`

### Internal server error (500) when trying to edit homepage with Bricks

If you see a screen similar to the above, showing an internal server error (500) when trying to edit a page with Bricks (often reported as the homepage), you should look at the server logs and adjust the server configuration. This error is most probably caused by a security server configuration that prevents the request to hit WordPress and Bricks.

Some servers do not have theSecResponseBodyLimitdefined leading to errors like:

`SecResponseBodyLimit`

```
ModSecurity: Output filter: Response body too large (over limit of 1048576, total not specified).
```

`ModSecurity: Output filter: Response body too large (over limit of 1048576, total not specified).`

(Note: the SecResponseBodyLimit sets the maximum response body size that will be accepted for buffering).

Check thisforum postfor possible solutions. If the issue persists, please contact your hosting support for guidance.

ForGoDaddyusers, you might need to add this line of code in your .htaccess file (first line)

```
SubstituteMaxLineLength 10M
```

`SubstituteMaxLineLength 10M`

### My Blog page is not using the posts archive template

The Blog page (WordPress Posts Page set in the Settings > Reading) is a special WordPress page, and therefore it is not an archive. If you want to set a Bricks template for the Blog page, you would need to set the template condition Individual and select the Blog page.

### I’m using SVG files in Bricks elements but I cannot change their color

This usually happens when your SVG file contains inline styles which override the styles generated by the Bricks builder. If you want to use these SVG files in combination with the Bricks style’s controls, you need to remove the inline styles from the SVG file before uploading it to the WordPress installation.

### Custom Fonts not working on the frontend

If your custom fonts are not displayed in the frontend, it is probably because your WordPress website is delivered via HTTPS, but your WordPress URLs are still set to HTTP (WordPress Settings » General).

Changing the WordPress URLs fromhttp://tohttps://will fix the problem and your fonts will be displayed correctly from now on.

`http://`

`https://`

### YouTube background video doesn’t autoplay on mobile

This restriction is imposed by the YoutTube iFrame Player API and cannot be influenced by us. Seehttps://developers.google.com/youtube/iframe_api_reference#Mobile_considerations

However, Vimeo and local videos (mp4) should work as long as the mobile device is not in low-battery mode.

### Slider doesn’t autoplay / Animation Flickering

This is most likely caused by the reduced motion or animation setting of your operating system.

On Windows, please make sure that the“Show animations in windows”setting is enabled:

On macOS, please make sure that the“Reduce motion”setting is NOT enabled:

### Invalid Post Type / Custom Post Type 404 Errors

This problem is probablythe most common problemin WordPress: your custom post type returns a 404 error. In most cases, however, the problem can be solved very easily.

#### Re-save your permalink settings

All you have to do is go to WordPress » Settings » Permalinks and click on “Save Changes”.

#### Check for slug conflicts

The slug refers to the user-friendly and URL-valid name of a post, page, category, tag, or any content (even images) within your website. It is a part of the URL that identifies a specific piece of content.

Let’s assume you have a “Portfolio” page whose slug is “portfolio”. Now you create a custom post type called “Portfolio”, whose slug is also “portfolio”. If you now try to call up a single post from your portfolio (yoursite.com/portfolio/your-portfolio-post), there will be a 404 error too. To solve this issue, rename either the page slug, or the custom post type slug to something else. Re-save your permalinks again, and everything should work as expected.

### Builder changes not saved

If you save changes in the builder and everything appears to be saved, but upon refreshing or viewing on the frontend the changes are lost, it could be due to an issue with your database schema.

Specifically, check themeta_valuecolumn in yourwp_postmetatable (or your table prefix, e.g.,psjw_postmeta). This column should be set to “LONGTEXT” to ensure it can store large amounts of data. If it’s set to a type with a lower storage capacity, such as “TEXT,” it may not save larger data correctly.

`meta_value`

`wp_postmeta`

`psjw_postmeta`

For more details on storage limitations, refer to this resource:Understanding Storage Sizes for MySQL TEXT Data Types.

WordPress defaults to using “LONGTEXT” for themeta_valuecolumn, which allows for much larger data storage. See the default schema here:WordPress Database Description.

`meta_value`

To resolve this issue:

1. Check yourmeta_valuecolumn type in thewp_postmetatable (orpsjw_postmeta).
2. Ensure it is set to “LONGTEXT.”

`meta_value`

`wp_postmeta`

`psjw_postmeta`

You can change the column type to “LONGTEXT” using the following MySQL command:

```
ALTER TABLE your_prefix_postmeta MODIFY COLUMN meta_value LONGTEXT;
```

`ALTER TABLE your_prefix_postmeta MODIFY COLUMN meta_value LONGTEXT;`

Replaceyour_prefix_postmetawith your actual table name, e.g.,psjw_postmeta.

`your_prefix_postmeta`

`psjw_postmeta`

1. Verify that other columns in yourpostmetatable match the default WordPress schema.

`postmeta`

If you are not comfortable making these changes or are using a managed hosting provider, it’s best to get in touch with your hosting provider. They can help address this issue, which might persist across different hosting services due to the migration of the incorrect database schema.

### Save button spinning endlessly due to ModSecurity

If you find that the save button in the Bricks builder is spinning endlessly, and your server logs point to ModSecurity errors, this could be caused by certain ModSecurity variables being too restrictive:

- SecRequestBodyLimit
- SecRequestBodyNoFilesLimit
- SecResponseBodyLimit

`SecRequestBodyLimit`

`SecRequestBodyNoFilesLimit`

`SecResponseBodyLimit`

While we can’t guarantee this will resolve your specific issue, other users have found that increasing these values fixed the problem.

The values can vary depending on your server, so you might need to experiment or consult your hosting provider to make these changes.

### Query Filter Indexer: No Progress

If the filter element continues to display “Indexing in Progress” in the builder, try clicking the “Continue Index Job” button by following the instructions inthis article.

However, if the indexing jobs remain pending without any progress, it might be caused by specific firewall rules blocking the background process.

Best to check your website firewall settings or contact your hosting support. If your website is protected by HTTP Authentication, please add thiscode snippetin your child theme’s functions.php as well.

For users with Cloudflare proxy enabled, ensure that Bot Fight Mode is disabled.Refer to this guide to prevent false positives.

### Avoiding Slow Queries in Media/Attachment Dynamic Data

When working with plugins likeACF,Meta Box, orJetEngineto create fields that store image or attachment file information, it is recommended to set the field’s return value toobjectorIDinstead ofURL.Examples of Field Types:

- ACF: Image, Gallery, File
- JetEngine: Media, Gallery
- Meta Box: File Input, Image Select
- Toolset: Attachment URL to Post ID

This recommendation is important because Bricks uses theattachment_url_to_postidWordPress function to retrieve additional image data, such as dimensions and available sizes, when working with URL values. On websites with a large number of posts, this function can be resource-intensive, potentially slowing down page loading times.By returning the field as an object or ID, Bricks can access the required data directly, improving performance and reducing the likelihood of slow queries.

`attachment_url_to_postid`

### Slider doesn’t autoplay / Animations not working

If your animations on your site are not working or your slider isn’t autoplaying, it might be due to the “Reduce motion” setting on your device. This is an accessibility feature that Bricks respects. To see animations:

- On Windows: Ensure that the “Show animations in windows” setting is enabled.
- On macOS: Make sure that the “Reduce motion” setting is NOT enabled.

###### Understanding The Layout

###### Best Practices

