{
    "document-title": "Keypressiv",
    "aspect-ratio": 1.33,
    "footer-text": "Keypressiv Introduction",
    "show-footer-in-title-page": false
}
!SLIDE

<center>
# Keypressiv Introduction
</center>
<br/>
<br/>
<br/>
<center>
## author: Toshihiro Kamiya
</center>

<center>kamiya@mbj.nifty.com</center>

!SLIDE

## Keypressiv is...

* A [Keydown](https://github.com/infews/keydown)-inspired presentation tool.
* Use [Markdown](http://daringfireball.net/projects/markdown/) and HTML markup to describe slide pages.
* Fixed aspect ratio. Auto font resizing.
* Neutral in CSS styles of common elements. No pre-defined themes except for
* An animation on page transition.

!SLIDE

## How to Use

(1) Write slide pages in **presentation.md**

(2) Run a HTTP file server, e.g.,:
<pre class="prettyprint">
$ cd (directory of presentation.md)<br/>
$ python -m SimpleHTTPServer
</pre>

(3) Open it with a web browser, e.g.,:
open an URL **http://localhost:8000**
<br/>
<br/>
(4') A handout (note) is shown in [handout.html](handout.html), e.g.:
open an URL **http://localhost:8000/handout.html**
<br/>
<br/>
(5') To print out slides as it is, save as PDF in the web browser, OR...

!SLIDE trans-vert-stack

## How to Use (cont'd)

(5'') To print out slides as it is,

* Show [printing.html](printing.html), e.g.: open an URL **http://localhost:8000/printing.html**

* Save as a HTML file (e.g., "slides.html"), and

* Convert it to a PDF file with a utility such as [wkhtmltopdf](https://pypi.python.org/pypi/pdfkit).

<pre class="prettyprint">
$ wkhtmltopdf -O Landscape -T 0 -B 0 slides.html slides.pdf
</pre>

### Note:

* When web fonts are used in a presentation, you need to copy such font files (e.g. `font/fontawesome-webfont.ttf` in case of this presentation) in your PC's font directory (e.g. `~/.fonts`).

!SLIDE

## Controls in Presentation

With either keyboard, mouse, or touch pad.

* **[&larr;]**, **[Page Up]**, **Swipe right** : previous page
* **[&rarr;]**, **[Page Down]**, **Swipe left** : next page
* Number **[Enter]** : go to the page
* **[M]** **[Enter]**, **[Tab]**: to Map mode
* **[S]** **[Enter]**, **[Esc]**: to Slide mode

!SLIDE

## Listings

Both markdown listing and HTML listing can be used.

* Normal
  + upto 2 levels are supported by default.

<ul>
<li class="li-ballot-checked">Checked</li>
<li class="li-ballot">Unchecked</li>
</ul>

<p class="listing-indent">
(1) Or user defined listing style
</p>
<p>
(ii) can be used
</p>
<p>
three) if needed.
</p>

!SLIDE

## Two-Column Layout

<div class="column-container">
<div class="column_2">
### Left Coumn

* Some long long long long long long long sentence.
</div>
<div class="column_2">
### Right Coumn

* Another long long long long long long long sentence.
</div>
</div>

!SLIDE
<div style="height:100%;background:#ffff00;">

## Image, Background

<img style="width:50%;float:right;" src="img/640px-Play-of-fireworks-and-night-scenes-in-Hakodate.jpg">

* in an auto resizing manner
  + The image size is relative to window size.

<div style="clear:both;"></div>

<img style="width:320px;float:right" src="img/640px-Play-of-fireworks-and-night-scenes-in-Hakodate.jpg">

* in a size-fixed manner
  + The image size is specified in pixel.

<div style="clear:both;"></div>

Image: [Play of fireworks and night scenes in hakodate](http://ja.wikipedia.org/wiki/%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB:Play_of_fireworks_and_night_scenes_in_Hakodate.jpg) Cc-by-sa-3.0,2.5,2.0,1.0

</div>
!SLIDE

## Table, CSS

* A table with a custom style

<!-- ref: http://stackoverflow.com/questions/4932181/rounded-table-corners-css-only -->
<style>
table.roundcorner {
border: 2px solid #ddd;
border-collapse: separate;
border-left: 0;
border-radius: 8px;
border-spacing: 0px;
}
table.roundcorner thead {
display: table-header-group;
border-color: inherit;
border-collapse: separate;
}
table.roundcorner tr {
display: table-row;
border-color: inherit;
}
table.roundcorner th, table.roundcorner td {
padding: 5px 4px 6px 4px;
border-left: 2px solid #ddd;
}
table.roundcorner td {
border-top: 2px solid #ddd;
}
table.roundcorner thead:first-child tr:first-child th:first-child, table.roundcorner tbody:first-child tr:first-child td:first-child {
border-radius: 8px 0 0 0;
}
table.roundcorner thead:last-child tr:last-child th:first-child, table.roundcorner tbody:last-child tr:last-child td:first-child {
border-radius: 0 0 0 8px;
}
</style>

<table class="roundcorner">
<thead>
<tr><th></th><th>Mon</th><th>Tue</th><th>Wed</th><th>...</th></tr>
</thead>
<tbody>
<tr><td>1</td><td>- </td><td>Programming I</td><td>-</td><td></td></tr>
<tr><td>2</td><td>Math</td><td>Algorithm I</td><td>PE</td><td></td></tr>
</tbody>
</table>

!SLIDE

## Syntax Highlighting

* gfm-like code block (\`\`\` ... \`\`\`) is available (new v1.1).

```js
/* A sample of syntax highlighting */
function decrimentToZero(n) {
    if (n > 0)
        return n - 1;
    else
        return 0;
}
```

* Supported languages are: sh, c, cc, java, js, coffee, pl, py, sql, xml, html, lua, vb, hs, ml, el, cs, vhdl, yaml, scala, go, erlang, etc.
  * syntax highlighting is done with [google-code-prettify](https://code.google.com/p/google-code-prettify/).

!SLIDE trans-none

## Page transition animation
(new v1.2)

* The default page-transition animation is a horizontal sliding.
* By specifying "!SLIDE trans-none" in top of a page description, no page-transition animation (like this slide).
* By specifying "!SLIDE trans-vert" in top of a page description, a vartical sliding is applied.
* By specifying "!SLIDE trans-vert-stack", the slide appears as if it is put on the previous slide.

!SLIDE
<br/>
<br/>
<br/>
<center>
# Enjoy!
</center>
<center>
<button type="button" onclick="location.href='#1';">&rarr; Go to title slide</button>
</center>
<br/>
<br/>
<br/>
<center>
Keypressiv is available in [github.com/tos-kamiya/Keypressiv](https://github.com/tos-kamiya/Keypressiv).
</center>
