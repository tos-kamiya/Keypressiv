from browser import doc, markdown
import json

SLIDE_OPTIONS = ("no-animation",)

def read_pages(presentation_file):
    lines = open(presentation_file).readlines()
    footer_text = None
    pages = []
    page_options = []
    pls = []
    config_data = None
    in_header = True
    for li, L in enumerate(lines):
        if L.startswith("!SLIDE"):
            if pls:
                if in_header:
                    config_data = json.loads(''.join(pls))
                else:
                    pages.append('\n'.join(pls))
            pls = []
            option_strs = L.split()[1:]
            for s in option_strs:
                if s not in SLIDE_OPTIONS:
                    console.log("line %d: invalid option found" % (li + 1))
            page_options.append(option_strs)
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

    return page_datas, config_data, page_options

def draw_slide(doc, zone_id, page_data, confing_data):
    mk, scripts = page_data
    doc[zone_id].html = mk
    for script in scripts:
        exec(script, globals())
    page_num = confing_data['page']
    p = doc.get(classname="slidefooter-page")[0]
    p.text = page_num
    op = 1 if page_num > 1 or confing_data.get("show-footer-in-title-page") else 0
    doc.get(classname="slidefooter-text")[0].style.opacity = p.style.opacity = op

def draw_minimap(doc, zone_id, page_datas, config_data):
    h = []
    h.append("<table><tr>")
    col = 0
    cur_page = config_data.get("page", -1)
    for i, (mk, _) in enumerate(page_datas):
        page_num = i + 1
        h.append("""<td onclick="switchToSlideMode(%d);"><div class="minimap-page">""" % i)
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

def draw_handout(doc, zone_id, page_datas, config_data):
    h = []
    for i, (mk, _) in enumerate(page_datas):
        h.append(mk)
        h.append("""<div class="handout-page-num">%d</div>""" % (i + 1))
        h.append("""<hr/>""")
    doc[zone_id].html = "".join(h)
    for _, scripts in page_datas:
        for script in scripts:
            exec(script, globals())

def draw_printing(doc, zone_id, page_datas, config_data):
    h = []
    for i, (mk, _) in enumerate(page_datas):
        h.append("""<div class="page">""")
        h.append(mk)
        h.append("""<div class="slidefooter-page">%d</div>""" % (i + 1))
        h.append("""<div class="slidefooter-text">%s</div>""" % config_data.get("footer-text", ""))
        h.append("""</div>""")
    doc[zone_id].html = "".join(h)
    for _, scripts in page_datas:
        for script in scripts:
            exec(script, globals())
    
