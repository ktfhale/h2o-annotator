// jQuery related to form creation and submission

jQuery(function() {

    jQuery("#url_review").live('click', function() {
        var container_id = jQuery('#container_id').text();

        jQuery.ajax({
            type: "post",
            dataType: 'json',
            url: '/playlists/url_check',
            data: {
                'url_string': jQuery("#url_input").val()
            },
            success: function(data, textStatus, XMLHttpRequest){
                jQuery("#result_data").load("/playlists/item_chooser",{
                    'type': data.type,
                    'url_string': data.url_string,
                    'container_id': container_id,
                    'body': data.body
                })
            }
        });


    });

    jQuery("#item_type").live('change', function() {

        jQuery("#playlist_item_form").load("/playlists/load_form",{
            'item_type': jQuery('#item_type').val(),
            'url_string': jQuery('#url_selected').text(),
            'container_id': jQuery('#container_id').text()
        });


    });

    initPlaylistGroup();

    var form_options = {
        //target: '#error_block'  // target element(s) to be updated with server response
        //dataType: 'script'
        //beforeSubmit:  showRequest,  // pre-submit callback
        //success:  function(data) {  },
        //error: showResponse

        error: function(XMLHttpRequest, textStatus, errorThrown) {
            jQuery('#error_block').html(XMLHttpRequest.responseText);
        }

    // other available options:
    //url:       url         // override for form's 'action' attribute
    //type:      type        // 'get' or 'post', override for form's 'method' attribute
    //dataType:  null        // 'xml', 'script', or 'json' (expected server response type)
    //clearForm: true        // clear all form fields after successful submit
    //resetForm: true        // reset the form after successful submit

    // $.ajax options can be used here too, for example:
    //timeout:   3000
    };

    //playlist dialogs
    objectDialog('#dialog-playlist-new', '#new_playlist', rules_playlist, messages_playlist, 'playlists');
    objectDialog('#dialog-playlist-edit', '[id^=edit_playlist]', rules_playlist, messages_playlist, 'playlists');

    objectConfirm('#dialog-playlist-delete', '#delete_playlist', 'playlists');

    //playlist item dialogs
    playlistDialog('#dialog-item-new', rules_item, messages_item, 'playlist_items');
    playlistDialog('#dialog-item-edit', rules_item, messages_item, 'playlist_items');

    objectConfirm('#dialog-item-delete', '#delete_playlist_item', 'playlist_items');

});

// Arrays of validation rules and messages

var rules_playlist = {
    "playlist[output_text]": {
        required: true
    }
};

var messages_playlist = {
    "playlist[output_text]": "Please enter display text"
};

var rules_item = {
    "playlist_item[output_text]": {
        required: true
    }
};

var messages_item = {
    "playlist_item[output_text]": "Please enter display text"
};

function initPlaylistGroup() {

    // Spawn playlist dialog when button is clicked
    initButton('button-playlist-create', '#button-playlist-create', '#dialog-playlist-new', 'playlists', 'new');
    initButton('button-playlist-edit', '[name=button-playlist-edit]', '#dialog-playlist-edit', 'playlists', 'edit');
    initButton('button-playlist-delete', '[name=button-playlist-delete]', '#dialog-playlist-delete', 'playlists', 'delete');

    // Spawn item dialog when button is clicked
    initButton('button-item-create', '[name=button-item-create]', '#dialog-item-new', 'playlist_items', 'new');
    initButton('button-item-edit', '[name=button-item-edit]', '#dialog-item-edit', 'playlist_items', 'edit');
    initButton('button-item-delete', '[name=button-item-delete]', '#dialog-item-delete', 'playlist_items', 'delete');

}

function playlistDialog(dialog_id, rules_block, messages_block, controller_name) {

    var options = {
        success:  function() {
            var container_id = jQuery('#container_id').text();
            var container_id_string = "";
            if (container_id) {
                container_id_string = "?container_id=" + container_id;
            }

            jQuery(dialog_id).dialog('close');
            jQuery('#list_block').load('/' + controller_name + '/block' + container_id_string, function() {
                //initGroup();
                });
        },
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            jQuery('#error_block').html(XMLHttpRequest.responseText);
        }
    };

    jQuery(dialog_id).dialog({
        bgiframe: true,
        autoOpen: false,
        height: "auto",
        position: "top",
        width: 500,
        modal: true,
        buttons: {
            'Submit': function() {
                var dialogObject = this;
                jQuery("form.playlist_form").validate({
                    //debug: true,
                    rules: rules_block,
                    messages: messages_block,
                    submitHandler: function(form) {
                        jQuery(form).ajaxSubmit(options);
                    //jQuery(dialogObject).dialog('close');
                    //jQuery('#list_block').load('/' + controller_name + '/block', function() {initButtonGroup();});

                    },
                    errorClass: "error",
                    errorElement: "div",
                    errorPlacement:  function(error, element) {
                        error.appendTo(element.parent("li").next("li") );
                    }
                });
                jQuery("form.playlist_form").submit();


            },
            'Cancel': function() {
                jQuery(this).dialog('close');
            }
        }
    });

}




