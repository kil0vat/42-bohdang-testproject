$(document).ready(function(){
    $('#id_birth_date').jdPicker({
        date_format: "YYYY-mm-dd"
    });
}); 

$(document).ready(function() { 
    var options = { 
        beforeSubmit: showRequest,
        success: showResponse,
        dataType: 'json'
    };
    $('#contact-form').ajaxForm(options); 

}); 

// pre-submit callback 
function showRequest(formData, jqForm, options) { 
    // set is_ajax_request field value to 1
    $("input[name='is_ajax_request']").val(1);
    options = {
        backdrop: 'static'
    }
    $('#message-submitting-data').modal(options);
} 

// post-submit callback 
function showResponse(responseJSON, statusText, xhr, $form)  { 
    if(responseJSON['success']){
        $('#message-submitting-data').modal('hide');
        $('#response-message-success').html(responseJSON['html']);
        $('#response-modal-success').modal('show');
    } else {
        $('#message-submitting-data').modal('hide');
        $('#response-message-error').html(responseJSON['html']);
        $('#response-modal-error').modal('show');
    };
} 
