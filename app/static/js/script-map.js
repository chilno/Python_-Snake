$(document).ready(function(){
    var userCords;
    var location;
    //start geolocation
    if(navigator.geolocation) {
        function error(err) {
            console.log('ERROR('+err.code+'):'+ err.message);
        }
        function success(pos) {
            userCords = pos.coords;
        }
        navigator.geolocation.getCurrentPosition(success, error);
        
    }else{
        alert('Geolocation is not supported in your browser')
    }

    //map options
    var mapOptions = {
        zoom:12,
        center: new google.maps.LatLng(37.7749, -122.4194),
        panControl: false,
        panControlOptions: {
            position: google.maps.ControlPosition.BOTTOM_LEFT
        },
        zoomControl: true,
        zoomControlOptions: {
            style: google.maps.ZoomControlStyle.LARGE,
            position: google.maps.ControlPosition.RIGHT_CENTER
        },
        scaleControl: false
    };
    
    //info window
    var infowindow = new google.maps.InfoWindow({
        content: "holding..."
    });
    
    //fire map
    var map = new google.maps.Map(document.getElementById('map'), mapOptions);

    //Grap form data

    $("#form").submit(function(e){
        e.preventDefault();
        var data = {destination : $('#destination').val(), userCords : userCords};
        $.post('/locate', data, function(res) {

            $('#data').html(res);
           
        });
     });
//    return false;
});