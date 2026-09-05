const baseUrl = "https://api.restful-api.dev";

async function addProduct(data) {
  try {
    const response = await fetch(`${baseUrl}/objects`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });
    return await response.json();
  } catch (error) {
    console.error("Error al agregar el producto:", error.message);
  }
}

async function getProduct(id) {
  try {
    const response = await fetch(`${baseUrl}/objects/${id}`);
    return await response.json();
  } catch (error) {
    console.error("Error al obtener el producto:", error.message);
  }
}

async function updateProduct(id, data) {
  try {
    const response = await fetch(`${baseUrl}/objects/${id}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });
    return await response.json();
  } catch (error) {
    console.error("Error al actualizar el producto:", error.message);
  }
}

async function main() {
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
