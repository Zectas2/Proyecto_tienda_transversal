function validar(){
    /*Llamamos los datos de campos*/
    let nombreInput = document.querySelector('input[name=nombre]');
    let apPaternoInput = document.querySelector('input[name=apellidoPat]');
    let fonoInput = document.querySelector('input[name=fono]');
    let emailInput = document.querySelector('input[name=email]');
    /*Definimos datros ingresados como variables*/ 
    let nombreIngresado = nombreInput.value;
    let apellidoPatIngresado = apPaternoInput.value;
    let fonoIngresado = fonoInput.value;
    let emailIngresado = emailInput.value;
    /*Se definen expresiones regulares*/ 
    let regexNombre = /^[a-zA-Z]{3,11}$/
    let regexApellidos = /^[a-zA-ZáéíóúÁÉÍÓÚñÑ]{3,15}$/
    let regexFono = /^\+\d{10,15}$/
    let regexEmail = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/
    
    /*Se Definen los metodos y validaciones correspondientes*/
    if(!regexNombre.test(nombreIngresado)){
        alert("El nombre debe contener entre 3 y 11 letras y no debe contener números ni caracteres especiales.")
        return false;
    }
    if(!regexApellidos.test(apellidoPatIngresado)){
        alert("Los apellidos deben contener entre 3 y 15 letras y no debe contener números ni caracteres especiales.")
        return false;
    }
    if(!regexFono.test(fonoIngresado)){
        alert("El numero de telefono debe contener debe incluir digito de la region +12312345678 y un large entre 10 y 15 digitos.")
        return false;
    }
    if(!regexEmail.test(emailIngresado)){
        alert("El formato del Email debe ser el siguiente: usuario.ejemplo123@example-domain.com.")
        return false;
    }
    else{
        if(confirm("¿Estas seguro de Enviar los Datos?")){
            alert("Datos Enviados.")
            return true;
            
        }else{
            return false;
        }
            
    }
    
}