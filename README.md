# Static Site Generator

A Python static site generator that converts Markdown files into a fully navigable HTML website. Built from scratch as part of the [boot.dev](https://boot.dev) course, no site-generation frameworks used.

**[Live Demo](https://codebiscuits.github.io/static_site_generator/)**

## Features

- Parses Markdown into an HTML node tree from first principles
- Supports headings, paragraphs, bold, italic, code, links, images, blockquotes, ordered and unordered lists
- Recursive page generation, mirrors your `content/` directory structure as output HTML
- Template-based layout, a single `template.html` controls the site's structure and styling
- Copies static assets (images, CSS) to the output directory automatically
- Test suite covering all parsing and generation components

## How it works

1. Markdown files in `content/` are parsed into an HTML node tree
2. Each page is rendered into `template.html` (replacing `{{ Title }}` and `{{ Content }}`)
3. Output HTML is written to `docs/` (served by GitHub Pages)
4. Static assets from `static/` are copied to `docs/`

## Project structure

```
content/                    # Markdown source files
static/                     # Static assets (images, CSS)
docs/                       # Generated output — served by GitHub Pages
src/                        # Python source
  main.py                   # Entry point
  generate_page.py
  markdown_to_htmlnode.py
  htmlnode.py
  ...
template.html               # HTML wrapper applied to every page
build.sh                    # Build script
test.sh                     # Run the test suite
```

## To Build the Site for Github Pages

```bash
./build.sh
```

## Running tests

```bash
./test.sh
```
