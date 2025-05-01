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

The documentation is organized as follows:

```
/
├── docs/
│   ├── articles/
│   │   ├── actions/      # Documentation for Bricks actions
│   │   ├── filters/      # Documentation for Bricks filters
│   │   ├── custom/       # Custom implementation guides
│   │   └── guides/       # How-to guides and tutorials
│   ├── topics/           # Topic overview pages
│   ├── summary.md        # Documentation summary
│   └── summary.json      # Documentation metadata
├── .gitignore
└── README.md
```

## Content

This repository contains Bricks Builder documentation files, primarily focused on developer resources including:

- Actions
- Filters
- Hooks
- Customization guides
- API documentation

## Important Note

This is a proof of concept, not the final implementation. It serves as a demonstration of how GitHub-hosted documentation can enhance the developer experience, particularly for those using AI assistants in their workflow.

## Attribution

Created by Alex Vasquez, [Digisavvy.com](https://digisavvy.com)  
Twitter: [@alexjvasquez](https://twitter.com/alexjvasquez)
