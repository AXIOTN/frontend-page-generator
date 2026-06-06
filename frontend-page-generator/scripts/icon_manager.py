#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Icon Manager Tool"""

import argparse
import os

DEFAULT_ICONS_DIR = "images/icons"

ICON_TEMPLATES = {
    "default": """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <circle cx="12" cy="12" r="10"/>
</svg>""",
    
    "document": """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <path d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5L14.5 2z"/>
  <polyline points="14 2 14 8 20 8"/>
</svg>""",
    
    "action": """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <circle cx="12" cy="12" r="10"/>
  <path d="m9 12 2 2 4-4"/>
</svg>""",
    
    "navigation": """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <polygon points="3 11 22 2 13 21 11 13 3 11"/>
</svg>""",
    
    "media": """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <rect width="18" height="18" x="3" y="3" rx="2"/>
  <circle cx="9" cy="9" r="2"/>
  <path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"/>
</svg>"""
}

def list_icons(icons_dir):
    if not os.path.exists(icons_dir):
        print(f"Icons directory not found: {icons_dir}")
        return
    
    icons = [f for f in os.listdir(icons_dir) if f.endswith('.svg')]
    
    if not icons:
        print("No icons found")
        return
    
    print(f"Icons ({len(icons)}):")
    print("-" * 40)
    for icon in sorted(icons):
        name = icon.replace('.svg', '')
        print(f"  - {name}")

def create_icon(icons_dir, name, template="default"):
    if not os.path.exists(icons_dir):
        os.makedirs(icons_dir, exist_ok=True)
    
    filepath = os.path.join(icons_dir, f"{name}.svg")
    
    if os.path.exists(filepath):
        print(f"Icon already exists: {filepath}")
        return
    
    svg_content = ICON_TEMPLATES.get(template, ICON_TEMPLATES["default"])
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(svg_content)
    
    print(f"Icon created: {filepath}")
    print("Please edit the file to add icon paths")

def search_icons(icons_dir, keyword):
    if not os.path.exists(icons_dir):
        print(f"Icons directory not found: {icons_dir}")
        return
    
    icons = [f for f in os.listdir(icons_dir) if f.endswith('.svg')]
    results = [i for i in icons if keyword.lower() in i.lower()]
    
    if not results:
        print(f"No icons found matching '{keyword}'")
        return
    
    print(f"Search results ({len(results)}):")
    print("-" * 40)
    for icon in results:
        name = icon.replace('.svg', '')
        print(f"  - {name}")

def main():
    parser = argparse.ArgumentParser(description="Icon Manager")
    parser.add_argument("--list", action="store_true", help="List all icons")
    parser.add_argument("--create", action="store_true", help="Create new icon")
    parser.add_argument("--search", action="store_true", help="Search icons")
    parser.add_argument("--name", help="Icon name")
    parser.add_argument("--keyword", help="Search keyword")
    parser.add_argument("--template", choices=list(ICON_TEMPLATES.keys()), default="default")
    parser.add_argument("--dir", default=DEFAULT_ICONS_DIR)
    
    args = parser.parse_args()
    
    if args.list:
        list_icons(args.dir)
    elif args.create:
        if not args.name:
            print("Please specify icon name: --name <name>")
            return
        create_icon(args.dir, args.name, args.template)
    elif args.search:
        if not args.keyword:
            print("Please specify search keyword: --keyword <keyword>")
            return
        search_icons(args.dir, args.keyword)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
