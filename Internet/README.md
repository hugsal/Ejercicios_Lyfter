# Analisis de API

**JSON Placeholder** es un API para poner en practica la peticiones HTTP y el manejo de JSON.
no necesita autenticación y es totalmente gratuito.

Para este analisis se utilizaran los siguientes metodos HTTP:

- **GET**
- https://jsonplaceholder.typicode.com/posts
- esta peticion no necesita parametros ni cuerpo de solicitud.
- la repuesta es un array de objetos, cada objeto tiene las propiedades: userId, id, title, body y code status **200**
```[
    {
        "userId": 1,
        "id": 1,
        "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
        "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
    },
    {
        "userId": 1,
        "id": 2,
        "title": "qui est esse",
        "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"
    }
]
```

- **POST**
- https://jsonplaceholder.typicode.com/posts
```
{
    "title": "foo",
    "body": "bar",
    "userId": 1
}
```
- la respuesta es un objeto con las propiedades: userId, id, title, body y code status **201**
```
{
    "title": "foo",
    "body": "bar",
    "userId": 1,
    "id": 101
}
```

- **DELETE**
- https://jsonplaceholder.typicode.com/posts/:id
- esta peticion necesita el id como parametro
- la respuesta es un objeto vacio con code status **200**

En conclusion JSONPlaceholder es un API muy util para poner en practica la peticiones HTTP, con la posibilidad de hacer peticiones GET, POST, PUT y DELETE, ademas de tener un code status y una respuesta para cada peticion.
Con esta practicaq queda entendido el funcionamiento de las API REST por medio de peticiones HTTP
