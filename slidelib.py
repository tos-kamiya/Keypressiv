import markdown
import json

def read_pages(presentation_file):
    lines = open(presentation_file).readlines()
    footer_text = None
    pages = []
    pls = []
    config_data = None
    in_header = True
    for L in lines:
        if L.startswith("!SLIDE"):
            if pls:
                if in_header:
                    config_data = json.loads(''.join(pls))
                else:
                    pages.append('\n'.join(pls))
            pls = []
            in_header = False
        else:
            pls.append(L)
    if in_header:
        config_data = json.loads(''.join(pls))
    else:
        pages.append('\n'.join(pls))

    page_datas = []
    for page in pages:
        mk, scripts = markdown.mark(page)
        page_datas.append((mk, scripts))

    return page_datas, config_data

