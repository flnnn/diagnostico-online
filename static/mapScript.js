var map = L.map('map').setView([-19.933327, -40.404056], 17);
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {maxZoom: 19, attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'}).addTo(map);
var marker = L.marker([-19.933467, -40.404622]).addTo(map);
