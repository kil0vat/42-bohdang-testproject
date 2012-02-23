$(document).ready(function(){

    var options = {
            valueNames: [ 'id', 'time', 'path', 'method', 'priority' ]
    };

    var hackerList = new List('requests', options);

    $('.update-priority').click(function() {
        data = {
            id: $(this).attr('data-id'),
            priority: parseInt($(this).parent().prev(".priority").html(), 10) == 1 ? 0 : 1
        };
        var that = this;
        $.ajax({
            type: "POST",
            url: '/requests/update_priority/',
            data: data,
            dataType: 'json',
            success: function(result) {
                if (result.success){
                    var item = hackerList.get('id', result.id);
                    item.values(
                            {priority: result.priority}
                            );
                } else {
                    alert('Error updating priority');
                }
            }
        });
    });

    $('#filter-1').click(function() {
        hackerList.filter(function(values) {
            if (values.priority == "1") {
                return true;
            } else {
                return false;
            }
        });
        return false;
    });

    $('#filter-0').click(function() {
        hackerList.filter(function(values) {
            if (values.priority == "0") {
                return true;
            } else {
                return false;
            }
        });
        return false;
    });

    $('#show-all').click(function() {
        hackerList.filter();
        return false;
    });
});

// https://docs.djangoproject.com/en/1.3/ref/contrib/csrf/
$(document).ajaxSend(function(event, xhr, settings) {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    function sameOrigin(url) {
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }
    function safeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    if (!safeMethod(settings.type) && sameOrigin(settings.url)) {
        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    }
});
