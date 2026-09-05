const baseUrl = "https://api.restful-api.dev";

async function getProduct() {
  try {
    const response = await fetch(`${baseUrl}/objects`);
    let data = await response.json();
    data = data.filter((item) => item.data);
    data.forEach((item) => {
      const info = item.data;
      Object.assign(item, info);
      delete item.data;
    });
    console.log(data);
  } catch (error) {
    console.error("Error al obtener los productos:", error.message);
  }
}

getProduct();
