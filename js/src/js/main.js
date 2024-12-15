document.getElementById('fetchPokemonBtn').addEventListener('click', fetchPokemonList);

async function fetchPokemonList() {
  const pokemonListDiv = document.getElementById('pokemonList');
  pokemonListDiv.innerHTML = 'Carregando...';

  try {
    const response = await fetch('https://pokeapi.co/api/v2/pokemon?limit=20');
    const data = await response.json();

    pokemonListDiv.innerHTML = ''; 
    data.results.forEach((pokemon, index) => {
      pokemonListDiv.innerHTML += `
        <div class="item" data-url="${pokemon.url}">
          ${index + 1}. ${pokemon.name.toUpperCase()}
        </div>
      `;
    });

    document.querySelectorAll('.item').forEach(item => {
      item.addEventListener('click', () => fetchPokemonDetails(item.dataset.url));
    });
  } catch (error) {
    pokemonListDiv.innerHTML = 'Erro ao buscar Pokémon!';
    console.error(error);
  }
}

async function fetchPokemonDetails(url) {
  const pokemonDetailsDiv = document.getElementById('pokemonDetails');
  pokemonDetailsDiv.innerHTML = 'Carregando...';

  try {
    const response = await fetch(url);
    const pokemon = await response.json();

    pokemonDetailsDiv.innerHTML = `
      <h3>${pokemon.name.toUpperCase()}</h3>
      <p><strong>Altura:</strong> ${pokemon.height / 10} m</p>
      <p><strong>Peso:</strong> ${pokemon.weight / 10} kg</p>
      <p><strong>Tipos:</strong> ${pokemon.types.map(t => t.type.name).join(', ')}</p>
      <p><strong>Habilidades:</strong> ${pokemon.abilities.map(a => a.ability.name).join(', ')}</p>
      <img src="${pokemon.sprites.front_default}" alt="${pokemon.name}">
    `;
  } catch (error) {
    pokemonDetailsDiv.innerHTML = 'Erro ao buscar detalhes!';
    console.error(error);
  }
}
