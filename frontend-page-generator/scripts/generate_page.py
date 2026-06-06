#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Frontend Page Generator Tool"""

import argparse
import os
import json

TEMPLATES = {
    "landing": {
        "name": "Landing Page",
        "sections": ["hero", "features", "pricing", "testimonials", "cta", "footer"]
    },
    "dashboard": {
        "name": "Dashboard",
        "sections": ["sidebar", "topbar", "stats", "charts", "table", "footer"]
    },
    "blog": {
        "name": "Blog",
        "sections": ["navbar", "hero", "articles", "categories", "about", "contact", "footer"]
    },
    "ecommerce": {
        "name": "E-commerce",
        "sections": ["navbar", "hero", "products", "categories", "cart", "footer"]
    },
    "portfolio": {
        "name": "Portfolio",
        "sections": ["navbar", "hero", "projects", "skills", "about", "contact", "footer"]
    }
}

COLOR_SCHEMES = {
    "blue": {"primary": "#3B82F6", "name": "Blue - Professional"},
    "purple": {"primary": "#8B5CF6", "name": "Purple - Creative"},
    "green": {"primary": "#10B981", "name": "Green - Healthy"},
    "orange": {"primary": "#F59E0B", "name": "Orange - Energetic"},
    "pink": {"primary": "#EC4899", "name": "Pink - Playful"},
    "gray": {"primary": "#6B7280", "name": "Gray - Minimal"}
}

def generate_html_template(page_type, page_name, color_scheme):
    template = TEMPLATES.get(page_type, TEMPLATES["landing"])
    color = COLOR_SCHEMES.get(color_scheme, COLOR_SCHEMES["purple"])
    
    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{page_name}</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="css/style.css">
</head>
<body class="bg-gray-50 min-h-screen">
  <div class="flex items-center justify-center min-h-screen">
    <div class="text-center">
      <h1 class="text-4xl font-bold text-gray-900 mb-4">{page_name}</h1>
      <p class="text-gray-500">Type: {template["name"]}</p>
      <p class="text-gray-500">Color: {color["name"]}</p>
    </div>
  </div>
</body>
</html>"""
    
    return html

def create_project_structure(output_dir):
    dirs = [
        output_dir,
        os.path.join(output_dir, "css"),
        os.path.join(output_dir, "js"),
        os.path.join(output_dir, "images"),
        os.path.join(output_dir, "images", "icons"),
        os.path.join(output_dir, "pages")
    ]
    for d in dirs:
        os.makedirs(d, exist_ok=True)
    return dirs

def main():
    parser = argparse.ArgumentParser(description="Frontend Page Generator")
    parser.add_argument("--type", choices=list(TEMPLATES.keys()), default="landing")
    parser.add_argument("--name", default="My Page")
    parser.add_argument("--color", choices=list(COLOR_SCHEMES.keys()), default="purple")
    parser.add_argument("--output", default=".")
    
    args = parser.parse_args()
    
    output_dir = os.path.join(args.output, args.name.replace(" ", "-"))
    create_project_structure(output_dir)
    
    html = generate_html_template(args.type, args.name, args.color)
    with open(os.path.join(output_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    
    config = {
        "name": args.name,
        "type": args.type,
        "color": args.color,
        "sections": TEMPLATES[args.type]["sections"]
    }
    with open(os.path.join(output_dir, "config.json"), "w", encoding="utf-8") as f:
        json.dump(config, f, ensure_ascii=False, indent=2)
    
    print(f"Project created: {output_dir}")
    print(f"Page type: {TEMPLATES[args.type]['name']}")
    print(f"Color scheme: {COLOR_SCHEMES[args.color]['name']}")
    print(f"Sections: {', '.join(TEMPLATES[args.type]['sections'])}")

if __name__ == "__main__":
    main()
