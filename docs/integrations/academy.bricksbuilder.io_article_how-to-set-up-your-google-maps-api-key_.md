---
title: "How to set up your Google Maps API key – Bricks Academy"
url: https://academy.bricksbuilder.io/article/how-to-set-up-your-google-maps-api-key/
date: 2026-01-05T11:09:02.669975
status: success
---

# How to set up your Google Maps API key – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/how-to-set-up-your-google-maps-api-key/](https://academy.bricksbuilder.io/article/how-to-set-up-your-google-maps-api-key/)*

## Table of Contents

- [How to set up your Google Maps API key](#how-to-set-up-your-google-maps-api-key)
  - [Prerequisites](#prerequisites)
  - [API and application restrictions](#api-and-application-restrictions)
    - [Application restrictions](#application-restrictions)
    - [API Restrictions](#api-restrictions)
  - [Common problems](#common-problems)
        - [Maintenance Mode](#maintenance-mode)
        - [Query Sort, Filter & Live Search](#query-sort-filter--live-search)

## How to set up your Google Maps API key

Thanks to theMapelement, adding a Google Map to Bricks is easy. The biggest hurdle is creating the Google Maps API key. This article will show you how to create an API key and how to prevent unauthorized use by setting API and application restrictions.

`Map`

SinceBricks 1.10.2, Google Maps can be used without an API key through the Embed API, which is very limited by Google. It only allows for one address, zoom level, and map type. For more options, you have to use an API key.

### Prerequisites

Before you start using the Maps JavaScript API, you need a project with abilling account,and theMaps JavaScript APIandGeocoding APIenabled. Check out theGoogle documentationon how to do so.

As soon as you have completed the setup, you will find your API key underKeys and Credentials » API Keys.

Copy and paste the key intoBricks » Settings » API keys » Google Maps: API keyand hit save.

Now, you can use the “Map” element on any page. If your map doesn’t show properly, inspect the developer console for more information.

### API and application restrictions

We recommend restricting where and for which APIs the API key can be used to prevent unauthorized use.

#### Application restrictions

Since you’re running a website, restrict the API key for websites only. Select “Websites” and add your URL by clicking the “Add” button. Here are some examples of URLs that you can allow to set up a website:

- Any URL in a single domain with no subdomains: https://example.com
- Any URL in a single subdomain: https://sub.example.com
- Any subdomain in a single domain, using a wildcard asterisk (*): https://*.example.com
- A domain and all its subdomains, using a wildcard asterisk (*):https://example.comhttps://*.example.com

#### API Restrictions

Restrict key» Select APIs and enable theMaps JavaScript APIandGeocoding API.

Save your API key settings.

### Common problems

If the map is not showing, open the developer console. You will receive further information and how to solve your specific issue there. In most cases, no billing account is assigned, the necessary APIs are not activated, or the restrictions are incorrect.

###### Maintenance Mode

###### Query Sort, Filter & Live Search

