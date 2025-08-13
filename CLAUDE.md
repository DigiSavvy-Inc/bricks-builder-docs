# Bricks Builder Documentation Scraper

## Overview
This project is a web scraping utility designed to create a comprehensive knowledge base from the Bricks Builder Academy documentation. It systematically downloads and converts documentation pages into structured markdown files for offline access and reference.

## Purpose
- **Documentation Preservation**: Creates an offline searchable copy of Bricks Builder documentation
- **Developer Reference**: Focuses on developer-oriented documentation including filters, actions, and API references
- **Structured Knowledge Base**: Converts HTML documentation into well-organized markdown files with table of contents

## Project Structure
```
bricks-scraper-docs/
├── bricks-academy-page_titles_all.csv   # Source CSV with all documentation URLs
├── scraper.py                           # Main scraping utility
├── knowledge_base/                      # Full documentation scrape output
│   ├── *.md                            # Individual documentation pages
│   ├── summary.md                      # Summary of scraping results
│   └── summary.json                    # JSON summary for programmatic access
├── knowledge_base_dev/                  # Developer-focused documentation subset
│   ├── *.md                            # Developer-oriented pages only
│   ├── summary.md                      # Summary of dev docs scraping
│   └── summary.json                    # JSON summary for dev docs
└── bricks_env/                          # Python virtual environment
```

## Scraping Tool Usage

### Basic Usage
```bash
python scraper.py bricks-academy-page_titles_all.csv
```

### Developer Documentation Only
```bash
python scraper.py bricks-academy-page_titles_all.csv --output knowledge_base_dev --dev-only
```

### Command Line Options
- `csv_path`: Path to CSV file containing URLs (required)
- `--output`: Output directory (default: 'knowledge_base')
- `--delay`: Delay between requests in seconds (default: 1.0)
- `--dev-only`: Filter for developer-oriented documentation only

## Features

### Content Extraction
- Extracts page title, structured content, and full text
- Preserves code blocks with proper markdown formatting
- Creates hierarchical table of contents for each page
- Maintains heading structure and relationships

### Developer Documentation Filtering
When using `--dev-only` flag, the scraper filters for:
- Filter hooks (`filter-bricks-*`)
- Action hooks (`action-bricks-*`)
- Function references (`function-bricks-*`)
- Custom development articles (custom code, JavaScript events, etc.)
- API and developer collections

### Output Format
Each scraped page is saved as a markdown file with:
- YAML frontmatter (title, URL, date, status)
- Source URL reference
- Table of contents with anchor links
- Hierarchically structured content sections
- Preserved code blocks and lists

### Progress Tracking
- Skips already scraped pages to avoid duplicates
- Creates summary reports (both .md and .json)
- Shows success/failure status for each URL
- Progress bar during scraping operation

## CSV Input Format
The CSV file should contain URLs in a column with one of these headers:
- `Address`, `URL`, `Link`, or any column containing 'url', 'link', or 'address'

Example CSV structure:
```csv
Address,Occurrences,Title 1,Title 1 Length,Title 1 Pixel Width,Indexability,Indexability Status
https://academy.bricksbuilder.io/...,1,Page Title,30,282,Indexable,
```

## Implementation Details

### Key Functions
- `scrape_webpage(url, headers)`: Main scraping function that extracts content
- `save_as_markdown(data, filepath)`: Converts scraped data to markdown format
- `create_knowledge_base(csv_path, output_dir, delay, dev_only)`: Orchestrates the scraping process

### Content Processing
1. Removes script and style elements from HTML
2. Identifies main content area (main, article, or content div)
3. Extracts headings and associated content sequentially
4. Preserves code formatting with markdown code blocks
5. Processes lists with proper markdown syntax

### Error Handling
- Timeout protection (30 seconds per request)
- Graceful failure with error logging
- Continues processing remaining URLs on individual failures

## Notes
- Respects server resources with configurable delay between requests
- Creates well-structured, searchable offline documentation
- Particularly useful for developers working with Bricks Builder customizations
- Non-destructive: skips already scraped content to allow incremental updates