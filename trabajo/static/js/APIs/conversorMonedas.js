//ALMACENA PRECIOS ORIGINALES
let preciosOriginales = {};

// PRECIOS ORIGINALES(REVISION)
function inicializarPreciosOriginales() {
    const obtenerPrecios = document.querySelectorAll('.price');
    obtenerPrecios.forEach((precio, index) => {
        preciosOriginales[index] = precio.textContent.trim();
    });
}

//CARGA LA API
inicializarPreciosOriginales();

//precios originales
function obtenerValorOriginal(precioElemento, index) {
    const precioOriginal = preciosOriginales[index];
    precioElemento.textContent = precioOriginal;
}

//Defenimos las variables de dollar y euro como globales
let dollar, euro;
fetch('https://mindicador.cl/api').then(function(response) {
    return response.json();
}).then(function(dailyIndicators) {
    dollar = dailyIndicators.dolar_intercambio.valor;
    euro = dailyIndicators.euro.valor;
}).catch(function(error) {
    console.log('Requestfailed', error);
});


function coinversor() {
    const preciosBase = obtenerPreciosBase(); 

   
    if (isNaN(dollar) || isNaN(euro) || !preciosBase.every(precio => typeof precio === 'number' && !isNaN(precio))) {
        console.error("Error: Variables no definidas o precios base no válidos.");
        return;
    }
    
    const menuOption = document.querySelector('select[name="coinversorMenu"]');
    const opcionSeleccionada = parseInt(menuOption.value); 

    preciosBase.forEach((precioBase, index) => {
        
        let precioDollar = (precioBase / dollar).toFixed(2);
        let precioEuro = (precioBase / euro).toFixed(2);

        const obtenerPrecioBase = document.querySelectorAll('.price')[index];
        const simboloMoneda = document.querySelectorAll('.simboloMoneda')[index]; 

        if (opcionSeleccionada === 0) {
            obtenerValorOriginal(obtenerPrecioBase, index); //Restaurar precios originales
            simboloMoneda.textContent= "CLP ";
        } else if (opcionSeleccionada === 1) {
            obtenerValorOriginal(obtenerPrecioBase, index);
            obtenerPrecioBase.textContent = precioDollar;
            simboloMoneda.textContent = "$ ";
        } else if (opcionSeleccionada === 2) {
            obtenerValorOriginal(obtenerPrecioBase, index);
            obtenerPrecioBase.textContent = precioEuro;
            simboloMoneda.textContent= "€ ";
        } else {
            console.log("Ha habido un error");
        }
    });
    showHTML();

}

//PRECIOS BASES
function obtenerPreciosBase() {
    const obtenerPrecios = document.querySelectorAll('.price');
    return Array.from(obtenerPrecios).map(precio => {
        const textoPrecio = precio.textContent;
        //expresión regular para capturar el precio completo
        const precioCompleto = textoPrecio.match(/\d+(\.\d+)?/g)[0]; //Captura los dígitos y el punto opcional si es decimal
        return parseFloat(precioCompleto.replace(/\./g, '')); //Remueve el punto antes de convertir a número
    });
}
