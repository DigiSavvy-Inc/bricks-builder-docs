#!/bin/bash

# Create directories if they don't exist
mkdir -p docs/articles/getting-started
mkdir -p docs/articles/features
mkdir -p docs/articles/woocommerce
mkdir -p docs/articles/templates
mkdir -p docs/articles/controls
mkdir -p docs/articles/elements

# Move files to appropriate directories
# Getting Started files
mv docs/articles/academy.bricksbuilder.io_article_installation-activation_.md docs/articles/getting-started/ 2>/dev/null
mv docs/articles/academy.bricksbuilder.io_article_requirements_.md docs/articles/getting-started/ 2>/dev/null
mv docs/articles/academy.bricksbuilder.io_article_builder-intro_.md docs/articles/getting-started/ 2>/dev/null
mv docs/articles/academy.bricksbuilder.io_article_best-practices_.md docs/articles/getting-started/ 2>/dev/null
mv docs/articles/academy.bricksbuilder.io_article_editing-with-bricks_.md docs/articles/getting-started/ 2>/dev/null
mv docs/articles/academy.bricksbuilder.io_article_save-publish_.md docs/articles/getting-started/ 2>/dev/null
mv docs/articles/academy.bricksbuilder.io_article_revisions_.md docs/articles/getting-started/ 2>/dev/null
mv docs/articles/academy.bricksbuilder.io_article_settings_.md docs/articles/getting-started/ 2>/dev/null
mv docs/articles/academy.bricksbuilder.io_article_responsive-editing_.md docs/articles/getting-started/ 2>/dev/null
mv docs/articles/academy.bricksbuilder.io_article_editing-elements_.md docs/articles/getting-started/ 2>/dev/null
mv docs/articles/academy.bricksbuilder.io_article_theme-styles_.md docs/articles/getting-started/ 2>/dev/null
mv docs/articles/academy.bricksbuilder.io_article_page-settings_.md docs/articles/getting-started/ 2>/dev/null
mv docs/articles/academy.bricksbuilder.io_article_layout_.md docs/articles/getting-started/ 2>/dev/null
mv docs/articles/academy.bricksbuilder.io_article_gutenberg_.md docs/articles/getting-started/ 2>/dev/null
mv docs/articles/academy.bricksbuilder.io_article_builder-mode_.md docs/articles/getting-started/ 2>/dev/null
mv docs/articles/academy.bricksbuilder.io_article_known-issues_.md docs/articles/getting-started/ 2>/dev/null

# WooCommerce files
mv docs/articles/academy.bricksbuilder.io_article_woocommerce-*.md docs/articles/woocommerce/ 2>/dev/null
mv docs/articles/academy.bricksbuilder.io_article_product-*.md docs/articles/woocommerce/ 2>/dev/null
mv docs/articles/academy.bricksbuilder.io_article_cart_.md docs/articles/woocommerce/ 2>/dev/null
mv docs/articles/academy.bricksbuilder.io_article_checkout_.md docs/articles/woocommerce/ 2>/dev/null
mv docs/articles/academy.bricksbuilder.io_article_creating-dynamic-woocommerce-*.md docs/articles/woocommerce/ 2>/dev/null
mv docs/articles/academy.bricksbuilder.io_article_element-checkout-*.md docs/articles/woocommerce/ 2>/dev/null

# Templates files
mv docs/articles/academy.bricksbuilder.io_article_template-*.md docs/articles/templates/ 2>/dev/null
mv docs/articles/academy.bricksbuilder.io_article_an-intro-to-templates_.md docs/articles/templates/ 2>/dev/null
mv docs/articles/academy.bricksbuilder.io_article_create-template_.md docs/articles/templates/ 2>/dev/null
mv docs/articles/academy.bricksbuilder.io_article_remote-templates_.md docs/articles/templates/ 2>/dev/null
mv docs/articles/academy.bricksbuilder.io_article_filter-bricks-active_templates_.md docs/articles/templates/ 2>/dev/null
mv docs/articles/academy.bricksbuilder.io_article_password-protection_.md docs/articles/templates/ 2>/dev/null

