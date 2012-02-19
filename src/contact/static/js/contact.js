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
} 

// post-submit callback 
function showResponse(responseJSON, statusText, xhr, $form)  { 
    if(responseJSON['success']){
        $('#response-message-success').html(responseJSON['html']);
        $('#response-modal-success').modal();
    } else {
        $('#response-message-error').html(responseJSON['html']);
        $('#response-modal-error').modal();
    };
} 
