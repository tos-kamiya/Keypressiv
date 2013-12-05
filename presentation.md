{
    "footer-text": "Kyepressiv Introduction",
    "show-footer-in-title-page": false
}
!SLIDE

<center>
# Kyepression Introduction
</center>
<br/>
<center>
## author: Toshihiro Kamiya
</center>

<center>kamiya@mbj.nifty.com</center>

!SLIDE

## Keypressive is...

* A [Keydown](https://github.com/infews/keydown)-inspired presentation tool.
* Use [Markdown](http://daringfireball.net/projects/markdown/) and HTML markup to describe slide pages.
* Fixed aspect ratio. Auto font resizing.

!SLIDE

## How to Use

(1) Write slide pages in **presentation.md**

(2) Run a HTTP file server, e.g.,:
<pre>
  $ cd (presentation.md's directory)
  $ python -m SimpleHTTPServer
</pre>

(3) Open it with a web browser, e.g.,:
open an URL **http://localhost:8000**
<br/>
<br/>
(4') A handout is shown in [handout.html](handout.html), e.g.:
open an URL **http://localhost:8000/handout.html**

!SLIDE

## Controls in Presentation

With either keyboard, mouse, or touch pad.

* **[&larr;]**, **Swipe right** : previous page
* **[&rarr;]**, **Swipe left** : next page
* Number + **[Enter]** : go to the page

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

<div style="display:-webkit-box;display:-moz-box;">
<div style="width:40%;margin:0em e3m;">
### Left Coumn
* Some long long long long long long long sentence.
</div>
<div style="width:40%;margin:0em e3m;">
### Right Coumn
* Another long long long long long long long sentence.
</div>
</div>

!SLIDE

## Image

* in an auto resizing manner
<img style="width:50%;" src="img/640px-Play-of-fireworks-and-night-scenes-in-Hakodate.jpg">

* in a size-fixed manner
<img style="width:320px;" src="img/640px-Play-of-fireworks-and-night-scenes-in-Hakodate.jpg">

Image: [Play of fireworks and night scenes in hakodate](http://ja.wikipedia.org/wiki/%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB:Play_of_fireworks_and_night_scenes_in_Hakodate.jpg) Cc-by-sa-3.0,2.5,2.0,1.0

!SLIDE

## Table

* A table with CSS3

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

<pre class="prettyprint lang-js">
    /* A sample of syntax highlighting */
    function plusOne(n) {
        return n + 1;
    }
</pre>

!SLIDE
<br/>
<br/>
<br/>
<center>
# Enjoy!
</center>
<br/>
<br/>
<br/>
Keypressiv is available in [github.com/tos-kamiya/Keypressiv](https://github.com/tos-kamiya/Keypressiv).


