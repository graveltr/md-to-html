Example usage of pandoc with custom filters to convert markdown to html with styles.

# Dependencies
- pandoc
- panflute

Make sure that the panflute and pandoc you are using are compatible.

# Usage
```pandoc --filter custom-filter.py {your-markdown-file.md}```

This will print the resultant html to stdout. Copy this and paste it inside the
`<body>` tags in `page.html`. 

