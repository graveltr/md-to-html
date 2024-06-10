Example usage of pandoc with custom filters to convert markdown to html with
styles.

In this basic example, the markdown headers are given html ids, which can then
be styled inside of `styles.css`. This serves as a starting point for more complicated
styling of the resultant html when using pandoc.

# Dependencies
- pandoc
- panflute

Make sure that the panflute and pandoc you are using are compatible.

# Usage
```pandoc --filter custom-filter.py {your-markdown-file.md}```

This will print the resultant html to stdout. Copy this and paste it inside the
`<body>` tags in `page.html`. 

