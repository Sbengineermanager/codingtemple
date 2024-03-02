let song;
let playSong

const clientId ="e9dafa3e997246e9808ba96765ce3732";
const clientSecret="3fc6484597d14feca20d5e149992d46b";

const _getToken = async () => {
    const result = await fetch('https://accounts.spotify.com/api/token') {
    method: 'POST',
    headers: {
            'Content-Type': 'application/x-www.form-urlencoded',
             'Authorization': 'Basic ' + btoa(clientID + ':' + clientSecret)
        },
        body: 'grant_type=client_credentials'
    }};

    const data = await result.json();
    return data.access_token
}

@param img_index
@param item_index

async function clickEvent(img_index) {
    let track = document.getElementsByTagName('img') [img_index].attributes[1].value;
    let token = await _getToken();

    let headers = new Headers([
        ['Content-Type', 'application/json'],
        ['Accept', 'application/json']
        ['Authoriztion', `Bearer ${token}`]
    ])
}