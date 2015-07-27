$('input#submit').click(function() {
    // ajax call
    var entry = $('input#zipcodeInput'),
        zipCode = entry.val(),
        apiUrl = 'https://congress.api.sunlightfoundation.com/legislators/locate?zip=' + zipCode + '&apikey=6b879d65c49742058a88a0b955b3f172';
        templateSource = $("#simple-template").html(),
        template = Handlebars.compile(templateSource);

    $.ajax({
        async: true,
        url: apiUrl,
        dataType: 'jsonp',
        success: function ( response ) {
            var data = response.results;
            $("#main").html(template({data: data}));
        }
    })
});
