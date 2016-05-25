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
/*
    var request = {
          location:
    };*/

    //Places service

    
    //fire map
    var map = new google.maps.Map(document.getElementById('map'), mapOptions);

    //Grap form data
/*    $("#form").submit(function(){
     //relocate map
          var userDest = $("#destination").val();
          var userType = $("#type").val();
          var restaurants;
          var accessURL;

          if(userDest){
          accessURL = "https://maps.googleapis.com/maps/api/geocode/json?address="+userDest+"&key=AIzaSyDtUacD4feeXpYF3Fg_XkSAGqa7ZehTk2c"
          }
          else{
          accessURL = "https://maps.googleapis.com/maps/api/geocode/json?latlng="+ userCords.latitude +","+ userCords.longitude +"&key=AIzaSyDtUacD4feeXpYF3Fg_XkSAGqa7ZehTk2c"
          }


          $.get(accessURL, function(loc){

          userLat = loc.results[0].geometry.location.lat;
          userLon = loc.results[0].geometry.location.lng;
          newCenter = new google.maps.LatLng(userLat, userLon)
          map.setCenter(newCenter);
          }, 'json');


          return false;
     });*/
});