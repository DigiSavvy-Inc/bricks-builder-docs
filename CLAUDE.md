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
├── CLAUDE.md                            # This documentation file
├── README.md                            # Repository overview and benefits
├── .gitignore                           # Git ignore configuration
├── docs/                                # Organized documentation output
│   ├── actions/                        # WordPress action hooks
│   ├── articles/                       # General documentation articles
│   ├── customization/                  # Customization guides
│   ├── developer/                      # Developer documentation
│   ├── filters/                        # WordPress filter hooks
│   ├── integrations/                   # Third-party integrations
│   ├── security/                       # Security documentation
│   ├── tools/                          # CLI and development tools
│   ├── topics/                         # Topic overviews
│   ├── tutorials/                      # How-to guides
│   ├── index.md                        # Documentation index
│   ├── summary.md                      # Scraping summary report
│   └── summary.json                    # JSON summary for programmatic access
└── bricks_env/                          # Python virtual environment
```

## Scraping Tool Usage

### Basic Usage
```bash
# Activate virtual environment
source bricks_env/bin/activate

# Scrape all documentation to /docs
python scraper.py bricks-academy-page_titles_all.csv

# Or specify custom output directory
python scraper.py bricks-academy-page_titles_all.csv --output docs
```

### Developer Documentation Only
```bash
python scraper.py bricks-academy-page_titles_all.csv --dev-only
```

### Command Line Options
- `csv_path`: Path to CSV file containing URLs (required)
- `--output`: Output directory (default: 'docs')
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

## Documentation Update Strategy

### Regular Updates
To keep the documentation current with Bricks Builder Academy updates, follow this maintenance strategy:

#### 1. Discovering New Documentation
**Manual Check (Weekly/Monthly)**
- Visit https://academy.bricksbuilder.io periodically
- Check their changelog or news section for new articles
- Monitor Bricks Builder release notes for documentation updates

**Automated Discovery Options**
- Export a fresh sitemap or page list from the Academy site
- Use a web scraping tool to generate an updated CSV of all URLs
- Compare with existing `bricks-academy-page_titles_all.csv` to find new pages

#### 2. Updating the CSV Source
```bash
# If you have a new export of URLs, update the CSV:
cp new_export.csv bricks-academy-page_titles_all.csv

# Or manually add new URLs to the existing CSV
echo "https://academy.bricksbuilder.io/article/new-feature/,1,New Feature Title,..." >> bricks-academy-page_titles_all.csv
```

#### 3. Incremental Scraping
The scraper automatically skips existing files, making updates efficient:
```bash
# Activate environment
source bricks_env/bin/activate

# Run scraper - it will only fetch new/missing pages
python scraper.py bricks-academy-page_titles_all.csv

# The scraper will:
# - Skip all existing documentation files
# - Only download new pages
# - Automatically categorize them into the correct /docs subdirectory
# - Update summary.md and summary.json with the latest stats
```

#### 4. Handling Updated Content
For pages that have been updated (not new):
```bash
# Remove the specific file to force re-scraping
rm docs/articles/academy.bricksbuilder.io_article_specific-page_.md

# Or remove multiple files that need updating
rm docs/filters/academy.bricksbuilder.io_article_filter-bricks-*.md

# Run scraper to fetch fresh versions
python scraper.py bricks-academy-page_titles_all.csv
```

#### 5. Version Control Best Practices
```bash
# Before updating, create a branch
git checkout -b docs-update-$(date +%Y%m%d)

# Run the scraper
python scraper.py bricks-academy-page_titles_all.csv

# Review changes
git status
git diff docs/

# Commit updates with descriptive message
git add -A
git commit -m "docs: Update Bricks Academy documentation $(date +%Y-%m-%d)

- Added X new articles
- Updated Y existing pages
- New filters/actions documented: [list key ones]"

# Push and create PR
git push origin docs-update-$(date +%Y%m%d)
```

### Monitoring Documentation Health

#### Quality Checks
1. **Broken Links**: Periodically check for 404s in scraped content
2. **Missing Categories**: Review uncategorized docs in `/docs/articles`
3. **Duplicates**: Check for duplicate content across categories

#### Automated Validation Script
Consider creating a validation script that:
```python
# validate_docs.py example structure
def validate_documentation():
    # Check all files have proper frontmatter
    # Verify no broken internal links
    # Ensure consistent formatting
    # Flag documents that may need recategorization
    # Generate health report
```

### Documentation Categories

The scraper automatically categorizes based on URL patterns:

| Pattern | Category | Example |
|---------|----------|---------|
| `filter-bricks-*` | `/docs/filters/` | Filter hooks documentation |
| `action-bricks-*` | `/docs/actions/` | Action hooks documentation |
| `function-bricks-*` | `/docs/developer/` | Function references |
| `/topic/` | `/docs/topics/` | Topic overviews |
| `custom-`, `create-your-own` | `/docs/customization/` | Customization guides |
| `wpml`, `polylang`, etc. | `/docs/integrations/` | Third-party integrations |
| `how-to-*` | `/docs/tutorials/` | Step-by-step guides |
| `woocommerce`, `cart`, `checkout` | `/docs/tutorials/` | WooCommerce guides |
| Default | `/docs/articles/` | General documentation |

To add new categorization rules, update the `categorize_doc()` function in `scraper.py`.

### Troubleshooting Common Issues

#### Issue: Scraper Fails on Specific Pages
```bash
# Check specific URL manually
curl -I https://academy.bricksbuilder.io/article/problematic-page/

# Run scraper with increased timeout
python scraper.py bricks-academy-page_titles_all.csv --delay 2.0
```

#### Issue: Wrong Categorization
```bash
# Move file to correct category
mv docs/articles/misplaced_file.md docs/filters/

# Update categorize_doc() function in scraper.py for future runs
```

#### Issue: Rate Limiting
```bash
# Increase delay between requests
python scraper.py bricks-academy-page_titles_all.csv --delay 3.0
```

### Future Enhancements

Consider implementing:
1. **RSS/Feed Monitor**: Auto-detect new documentation via RSS feeds
2. **Diff Reports**: Generate reports showing what changed in updated pages
3. **Search Index**: Build a searchable index of all documentation
4. **API Documentation Generator**: Extract API details into structured format
5. **Automated PR Creation**: GitHub Action to check for updates weekly