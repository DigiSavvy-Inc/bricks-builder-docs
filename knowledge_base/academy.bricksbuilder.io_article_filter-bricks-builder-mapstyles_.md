---
title: "Filter: bricks/builder/map_styles – Bricks Academy"
url: https://academy.bricksbuilder.io/article/filter-bricks-builder-mapstyles/
date: 2025-02-27T15:29:46.726671
status: success
---

# Filter: bricks/builder/map_styles – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/filter-bricks-builder-mapstyles/](https://academy.bricksbuilder.io/article/filter-bricks-builder-mapstyles/)*

## Table of Contents

- [Filter: bricks/builder/map_styles](#filter-bricksbuildermapstyles)
        - [Filter: bricks/builder/i18n](#filter-bricksbuilderi18n)
        - [Filter: bricks/builder/save_messages](#filter-bricksbuildersavemessages)

## Filter: bricks/builder/map_styles

This filter allows you to define your own custom map styles for theMapelement.

The example below shows how we added a custom map style fromhttps://snazzymaps.com/style/38/shades-of-greyto the builder.

The best resource for professional predefined map styles is available underhttps://snazzymaps.com/explore. Open any map style and copy&paste the code under “JAVASCRIPT STYLE ARRAY” as shown in the example below.

```
add_filter( 'bricks/builder/map_styles', function( $map_styles ) {
  // Example: Custom map style from: https://snazzymaps.com/style/38/shades-of-grey
  $map_styles['shadesOfGrey'] = [
    'label' => esc_html__( 'Shades of grey', 'bricks' ),
    'style' => '[ { "featureType": "all", "elementType": "labels.text.fill", "stylers": [ { "saturation": 36 }, { "color": "#000000" }, { "lightness": 40 } ] }, { "featureType": "all", "elementType": "labels.text.stroke", "stylers": [ { "visibility": "on" }, { "color": "#000000" }, { "lightness": 16 } ] }, { "featureType": "all", "elementType": "labels.icon", "stylers": [ { "visibility": "off" } ] }, { "featureType": "administrative", "elementType": "geometry.fill", "stylers": [ { "color": "#000000" }, { "lightness": 20 } ] }, { "featureType": "administrative", "elementType": "geometry.stroke", "stylers": [ { "color": "#000000" }, { "lightness": 17 }, { "weight": 1.2 } ] }, { "featureType": "landscape", "elementType": "geometry", "stylers": [ { "color": "#000000" }, { "lightness": 20 } ] }, { "featureType": "poi", "elementType": "geometry", "stylers": [ { "color": "#000000" }, { "lightness": 21 } ] }, { "featureType": "road.highway", "elementType": "geometry.fill", "stylers": [ { "color": "#000000" }, { "lightness": 17 } ] }, { "featureType": "road.highway", "elementType": "geometry.stroke", "stylers": [ { "color": "#000000" }, { "lightness": 29 }, { "weight": 0.2 } ] }, { "featureType": "road.arterial", "elementType": "geometry", "stylers": [ { "color": "#000000" }, { "lightness": 18 } ] }, { "featureType": "road.local", "elementType": "geometry", "stylers": [ { "color": "#000000" }, { "lightness": 16 } ] }, { "featureType": "transit", "elementType": "geometry", "stylers": [ { "color": "#000000" }, { "lightness": 19 } ] }, { "featureType": "water", "elementType": "geometry", "stylers": [ { "color": "#000000" }, { "lightness": 17 } ] } ]'
];

  return $map_styles;
} );
```

###### Filter: bricks/builder/i18n

###### Filter: bricks/builder/save_messages

