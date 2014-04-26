Keypressiv
==========

A keydown-inspired markdown-based presentation tool.

* Fixted aspect ratio (1.33 (4:3) by default) against any screen resolution.
* Auto font resizing. Font sizes are relative to a screen(window).
* Easy installation. No installation required in an actual sense.
* Encourage to use markdown mixed with html. Use markdown for smiple formattings. Use html for complicated formattings. 
* Slides can be converted into a PDF file (in a somehow manual way). A sample [presentation.pdf](presentation.pdf).

Read [presentation.md](presentation.md) for usage,
or see this usage as [a sample presentation](http://tos-kamiya.github.io/Keypressiv/).

## Make your own presentation with Keypressiv

Step 1. Clone the repo

```bash
$ git clone https://github.com/tos-kamiya/Keypressiv.git /path/to/presen
$ cd /path/of/presen
```

Step 2. Edit presentation.md

```bash
$ gedit presentation.md
```

Step 3. Serve index.html by a Http server

```bash
$ python -m SimpleHTTPServer
```
