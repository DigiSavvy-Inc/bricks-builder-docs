import pandas as pd
import requests
from bs4 import BeautifulSoup
import os
import time
from urllib.parse import urlparse
import json
import re
import datetime
from tqdm import tqdm

def scrape_webpage(url, headers=None):
    """Scrape content from a webpage."""
    if headers is None:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
    
    try:
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.extract()
            
        # Get title
        title = soup.title.string if soup.title else "No Title"
        
        # Get main content (this is a simplified approach)
        # For better results, you might need site-specific selectors
        main_content = soup.find('main') or soup.find('article') or soup.find('div', class_='content')
        
        # Extract structured content (headings and their sections)
        structured_content = []
        if main_content:
            content_container = main_content
        else:
            content_container = soup.body or soup
        
        # First, find all content elements (headings, paragraphs, code blocks, etc.)
        content_elements = []
        for element in content_container.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'pre', 'code', 'ul', 'ol', 'blockquote']):
            content_elements.append(element)
        
        # Process elements sequentially to build structured content
        current_heading = None
        current_content = ""
        
        for i, element in enumerate(content_elements):
            # If this is a heading, start a new section
            if element.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                # Save previous section if exists
                if current_heading is not None:
                    structured_content.append({
                        'level': int(current_heading.name[1]),
                        'heading': current_heading.get_text(strip=True),
                        'content': current_content.strip()
                    })
                
                # Start new section
                current_heading = element
                current_content = ""
            else:
                # Add content to current section
                if element.name == 'pre' or element.name == 'code':
                    # Preserve formatting for code blocks
                    element_text = element.get_text()
                    # Add markdown code block formatting
                    if element.name == 'pre':
                        current_content += "```\n" + element_text + "\n```\n\n"
                    else:
                        current_content += "`" + element_text + "`\n\n"
                elif element.name in ['ul', 'ol']:
                    # Process list items
                    list_text = ""
                    for i, li in enumerate(element.find_all('li')):
                        prefix = "- " if element.name == 'ul' else f"{i + 1}. "
                        list_text += f"{prefix}{li.get_text(strip=True)}\n"
                    current_content += list_text + "\n"
                else:
                    # Regular content
                    element_text = element.get_text(strip=True)
                    if element_text:
                        current_content += element_text + "\n\n"
        
        # Add the final section
        if current_heading is not None:
            structured_content.append({
                'level': int(current_heading.name[1]),
                'heading': current_heading.get_text(strip=True),
                'content': current_content.strip()
            })
        
        # Extract text content
        if main_content:
            text = main_content.get_text(separator='\n', strip=True)
        else:
            # Fallback to body content
            text = soup.get_text(separator='\n', strip=True)
        
        return {
            'url': url,
            'title': title,
            'content': text,
            'structured_content': structured_content,
            'html': response.text,  # Store full HTML as well
            'status': 'success'
        }
    
    except Exception as e:
        return {
            'url': url,
            'title': None,
            'content': None,
            'structured_content': [],
            'html': None,
            'status': f'error: {str(e)}'
        }

def save_as_markdown(data, filepath):
    """Convert scraped data to markdown format and save to file."""
    with open(filepath, 'w', encoding='utf-8') as f:
        # Metadata section as YAML frontmatter
        f.write('---\n')
        f.write(f'title: "{data["title"]}"\n')
        f.write(f'url: {data["url"]}\n')
        f.write(f'date: {datetime.datetime.now().isoformat()}\n')
        f.write(f'status: {data["status"]}\n')
        f.write('---\n\n')
        
        # Main title
        f.write(f'# {data["title"]}\n\n')
        
        # Source URL as reference
        f.write(f'*Source: [{data["url"]}]({data["url"]})*\n\n')
        
        # If we have structured content, use that for better organization
        if data.get('structured_content') and len(data['structured_content']) > 0:
            # Add table of contents
            f.write('## Table of Contents\n\n')
            for section in data['structured_content']:
                level = section['level']
                heading = section['heading']
                indent = '  ' * (level - 1)
                # Create a slug for the heading
                slug = heading.lower().replace(' ', '-')
                slug = re.sub(r'[^a-z0-9-]', '', slug)
                f.write(f'{indent}- [{heading}](#{slug})\n')
            f.write('\n')
            
            # Write each section
            for section in data['structured_content']:
                level = section['level']
                heading = section['heading']
                content = section['content']
                
                # Write heading with appropriate markdown level (add 1 to level since we used # for the title)
                heading_marks = '#' * (level + 1)
                f.write(f'{heading_marks} {heading}\n\n')
                
                # Write section content
                if content:
                    f.write(f'{content}\n\n')
        else:
            # Fallback to simple content if no structure was found
            # Split content into paragraphs and format
            paragraphs = data['content'].split('\n')
            for p in paragraphs:
                if p.strip():
                    f.write(f'{p.strip()}\n\n')

