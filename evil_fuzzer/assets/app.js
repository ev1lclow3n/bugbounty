function getKeywordss(){
    $.get($('#urla').val(), function(resp) {
        document.getElementById('keywords1').value = resp;
    });
}

function Generate() {
    // Clear previous results
    $('#results').empty();

    // Get payloads from the keywords1 textarea
    var payloads = $('#keywords1').val().split('\n');
    var targetUrl = $('#targets').val();

    // Generate URLs and make them clickable
    $.each(payloads, function(index, payload) {
        if (payload.trim() !== '') {
            var modifiedUrl = targetUrl.replace('FUZZ', encodeURIComponent(payload.trim()));
            var link = $('<a></a>').attr('href', modifiedUrl).attr('target', '_blank').text(modifiedUrl);
            $('#results').append(link).append('<br>');
        }
    });
}