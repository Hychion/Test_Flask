function updateActiveNavItem() {
  // Obtenez l'URL actuelle sans la partie query
  var currentPath = window.location.pathname;

  // Sélectionnez tous les éléments de navigation
  var navItems = document.querySelectorAll('.nav .nav-item .nav-link');

  // Boucle à travers les éléments de navigation
  navItems.forEach(function(item) {
    // Retirez la classe 'active' si elle est présente
    item.classList.remove('active');

    // Récupérez le chemin de l'élément de navigation
    var itemPath = item.getAttribute('href');

    // Si le chemin correspond à l'URL actuelle, ajoutez la classe 'active'
    if (currentPath === itemPath) {
      item.setAttribute('class','nav-link active')
    }
  });
}

// Appeler la fonction au chargement de la page et à chaque changement d'état de l'historique
document.addEventListener('DOMContentLoaded', updateActiveNavItem);
window.addEventListener('popstate', updateActiveNavItem);