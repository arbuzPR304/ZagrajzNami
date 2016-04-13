var geokoder 	= new google.maps.Geocoder();
function geocodeLatLng(latlngStr) {
  var latlngStr2 = (String)(latlngStr).split(',',2);
  var latlng = {lat: parseFloat(latlngStr2[0].replace("(", "")), lng: parseFloat(latlngStr2[1].replace(")", ""))};
  geokoder.geocode({'location': latlng}, function(results, status) {
    if (status === google.maps.GeocoderStatus.OK) {
      if (results[0]) {
      	alert(results[0].formatted_address);
        return (results[0].formatted_address);
      } else {
        window.alert('No results found');
      }
    } else {
      window.alert('Geocoder failed due to: ' + status);
    }
  });
}
