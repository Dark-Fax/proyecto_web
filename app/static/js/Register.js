// Esperamos a que el contenido del DOM esté listo
document.addEventListener("DOMContentLoaded", () => {
    // Obtenemos el formulario y los campos
    const form = document.getElementById("registroForm");
    const usuarioInput = document.getElementById("usuario");
    const emailInput = document.getElementById("email");
    const passwordInput = document.getElementById("password");
    const telefonoInput = document.getElementById("telefono");

    // Escuchamos el evento "submit"
    form.addEventListener("submit", (event) => {
        event.preventDefault(); // Evita que se recargue la página

        // Obtenemos los valores ingresados
        const usuario = usuarioInput.value.trim();
        const email = emailInput.value.trim();
        const password = passwordInput.value.trim();
        const telefono = telefonoInput.value.trim();

        // Validaciones básicas
        if (!usuario || !email || !password || !telefono) {
            alert("Por favor, completa todos los campos.");
            return;
        }

        if (!/^[0-9]{10}$/.test(telefono)) {
            alert("El teléfono debe tener exactamente 10 dígitos numéricos.");
            return;
        }

        // Si todo está correcto, mostramos los datos (puedes luego enviarlos a tu backend)
        console.log("=== Datos del Registro ===");
        console.log("Usuario:", usuario);
        console.log("Email:", email);
        console.log("Contraseña:", password);
        console.log("Teléfono:", telefono);

        // Ejemplo: mostrar un mensaje de éxito
        alert(`¡Registro exitoso!\nBienvenido, ${usuario}.`);

        // Opcional: limpiar el formulario
        form.reset();
    });
});
