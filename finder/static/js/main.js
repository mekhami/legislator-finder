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
        async: false,
        success: function ( response ) {
            data = response.results;
            console.log( data );
            console.log(templateSource);
            console.log(template(data));
            $("#main").html(template({data: data}));
        }
    })
});
