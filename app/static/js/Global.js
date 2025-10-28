// 🌍 global.js — Funciones universales para todas las vistas
document.addEventListener("DOMContentLoaded", () => {
    console.log("✅ Global.js cargado correctamente");

    const logoutBtn = document.getElementById("logoutBtn");
    const nombreUsuario = document.getElementById("nombreUsuario");

  // === Guardar nombre en sessionStorage si viene del HTML ===
    if (nombreUsuario) {
        const nombre = nombreUsuario.textContent.trim();
        if (nombre) {
            sessionStorage.setItem("usuario_nombre", nombre);
            console.log("👤 Usuario guardado en sessionStorage:", nombre);
        }
    }

  // === Mostrar nombre desde sessionStorage si existe ===
    const storedUser = sessionStorage.getItem("usuario_nombre");
    if (storedUser && nombreUsuario) {
        nombreUsuario.textContent = storedUser;
    }

  // === Botón universal de cerrar sesión ===
    if (logoutBtn) {
        logoutBtn.addEventListener("click", () => {
        const logoutUrl = logoutBtn.dataset.logoutUrl;
        if (logoutUrl) {
            console.log("👋 Cerrando sesión...");
            sessionStorage.clear(); // Limpia datos locales
            window.location.href = logoutUrl; // Redirige al logout de Flask
        } else {
            console.error("⚠️ No se encontró la URL de logout.");
        }
    });
    } else {
        console.warn("⚠️ Botón de logout no encontrado en esta vista.");
    }


// 🔁 Botón "Volver" (nuevo)
    const btnVolver = document.getElementById("btnVolver");
    if (btnVolver) {
        btnVolver.addEventListener("click", () => {
            const url = btnVolver.dataset.url;
            if (url) {
                window.location.href = url;
            }
            });
    }

    document.addEventListener("DOMContentLoaded", () => {
        const btnVolver = document.getElementById("btnVolver");
        if (btnVolver) {
            btnVolver.addEventListener("click", () => {
                window.location.href = "{{ url_for('vehiculos.listar') }}";
        });
    }
});

});
