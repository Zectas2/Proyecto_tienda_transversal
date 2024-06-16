const fetch = require('node-fetch');

// Función para crear un grupo
async function crearGrupo(nombreGrupo) {
    try {
        const response = await fetch('https://myths.cl/api/grupos.php', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                nombre: nombreGrupo
            })
        });
        const data = await response.json();
        console.log('Grupo creado:', data);
    } catch (error) {
        console.error('Error al crear el grupo:', error);
    }
}

// Función para agregar un producto (o mercancia)
async function agregarProducto(nombreProducto, descripcion, precio, imagen, nombreGrupo) {
    try {
        const response = await fetch('https://myths.cl/api/productos.php', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                nombre_producto: nombreProducto,
                descripcion: descripcion,
                precio: precio,
                imagen: imagen,
                nombre_grupo: nombreGrupo
            })
        });
        const data = await response.json();
        console.log('Producto agregado:', data);
    } catch (error) {
        console.error('Error al agregar el producto:', error);
    }
}

// Llamar a las funciones para crear un grupo y agregar productos
async function main() {
    // Crear un grupo
    await crearGrupo('GrupoEjemplo');

    // Agregar productos
    await agregarProducto('Producto 1', 'Descripción del producto 1', 500, 'url_de_la_imagen_1.jpg', 'GrupoEjemplo');
    await agregarProducto('Producto 2', 'Descripción del producto 2', 750, 'url_de_la_imagen_2.jpg', 'GrupoEjemplo');
    await agregarProducto('Producto 3', 'Descripción del producto 3', 1000, 'url_de_la_imagen_3.jpg', 'GrupoEjemplo');
}

main();
