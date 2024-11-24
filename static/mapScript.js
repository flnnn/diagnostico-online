function criarMapa(coordsCenter) {
    let map = L.map('map').setView(coordsCenter, 13);
    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(map);
    return map;
}

function inserirPonto(coords, map, popupText) {
    let marker = L.marker(coords).addTo(map);
    marker.bindPopup(popupText);
    return marker;
}

function criarRaio(coords, map, raio) {
    let circle = L.circle(coords, {
        radius: raio
    }).addTo(map);
    return circle;
}

function validarCep(cep) {
    regex = /^\d{2}\.\d{3}-\d{3}$/;
    if (!regex.test(cep)) {
        return 1;
    }
    return cep.replace(".", "").replace("-", "");
}

function buscarFarmacias() {
    const cep = document.getElementById("cep").value;
    const raio = document.getElementById("raio").value;

    document.getElementById("raio-info").textContent = `Raio: ${raio} metros.`;

    fetch("/buscar", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            cep: cep,
            raio: raio
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            coords = data.coords;
            let mapa = criarMapa(coords);
            document.getElementById("map").style.opacity = "1";
            let seletorRaio = document.getElementById("raio");
            let farmaciasCep = data.pharmacies;

            for (let farmacia of farmaciasCep) {
                inserirPonto([farmacia.geometry.location.lat, farmacia.geometry.location.lng], mapa, `<b>${farmacia["name"]}</b>`);
            }

            criarRaio(coords, mapa, seletorRaio.value);
        } else {
            alert("<!> Não foi possível encontrar farmácias para o CEP informado.");
        }
    });
}
