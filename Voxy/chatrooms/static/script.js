document.addEventListener("DOMContentLoaded", function () {
    const changerTheme = document.getElementById("bouton-changement-theme");
    const body = document.body;

    changerTheme.addEventListener("click", function () {
        body.classList.toggle("theme-sombre");
        updateBoutonTheme();
    });

    function updateBoutonTheme() {
        const iconeTheme = document.getElementById("icone-theme");
        const estModeSombre = body.classList.contains("theme-sombre");
        iconeTheme.className = estModeSombre ? "fas fa-sun" : "fas fa-moon";
    }

    updateBoutonTheme();
});
