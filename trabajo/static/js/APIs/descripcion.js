var paragraphs = '1';
fetch('https://api.api-ninjas.com/v1/loremipsum?paragraphs=' + paragraphs, {
    method: 'GET',
    headers: {
        'X-Api-Key': 'nw3wfTQg8y65gkK0XKEI3g==4t1GRS7IBpYisIJe',
        'Content-Type': 'application/json'
    }
})
.then(response => {
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    return response.json();
})
.then(data => {
    const maxLength = 25;
    let textoLorem = data.text.slice(0, maxLength);
    if (data.text.length > maxLength) {
        textoLorem += '.';
    }
    
    // Obtener todos los elementos con clase .descripcion
    const descripciones = document.querySelectorAll('.descripcion');

    descripciones.forEach(descripcion => {
        descripcion.innerHTML = `
            <p class="letraNegra">${textoLorem}</p>
        `;
    });
})
.catch(error => {
    console.error('Error fetching data:', error);
});
