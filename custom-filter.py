#!/usr/bin/env python3

import panflute as pf

def conditional_styling(element, doc):
    if isinstance(element, pf.Header):
        text_content = ''.join(str(e) for e in element.content)
        if text_content == "Education":
            return pf.Div(*element.content, classes=["education-header"])
        elif text_content == "Publications":
            return pf.Div(*element.content, classes=["publications-header"])

def main(doc=None):
    return pf.run_filter(conditional_styling, doc=doc)

if __name__ == '__main__':
    main()
