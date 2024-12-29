const API_URL = 'http://127.0.0.1:8000/';

function getArtistas() {
    fetch(`${API_URL}artistas/`)
        .then(response => response.json())
        .then(data => displayArtistas(data))
        .catch(error => console.error('Erro ao buscar artistas:', error));
}

function displayArtistas(artistas) {
    const container = document.getElementById('artistas-list');
    container.innerHTML = '';

    if (artistas.length === 0) {
        container.innerHTML = '<p>Nenhum artista encontrado.</p>';
        return;
    }

    artistas.forEach(artista => {
        const artistaDiv = document.createElement('div');
        artistaDiv.classList.add('item');
        artistaDiv.innerHTML = `
            <h3>${artista.nome}</h3>
            <p><strong>Origem:</strong> ${artista.local}</p>
            <p><strong>Ano de Criação:</strong> ${artista.ano_criacao}</p>
        `;
        container.appendChild(artistaDiv);
    });
}

function submitForm(event) {
    event.preventDefault();

    const nome = document.getElementById('artist-name').value;
    const local = document.getElementById('artist-origin').value;
    const anoCriacao = document.getElementById('creation-year').value;

    const artistaData = { nome, local, ano_criacao: anoCriacao };

    fetch(`${API_URL}artistas/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(artistaData),
    })
        .then(response => response.json())
        .then(() => {
            alert('Artista cadastrado com sucesso!');
            document.getElementById('form-artista').reset();
            getArtistas(); 
        })
        .catch(error => {
            console.error('Erro ao cadastrar artista:', error);
            alert('Erro ao cadastrar artista.');
        });
}

window.onload = getArtistas;
