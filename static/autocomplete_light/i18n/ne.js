/*! Select2 4.1.0-rc.0 | https://github.com/select2/select2/blob/master/LICENSE.md */
var dalLoadLanguage=function(n){var e;(e=n&&n.fn&&n.fn.select2&&n.fn.select2.amd?n.fn.select2.amd:e).define("select2/i18n/ne",[],function(){return{errorLoading:function(){return"नतिजाहरु देखाउन सकिएन।"},inputTooLong:function(n){var e=n.input.length-n.maximum,n="कृपया "+e+" अक्षर मेटाउनुहोस्।";return 1!=e&&(n+="कृपया "+e+" अक्षरहरु मेटाउनुहोस्।"),n},inputTooShort:function(n){return"कृपया बाँकी रहेका "+(n.minimum-n.input.length)+" वा अरु धेरै अक्षरहरु भर्नुहोस्।"},loadingMore:function(){return"अरु नतिजाहरु भरिँदैछन् …"},maximumSelected:function(n){var e="तँपाई "+n.maximum+" वस्तु मात्र छान्न पाउँनुहुन्छ।";return e=1!=n.maximum?"तँपाई "+n.maximum+" वस्तुहरु मात्र छान्न पाउँनुहुन्छ।":e},noResults:function(){return"कुनै पनि नतिजा भेटिएन।"},searching:function(){return"खोजि हुँदैछ…"}}}),e.define,e.require},event=new CustomEvent("dal-language-loaded",{lang:"ne"});document.dispatchEvent(event);