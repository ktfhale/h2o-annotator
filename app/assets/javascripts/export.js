var all_tts;
var annotations;
var original_data = {};
var layer_data;
var collage_id;
var h2o_annotator;

var collages = {
  listenToRecordCollageState: function() {
    //do nothing
  },
  clean_layer: function(layer_name) {
    return layer_name.replace(/ /, 'whitespace').replace(/\./, 'specialsymbol');
  },
  rehighlight: function() {
    //do nothing
  },
  hideShowUnlayeredOptions: function() {
    //do nothing
  },
  updateWordCount: function() {
    //do nothing
  },
  loadState: function(collage_id, data) {
    $.each(data, function(i, e) {
	   if(i.match(/^unlayered/)) {
		    $('#collage' + collage_id + ' .unlayered-' + e).remove();
		    $('#collage' + collage_id + ' .unlayered-ellipsis-' + e).replaceWith($('<span>').addClass('unlayered-ellipsis').html('[...]').show());
		  } else if(i.match(/^layered/)) {
		      $('#collage' + collage_id + ' .annotation-' + e).remove();
		      $('#collage' + collage_id + ' .layered-ellipsis-' + e).replaceWith($('<span>').addClass('layered-ellipsis').html('[...]').show());
      } else if(i == 'font_face') {
        $('#fontface').val(e);
      } else if(i == 'font_size') {
        $('#fontsize').val(e);
      } else if(i == 'highlights') {
        $('#printhighlights').val('original');
        export_functions.highlightCollage(collage_id, e);
      }
    });
    $('#collage' + collage_id + ' .unlayered-ellipsis:not(:visible),#collage' + collage_id + ' .layered-ellipsis:not(:visible)').remove();

    $.each(['a', 'em', 'sup', 'p', 'center', 'h2', 'pre'], function(i, selector) {
      var set = $('#collage' + collage_id + ' div.article ' + selector);
      set = set.filter(':not(:visible):not(:has(*:visible)):not(.paragraph-numbering)');
      if(selector == 'em') {
        set = set.filter(':not(.original_content)');
      }
      if(selector == 'a') {
        set = set.filter(':not(.paragraph-numbering)');
      }
      set.remove();
    });
    
    var cannotations = eval("annotations_" + collage_id);
    $.each(cannotations, function(i, ann) {
      var annotation = $.parseJSON(ann);
      if(annotation.annotation != '') {
        $('<span>').addClass('annotation-content annotation-content-' + annotation.id).html(annotation.annotation).insertAfter($('.annotation-' + annotation.id + ':last'));
      }
    });
  }
};

