<!-- @format -->

# Bricks Builder Documentation

This repository is a proof of concept (POC) for hosting Bricks Builder documentation on GitHub, making it more accessible to users and developers using AI-enhanced tooling.

## Purpose

This repository demonstrates how Bricks Builder documentation can benefit from being hosted on GitHub, either as a primary repository or as a mirrored version of the existing documentation. While this wouldn't necessarily replace the current documentation system, it provides significant additional value in today's AI-enhanced development environment.

## Key Benefits

- **Enhanced AI Integration**: Today's developers increasingly leverage Large Language Model (LLM) tools like ChatGPT and Claude to streamline their workflows. These AI assistants can directly connect to GitHub repositories through Model Context Protocol (MCP) and similar technologies, allowing developers to have interactive conversations about codebases and documentation stored here.

- **Unified Developer Experience**: By having both code and documentation in the same ecosystem, developers can maintain context while switching between implementation details and documentation guidance, creating a more seamless development experience.

- **Community Contributions**: GitHub's established contribution workflow (issues, pull requests, discussions) enables the community to more easily suggest improvements, corrections, or expansions to documentation, potentially increasing both quality and coverage.

- **Version Control and History**: Documentation changes are tracked with the same robust version control that GitHub provides for code, making it easier to understand how documentation has evolved alongside the software.

## Repository Structure

The documentation is organized into focused directories for different types of content. For a comprehensive overview, see the [Documentation Index](/docs/index.md):

| Directory | Description | Contents |
|-----------|-------------|----------|
| [`docs/actions/`](/docs/actions/) | WordPress action hooks | Documentation for Bricks action hooks |
| [`docs/articles/`](/docs/articles/) | General articles | Core documentation organized by topic |
| [`docs/customization/`](/docs/customization/) | Customization guides | How to customize Bricks functionality |
| [`docs/developer/`](/docs/developer/) | Developer documentation | Creating custom elements and features |
| [`docs/filters/`](/docs/filters/) | WordPress filter hooks | Documentation for Bricks filter hooks |
| [`docs/integrations/`](/docs/integrations/) | Third-party integrations | WPML, Polylang, and other integrations |
| [`docs/security/`](/docs/security/) | Security documentation | Security best practices and considerations |
| [`docs/tools/`](/docs/tools/) | CLI and other tools | Bricks CLI and other development tools |
| [`docs/topics/`](/docs/topics/) | Topic overviews | High-level topic documentation |
| [`docs/tutorials/`](/docs/tutorials/) | How-to guides | Step-by-step guides for common tasks |

Within the `articles` directory, content is further organized into subdirectories:

```
docs/articles/
├── getting-started/  # Installation, setup and core concepts
├── features/         # Bricks Builder features
├── controls/         # Control types and usage
├── elements/         # Element documentation
├── templates/        # Template system
└── woocommerce/      # WooCommerce integration
```

## Documentation Categories

### User Documentation

- **Getting Started**: Installation, requirements, builder introduction, and basic concepts
- **Features**: Dynamic data, interactions, global classes, layouts, and more feature documentation
- **Templates**: Template creation, settings, library, and template conditions
- **WooCommerce**: Integration with WooCommerce, product templates, checkout customization

### Developer Documentation

- **Actions**: WordPress action hooks for running code at specific points
- **Controls**: Documentation for all control types (color, text, image, etc.)
- **Customization**: Guides for customizing Bricks functionality
- **Developer**: Documentation for extending Bricks with custom elements and features
- **Elements**: Element documentation, custom elements, and element conditions
- **Filters**: WordPress filter hooks for modifying Bricks functionality
- **Integrations**: Guides for third-party integrations
- **Security**: Security best practices and considerations
- **Tools**: CLI and other development tools
- **Tutorials**: Step-by-step guides for common tasks

## Important Note

This is a proof of concept, not the final implementation. It serves as a demonstration of how GitHub-hosted documentation can enhance the developer experience, particularly for those using AI assistants in their workflow.

## Attribution

Created by Alex Vasquez, [Digisavvy.com](https://digisavvy.com)  
Twitter: [@alexjvasquez](https://twitter.com/alexjvasquez)
