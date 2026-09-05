const axiosInstance = axios.create({
  baseURL: "https://api.restful-api.dev",
  timeout: 1000,
  headers: { "content-type": "application/json" },
});

async function listProducts() {
  const { data: list } = await axiosInstance.get("/objects");
  return list;
}

async function addProduct(data) {
  try {
    const { data: response } = await axiosInstance.post("/objects", data);
    return response;
  } catch (error) {
    console.error("Error al agregar el producto:", error.message);
  }
}

async function getProduct(id) {
  try {
    const { data: response } = await axiosInstance.get(`/objects/${id}`);
    return response;
  } catch (error) {
    console.error("Error al obtener el producto:", error.message);
  }
}

async function updateProduct(id, data) {
  try {
    const { data: response } = await axiosInstance.put(`/objects/${id}`, data);
    return response;
  } catch (error) {
    console.error("Error al actualizar el producto:", error.message);
  }
}

async function main() {
  const products = await listProducts();
  console.log(products);

  const newProductData = {
    name: "Hugs phone 16",
    data: {
      year: 2026,
      price: 1849.99,
      "CPU model": "Intel Core i11",
      "Hard disk size": "10 TB",
    },
  };
  const newProduct = await addProduct(newProductData);
  console.log(newProduct);
  const newId = newProduct.id;
  const product = await getProduct(newId);
  console.log(product);
  const productId = product.id;
  delete product.id;
  product.data.price = 1549.99;
  product.name = "Hugs phone 16 Pro Max";
  const updatedProduct = await updateProduct(productId, product);
  console.log(updatedProduct);
}

main();
