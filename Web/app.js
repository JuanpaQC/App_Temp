document.addEventListener('DOMContentLoaded', function() {
    const mostrarTemperaturasButton = document.getElementById('mostrarTemperaturasBtn');
  
    mostrarTemperaturasButton.addEventListener('click', function() {
        const fechaInput = document.querySelector('input[type="date"]').value;
        
        // Verificar si se seleccionó una fecha
        if (!fechaInput) {
            console.error('¡Por favor selecciona una fecha!');
            return;
        }

        // Mostrar un mensaje al usuario para confirmar la fecha seleccionada
        const confirmacion = confirm(`¿Consultar temperaturas para la fecha ${fechaInput}?`);

        if (confirmacion) {
            mostrarTemperaturas(fechaInput);
        }
    });
});

async function mostrarTemperaturas(fechaInput) {
    try {
        // Convertir la fecha al formato 'dd-mm-yyyy'
        const fechaFormateada = formatDate(fechaInput);
  
        const snapshot = await firebase.firestore().collection('App_Temp').doc(fechaFormateada).get();
        if (!snapshot.exists) {
            console.log('El documento no existe para la fecha:', fechaFormateada);
            return;
        }
  
        const data = snapshot.data();
        const temperaturas = data.temperaturas;
        const contenedor = document.getElementById('temperaturas-container');
    
        contenedor.innerHTML = '';
    
        temperaturas.forEach((temperatura, index) => {
            const temperaturaDiv = document.createElement('div');
            temperaturaDiv.classList.add('temperatura');
            temperaturaDiv.innerHTML = `
                <h3>Temperatura ${index + 1}</h3>
                <p><strong>Celsius:</strong> ${temperatura.celcius}</p>
                <p><strong>Fahrenheit:</strong> ${temperatura.fahrenheit}</p>
                <p><strong>Fecha:</strong> ${temperatura.date}</p>
                <p><strong>Hora:</strong> ${temperatura.hour}</p>
            `;
            contenedor.appendChild(temperaturaDiv);
        });
    } catch (error) {
        console.error('Error al mostrar las temperaturas:', error);
    }
}

// Función para formatear la fecha al formato 'dd-mm-yyyy'
function formatDate(date) {
    const [year, month, day] = date.split('-');
    return `${day}-${month}-${year}`;
}