var export_functions = {
  init: function() {
    if(document.location.hash.match('fontface')) {
      var vals = document.location.hash.replace('#', '').split('-');
      for(var i in vals) {
        var font_values = vals[i].split('=');
        if(font_values[0] == 'fontsize' || font_values[0] == 'fontface') {
          $('#' + font_values[0]).val(font_values[1]);
        }
      }
    }

    if($.cookie('user_id') !== null) {
      if($.cookie('print_titles') == 'false') {
        $('#printtitle').val('no');
	      $('h1').hide();
	      $('.playlists h3').hide();
      }
      if($.cookie('print_dates_details') == 'false') {
        $('#printdetails').val('no');
	      $('.details').hide();
      }
      if($.cookie('print_paragraph_numbers') == 'false') {
        $('#printparagraphnumbers').val('no');
	      $('.paragraph-numbering').hide();
	      $('.collage-content').css('padding-left', '0px');
      }
      if($.cookie('print_annotations') == 'true') {
        $('#printannotations').val('yes');
        $('.annotation-content').show();
      }
      if($.cookie('print_highlights') == 'none') {
        $('#printhighlights').val('none');
	      $('.collage-content').each(function(i, el) {
	        var id = $(el).data('id');
	        export_functions.highlightCollage(id, {});
	      });
      } else if($.cookie('print_highlights') == 'all') {
        $('#printhighlights').val('all');
	      $('.collage-content').each(function(i, el) {
	        var id = $(el).data('id');
	        export_functions.highlightCollage(id, eval("layer_data_" + id));
	      });
      }
      $('#fontface').val($.cookie('print_font_face'));
      $('#fontsize').val($.cookie('print_font_size'));
    }

	  $('#fontface').selectbox({
	    className: "jsb", replaceInvisible: true
	  }).change(function() {
	    export_functions.setFontPrint();
	  });
	  $('#fontsize').selectbox({
	    className: "jsb", replaceInvisible: true
	  }).change(function() {
	    export_functions.setFontPrint();
	  });
	  $('#printannotations').selectbox({
	    className: "jsb", replaceInvisible: true
	  }).change(function() {
      // Go through annotation content
      if($(this).val() == 'yes') {
        $('.annotation-content').show();
      } else {
        $('.annotation-content').hide();
      }
	  });

	  $('#printtitle').selectbox({
	    className: "jsb", replaceInvisible: true
	  }).change(function() {
	    var choice = $(this).val();
	    if (choice == 'yes') {
	      $('h1').show();
	      $('.playlists h3').show();
	    }
	    else {
	      $('h1').hide();
	      $('.playlists h3').hide();
	    }
	  });
	  $('#printdetails').selectbox({
	    className: "jsb", replaceInvisible: true
	  }).change(function() {
	    var choice = $(this).val();
	    if (choice == 'yes') {
	      $('.details').show();
	    }
	    else {
	      $('.details').hide();
	    }
	  });
	  $('#printparagraphnumbers').selectbox({
	    className: "jsb", replaceInvisible: true
	  }).change(function() {
	    var choice = $(this).val();
	    if (choice == 'yes') {
	      $('.paragraph-numbering').show();
	      $('.collage-content').css('padding-left', '50px');
	    }
	    else {
	      $('.paragraph-numbering').hide();
	      $('.collage-content').css('padding-left', '0px');
	    }
	  });
	  $('#printhighlights').selectbox({
	    className: "jsb", replaceInvisible: true
	  }).change(function() {
	    var choice = $(this).val();
      $('#highlight_styles').text('');
	    if(choice == 'original') {
	      $('.collage-content').each(function(i, el) {
	        var id = $(el).data('id');
	        var data = eval("collage_data_" + id);
	        export_functions.highlightCollage(id, data.highlights);
	      });
	    } else if(choice == 'all') {
	      $('.collage-content').each(function(i, el) {
	        var id = $(el).data('id');
	        export_functions.highlightCollage(id, eval("layer_data_" + id));
	      });
	    } else {
	      $('.collage-content').each(function(i, el) {
	        var id = $(el).data('id');
	        export_functions.highlightCollage(id, {});
	      });
	    }
	  });

	  export_functions.setFontPrint();
  },
  setFontPrint: function() {
    var font_size = $('#fontsize').val();
    var font_face = $('#fontface').val();
    var base_font_size = h2o_fonts.base_font_sizes[font_face][font_size];

    var base_selector = 'body#' + $('body').attr('id') + ' .singleitem';
    if(font_face == 'verdana') {
      $.rule(base_selector + " * { font-family: Verdana, Arial, Helvetica, Sans-serif; font-size: " + base_font_size + 'px; }').appendTo('#additional_styles');
    } else {
      $.rule(base_selector + " * { font-family: '" + h2o_fonts.font_map[font_face] + "'; font-size: " + base_font_size + 'px; }').appendTo('#additional_styles');
    }
    $.rule(base_selector + ' *.scale1-5 { font-size: ' + base_font_size*1.5 + 'px; }').appendTo('#additional_styles');
    $.rule(base_selector + ' *.scale1-4 { font-size: ' + base_font_size*1.4 + 'px; }').appendTo('#additional_styles');
    $.rule(base_selector + ' *.scale1-3 { font-size: ' + base_font_size*1.3 + 'px; }').appendTo('#additional_styles');
    $.rule(base_selector + ' *.scale1-2 { font-size: ' + base_font_size*1.2 + 'px; }').appendTo('#additional_styles');
    $.rule(base_selector + ' *.scale1-1 { font-size: ' + base_font_size*1.1 + 'px; }').appendTo('#additional_styles');
    $.rule(base_selector + ' *.scale0-9 { font-size: ' + base_font_size*0.9 + 'px; }').appendTo('#additional_styles');
    $.rule(base_selector + ' *.scale0-8,' + base_selector + ' *.scale0-8 * { font-size: ' + base_font_size*0.8 + 'px; }').appendTo('#additional_styles');
  },
  loadAnnotator: function(id) {
    annotations = eval("annotations_" + id);

    var elem = $('#collage' + id + ' div.article');
    var factory = new Annotator.Factory();
    var Store = Annotator.Plugin.fetch('Store');
    var h2o = Annotator.Plugin.fetch('H2O');

    h2o_annotator = factory.addPlugin(h2o, layer_data).getInstance();
    h2o_annotator.attach(elem);
    h2o_annotator.plugins.H2O.loadAnnotations(id, annotations, true);
  },
  filteredLayerData: function(layer_data) {
    var filtered_layer_data = {}; 
    $.each(layer_data, function(i, j) {
      filtered_layer_data[collages.clean_layer(i)] = j;
    });
    return filtered_layer_data;
  },
  highlightCollage: function(collage_id, highlights) {
    if(highlights === undefined) {
      highlights = {};
    }
    layer_data = export_functions.filteredLayerData(eval("layer_data_" + collage_id));

    var keys = new Array();
    $.each(highlights, function(i, j) {
      keys.push(collages.clean_layer(i));
    });

    $.each(layer_data, function(i, j) {
      if($.inArray(i, keys) == -1) {
        $('#collage' + collage_id + ' .layer-' + i).removeClass('highlight-' + i);
      }
    });

    $.each(highlights, function(i, j) {
      $('#collage' + collage_id + ' .annotator-wrapper .layer-' + collages.clean_layer(i)).addClass('highlight-' + collages.clean_layer(i));
    });
    $('#collage' + collage_id + ' .layered-empty').removeClass('layered-empty');

	  var total_selectors = new Array();
	  $.each($('#collage' + collage_id + ' .annotator-wrapper .annotator-hl'), function(i, child) {
	    var this_selector = '';
	    var parent_class = '';
	    var classes = $(child).attr('class').split(' ');
	    for(var j = 0; j<classes.length; j++) {
	      if(classes[j].match(/^highlight/)) {
	        parent_class += '.' + classes[j];
	      }
	    }
	    if(parent_class != '') {
	      this_selector = parent_class;
	    }

	    $.each($(child).parentsUntil('.annotator-wrapper'), function(j, node) {
	      if($(node).is('span.annotator-hl')) {
	        var selector_class = '';
	        var classes = $(node).attr('class').split(' ');
	        for(var j = 0; j<classes.length; j++) {
	          if(classes[j].match(/^highlight/)) {
	            selector_class += '.' + classes[j];
	         }
	        }
	        if(selector_class != '') {
	          this_selector = selector_class + ' ' + this_selector;
	        }
	      }
	    });
	    if(this_selector != '') {
	      total_selectors.push(this_selector.replace(/ $/, ''));
	    }
	  });
	  var updated = {};
	  for(var i = 0; i<total_selectors.length; i++) {
	    updated[total_selectors[i]] = 0;
	  }

	  for(var i = 0; i<total_selectors.length; i++) {
	    var selector = total_selectors[i];
	    if(updated[selector] == 0) {
	      var unique_layers = {};
	      var layer_count = 0;
	      var x = selector.split(' ');
	      for(var a = 0; a < x.length; a++) {
	        var y = x[a].split('.');
	        for(var b = 0; b < y.length; b++) {
	          var key = y[b].replace(/^highlight-/, '');
	          if(key != '') {
	            unique_layers[key] = 1;
	          }
	        }
	      }
	      var current_hex = '#FFFFFF';
	      var key_length = 0;
	      $.each(unique_layers, function(key, value) {
	        key_length++;
	      });
	      var opacity = 0.4 / key_length;
	      $.each(unique_layers, function(key, value) {
	        var color_combine = $.xcolor.opacity(current_hex, layer_data[key], opacity);
	        current_hex = color_combine.getHex();
	      });
	      $.rule('#collage' + collage_id + ' ' + selector + ' { border-bottom: 2px solid ' + current_hex + '; }').appendTo('#highlight_styles');
	      updated[selector] = 1;
	    }
	  }
	  var keys_arr = new Array();
	  $.each(updated, function(key, value) {
	    keys_arr.push(key);
	  });
    if(keys_arr.length > 0) {
	    $('#collage' + collage_id + ' .annotator-hl:not(' + keys_arr.join(',') + ')').addClass('layered-empty');
    } else {
      $('#collage' + collage_id + ' .annotator-hl').addClass('layered-empty');
    }
  }
};

$(document).ready(function(){
  $('article sub, article sup, div.article sub, div.article sup').addClass('scale0-8');
  $('article h1, div.article h1').addClass('scale1-4');
  $('article h2, div.article h2').addClass('scale1-3');
  $('article h3, div.article h3').addClass('scale1-2');
  $('article h4, div.article h4').addClass('scale1-1');

  $('.collage-content').each(function(i, el) {
    export_functions.loadAnnotator($(el).data('id')); 
  });

  export_functions.init();
});
