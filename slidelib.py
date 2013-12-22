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

def draw_slide(doc, zone_id, page_data, confing_data):
    mk, scripts = page_data
    doc[zone_id].html = mk
    for script in scripts:
        exec(script, globals())
    page_num = confing_data['page']
    doc["slidefooter-page"].text = page_num
    op = 1 if page_num > 1 or confing_data.get("show-footer-in-title-page") else 0
    doc["slidefooter-text"].style.opacity = doc["slidefooter-page"].style.opacity = op

def draw_minimap(doc, zone_id, page_datas, config_data):
    h = []
    h.append("<table><tr>")
    col = 0
    cur_page = config_data.get("page", -1)
    for i, (mk, _) in enumerate(page_datas):
        page_num = i + 1
        additional_attr = ""
        h.append("""<td%s onclick="switchToSlideMode(%d);"><div class="minimap-page">""" % (additional_attr, i))
        h.append(mk)
        h.append("""</div></td>""")
        col += 1
        if col % 4 == 0:
            h.append("</tr><tr>")
    while col % 4 != 0:
        h.append("""<td class="empty-page"><div class="minimap-page">&nbsp;</div></td>""")
        col += 1
    h.append("</tr></table>")
    doc[zone_id].html = "".join(h)
    for _, scripts in page_datas:
        for script in scripts:
            exec(script, globals())
