---
title: "Action: bricks/query/after_loop – Bricks Academy"
url: https://academy.bricksbuilder.io/article/action-bricks-query-after_loop/
date: 2026-01-05T11:08:33.738842
status: success
---

# Action: bricks/query/after_loop – Bricks Academy

*Source: [https://academy.bricksbuilder.io/article/action-bricks-query-after_loop/](https://academy.bricksbuilder.io/article/action-bricks-query-after_loop/)*

## Table of Contents

- [Action: bricks/query/after_loop](#action-bricksqueryafterloop)
        - [Action: bricks/query/before_loop](#action-bricksquerybeforeloop)
        - [Action: bricks/generate_css_file](#action-bricksgeneratecssfile)

## Action: bricks/query/after_loop

If you are creating a custom query loop or a custom plugin, you might want to perform some additional tasks like setting/resetting specific data after the loop runs. (@since 1.7.2)

`@since 1.7.2`

```
// Perform certain action after the loop of query element oklvcq
add_action( 'bricks/query/after_loop', function( $query, $args ) {
  if ( $query->element_id !== 'oklvcq' ) {
    return;
  }
  // $args is an array of the element settings
  // Perform your own logic here

}, 10, 2 );
```

`// Perform certain action after the loop of query element oklvcq
add_action( 'bricks/query/after_loop', function( $query, $args ) {
  if ( $query->element_id !== 'oklvcq' ) {
    return;
  }
  // $args is an array of the element settings
  // Perform your own logic here

}, 10, 2 );`

###### Action: bricks/query/before_loop

###### Action: bricks/generate_css_file

