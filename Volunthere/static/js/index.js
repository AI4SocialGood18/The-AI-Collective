function send_location(){
    $.ajax({
        type: "GET",
        url: "https://maps.googleapis.com/maps/api/place/autocomplete/json",
        data: {
            "input": $("#location").val(),
            "key": "AIzaSyDm5Fr4W-XPzXpP4WS_NjPUlm9F70QOcVI",
        },
        headers: {
            'X-CSRFToken': $('meta[name="token"]').attr('content')
        },
        success: function(data){
            console.log("success");
            console.log(data);
        },
        failure: function(data){
            console.log("failure");
            console.log(data);
        },
    });
}
