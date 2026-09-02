async function request(userId) {
  const response = await fetch(`https://reqres.in/api/users/${userId}`);

  if (!response.ok) {
    throw new Error(`HTTP error! Status: ${userId} ${response.statusText}`);
  }

  return response.json();
}

let userIds = [2, 23, 4];

try {
  for await (const id of userIds) {
    const { data } = await request(id);
    console.log(data);
  }
} catch (error) {
  console.log(error.message);
}
