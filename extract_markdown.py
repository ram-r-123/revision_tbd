#!/usr/bin/env python3
"""
Extract markdown cells from Jupyter notebooks and compile into a single markdown file.
"""

import json
import glob
import os
from collections import defaultdict

def extract_markdown_from_notebook(notebook_path):
    """Extract all markdown cells from a Jupyter notebook."""
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)

    markdown_cells = []
    for cell in notebook.get('cells', []):
        if cell.get('cell_type') == 'markdown':
            # Join source lines if it's a list
            source = cell.get('source', [])
            if isinstance(source, list):
                source = ''.join(source)
            markdown_cells.append(source)

    return markdown_cells

def get_topic_name(filename):
    """Extract topic name from filename."""
    # Remove .ipynb extension
    name = filename.replace('.ipynb', '')

    # Check if it's a solution file
    is_solution = False
    if '-Solutions' in name or '-solutions' in name:
        is_solution = True
        # Remove the solution suffix
        name = name.replace('-Solutions', '').replace('-solutions', '')
        # Remove " (1)" or similar
        name = name.split(' (')[0]

    return name, is_solution

def main():
    # Find all notebook files
    notebooks = glob.glob('*.ipynb')

    # Group notebooks by topic
    topics = defaultdict(lambda: {'main': None, 'solutions': None})

    for notebook in notebooks:
        topic, is_solution = get_topic_name(notebook)
        if is_solution:
            topics[topic]['solutions'] = notebook
        else:
            topics[topic]['main'] = notebook

    # Sort topics alphabetically
    sorted_topics = sorted(topics.keys())

    # Generate the compiled markdown file
    output_lines = []
    output_lines.append("# Python Learning Materials - Compiled Notes\n\n")
    output_lines.append("*This document contains markdown content extracted from Jupyter notebooks*\n\n")
    output_lines.append("---\n\n")

    for topic in sorted_topics:
        # Create a master section for this topic
        topic_header = topic.replace('_', ' ').replace('-', ' ')
        output_lines.append(f"# {topic_header}\n\n")

        # Add main content
        if topics[topic]['main']:
            output_lines.append(f"## {topic_header} - Main Content\n\n")
            markdown_cells = extract_markdown_from_notebook(topics[topic]['main'])
            for cell in markdown_cells:
                output_lines.append(cell)
                output_lines.append("\n\n")

        # Add solutions content
        if topics[topic]['solutions']:
            output_lines.append(f"## {topic_header} - Solutions\n\n")
            markdown_cells = extract_markdown_from_notebook(topics[topic]['solutions'])
            for cell in markdown_cells:
                output_lines.append(cell)
                output_lines.append("\n\n")

        output_lines.append("---\n\n")

    # Write to output file
    with open('compiled_notes.md', 'w', encoding='utf-8') as f:
        f.writelines(output_lines)

    print(f"✓ Processed {len(notebooks)} notebooks")
    print(f"✓ Found {len(sorted_topics)} topics")
    print(f"✓ Compiled markdown written to: compiled_notes.md")

if __name__ == '__main__':
    main()
