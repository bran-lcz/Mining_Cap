function enviarDatos() {
    var rut = document.getElementById('rut').value;
    var nombres = document.getElementById('nombres').value;

    var datos = {
        rut: rut,
        nombres: nombres
        // Agrega otros campos según sea necesario
    };

    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/contactanos/', true);  // Actualiza la URL con la ruta de tu vista de Django
    xhr.setRequestHeader('Content-Type', 'application/json');

    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                // Lógica para manejar la respuesta exitosa
                console.log('Datos enviados con éxito');
            } else {
                // Lógica para manejar errores
                console.error('Error al enviar datos');
            }
        }
    };

    xhr.send(JSON.stringify(datos));

    // Devolver false para evitar que el formulario se envíe de la manera tradicional
    return false;
}

