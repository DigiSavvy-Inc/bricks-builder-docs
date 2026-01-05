---
title: "Action: bricks/query/before_loop – Bricks Academy"
url: https://academy.bricksbuilder.io/article/action-bricks-query-before_loop/
date: 2026-01-05T11:07:33.204378
status: success
---

# Action: bricks/query/before_loop – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/action-bricks-query-before_loop/](https://academy.bricksbuilder.io/article/action-bricks-query-before_loop/)*

## Table of Contents

- [Action: bricks/query/before_loop](#action-bricksquerybeforeloop)
        - [Action: bricks/query/after_loop](#action-bricksqueryafterloop)

## Action: bricks/query/before_loop

If you are creating a custom query loop or a custom plugin, you might want to perform some additional tasks like setting/resetting specific data before the loop runs. (@since 1.7.2)

`@since 1.7.2`

```
// Perform certain action before the loop of query element oklvcq
add_action( 'bricks/query/before_loop', function( $query, $args ) {
  if ( $query->element_id !== 'oklvcq' ) {
    return;
  }
  // $args is an array of the element settings
  // Perform your own logic here

}, 10, 2 );
```

`// Perform certain action before the loop of query element oklvcq
add_action( 'bricks/query/before_loop', function( $query, $args ) {
  if ( $query->element_id !== 'oklvcq' ) {
    return;
  }
  // $args is an array of the element settings
  // Perform your own logic here

}, 10, 2 );`

###### Action: bricks/query/after_loop

