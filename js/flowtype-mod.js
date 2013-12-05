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

/* modified by Toshihiro Kamiya 2013-11-27 */

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
         aspectRatio: 1.33
      }, options),

// Do the magic math
// =================
      changes = function(el) {
         var $el = $(el),
		    elh = $(window).height(),
		    elaw = $(window).width(),
            elw = elaw > settings.aspectRatio * elh ? (elh * settings.aspectRatio) : elaw,
            paddingw = elw < elaw ? (elaw - elw) * 0.5 : 0,
            width = elw < settings.minimum ? settings.minimum : elw,
            fontBase = width / settings.fontRatio,
            fontSize = fontBase > settings.maxFont ? settings.maxFont : fontBase < settings.minFont ? settings.minFont : fontBase;

         $el.css({
            'font-size'   : fontSize + 'px',
            'line-height' : fontSize * settings.lineRatio + 'px',
            'padding-left' : paddingw + 'px',
            'padding-right' : paddingw + 'px',
         });
      };

// Make the magic visible
// ======================
      return this.each(function() {
         
      // Context for resize callback
         var that = this;
         
      // Set changes on load
         changes(this);
         
      // Make changes upon resize
         $(window).resize(function(){changes(that);});
      });
   };
}(jQuery));
