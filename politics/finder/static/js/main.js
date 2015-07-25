$('input#submit').click(function() {
    // ajax call
    var entry = $('input#zipcodeInput'),
        zipCode = entry.val(),
        apiUrl = 'https://congress.api.sunlightfoundation.com/legislators/locate?zip=' + zipCode + '&apikey=6b879d65c49742058a88a0b955b3f172';
        templateSource = $("#simple-template").html(),
        template = Handlebars.compile(templateSource);

    if (entry.length !== 5) {
        // Add an error message, change the form class to represent the error
    } else {
        $.ajax({
            async: true,
            url: apiUrl,
            dataType: 'jsonp',
            async: false,
            success: function ( response ) {
                data = response.results;
                $("#main").html(template({data: data}));
            }
        })
    }
});
