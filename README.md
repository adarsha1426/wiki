# Wiki Encyclopedia

Welcome to the Wiki Encyclopedia! This project is a simple encyclopedia platform built with Python and Django, allowing users to view, search, and manage encyclopedia entries.

## Features

### 1. Entry Page
- **URL:** `/wiki/TITLE`
  - Replace `TITLE` with the name of the encyclopedia entry you want to view.
- Displays the content of the encyclopedia entry specified by `TITLE`.
- Shows an error page if the entry does not exist.

### 2. Index Page
- Lists all encyclopedia entries.
- Entries are clickable to navigate directly to the entry page.

### 3. Search
- Users can search for entries using the search box in the sidebar.
- Exact match queries redirect to the entry’s page.
- Partial match queries display a list of matching entries.

### 4. New Page
- Allows users to create a new encyclopedia entry with a title and Markdown content.
- Displays an error message if an entry with the same title already exists.

### 5. Edit Page
- Users can edit existing entries' Markdown content.
- Pre-populated textarea with existing content for editing.
- Saves changes and redirects to the entry’s page.

### 6. Random Page
- Provides a link to a random encyclopedia entry.

### 7. Markdown to HTML Conversion
- Converts Markdown content to HTML on each entry’s page.
- Uses the `python-markdown2` package for conversion.

## Installation

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/adarsha1426/wiki.git
   cd wiki-encyclopedia
