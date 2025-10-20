document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("loginForm");
    const usuarioInput = document.getElementById("usuario");
    const passwordInput = document.getElementById("password");

    form.addEventListener("submit", (event) => {
        event.preventDefault(); // Evita recargar la página

        const usuario = usuarioInput.value.trim();
        const password = passwordInput.value.trim();

        if (!usuario || !password) {
            alert("Por favor, ingresa tu usuario y contraseña.");
            return;
        }

        // Simulación de inicio de sesión
        // Aquí luego puedes reemplazar por una validación real (backend)
        if (usuario === "admin" && password === "1234") {
            alert(`¡Bienvenido, ${usuario}!`);
            // Ejemplo: redirigir a otra página
            window.location.href = "inicio.html";
        } else {
            alert("Usuario o contraseña incorrectos. Intenta nuevamente.");
        }

        form.reset();
    });
});