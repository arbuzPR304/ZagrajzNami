 
		<!-- 
			var mapa; 		// obiekt globalny
			var dymek; 		// okno z informacjami
			var latlngStr;
			var geokoder 	= new google.maps.Geocoder();
			
			var rozmiar 			= new google.maps.Size(32,32);
			var rozmiar_cien 		= new google.maps.Size(59,32);
			var punkt_startowy		= new google.maps.Point(0,0);
			var punkt_zaczepienia	= new google.maps.Point(16,16);
			var ikona				= new google.maps.MarkerImage("http://maps.google.com/mapfiles/kml/pal3/icon20.png", rozmiar, punkt_startowy, punkt_zaczepienia);
			var cien 				= new google.maps.MarkerImage("http://maps.google.com/mapfiles/kml/pal3/icon20s.png", rozmiar_cien, punkt_startowy, punkt_zaczepienia);
			var wskaznik			= new google.maps.Marker({icon: ikona, shadow: cien});
						
 		function mapaStart()  
            {  
                var wspolrzedne = new google.maps.LatLng(50.668444, 17.922326);
                var opcjeMapy = {
                    zoom: 15,
                    center: wspolrzedne,
                    mapTypeId: google.maps.MapTypeId.ROADMAP,
                    disableDefaultUI: false
                };
                mapa = new google.maps.Map(document.getElementById("mapka"), opcjeMapy);
                mapa.poi = function(state){

				  var styles = [
				    {
				      "featureType": "transit",
				      "stylers": [
				        { "visibility": "off" }
				      ]
				    },{
				      "featureType": "poi",
				      "stylers": [
				        { "visibility": "off" }
				      ]
				    },
				  ];

				  this.set("styles", (state)? {} : styles );  
				}
				mapa.poi(false);          
                dymek = new google.maps.InfoWindow();
                
                geokoder.geocode({address:"Opole, Rynek 1" }, obslugaGeokodowania);

                google.maps.event.addListener(mapa,'click',function(zdarzenie)
				{
					if(zdarzenie.latLng)	
					{
						latlngStr = zdarzenie.latLng; 
						geocodeLatLng(latlngStr);

					}
				});

            }
			
			function skoczDoAdresu(adres)
			{
				wskaznik.setMap(null);
				geokoder.geocode({address: adres}, function(wyniki, status)
				{
					if(status == google.maps.GeocoderStatus.OK)
					{
						mapa.setCenter(wyniki[0].geometry.location);
						wskaznik.setPosition(wyniki[0].geometry.location);
						wskaznik.setMap(mapa);
						dymek.open(mapa, wskaznik);
						dymek.setContent('<strong>Poszukiwany adres</strong><br />'+adres);
						latlngStr = wyniki[0].geometry.location;
						printAddres();
					}
					else
					{
						alert("Nie znalazłem podanego adresu!");
					}
				});
			}


			
			function obslugaGeokodowania(wyniki, status)
			{
				
			}


		function printAddres(){

			document.getElementById("id_latlong").value = latlngStr;
		}
		--> 
		function geocodeLatLng() {

		  var latlngStr2 = (String)(latlngStr).split(',',2);
		  
		  var latlng = {lat: parseFloat(latlngStr2[0].replace("(", "")), lng: parseFloat(latlngStr2[1].replace(")", ""))};
		  
		  geokoder.geocode({'location': latlng}, function(results, status) {
		    if (status === google.maps.GeocoderStatus.OK) {
		      if (results[0]) {
		        var marker = new google.maps.Marker({
		          position: latlng,
		          mapa: mapa
		        });
		        
		        wskaznik.setPosition(latlngStr);
				wskaznik.setMap(mapa);
		        dymek.setContent('Adres klikniętego punktu:<br />'+results[0].formatted_address);  
				dymek.setPosition(latlngStr);  
				dymek.open(mapa);
		        printAddres();
		        
		      } else {
		        window.alert('No results found');
		      }
		    } else {
		      window.alert('Geocoder failed due to: ' + status);
		    }
		  });
		}