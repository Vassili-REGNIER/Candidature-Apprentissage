// Menu
const toggle = document.getElementById('menu-toggle');
const menu = document.querySelector('.menu');

toggle.addEventListener('click', () => {
  menu.classList.toggle('show');
});





// Bouton pour remonter
window.onscroll = function() {
  var btn = document.getElementById("scrollToTopButton");
  if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
    btn.style.display = "block"; // Affiche le bouton quand on descend de 100px
  } else {
    btn.style.display = "none"; // Cache le bouton quand on est tout en haut
  }
};

// Fonction pour remonter en haut de la page
function scrollToTop() {
  window.scrollTo({
    top: 0,
    behavior: 'smooth' // Ajoute un défilement fluide
  });
}


// Bouton pour déscendre jusqu'au boutons
function scrollDown() {
  const targetElement = document.querySelector('.buttons-section');
        targetElement.scrollIntoView({
            behavior: 'smooth', // Défilement fluide
            block: 'start' // Alignement du haut de l'élément avec le haut de la fenêtre
        });
}


// Scroll automatique 
let lastScrollY = 0; // Pour suivre la dernière position Y
// Fonction pour détecter le scroll
function handleScroll() {
    const currentScrollY = window.scrollY;
    // Vérifie si on est tout en haut de la page (position Y = 0) et qu'on scroll vers le bas
    if (currentScrollY < 100 && currentScrollY > lastScrollY) {
        // Descend jusqu'à la section about-me
        const targetElement = document.querySelector('.buttons-section');
        targetElement.scrollIntoView({
            behavior: 'smooth', // Défilement fluide
            block: 'start' // Alignement du haut de l'élément avec le haut de la fenêtre
        });
    }
    // Met à jour la position Y précédente
    lastScrollY = currentScrollY;
}
// Écouter l'événement scroll
//window.addEventListener('scroll', handleScroll);



