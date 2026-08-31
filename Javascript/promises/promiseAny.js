const pokemonIds = [12, 20, 43];

const requests = pokemonIds.map((id) =>
  fetch(`https://pokeapi.co/api/v2/pokemon/${id}`),
);

const results = await Promise.any(requests);

const pokemon = await results.json();

console.log(pokemon.name);
