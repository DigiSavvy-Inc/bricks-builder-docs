---
title: "Requirements – Bricks Academy"
url: https://academy.bricksbuilder.io/article/requirements/
date: 2025-05-01T12:32:10.650631
status: success
---

# Requirements – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/requirements/](https://academy.bricksbuilder.io/article/requirements/)*

## Table of Contents

- [Requirements](#requirements)
  - [How To Increase WP Memory Limit](#how-to-increase-wp-memory-limit)
  - [How To Increase Max File Upload Size](#how-to-increase-max-file-upload-size)
  - [How To Increase Maximum Execution Time](#how-to-increase-maximum-execution-time)
        - [Installation & Activation](#installation--activation)
        - [Understanding The Layout](#understanding-the-layout)

## Requirements

To provide you with a cutting-edge site builder for WordPress Bricks uses the most modern technology stack (VueJS 3, etc.) while keeping sufficient backward compatibility.

Below are a few minimum requirements your server should meet so Bricks runs smoothly:

- PHP 7.4+
- MySQL 5.6+
- WordPress memory limit of at least 64 MB
- Max file upload size of at least 16 MB
- Modern browser:Please use the latest version of Chrome, Firefox, Safari, or Microsoft Edge when editing your website with Bricks. Older browsers (e.g. Internet Explorer) lack support for some of the more advanced builder features.

Bricks is a self-hosted solution that you download & install on your own WordPress website!

### How To Increase WP Memory Limit

You can defineWP_MEMORY_LIMITby adding the following code to yourwp-config.phpfile (above the “That’s all, stop editing!” line):

```
define( 'WP_MEMORY_LIMIT', '256M' );
/* That's all, stop editing! Happy publishing. */
```

Some web hosts set the PHP memory limit to 8 MB. In that case, you might consider upgrading to a more powerful hosting plan. If your host does not allow you to config this setting by yourself, please get in touch with them.

### How To Increase Max File Upload Size

If you encounter problems uploading larger files to your site (or when downloading high-resolution images from Bricks’ Unsplash integration) there are a few ways to increase the maximum upload file size.

A maximum upload size of 16 MB should suffice. But 64 MB would be ideal. Log into your hosting account and change the following twoPHP server settingsto:

- post_max_size: 64M
- upload_max_filesize: 64M

If you have access to yourphp.inifile, located in the root directory of your WordPress installation, open it, and modify the following settings:

```
upload_max_filesize = 64M
post_max_size = 64M
```

You can also add the following code to your.htaccessfile, but make sure to backup your existing .htaccess file beforehand:

```
php_value upload_max_filesize 64M
php_value post_max_size 64M
```

If all above fails, you can try adding the following code to your wp-config.php:

```
@ini_set( 'upload_max_size' , '64M' );
@ini_set( 'post_max_size', '64M');
```

To confirm that your maximum upload file size has been updated successfully, go toMedia > Add New. On the bottom of this page, you should see your maximum upload file size.

### How To Increase Maximum Execution Time

When you start seeing a message like “Maximum execution time of 30 seconds exceeded” you have to increase the execution time of your website by using one of the following three solutions:

#1: Add the following code to your wp-config.php file (above the “That’s all, stop editing!” line):

```
set_time_limit(180);
/* That's all, stop editing! Happy publishing. */
```

#2: Backup your .htaccess file and add the following code to it:

```
php_value max_execution_time 180
```

#3: Add the following code to your php.ini file:

```
max_execution_time = 180
```

###### Installation & Activation

###### Understanding The Layout

