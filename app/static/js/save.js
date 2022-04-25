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

function gerarLatLong(url){
    r = fazGet(url);
    mudarTabela(r.lat, r.lon);
}


