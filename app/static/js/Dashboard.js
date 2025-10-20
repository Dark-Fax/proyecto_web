document.addEventListener("DOMContentLoaded", () => {
  // === Nombre del usuario ===
  const nombreUsuario = document.getElementById("nombreUsuario");
  // No podemos usar {{ usuario_nombre }} aquí directamente en JS externo
  // Mejor pasarlo desde HTML usando Jinja en un data-attribute o directamente en el span

  // === Noticias de ejemplo ===
  const noticias = [
    { id: 1, titulo: "Futuro eléctrico", categoria: "Autos", vistas: 1200, texto: "Un vistazo al futuro de los vehículos eléctricos y autónomos.", vista: false },
    { id: 2, titulo: "Baterías de hidrógeno", categoria: "Energía", vistas: 980, texto: "Las nuevas baterías prometen revolucionar el mercado.", vista: false },
    { id: 3, titulo: "Comparativa de precios", categoria: "Precios", vistas: 1500, texto: "Comparativa entre los nuevos modelos eléctricos.", vista: true }
  ];

  const listaNoticias = document.getElementById("newsList");
  const btnSinVer = document.getElementById("btnSinVer");
  const btnVistas = document.getElementById("btnVistas");
  const logoutBtn = document.getElementById("logoutBtn");
  const logoutUrl = logoutBtn.dataset.logoutUrl; // URL pasada desde HTML

  // === Renderizar noticias ===
  function renderNoticias(filtro = "sinver") {
    listaNoticias.innerHTML = "";
    const filtradas = filtro === "sinver" ? noticias.filter(n => !n.vista) : noticias.filter(n => n.vista);

    if (filtradas.length === 0) {
      listaNoticias.innerHTML = "<p>No hay noticias en esta categoría.</p>";
      return;
    }

    filtradas.forEach(n => {
      const card = document.createElement("div");
      card.classList.add("news-card");

      card.innerHTML = `
        <div class="news-info">
          <h3>${n.titulo}</h3>
          <p>Categoría: ${n.categoria} • ${n.vistas} vistas</p>
          <p>${n.texto}</p>
        </div>
        <div class="news-actions" data-id="${n.id}">
          ⭐⭐⭐⭐${n.vista ? "⭐" : "☆"} 
          <span class="like" style="cursor:pointer;">${n.vista ? "❤️" : "🤍"}</span>
        </div>
      `;

      card.querySelector(".like").addEventListener("click", () => {
        n.vista = !n.vista;
        renderNoticias(filtro);
      });

      listaNoticias.appendChild(card);
    });
  }

  renderNoticias();

  // === Filtros de noticias ===
  btnSinVer.addEventListener("click", () => {
    btnSinVer.classList.add("activo");
    btnVistas.classList.remove("activo");
    renderNoticias("sinver");
  });

  btnVistas.addEventListener("click", () => {
    btnVistas.classList.add("activo");
    btnSinVer.classList.remove("activo");
    renderNoticias("vistas");
  });

  // === Menú lateral ===
  const menuItems = document.querySelectorAll("#menu li");
  const secciones = document.querySelectorAll(".main-section");

  menuItems.forEach(item => {
    item.addEventListener("click", () => {
      menuItems.forEach(i => i.classList.remove("active"));
      item.classList.add("active");

      const target = item.getAttribute("data-section");
      secciones.forEach(sec => {
        sec.style.display = sec.id === target ? "block" : "none";
      });
    });
  });

  // === Logout ===
  logoutBtn.addEventListener("click", () => {
    window.location.href = logoutUrl;
  });
});
