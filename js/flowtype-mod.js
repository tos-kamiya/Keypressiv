/*
* If you create a derivative, please leave this text intact:
*
* FlowType.JS 1.0
* Copyright (c) 2013, Simple Focus http://simplefocus.com/
*
* FlowType.JS by Simple Focus (http://simplefocus.com/)
* is licensed under the MIT License. Read a copy of the
* license in the LICENSE.txt file or at
* http://choosealicense.com/licenses/mit
*
* Thanks to Giovanni Difeterici (http://www.gdifeterici.com/)
*/

/* modified by Toshihiro Kamiya 2013-11-27, 2013-12-07, 2013-12-20, 2014-05-09 */

(function($) {
   $.fn.flowtype = function(options) {

// Establish default settings/variables
// ====================================
      var settings = $.extend({
         minimum   : 10,
         maxFont   : 9999,
         minFont   : 1,
         fontRatio : 35,
         lineRatio : 1.45,
         aspectRatio: 1.33,
         onlyFontResizing: false,
         scaling   : 1.0,
         resizeToWindow : false
      }, options),

// Do the magic math
// =================
      changes = function(el) {
         var $win = settings.resizeToWindow ? $(window) : $(document);
         var $el = $(el),
            elah = $win.height(),
            elaw = $win.width();
         var elw = elaw,
             elh = elah;
         if (settings.aspectRatio != null) {
            if (elaw > settings.aspectRatio * elah)
                elw = elah * settings.aspectRatio;
            else
                elh = elaw / settings.aspectRatio;
         }
         elw = elw * settings.scaling;
         var paddingw = elw < elaw ? (elaw - elw) * 0.5 : 0,
            width = elw < settings.minimum ? settings.minimum : elw,
            fontBase = width / settings.fontRatio,
            fontSize = fontBase > settings.maxFont ? settings.maxFont : fontBase < settings.minFont ? settings.minFont : fontBase;

         if (settings.onlyFontResizing) {
            $el.css({
               'font-size': fontSize + 'px',
               'line-height': fontSize * settings.lineRatio + 'px',
            });
         } else {
            $el.css({
               'font-size': fontSize + 'px',
               'line-height': fontSize * settings.lineRatio + 'px',
               'padding-left': paddingw + 'px',
               'padding-right': paddingw + 'px',
               'width': elw + 'px',
               'height': elh + 'px',
            });
         }
      };

      return this.each(function() {
         changes(this);
      });
   };
}(jQuery));
