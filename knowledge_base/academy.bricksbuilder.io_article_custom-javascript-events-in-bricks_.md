---
title: "Custom JavaScript events in Bricks – Bricks Academy"
url: https://academy.bricksbuilder.io/article/custom-javascript-events-in-bricks/
date: 2025-02-27T15:28:52.659603
status: success
---

# Custom JavaScript events in Bricks – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/custom-javascript-events-in-bricks/](https://academy.bricksbuilder.io/article/custom-javascript-events-in-bricks/)*

## Table of Contents

- [Custom JavaScript events in Bricks](#custom-javascript-events-in-bricks)
  - [Form element events](#form-element-events)
  - [Tabs / Tabs (Nestable) element events](#tabs--tabs-nestable-element-events)
  - [Accordion / Accordion (Nestable) element events](#accordion--accordion-nestable-element-events)
  - [Animation events](#animation-events)
  - [Popup events](#popup-events)
    - [AJAX popup open event sequence](#ajax-popup-open-event-sequence)
  - [Bricks AJAX events](#bricks-ajax-events)
    - [Infinite scroll event sequence](#infinite-scroll-event-sequence)
    - [AJAX pagination event sequence](#ajax-pagination-event-sequence)
    - [AJAX filter event sequence](#ajax-filter-event-sequence)
        - [How to add a custom animation in interaction](#how-to-add-a-custom-animation-in-interaction)

## Custom JavaScript events in Bricks

Bricks offers a range of custom JavaScript events that you can leverage to enhance the functionality and interactivity of your website. These events allow you to respond to specific actions or changes within your Bricks-powered site. Let’s explore the custom events available in Bricks:

### Form element events

- bricks/form/submitEmitted before an AJAX call for form submission is made.
- bricks/form/successEmitted after a successful form submission AJAX call is returned.
- bricks/form/errorEmitted after an error in the form submission AJAX call is returned.

### Tabs / Tabs (Nestable) element events

- bricks/tabs/changed: Emitted after click on a tab title (@since 1.9.8)

`@since 1.9.8`

```
// Listen for the 'bricks/tabs/changed' event
document.addEventListener('bricks/tabs/changed', (event) => {
  // Extract information from the event detail
  const { elementId, activeIndex, activeTitle, activePane } = event.detail;
  
  // Only target elementID lwxvfh
  if( elementId !== 'lwxvfh' ) {
    return;
  } 

  // Example: Log the details to the console
  console.log(`Tabs Changed - Element ID: ${elementId}, Active Index: ${activeIndex}, Active Title: ${activeTitle}, Active Pane: ${activePane}`);

  // Your custom logic here
  // For example, update the UI based on the tab change
});
```

`// Listen for the 'bricks/tabs/changed' event
document.addEventListener('bricks/tabs/changed', (event) => {
  // Extract information from the event detail
  const { elementId, activeIndex, activeTitle, activePane } = event.detail;
  
  // Only target elementID lwxvfh
  if( elementId !== 'lwxvfh' ) {
    return;
  } 

  // Example: Log the details to the console
  console.log(`Tabs Changed - Element ID: ${elementId}, Active Index: ${activeIndex}, Active Title: ${activeTitle}, Active Pane: ${activePane}`);

  // Your custom logic here
  // For example, update the UI based on the tab change
});`

### Accordion / Accordion (Nestable) element events

- bricks/accordion/open: Emitted after an accordion item is opened/expanded via click action (@since 1.9.8)
- bricks/accordion/close: Emitted after an accordion item is closed/collapsed via click action (@since 1.9.8)

`@since 1.9.8`

`@since 1.9.8`

```
// Listen for the 'bricks/accordion/open' event
document.addEventListener('bricks/accordion/open', (event) => {
  // Extract information from the event detail
  const { elementId, openItem } = event.detail;

  // Only target elementID qwe3th
  if( elementId !== 'qwe3th' ) {
    return;
  } 

  // Example: Log the details to the console
  console.log(`Accordion Opened - Element ID: ${elementId}, Open Item ID: ${openItem}`);

  // Your custom logic here
  // For example, update the UI based on the accordion item being opened
});

```

`// Listen for the 'bricks/accordion/open' event
document.addEventListener('bricks/accordion/open', (event) => {
  // Extract information from the event detail
  const { elementId, openItem } = event.detail;

  // Only target elementID qwe3th
  if( elementId !== 'qwe3th' ) {
    return;
  } 

  // Example: Log the details to the console
  console.log(`Accordion Opened - Element ID: ${elementId}, Open Item ID: ${openItem}`);

  // Your custom logic here
  // For example, update the UI based on the accordion item being opened
});
`

```
// Listen for the 'bricks/accordion/close' event
document.addEventListener('bricks/accordion/close', (event) => {
  // Extract information from the event detail
  const { elementId, closeItem } = event.detail;

  // Only target elementID qwe3th
  if( elementId !== 'qwe3th' ) {
    return;
  } 

  // Example: Log the details to the console
  console.log(`Accordion Closed - Element ID: ${elementId}, Closed Item ID: ${closeItem}`);

  // Your custom logic here
  // For example, update the UI based on the accordion item being closed
});
```

`// Listen for the 'bricks/accordion/close' event
document.addEventListener('bricks/accordion/close', (event) => {
  // Extract information from the event detail
  const { elementId, closeItem } = event.detail;

  // Only target elementID qwe3th
  if( elementId !== 'qwe3th' ) {
    return;
  } 

  // Example: Log the details to the console
  console.log(`Accordion Closed - Element ID: ${elementId}, Closed Item ID: ${closeItem}`);

  // Your custom logic here
  // For example, update the UI based on the accordion item being closed
});`

### Animation events

- bricks/animation/end/{animationId}: Emitted when a specified animation (identified by {animationId}) completes its playback.

### Popup events

- bricks/popup/openEmitted after popup opened.
- bricks/popup/closeEmitted after popup closed.
- bricks/ajax/popup/startEmitted before making an AJAX popup call.
- bricks/ajax/popup/endEmitted after completing an AJAX popup call.
- bricks/ajax/popup/loadedEmitted after adding AJAX popup content to the DOM.

#### AJAX popup open event sequence

1. bricks/ajax/popup/start
2. bricks/ajax/popup/end
3. bricks/ajax/popup/loaded
4. bricks/popup/open

### Bricks AJAX events

Bricks AJAX = Infinite Scroll, Load More, AJAX Pagination, or Query Filter.

- bricks/ajax/start: Emitted before a Bricks AJAX call is made.
- bricks/ajax/end: Emitted after completing a Bricks AJAX call.
- bricks/ajax/pagination/completed: Emitted after an AJAX pagination call is completed.
- bricks/ajax/load_page/completed: Emitted after an Infinite scroll AJAX call is completed.
- bricks/ajax/query_result/completed: Emitted after a Query filter AJAX call is completed.
- bricks/ajax/query_result/displayed: Emitted after adding all filtered results to the DOM.

#### Infinite scroll event sequence

1. bricks/ajax/start
2. bricks/ajax/end
3. bricks/ajax/load_page/completed

#### AJAX pagination event sequence

1. bricks/ajax/start
2. bricks/ajax/end
3. bricks/ajax/pagination/completed

#### AJAX filter event sequence

1. bricks/ajax/start
2. bricks/ajax/end
3. bricks/ajax/query_result/completed
4. bricks/ajax/query_result/displayed

```
document.addEventListener('bricks/ajax/start', (event) => {
  // Get the queryId from the event
  const queryId = event.detail.queryId || false;

  if (!queryId) {
    return;
  }

  // Your custom logic here
  // For example, initiate a loader or update UI to indicate AJAX request start
});
```

`document.addEventListener('bricks/ajax/start', (event) => {
  // Get the queryId from the event
  const queryId = event.detail.queryId || false;

  if (!queryId) {
    return;
  }

  // Your custom logic here
  // For example, initiate a loader or update UI to indicate AJAX request start
});`

```
document.addEventListener('bricks/ajax/end', (event) => {
  // Get the queryId from the event
  const queryId = event.detail.queryId || false;

  if (!queryId) {
    return;
  }

  // Your custom logic here
  // For example, initiate a loader or update UI to indicate AJAX request end
});
```

`document.addEventListener('bricks/ajax/end', (event) => {
  // Get the queryId from the event
  const queryId = event.detail.queryId || false;

  if (!queryId) {
    return;
  }

  // Your custom logic here
  // For example, initiate a loader or update UI to indicate AJAX request end
});`

```
document.addEventListener('bricks/ajax/pagination/completed', (event) => {
  // Extract queryId from the event detail
  const queryId = event.detail.queryId;

  // Your custom logic here
  // For example, handle the completed pagination for the specific queryId
});
```

`document.addEventListener('bricks/ajax/pagination/completed', (event) => {
  // Extract queryId from the event detail
  const queryId = event.detail.queryId;

  // Your custom logic here
  // For example, handle the completed pagination for the specific queryId
});`

```
document.addEventListener('bricks/ajax/load_page/completed', (event) => {
  // Extract information from the event detail
  const { queryTrailElement, queryId } = event.detail;

  // Your custom logic here
  // For example, handle the completed AJAX page load for the specific queryId and queryTrailElement
});
```

`document.addEventListener('bricks/ajax/load_page/completed', (event) => {
  // Extract information from the event detail
  const { queryTrailElement, queryId } = event.detail;

  // Your custom logic here
  // For example, handle the completed AJAX page load for the specific queryId and queryTrailElement
});`

```
document.addEventListener('bricks/ajax/query_result/completed', (event) => {
  // Extract information from the event detail
  const queryId = event.detail.queryId;

  // Your custom logic here
});
```

`document.addEventListener('bricks/ajax/query_result/completed', (event) => {
  // Extract information from the event detail
  const queryId = event.detail.queryId;

  // Your custom logic here
});`

```
document.addEventListener('bricks/ajax/query_result/displayed', (event) => {
  // Extract information from the event detail
  const queryId = event.detail.queryId;

  // Your custom logic here
});
```

`document.addEventListener('bricks/ajax/query_result/displayed', (event) => {
  // Extract information from the event detail
  const queryId = event.detail.queryId;

  // Your custom logic here
});`

###### How to add a custom animation in interaction

