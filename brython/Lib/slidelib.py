from browser import doc, markdown, console
import html
import json

SLIDE_OPTIONS = ("no-animation",)

def escape_code_block(code_spec, code_lines):
    s = "<br/>".join(map(html.escape, code_lines))
    c = "prettyprint"
    if code_spec:
        c = c + " lang-" + code_spec
    return """<pre class="%s">%s</pre>""" % (c, s)

def read_pages(presentation_file):
    lines = open(presentation_file).readlines()
    footer_text = None
    page_datas = []
    page_options = []
    page_htmls = []
    page_scripts = []
    code_spec, code_block = None, []
    text_block = []
    config_data = None
    in_header = True

    def flash_text_block():
        marked, scripts = markdown.mark('\n'.join(text_block))
        page_htmls.append(marked)
        page_scripts.extend(scripts)
        text_block[:] = []

    if lines and not lines[-1].startswith("!SLIDE"):
        lines.append("!SLIDE")  # sentinel

    for li, L in enumerate(lines):
        if L.startswith("!SLIDE"):
            if code_spec is not None:
                page_htmls.append(escape_code_block(code_spec, code_block))
                code_spec, code_block = None, []
            if text_block:
                if in_header:
                    config_data = json.loads(''.join(text_block))
                    text_block[:] = []
                else:
                    flash_text_block()
                    page_datas.append(('\n'.join(page_htmls), page_scripts))
            option_strs = L.split()[1:]
            for s in option_strs:
                if s not in SLIDE_OPTIONS:
                    console.log("line %d: invalid option found" % (li + 1))
            page_options.append(option_strs)
            in_header = False
            page_htmls = []
        elif L.startswith("```"):
            if text_block:
                flash_text_block()
            if code_spec is None:
                code_spec, code_block = L[len("```"):].strip(), []
            else:
                page_htmls.append(escape_code_block(code_spec, code_block))
                code_spec, code_block = None, []
        else:
            if code_spec is not None:
                code_block.append(L)
            else:
                text_block.append(L)

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
    