# Move controls (most are already in the right directory)
mv docs/articles/academy.bricksbuilder.io_article_*-control_.md docs/articles/controls/ 2>/dev/null

# Move elements
for f in docs/articles/academy.bricksbuilder.io_article_*-element_.md; do
  if [ -f "$f" ]; then
    mv "$f" docs/articles/elements/ 2>/dev/null
  fi
done

# Move remaining topics to features folder that match common feature terms
mv docs/articles/academy.bricksbuilder.io_article_accessibility_.md docs/articles/features/ 2>/dev/null
mv docs/articles/academy.bricksbuilder.io_article_adobe-fonts_.md docs/articles/features/ 2>/dev/null
mv docs/articles/academy.bricksbuilder.io_article_asset-loading_.md docs/articles/features/ 2>/dev/null
mv docs/articles/academy.bricksbuilder.io_article_cascade-layer_.md docs/articles/features/ 2>/dev/null
mv docs/articles/academy.bricksbuilder.io_article_components_.md docs/articles/features/ 2>/dev/null
mv docs/articles/academy.bricksbuilder.io_article_contextual-spacing_.md docs/articles/features/ 2>/dev/null
mv docs/articles/academy.bricksbuilder.io_article_converter_.md docs/articles/features/ 2>/dev/null
mv docs/articles/academy.bricksbuilder.io_article_css-grid-layout_.md docs/articles/features/ 2>/dev/null
mv docs/articles/academy.bricksbuilder.io_article_dynamic-data_.md docs/articles/features/ 2>/dev/null
mv docs/articles/academy.bricksbuilder.io_article_element-conditions_.md docs/articles/features/ 2>/dev/null
mv docs/articles/academy.bricksbuilder.io_article_global-*.md docs/articles/features/ 2>/dev/null
mv docs/articles/academy.bricksbuilder.io_article_gradients-overlays_.md docs/articles/features/ 2>/dev/null
mv docs/articles/academy.bricksbuilder.io_article_hover-styles_.md docs/articles/features/ 2>/dev/null
mv docs/articles/academy.bricksbuilder.io_article_interactions_.md docs/articles/features/ 2>/dev/null
mv docs/articles/academy.bricksbuilder.io_article_keyboard-shortcuts_.md docs/articles/features/ 2>/dev/null
mv docs/articles/academy.bricksbuilder.io_article_masonry-layout_.md docs/articles/features/ 2>/dev/null
mv docs/articles/academy.bricksbuilder.io_article_menu-builder_.md docs/articles/features/ 2>/dev/null
mv docs/articles/academy.bricksbuilder.io_article_nestable-*.md docs/articles/features/ 2>/dev/null
mv docs/articles/academy.bricksbuilder.io_article_popup-builder_.md docs/articles/features/ 2>/dev/null
mv docs/articles/academy.bricksbuilder.io_article_pseudo-classes_.md docs/articles/features/ 2>/dev/null
mv docs/articles/academy.bricksbuilder.io_article_query-*.md docs/articles/features/ 2>/dev/null
mv docs/articles/academy.bricksbuilder.io_article_scroll-snap_.md docs/articles/features/ 2>/dev/null
mv docs/articles/academy.bricksbuilder.io_article_shape-dividers_.md docs/articles/features/ 2>/dev/null
mv docs/articles/academy.bricksbuilder.io_article_sidebars_.md docs/articles/features/ 2>/dev/null
mv docs/articles/academy.bricksbuilder.io_article_svg-uploads_.md docs/articles/features/ 2>/dev/null
mv docs/articles/academy.bricksbuilder.io_article_unsplash_.md docs/articles/features/ 2>/dev/null
mv docs/articles/academy.bricksbuilder.io_article_visual-grid-builder_.md docs/articles/features/ 2>/dev/null

echo "Files have been categorized into appropriate directories."