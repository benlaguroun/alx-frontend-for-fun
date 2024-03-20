#!/usr/bin/python3
"""
Markdown to HTML conversion script
"""

import sys
import re

def start_script():
    """
    Start the script
    """
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

def parse_headings(line):
    """
    Parse Markdown headings syntax and generate HTML tags
    """
    headings = {
        '#': 'h1',
        '##': 'h2',
        '###': 'h3',
        '####': 'h4',
        '#####': 'h5',
        '######': 'h6'
    }
    for key, value in headings.items():
        if line.startswith(key):
            return f"<{value}>{line[len(key):].strip()}</{value}>"
    return line

def markdown_to_html(input_file, output_file):
    """
    Convert Markdown to HTML
    """
    with open(input_file, 'r') as md_file:
        markdown_lines = md_file.readlines()

    with open(output_file, 'w') as html_file:
        for line in markdown_lines:
            line = line.strip()
            if line:
                line = parse_headings(line)
                html_file.write(line + '\n')

if __name__ == "__main__":
    start_script()
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    markdown_to_html(input_file, output_file)

