function fazGet(url) {
    let request = new XMLHttpRequest();
    request.open("GET", url, false);
    request.send();
    request = request.responseText;
    request = JSON.parse(request);
    return request
}

function mudarTabela(lat, lon) {
    if (lat && lon) {
        document.getElementById('lat').innerText = lat
        document.getElementById('lon').innerText = lon
    } else {
        document.getElementById('lat').innerText = '----'
        document.getElementById('lon').innerText = '----'
    }
}


function gerarLinkMaps(lat, lon) {
    if (lat && lon){
        var paragMap = document.createElement('p')
        paragMap.classList.add('map-link')
        paragMap.innerHTML = `<iframe src="https://embed.waze.com/iframe?zoom=14&lat=${lat}&lon=${lon}&pin=1" width="500" height="350" allowfullscreen></iframe>`
    
        document.getElementById('mapa').appendChild(paragMap)
    }
}

var visibilidadeMapa = false
function ocultarMapa(){
    let mapa = document.getElementById('mapa')
    let botao = document.getElementById('mostrar-mapa')

    if (!visibilidadeMapa){
        mapa.style.display = 'block'
        botao.innerText = 'Ocultar Mapa'
        visibilidadeMapa = true
    } else {
        mapa.style.display = 'none'
        botao.innerText = 'Mostrar Mapa'
        visibilidadeMapa = false
    }

}

function gerarLatLong(url){
    r = fazGet(url);
    mudarTabela(r.lat, r.lon);
    gerarLinkMaps(r.lat, r.lon)
}


