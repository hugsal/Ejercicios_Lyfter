const pokemonIds = [10, 25, 40];

const requests = pokemonIds.map((id) =>
  fetch(`https://pokeapi.co/api/v2/pokemon/${id}`),
);

const results = await Promise.all(requests);

const pokemons = await Promise.all(results.map((response) => response.json()));

console.log(pokemons.map((pokemon) => pokemon.name));
