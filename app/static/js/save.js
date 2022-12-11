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
        paragMap.innerHTML = `<a href="https://www.google.com/maps/@${lat},${lon},14z" target="_blank">Mapa</a>`
    
        document.getElementById('mapa').appendChild(paragMap)
    }
}

function gerarLatLong(url){
    r = fazGet(url);
    mudarTabela(r.lat, r.lon);
    gerarLinkMaps(r.lat, r.lon)
}


