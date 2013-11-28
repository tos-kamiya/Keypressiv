!SLIDE

<center>
# Keypressiv Sample Presentation
</center>
<br/>
<center>
## author: Toshihiro Kamiya
</center>

<center>kamiya@mbj.nifty.com</center>

!SLIDE

## The keypressive is...

* A [Keydown](https://github.com/infews/keydown)-inspired presentation tool.
* Use [Markdown](http://daringfireball.net/projects/markdown/) and HTML markup to describe slide pages.
* Fixed aspect ratio. Auto font resizing.

!SLIDE

## How to Use

(1) Write slide pages in **presentation.md**

(2) Run a HTTP file server, e.g.,:
<br/>
<pre>
  $ cd (presentation.md's directory)
  $ python -m SimpleHTTPServer
</pre>
<br/>
(3) Open an URL **http://localhost:8000** with a web brower 

!SLIDE

## Control Keys in Presentation

* **[&larr;]** : previous page
* **[&rarr;]** : next page
* Number + **[Enter]** : go to the page

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
<img style="width:50%;" src="/img/640px-Play-of-fireworks-and-night-scenes-in-Hakodate.jpg">

* in a size-fixed manner
<img style="width:320px;" src="/img/640px-Play-of-fireworks-and-night-scenes-in-Hakodate.jpg">

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
<br/>
<center>
# Enjoy!
</center>


