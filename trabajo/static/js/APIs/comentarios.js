const cantidadUsuarios = 4;
for (let i = 0; i < cantidadUsuarios; i++) {
    //generador de comentarios
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
        const maxLength = 1;
        let textoLorem = data.text.slice(0,maxLength);
        if(data.text.length > maxLength){
            textoLorem += '...';
        }
    
        //Generador de usuarios
        fetch('https://randomuser.me/api/')
        .then(response => {
            if (!response.ok) {
            throw new Error('Ocurrió un error al obtener los datos');
            }
            return response.json();
        })
        .then(data => {
            // Obtencion los datos
            const user = data.results[0];
            const username = `${user.name.first} ${user.name.last}`;
            const gender = user.gender;
            const age = user.dob.age;
            const nationality = user.nat;
            const image = user.picture.thumbnail;
            //obtenermos la referencia de la secciones
            const obtenerUsuarios = document.querySelector('.usuarios')
            
            //Creamos los Usuarios
            const usuarios = document.createElement('div')
            
            // Mostrar los datos en la consola
            usuarios.innerHTML = `
            <div class="user">
                <img src="${image}" alt="imagen">
                <span class="letraNegra"> Nombre: ${username}-Edad: ${age}- Nacionalidad: ${nationality}</span>
                <div>
                    <p class="letraNegra">${textoLorem}</p> 
                </div>
            </div>
            `;
            obtenerUsuarios.appendChild(usuarios);
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
}