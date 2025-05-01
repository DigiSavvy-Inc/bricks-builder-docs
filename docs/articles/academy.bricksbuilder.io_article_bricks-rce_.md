---
title: "Steps to identify and repair a compromised Bricks site – Bricks Academy"
url: https://academy.bricksbuilder.io/article/bricks-rce/
date: 2025-05-01T12:03:08.380574
status: success
---

# Steps to identify and repair a compromised Bricks site – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/bricks-rce/](https://academy.bricksbuilder.io/article/bricks-rce/)*

## Table of Contents

- [Steps to identify and repair a compromised Bricks site](#steps-to-identify-and-repair-a-compromised-bricks-site)
  - [A disclaimer](#a-disclaimer)
  - [What happened?](#what-happened)
  - [How to check if your WordPress site has been compromised](#how-to-check-if-your-wordpress-site-has-been-compromised)
  - [Steps to clean a compromised site](#steps-to-clean-a-compromised-site)
    - [1 – Block incoming traffic:](#1--block-incoming-traffic)
    - [2 – Restore a backup in your local environment](#2--restore-a-backup-in-your-local-environment)
    - [3 – Update the Bricks theme to the latest version](#3--update-the-bricks-theme-to-the-latest-version)
    - [4 – Re-perform the steps outlined above](#4--re-perform-the-steps-outlined-above)
    - [5 – Reinstall WordPress core, all themes, and plugins](#5--reinstall-wordpress-core-all-themes-and-plugins)
    - [6 – Change sensitive credentials and keys](#6--change-sensitive-credentials-and-keys)
    - [7 – Migrate your local installation to your live environment](#7--migrate-your-local-installation-to-your-live-environment)
    - [8 – Alternative method (for hosts allowing site isolation)](#8--alternative-method-for-hosts-allowing-site-isolation)
    - [Additional steps (important for all scenarios)](#additional-steps-important-for-all-scenarios)

## Steps to identify and repair a compromised Bricks site

In this post, we’ll discuss the security vulnerability discovered in Bricks on February 10th, 2024, for which we provided a verified security patch on February 13th, 2024, with Bricks version 1.9.6.1.

If you still haven’t updated to the latest version of Bricks (1.9.6.1 or above), please do so now!

We’ll then go over some concrete, actionable steps you can take to inspect and clean up infected sites.

### A disclaimer

Although this recent vulnerability in Bricks sparked this article, we hope that you take this opportunity to review and adjust your website security measures in general. Both in terms of preventive care and the procedure to identify and clean up a possibly infected WordPress site.

In 2023, around 13,000 WordPress sites experienced security breaches each day. Given this statistic, it’s important for website owners to be prepared and informed about potential security threats, rather than if they might encounter them.

The information in this article contains some of the most known steps you can take to check if your Bricks site, or any WordPress site really, has been compromised and how to clean it up.

While we’ve made every effort to provide accurate and helpful steps in this article, please note that these are general guidelines. The effectiveness of these steps can vary based on individual site conditions and the nature of any potential compromise.

As such, we encourage caution and recommend regularly backing up your site as a safeguard. Consulting with a professional is always a wise decision if you’re unsure about any process or encounter complex issues. We aim to support and inform but can’t assume liability for unintended outcomes.

### What happened?

Security researcher Calvin Alkan contacted the Bricks team on February 10th, 2024, about his discovery of an “Unauthenticated Remote Code Execution in Bricks <= 1.9.6”, which can grant bad actors who know how to exploit it, access to your site.

The Bricks team immediately got to work on a fix that addressed the root problem.

Bricks 1.9.6.1 was released as a one-click update on February 13th, 2024, which contained a security patch to address this vulnerability.

After consulting with the WordPress security experts at patchstack.com, Bricks released a public changelog entry about the 1.9.6.1 release highlighting the security patch and immediately sent an email (subject: “Security Patch: Update to Bricks 1.9.6.1 Now”) to all customers about thismandatory security update, even if that meant temporary functionality loss. A second email was sent within the following 24 hours.

The same information was shared in a pinnedFacebook postin the Bricks Community group. Bricks urged everyone to update to Bricks 1.9.6.1 immediately and to share this news with fellow Bricks users in other groups, etc., to help spread awareness about it.

While no exploits of this vulnerability were reported at the time of the 1.9.6.1 release, not everyone was able to update in time, and the first affected sites were reported 5 to 6 hours later, as later confirmed by Patchstack.

Less than 72 hours after the release, this 1.9.6.1 security patch became the most downloaded version of the Bricks theme.

Even if you updated your Bricks site right away, and there are no signs that your site has been compromised, we urge you to take the time to ensure your site is clean.

### How to check if your WordPress site has been compromised

Take detailed notes of all your findings, as we will use those to clean up your site in the next section (“Steps to clean a compromised site”).

While all steps can be performed via the command line, we’ll focus on performing them through the GUI so as many users as possible can follow along.

1. Review user accounts:Go to your WordPress dashboard, then click onUsersLook for any user accounts you don’t recognize. Especially those with a user role ofAdministrator.
2. Go to your WordPress dashboard, then click onUsers
3. Look for any user accounts you don’t recognize. Especially those with a user role ofAdministrator.
4. Inspect child themes:In your WordPress dashboard, go toAppearance > Themes.Check for any themes you didn’t install yourself. Unfamiliar names are a red flag.
5. In your WordPress dashboard, go toAppearance > Themes.
6. Check for any themes you didn’t install yourself. Unfamiliar names are a red flag.
7. Examine server files for modifications:Use an FTP client (like FileZilla) or login to your hosting account to access your site’s files.Inspect the root directory (where your WordPress site is installed) and all its sub-folders.Search for Recently Changed Files: To find files that may have been added or modified by an attacker, use the commandfind . -type f -newermt "2024-02-01"in SSH. This command lists all files that were added or changed after February 1st, 2024.Note: this is not foolproof. Sophisticated attackers might hide their tracks by altering file timestamps or employing other tactics. So, even if this search doesn’t turn up anything suspicious, it doesn’t guarantee your site is completely safe. However, it’s still a valuable step as it can quickly flag obvious issues.Cryptic-named, non-WP files are a red flag: look for anything that seems out of place or unusual. This includes files with strange names, files in unexpected locations, or files that don’t appear to be related to WordPress or your usual content.Examples of unusual files might include:Files with random or nonsensical names likexj47v.phporfile.fplka28asin your WordPress directories.PHP files located in directories where they usually aren’t found, like image upload folders.Files with unusual extensions that are not typically associated with WordPress, such as.javaor.exefiles.
8. Use an FTP client (like FileZilla) or login to your hosting account to access your site’s files.
9. Inspect the root directory (where your WordPress site is installed) and all its sub-folders.
10. Search for Recently Changed Files: To find files that may have been added or modified by an attacker, use the commandfind . -type f -newermt "2024-02-01"in SSH. This command lists all files that were added or changed after February 1st, 2024.Note: this is not foolproof. Sophisticated attackers might hide their tracks by altering file timestamps or employing other tactics. So, even if this search doesn’t turn up anything suspicious, it doesn’t guarantee your site is completely safe. However, it’s still a valuable step as it can quickly flag obvious issues.
11. Cryptic-named, non-WP files are a red flag: look for anything that seems out of place or unusual. This includes files with strange names, files in unexpected locations, or files that don’t appear to be related to WordPress or your usual content.Examples of unusual files might include:Files with random or nonsensical names likexj47v.phporfile.fplka28asin your WordPress directories.PHP files located in directories where they usually aren’t found, like image upload folders.Files with unusual extensions that are not typically associated with WordPress, such as.javaor.exefiles.
12. Examples of unusual files might include:Files with random or nonsensical names likexj47v.phporfile.fplka28asin your WordPress directories.PHP files located in directories where they usually aren’t found, like image upload folders.Files with unusual extensions that are not typically associated with WordPress, such as.javaor.exefiles.
13. Files with random or nonsensical names likexj47v.phporfile.fplka28asin your WordPress directories.
14. PHP files located in directories where they usually aren’t found, like image upload folders.
15. Files with unusual extensions that are not typically associated with WordPress, such as.javaor.exefiles.
16. Check posts and pages:In your WordPress dashboard, review thePostsandPagessections. Plus, any custom post types you have registered.Look for any content that you or your team didn’t create.
17. In your WordPress dashboard, review thePostsandPagessections. Plus, any custom post types you have registered.
18. Look for any content that you or your team didn’t create.
19. Investigate server performance anomalies:Keep an eye out for errors when you load your site. Such as a page not loading correctly or displaying a500 Internal Server Error.Check with your hosting provider’s control panel for any sudden increases in CPU usage, which could indicate hidden activities on your site.
20. Keep an eye out for errors when you load your site. Such as a page not loading correctly or displaying a500 Internal Server Error.
21. Check with your hosting provider’s control panel for any sudden increases in CPU usage, which could indicate hidden activities on your site.
22. Check cron jobs:Cron jobs are scheduled tasks on your server. Access them through your hosting control panel. Check with your hosting provider for any unknown cron jobs.As for WordPress-specific cron jobs, you can use a free plugin likeWP Crontrol. Remove any unknown custom cron jobs.
23. Cron jobs are scheduled tasks on your server. Access them through your hosting control panel. Check with your hosting provider for any unknown cron jobs.
24. As for WordPress-specific cron jobs, you can use a free plugin likeWP Crontrol. Remove any unknown custom cron jobs.
25. Unknown redirects:Visit your website and see if you’re unexpectedly taken to a different site or page. This could be a sign of unauthorized redirects.
26. Visit your website and see if you’re unexpectedly taken to a different site or page. This could be a sign of unauthorized redirects.
27. Audit logs review:If your hosting provides an audit log, review it. It’s a record of activities on your site.Look for unusual login attempts, changes in user roles, or modifications in settings.Pay special attention to error messages like “Headers already sent” or sudden patterns of malfunctions.The key is to check the timestamps. If suspicious activities started occurring around or after February 13th, 2024, they could be related to the vulnerability discovered in Bricks.
28. If your hosting provides an audit log, review it. It’s a record of activities on your site.
29. Look for unusual login attempts, changes in user roles, or modifications in settings.
30. Pay special attention to error messages like “Headers already sent” or sudden patterns of malfunctions.
31. The key is to check the timestamps. If suspicious activities started occurring around or after February 13th, 2024, they could be related to the vulnerability discovered in Bricks.
32. Check .htaccess file:Access your site’s files using FTP or your hosting file manager.Find the.htaccessfile in your root directory.To check when it was last edited, you can use an FTP client to view the file’s properties or use the commandls -l .htaccessin SSH.If the last edit date is recent and you didn’t make the changes, examine the file for unknown rules or redirects.If you’re unsure about the contents, consult a professional or your hosting provider for assistance.
33. Access your site’s files using FTP or your hosting file manager.
34. Find the.htaccessfile in your root directory.
35. To check when it was last edited, you can use an FTP client to view the file’s properties or use the commandls -l .htaccessin SSH.
36. If the last edit date is recent and you didn’t make the changes, examine the file for unknown rules or redirects.
37. If you’re unsure about the contents, consult a professional or your hosting provider for assistance.

- Go to your WordPress dashboard, then click onUsers
- Look for any user accounts you don’t recognize. Especially those with a user role ofAdministrator.

`Users`

`Administrator`

- In your WordPress dashboard, go toAppearance > Themes.
- Check for any themes you didn’t install yourself. Unfamiliar names are a red flag.

`Appearance > Themes`

- Use an FTP client (like FileZilla) or login to your hosting account to access your site’s files.
- Inspect the root directory (where your WordPress site is installed) and all its sub-folders.
- Search for Recently Changed Files: To find files that may have been added or modified by an attacker, use the commandfind . -type f -newermt "2024-02-01"in SSH. This command lists all files that were added or changed after February 1st, 2024.Note: this is not foolproof. Sophisticated attackers might hide their tracks by altering file timestamps or employing other tactics. So, even if this search doesn’t turn up anything suspicious, it doesn’t guarantee your site is completely safe. However, it’s still a valuable step as it can quickly flag obvious issues.
- Cryptic-named, non-WP files are a red flag: look for anything that seems out of place or unusual. This includes files with strange names, files in unexpected locations, or files that don’t appear to be related to WordPress or your usual content.Examples of unusual files might include:Files with random or nonsensical names likexj47v.phporfile.fplka28asin your WordPress directories.PHP files located in directories where they usually aren’t found, like image upload folders.Files with unusual extensions that are not typically associated with WordPress, such as.javaor.exefiles.
- Examples of unusual files might include:Files with random or nonsensical names likexj47v.phporfile.fplka28asin your WordPress directories.PHP files located in directories where they usually aren’t found, like image upload folders.Files with unusual extensions that are not typically associated with WordPress, such as.javaor.exefiles.
- Files with random or nonsensical names likexj47v.phporfile.fplka28asin your WordPress directories.
- PHP files located in directories where they usually aren’t found, like image upload folders.
- Files with unusual extensions that are not typically associated with WordPress, such as.javaor.exefiles.

`find . -type f -newermt "2024-02-01"`

- Examples of unusual files might include:Files with random or nonsensical names likexj47v.phporfile.fplka28asin your WordPress directories.PHP files located in directories where they usually aren’t found, like image upload folders.Files with unusual extensions that are not typically associated with WordPress, such as.javaor.exefiles.
- Files with random or nonsensical names likexj47v.phporfile.fplka28asin your WordPress directories.
- PHP files located in directories where they usually aren’t found, like image upload folders.
- Files with unusual extensions that are not typically associated with WordPress, such as.javaor.exefiles.

- Files with random or nonsensical names likexj47v.phporfile.fplka28asin your WordPress directories.
- PHP files located in directories where they usually aren’t found, like image upload folders.
- Files with unusual extensions that are not typically associated with WordPress, such as.javaor.exefiles.

`xj47v.php`

`file.fplka28as`

`.java`

`.exe`

- In your WordPress dashboard, review thePostsandPagessections. Plus, any custom post types you have registered.
- Look for any content that you or your team didn’t create.

`Posts`

`Pages`

- Keep an eye out for errors when you load your site. Such as a page not loading correctly or displaying a500 Internal Server Error.
- Check with your hosting provider’s control panel for any sudden increases in CPU usage, which could indicate hidden activities on your site.

`500 Internal Server Error`

- Cron jobs are scheduled tasks on your server. Access them through your hosting control panel. Check with your hosting provider for any unknown cron jobs.
- As for WordPress-specific cron jobs, you can use a free plugin likeWP Crontrol. Remove any unknown custom cron jobs.

- Visit your website and see if you’re unexpectedly taken to a different site or page. This could be a sign of unauthorized redirects.

- If your hosting provides an audit log, review it. It’s a record of activities on your site.
- Look for unusual login attempts, changes in user roles, or modifications in settings.
- Pay special attention to error messages like “Headers already sent” or sudden patterns of malfunctions.
- The key is to check the timestamps. If suspicious activities started occurring around or after February 13th, 2024, they could be related to the vulnerability discovered in Bricks.

- Access your site’s files using FTP or your hosting file manager.
- Find the.htaccessfile in your root directory.
- To check when it was last edited, you can use an FTP client to view the file’s properties or use the commandls -l .htaccessin SSH.
- If the last edit date is recent and you didn’t make the changes, examine the file for unknown rules or redirects.
- If you’re unsure about the contents, consult a professional or your hosting provider for assistance.

`.htaccess`

`ls -l .htaccess`

### Steps to clean a compromised site

If you’ve followed the steps in our previous section and suspect your site has been compromised, here’s a guide on how you may fix it.

Remember, these are general steps, and it’s crucial to keep monitoring your site even after these actions.

The steps below assume you have recent backups of your site and that you can perform the cleanup locally on your computer to avoid your site getting compromised again during your cleanup.

#### 1 – Block incoming traffic:

If you are unable to set up a WordPress installation on your computer and you must perform the cleanup on your live site, please make sure to block incoming traffic to your site during this time to ensure your site can’t be compromised again while you clean it up.

If you are unsure how to do this or how to do it best, please get in touch with your hosting provider.

One possible solution is to block all IP addresses except your own by adding the following code at the very top of your.htaccessfile:

`.htaccess`

```
Order Deny,Allow
Deny from all
Allow from YOUR_IP_ADDRESS
```

`Order Deny,Allow
Deny from all
Allow from YOUR_IP_ADDRESS`

Make sure to replace theYOUR_IP_ADDRESSplaceholder with your own public IP address. You can retrieve and then copy & paste it from free websites likewhatismyip.com

`YOUR_IP_ADDRESS`

If you’re using a managed hosting solution, your provider may offer user-friendly options to enable a ‘maintenance mode’ or a similar setting that blocks all incoming traffic except for specific IP addresses. Check with your hosting provider for specific options they offer to make your site temporarily inaccessible.

#### 2 – Restore a backup in your local environment

1. Choose a backup:Pick one from February 12th, 2024, or earlier (the earlier, the better).
2. Create a local server:To restore your backup locally, you need to set up a local server environment on your computer. You can use software likeLocalWPorDevKinsta, which are specifically designed for WordPress and offer user-friendly interfaces. Alternatively, general-purpose tools like XAMPP or MAMP are also suitable. Choose the one you’re most comfortable with.
3. Restore the backup locally:Import your WordPress files and database into this local setup.

#### 3 – Update the Bricks theme to the latest version

1. Log into your local WordPress:Open your WordPress dashboard on the local site.
2. Update Bricks:Navigate toDashboard > Updatesand apply the update to Bricks version 1.9.6.1.

`Dashboard > Updates`

#### 4 – Re-perform the steps outlined above

1. Go over the stepsabove(“How to check if your WordPress site has been compromised”) again to ensure your backup wasn’t compromised either. And remove all suspicious user accounts, child themes, files, and content.

#### 5 – Reinstall WordPress core, all themes, and plugins

1. Reinstall WordPress:Go toDashboard > Updateand click the “Reinstall version x.x.x” button. This will reinstall your WordPress core files, without affecting your existing content (posts, pages, etc.), configurations, themes, and plugins.
2. Reinstall all plugins:Either update all plugins to their latest version or reinstall all plugins.
3. Reinstall all themes:Either update all themes to their latest version or reinstall all themes.

`Dashboard > Update`

While all of those steps can be done via the CLI for free themes and plugins listed in the WordPress repository, you still need to do this manually for some of your premium plugins. We recommend performing this manually, one by one, to verify that all the latest versions are working on your site as expected. This is also a great chance to revisit which plugins might no longer be needed.

#### 6 – Change sensitive credentials and keys

After ensuring that your site’s files and database are clean, it’s important to address the potential compromise of sensitive information such as API keys, SMTP passwords, and licenses. Attackers may have accessed these and could misuse them, leading to further security issues.

- Update API keys and secrets:Identify all APIs used in your WordPress site, including payment gateways, social media integrations, and other external services.Generate new API keys and secrets for each service.Update these new keys in your WordPress settings or relevant plugin settings.
- Identify all APIs used in your WordPress site, including payment gateways, social media integrations, and other external services.
- Generate new API keys and secrets for each service.
- Update these new keys in your WordPress settings or relevant plugin settings.
- Change SMTP passwords:If using an SMTP service for emails, assume the password is compromised.Change the SMTP password through your email service provider.Update the new SMTP password in your WordPress or email plugin settings.
- If using an SMTP service for emails, assume the password is compromised.
- Change the SMTP password through your email service provider.
- Update the new SMTP password in your WordPress or email plugin settings.
- Update license keys:For premium plugins, themes, or other licensed software, change their license keys.Contact the providers to issue new keys if necessary.Update these keys in your WordPress settings.
- For premium plugins, themes, or other licensed software, change their license keys.
- Contact the providers to issue new keys if necessary.
- Update these keys in your WordPress settings.
- Secure other sensitive data:Review and update any other sensitive data in your WordPress configuration. This includes custom authentication keys or custom credentials.
- Review and update any other sensitive data in your WordPress configuration. This includes custom authentication keys or custom credentials.

- Identify all APIs used in your WordPress site, including payment gateways, social media integrations, and other external services.
- Generate new API keys and secrets for each service.
- Update these new keys in your WordPress settings or relevant plugin settings.

- If using an SMTP service for emails, assume the password is compromised.
- Change the SMTP password through your email service provider.
- Update the new SMTP password in your WordPress or email plugin settings.

- For premium plugins, themes, or other licensed software, change their license keys.
- Contact the providers to issue new keys if necessary.
- Update these keys in your WordPress settings.

- Review and update any other sensitive data in your WordPress configuration. This includes custom authentication keys or custom credentials.

#### 7 – Migrate your local installation to your live environment

When you’re ready to migrate your local WordPress installation to your live environment, it’s important to ensure the site is not accessible to the public during this process. Refer back to1- Block incoming trafficfor methods to temporarily make your site inaccessible, either through editing the.htaccessfile or using options provided by your managed hosting service.

`.htaccess`

1. Fresh Install on Live Server: Start by installing a new instance of WordPress on your live server. This ensures you are working with a clean and secure base.
2. Transfer your site:You can use plugins likeDuplicator,WPVivid, orAll-in-One WP Migrationto move your updated local site to the new live server setup.

#### 8 – Alternative method (for hosts allowing site isolation)

1. Isolate your site:Ask your host to block internet access to your site temporarily.
2. Restore and update on the live server:Directly restore the backup and update Bricks to 1.9.6.1 on the live server before reopening access.

#### Additional steps (important for all scenarios)

1. Run security scans with a plugin like Wordfence:Install Wordfence:In your WordPress dashboard, go toPlugins > Add New. Search for “Wordfence”. Install and activate it.Run a scan:Navigate toWordfence > Scanin your dashboard. Click on “Start a new scan”. Make sure you’re in “High Sensitivity” mode for thorough scanning.Review scan results:After the scan, you’ll get a list of potential threats. Carefully review each item. If you’re unsure about a file, research it or ask for expert advice.Remember:While plugins like Wordfence can sometimes be valuable, they are not infallible since they’re running on the application level. It’s crucial to use them as part of a broader security strategy, including regular manual checks and monitoring for unusual site activity at the server level.
2. Install Wordfence:In your WordPress dashboard, go toPlugins > Add New. Search for “Wordfence”. Install and activate it.
3. Run a scan:Navigate toWordfence > Scanin your dashboard. Click on “Start a new scan”. Make sure you’re in “High Sensitivity” mode for thorough scanning.
4. Review scan results:After the scan, you’ll get a list of potential threats. Carefully review each item. If you’re unsure about a file, research it or ask for expert advice.
5. Remember:While plugins like Wordfence can sometimes be valuable, they are not infallible since they’re running on the application level. It’s crucial to use them as part of a broader security strategy, including regular manual checks and monitoring for unusual site activity at the server level.
6. Scan for malware at the server level:Use hosting provider tools:The best way to scan for malware is at the server level through tools provided by your hosting provider. Plugins can sometimes be tampered with, making them less reliable for thorough security checks.Consult with your provider:Engage with your hosting provider to understand and implement the security features they offer. These tools are generally more integrated with the server’s infrastructure, offering a more robust and comprehensive approach to malware scanning.
7. Use hosting provider tools:The best way to scan for malware is at the server level through tools provided by your hosting provider. Plugins can sometimes be tampered with, making them less reliable for thorough security checks.
8. Consult with your provider:Engage with your hosting provider to understand and implement the security features they offer. These tools are generally more integrated with the server’s infrastructure, offering a more robust and comprehensive approach to malware scanning.
9. Change database password:Access hosting control panel:Log into your web hosting account and go to the database section.Find database settings:Locate the database used by your WordPress site.Change password:Update the password. Ensure it’s strong and unique.Delete the oldwp-config.phpfile:Using FTP or your host’s file manager, access your site’s root directory.Locate the existingwp-config.phpfile and delete it. This is an important step to remove any potentially compromised or unsafe configurations.Start with a freshwp-config.phpfile:Download a freshwp-config.phpsample file from the official WordPress repository:WordPress Repo wp-config-sample.php.Copy and paste the content of this file directly into a new file namedwp-config.php. Alternatively, you may download the file, rename it towp-config.php, and upload it to your site’s root directory.Update newwp-config.php:Open the newwp-config.phpfile.Copy your new database password and paste it into the corresponding line (define( 'DB_PASSWORD', 'new_password' );).Fill in or update other necessary details like database name, user, and host.Note: If you’re using a managed hosting service and are unsure about this process, it’s advisable to contact your hosting provider for assistance. They can offer support and guidance in updating yourwp-config.phpfile.
10. Access hosting control panel:Log into your web hosting account and go to the database section.
11. Find database settings:Locate the database used by your WordPress site.
12. Change password:Update the password. Ensure it’s strong and unique.
13. Delete the oldwp-config.phpfile:Using FTP or your host’s file manager, access your site’s root directory.Locate the existingwp-config.phpfile and delete it. This is an important step to remove any potentially compromised or unsafe configurations.
14. Using FTP or your host’s file manager, access your site’s root directory.
15. Locate the existingwp-config.phpfile and delete it. This is an important step to remove any potentially compromised or unsafe configurations.
16. Start with a freshwp-config.phpfile:Download a freshwp-config.phpsample file from the official WordPress repository:WordPress Repo wp-config-sample.php.Copy and paste the content of this file directly into a new file namedwp-config.php. Alternatively, you may download the file, rename it towp-config.php, and upload it to your site’s root directory.
17. Download a freshwp-config.phpsample file from the official WordPress repository:WordPress Repo wp-config-sample.php.
18. Copy and paste the content of this file directly into a new file namedwp-config.php. Alternatively, you may download the file, rename it towp-config.php, and upload it to your site’s root directory.
19. Update newwp-config.php:Open the newwp-config.phpfile.Copy your new database password and paste it into the corresponding line (define( 'DB_PASSWORD', 'new_password' );).Fill in or update other necessary details like database name, user, and host.
20. Open the newwp-config.phpfile.
21. Copy your new database password and paste it into the corresponding line (define( 'DB_PASSWORD', 'new_password' );).
22. Fill in or update other necessary details like database name, user, and host.
23. Note: If you’re using a managed hosting service and are unsure about this process, it’s advisable to contact your hosting provider for assistance. They can offer support and guidance in updating yourwp-config.phpfile.
24. Reset all user passwords in WordPress:Go to users:In your WordPress dashboard, click onUsers.Edit each user:Click on each user account, especially admins, and set a new password. Use strong passwords.
25. Go to users:In your WordPress dashboard, click onUsers.
26. Edit each user:Click on each user account, especially admins, and set a new password. Use strong passwords.
27. Update security keys inwp-config.php:Access your site files:Use FTP or your host’s file manager to access your site’s root directory.Editwp-config.php: Open thewp-config.phpfile you’ve just created or updated.Generate new keys:VisitWordPress’s Security Key Generator. Copy the generated keys.Replace old keys:Inwp-config.php, find the section with authentication unique keys and salts. Replace them with the new ones you copied.Save changes:After replacing, save and close the file.
28. Access your site files:Use FTP or your host’s file manager to access your site’s root directory.
29. Editwp-config.php: Open thewp-config.phpfile you’ve just created or updated.
30. Generate new keys:VisitWordPress’s Security Key Generator. Copy the generated keys.
31. Replace old keys:Inwp-config.php, find the section with authentication unique keys and salts. Replace them with the new ones you copied.
32. Save changes:After replacing, save and close the file.
33. Check and adjust file permissions:Using FTP:Connect to your site using an FTP client.Navigate to WordPress folders:Look for thewp-admin,wp-includes, andwp-contentdirectories.Set folder permissions:Right-click on each folder and choose ‘File Permissions’. Set the numeric value to 755.Set file permissions:For individual files within these directories, set permissions to 644.
34. Using FTP:Connect to your site using an FTP client.
35. Navigate to WordPress folders:Look for thewp-admin,wp-includes, andwp-contentdirectories.
36. Set folder permissions:Right-click on each folder and choose ‘File Permissions’. Set the numeric value to 755.
37. Set file permissions:For individual files within these directories, set permissions to 644.

- Install Wordfence:In your WordPress dashboard, go toPlugins > Add New. Search for “Wordfence”. Install and activate it.
- Run a scan:Navigate toWordfence > Scanin your dashboard. Click on “Start a new scan”. Make sure you’re in “High Sensitivity” mode for thorough scanning.
- Review scan results:After the scan, you’ll get a list of potential threats. Carefully review each item. If you’re unsure about a file, research it or ask for expert advice.
- Remember:While plugins like Wordfence can sometimes be valuable, they are not infallible since they’re running on the application level. It’s crucial to use them as part of a broader security strategy, including regular manual checks and monitoring for unusual site activity at the server level.

`Plugins > Add New`

`Wordfence > Scan`

- Use hosting provider tools:The best way to scan for malware is at the server level through tools provided by your hosting provider. Plugins can sometimes be tampered with, making them less reliable for thorough security checks.
- Consult with your provider:Engage with your hosting provider to understand and implement the security features they offer. These tools are generally more integrated with the server’s infrastructure, offering a more robust and comprehensive approach to malware scanning.

- Access hosting control panel:Log into your web hosting account and go to the database section.
- Find database settings:Locate the database used by your WordPress site.
- Change password:Update the password. Ensure it’s strong and unique.
- Delete the oldwp-config.phpfile:Using FTP or your host’s file manager, access your site’s root directory.Locate the existingwp-config.phpfile and delete it. This is an important step to remove any potentially compromised or unsafe configurations.
- Using FTP or your host’s file manager, access your site’s root directory.
- Locate the existingwp-config.phpfile and delete it. This is an important step to remove any potentially compromised or unsafe configurations.
- Start with a freshwp-config.phpfile:Download a freshwp-config.phpsample file from the official WordPress repository:WordPress Repo wp-config-sample.php.Copy and paste the content of this file directly into a new file namedwp-config.php. Alternatively, you may download the file, rename it towp-config.php, and upload it to your site’s root directory.
- Download a freshwp-config.phpsample file from the official WordPress repository:WordPress Repo wp-config-sample.php.
- Copy and paste the content of this file directly into a new file namedwp-config.php. Alternatively, you may download the file, rename it towp-config.php, and upload it to your site’s root directory.
- Update newwp-config.php:Open the newwp-config.phpfile.Copy your new database password and paste it into the corresponding line (define( 'DB_PASSWORD', 'new_password' );).Fill in or update other necessary details like database name, user, and host.
- Open the newwp-config.phpfile.
- Copy your new database password and paste it into the corresponding line (define( 'DB_PASSWORD', 'new_password' );).
- Fill in or update other necessary details like database name, user, and host.
- Note: If you’re using a managed hosting service and are unsure about this process, it’s advisable to contact your hosting provider for assistance. They can offer support and guidance in updating yourwp-config.phpfile.

`wp-config.php`

- Using FTP or your host’s file manager, access your site’s root directory.
- Locate the existingwp-config.phpfile and delete it. This is an important step to remove any potentially compromised or unsafe configurations.

`wp-config.php`

`wp-config.php`

- Download a freshwp-config.phpsample file from the official WordPress repository:WordPress Repo wp-config-sample.php.
- Copy and paste the content of this file directly into a new file namedwp-config.php. Alternatively, you may download the file, rename it towp-config.php, and upload it to your site’s root directory.

`wp-config.php`

`wp-config.php`

`wp-config.php`

`wp-config.php`

- Open the newwp-config.phpfile.
- Copy your new database password and paste it into the corresponding line (define( 'DB_PASSWORD', 'new_password' );).
- Fill in or update other necessary details like database name, user, and host.

`wp-config.php`

`define( 'DB_PASSWORD', 'new_password' );`

`wp-config.php`

- Go to users:In your WordPress dashboard, click onUsers.
- Edit each user:Click on each user account, especially admins, and set a new password. Use strong passwords.

`Users`

`wp-config.php`

- Access your site files:Use FTP or your host’s file manager to access your site’s root directory.
- Editwp-config.php: Open thewp-config.phpfile you’ve just created or updated.
- Generate new keys:VisitWordPress’s Security Key Generator. Copy the generated keys.
- Replace old keys:Inwp-config.php, find the section with authentication unique keys and salts. Replace them with the new ones you copied.
- Save changes:After replacing, save and close the file.

`wp-config.php`

`wp-config.php`

`wp-config.php`

- Using FTP:Connect to your site using an FTP client.
- Navigate to WordPress folders:Look for thewp-admin,wp-includes, andwp-contentdirectories.
- Set folder permissions:Right-click on each folder and choose ‘File Permissions’. Set the numeric value to 755.
- Set file permissions:For individual files within these directories, set permissions to 644.

`wp-admin`

`wp-includes`

`wp-content`

While outlining the general steps you can take to check for and address compromises in your WordPress site, it’s important to understand that each site is unique, with different types of attacks and impacts.

Therefore, we recommend also consulting theWordPress Hardening Guide. This technical guide covers advanced security measures. If you’re using a managed hosting service, your provider typically handles many of these security aspects.

However, it’s still beneficial to be aware of these practices, as they provide valuable insights into securing your WordPress environment.

