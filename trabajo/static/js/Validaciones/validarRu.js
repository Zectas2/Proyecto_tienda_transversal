function validarRegistro(){
    /*Llamamos los datos de campos*/
    let nombreInput = document.querySelector('input[name=nombre]');
    let emailInput = document.querySelector('input[name=email]');
    let contraseñaInput = document.querySelector('input[name=contraseña]');
    /*Definimos datros ingresados como variables*/ 
    let nombreIngresado = nombreInput.value;
    let emailIngresado = emailInput.value;
    let contraseñaIngresada = contraseñaInput.value;
    /*Se definen expresiones regulares*/ 
    let regexNombre = /^[a-zA-Z0-9]{3,20}$/
    let regexEmail = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/
    let regexContraseña = /^(?=.*[A-Z])(?=.*[0-9])[a-zA-Z0-9]{5,11}$/
    /*Se Definen los metodos y validaciones correspondientes*/
    if(!regexNombre.test(nombreIngresado)){
        alert("El nombre debe contener entre 3 y 20 letras y puede contener números y mayusculas.")
        return false;
    }
    if(!regexEmail.test(emailIngresado)){
        alert("El formato del Email debe ser el siguiente: usuario.ejemplo123@example-domain.com.")
        return false;
    }
    if(!regexContraseña.test(contraseñaIngresada)){
        alert(`El formato de la contraseña debe ser el siguiente: P@ssw0rd123.\nDebe tener un largo de 5 y 11 caracteres.`)
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