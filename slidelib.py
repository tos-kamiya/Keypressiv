import markdown

def read_pages(presentation_file):
    lines = open(presentation_file).readlines()
    footer_text = None
    pages = []
    pls = []
    for L in lines:
        if L.startswith("!FOOTER_TEXT"):
            footer_text = L[len("!FOOTER_TEXT") + 1:]
        elif L.startswith("!SLIDE"):
            if pls:
                pages.append('\n'.join(pls))
            pls = []
        else:
            pls.append(L)
    if pls:
        pages.append('\n'.join(pls))

    page_datas = []
    for page in pages:
        mk, scripts = markdown.mark(page)
        page_datas.append((mk, scripts))

    slidefooter = { 'text': footer_text }

    return page_datas, slidefooter