def categorize_doc(url, title=None):
    """Determine which docs subdirectory a document belongs to based on URL and title."""
    url_lower = url.lower()
    
    # Filters
    if 'filter-bricks' in url_lower:
        return 'filters'
    
    # Actions
    if 'action-bricks' in url_lower:
        return 'actions'
    
    # Functions (developer)
    if 'function-bricks' in url_lower:
        return 'developer'
    
    # Topics
    if '/topic/' in url_lower:
        return 'topics'
    
    # Collections
    if '/collection/' in url_lower:
        if 'developer' in url_lower:
            return 'developer'
        elif 'tutorial' in url_lower:
            return 'tutorials'
        else:
            return 'articles'
    
    # Customization patterns
    if any(pattern in url_lower for pattern in ['custom-', 'create-your-own']):
        return 'customization'
    
    # Integrations
    if any(pattern in url_lower for pattern in ['wpml', 'polylang', 'instagram', 'adobe-fonts', 'unsplash', 'google-maps']):
        return 'integrations'
    
    # Security
    if any(pattern in url_lower for pattern in ['security', 'code-signatures', 'password-protection', 'restrict-license']):
        return 'security'
    
    # CLI and tools
    if any(pattern in url_lower for pattern in ['bricks-cli', 'bricks-rce']):
        return 'tools'
    
    # Tutorials/How-to
    if 'how-to' in url_lower:
        return 'tutorials'
    
    # WooCommerce
    if any(pattern in url_lower for pattern in ['woocommerce', 'cart', 'checkout', 'product']):
        return 'tutorials'  # WooCommerce tutorials
    
    # Default to articles
    return 'articles'

