document.addEventListener('DOMContentLoaded', () => {
    const btnCart = document.querySelector('.container-cart-icon');
    const containerCartProducts = document.querySelector('.container-cart-products');
    const productsList = document.querySelector('.container-items');
    const valorTotal = document.querySelector('.total-pagar');
    const countProducts = document.querySelector('#contador-productos');
    const cartEmpty = document.querySelector('.cart-empty');
    const cartTotal = document.querySelector('.cart-total');
    const rowProduct = document.querySelector('.row-product');

    let allProducts = [];

    if (btnCart) {
        btnCart.addEventListener('click', () => {
            if (containerCartProducts) {
                containerCartProducts.classList.toggle('hidden-cart');
            }
        });
    }

    if (productsList) {
        productsList.addEventListener('click', e => {
            if (e.target.classList.contains('btn-add-cart')) {
                const product = e.target.closest('.item'); // Buscar el contenedor más cercano
                if (product) {
                    const infoProduct = {
                        quantity: 1,
                        id: product.querySelector('.idProducto').textContent,
                        title: product.querySelector('h2').textContent,
                        price: product.querySelector('p.price').textContent,
                    };

                    const exists = allProducts.some(product => product.id === infoProduct.id);

                    if (exists) {
                        const products = allProducts.map(product => {
                            if (product.id === infoProduct.id) {
                                product.quantity++;
                            }
                            return product;
                        });
                        allProducts = [...products];
                    } else {
                        allProducts = [...allProducts, infoProduct];
                    }

                    showHTML();
                }
            }
        });
    }

    rowProduct.addEventListener('click', e => {
        if (e.target.classList.contains('icon-close')) {
            const product = e.target.closest('.cart-product'); // Buscar el contenedor más cercano
            if (product) {
                const id = product.querySelector('.idProducto').textContent;
                const foundIndex = allProducts.findIndex(p => p.id === id);

                if (foundIndex !== -1) {
                    if (allProducts[foundIndex].quantity > 1) {
                        allProducts[foundIndex].quantity--;
                    } else {
                        allProducts.splice(foundIndex, 1);
                    }
                }

                showHTML();
            }
        }
    });

    // Función para mostrar HTML
    const showHTML = () => {
        if (!allProducts.length) {
            cartEmpty.classList.remove('hidden');
            rowProduct.classList.add('hidden');
            cartTotal.classList.add('hidden');
        } else {
            cartEmpty.classList.add('hidden');
            rowProduct.classList.remove('hidden');
            cartTotal.classList.remove('hidden');
        }

        // Limpiar HTML
        rowProduct.innerHTML = '';

        let total = 0;
        let totalOfProducts = 0;

        allProducts.forEach(product => {
            const containerProduct = document.createElement('div');
            containerProduct.classList.add('cart-product');

            // Parsea el precio como un número
            const price = parseFloat(product.price);

            containerProduct.innerHTML = `
                <div class="info-cart-product">
                    <span class="cantidad-producto-carrito">${product.quantity}</span>
                    <p class="titulo-producto-carrito">${product.title}</p>
                    <span class="precio-producto-carrito">${price}</span>
                    <span class="idProducto hidden">${product.id}</span>
                </div>
                <svg
                    xmlns="http://www.w3.org/2000/svg"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke-width="1.5"
                    stroke="currentColor"
                    class="icon-close"
                >
                    <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        d="M6 18L18 6M6 6l12 12"
                    />
                </svg>
            `;

            rowProduct.append(containerProduct);

            // Calcula el subtotal del producto y añádelo al total
            total += product.quantity * price;
            totalOfProducts += product.quantity;
        });

        valorTotal.innerText = `${total.toFixed(2)}`; // Muestra el total con dos decimales
        countProducts.innerText = totalOfProducts;
    };

    // Mostrar productos al cargar la página
    showHTML();
});