def create_knowledge_base(csv_path, output_dir="docs", delay=1, dev_only=False):
    """Create a knowledge base from URLs in a CSV file, organized into docs structure."""
    # Create output directory and subdirectories
    os.makedirs(output_dir, exist_ok=True)
    
    # Create subdirectories
    subdirs = ['actions', 'articles', 'customization', 'developer', 
               'filters', 'integrations', 'security', 'tools', 
               'topics', 'tutorials']
    
    for subdir in subdirs:
        os.makedirs(os.path.join(output_dir, subdir), exist_ok=True)
    
    # Read CSV file
    df = pd.read_csv(csv_path)
    
    # Check if the CSV has a column with URLs
    url_column = None
    title_column = None
    
    for col in df.columns:
        if 'url' in col.lower() or 'link' in col.lower() or 'address' in col.lower():
            url_column = col
        if 'title' in col.lower():
            title_column = col
    
    if not url_column:
        print(f"No URL column found in {csv_path}. Available columns: {', '.join(df.columns)}")
        return
    
    # Extract URLs
    urls = df[url_column].tolist()
    
    # Filter for developer-oriented docs if requested
    if dev_only:
        # Define patterns that indicate developer documentation
        dev_patterns = [
            'filter:', 'action:', 'function:', 'developer', 'api', 'hook', 
            'custom', '/query/', '/element/', 'javascript', '/code/', 
            'create your own', 'dynamic data'
        ]
        
        # Define patterns for UI elements and basic usage docs to exclude
        exclude_patterns = [
            'element:', '– element', 'builder', 'template', 'style', 'layout',
            'responsive', 'hover', 'animation', 'theme', 'mode'
        ]
        
        # Filter based on URL patterns
        filtered_urls = []
        for url in urls:
            url_lower = url.lower()
            
            # Check if URL contains developer pattern
            is_dev_doc = any(pattern.lower() in url_lower for pattern in dev_patterns)
            
            # Check for specific developer collections
            is_dev_collection = any(collection in url for collection in [
                '/collection/developer/', '/topic/filters/', '/topic/actions/', 
                '/topic/controls/', '/topic/basics/', '/article/api'
            ])
            
            # Check if it's a filter or action or function doc
            is_api_doc = (
                'filter-bricks' in url_lower or 
                'action-bricks' in url_lower or 
                'function-bricks' in url_lower
            )
            
            # Add to filtered list if it matches any criteria
            if is_dev_doc or is_dev_collection or is_api_doc:
                filtered_urls.append(url)
        
        print(f"Filtered from {len(urls)} to {len(filtered_urls)} developer-oriented docs.")
        urls = filtered_urls
    
    print(f"Found {len(urls)} URLs to scrape.")
    
    # Scrape each URL
    results = []
    for url in tqdm(urls, desc="Scraping URLs"):
        # Create a filename based on the URL
        domain = urlparse(url).netloc
        path = urlparse(url).path.replace('/', '_')
        if path == '':
            path = '_index'
        
        # Determine category for this document
        category = categorize_doc(url)
        
        # Use markdown extension instead of json
        filename = f"{domain}{path}.md"
        filepath = os.path.join(output_dir, category, filename)
        
        # Skip if already scraped
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                # Extract URL from frontmatter
                url_match = re.search(r'url: (.*)', content)
                url = url_match.group(1) if url_match else url
                
                # Create a minimal data structure for the summary
                data = {
                    'url': url,
                    'status': 'success'  # Assume success for existing files
                }
                results.append(data)
            print(f"Skipped {url} (already scraped)")
            continue
        
        # Scrape the page
        data = scrape_webpage(url)
        results.append(data)
        
        # Save the result as markdown
        save_as_markdown(data, filepath)
        
        # Delay to be nice to the server
        time.sleep(delay)
    
    # Save a summary as markdown
    with open(os.path.join(output_dir, 'summary.md'), 'w', encoding='utf-8') as f:
        f.write('# Knowledge Base Summary\n\n')
        f.write(f'Generated on: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n\n')
        
        successful = sum(1 for r in results if r['status'] == 'success' or r['status'] == 'success')
        failed = sum(1 for r in results if not (r['status'] == 'success' or r['status'] == 'success'))
        
        f.write(f'Total URLs processed: {len(results)}\n')
        f.write(f'Successful: {successful}\n')
        f.write(f'Failed: {failed}\n\n')
        
        f.write('## Sources\n\n')
        for r in results:
            status_icon = "✅" if r['status'] == 'success' or r['status'] == 'success' else "❌"
            f.write(f'- {status_icon} [{r["url"]}]({r["url"]})\n')
    
    # Also save a JSON version of the summary for programmatic access
    summary = {
        'total': len(results),
        'successful': successful,
        'failed': failed,
        'sources': [{'url': r['url'], 'status': r['status']} for r in results]
    }
    
    with open(os.path.join(output_dir, 'summary.json'), 'w', encoding='utf-8') as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
    
    print(f"Completed: {successful} successful, {failed} failed.")
    print(f"Results saved to {output_dir}")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Create a knowledge base from URLs in a CSV file.')
    parser.add_argument('csv_path', help='Path to the CSV file containing URLs')
    parser.add_argument('--output', default='docs', help='Output directory (default: docs)')
    parser.add_argument('--delay', type=float, default=1.0, help='Delay between requests in seconds')
    parser.add_argument('--dev-only', action='store_true', help='Filter for developer-oriented documentation only')
    
    args = parser.parse_args()
    
    create_knowledge_base(args.csv_path, args.output, args.delay, args.dev_only)