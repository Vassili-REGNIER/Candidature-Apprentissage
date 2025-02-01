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
  const targetElement = document.querySelector('.my-proposal');
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


/* Barre nav mobile */
// Sélectionner tous les liens de navigation
const menuItems = document.querySelectorAll('.menu li a');

function updateCurrentPage() {
    let currentSection = null;

    // Parcourir les sections pour trouver celle visible
    document.querySelectorAll('section').forEach((section) => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.offsetHeight;

        // Vérifier si la section est visible
        if (window.scrollY >= sectionTop - sectionHeight / 3) {
            currentSection = section.id;
        }
    });

    // Mettre à jour la classe 'current-page'
    menuItems.forEach((item) => {
        const parent = item.parentElement;
        if (item.getAttribute('href') === `#${currentSection}`) {
            parent.classList.add('current-page');
        } else {
            parent.classList.remove('current-page');
        }
    });
}

// Écouter l'événement scroll et appeler la fonction
window.addEventListener('scroll', updateCurrentPage);

// Mettre à jour les classes au chargement initial
window.addEventListener('load', updateCurrentPage);



/* Scrolls animés */
// Sélectionner tous les liens du menu
const menuLinks = document.querySelectorAll('.menu a');

menuLinks.forEach((link) => {
    link.addEventListener('click', (e) => {
        e.preventDefault(); // Empêche le comportement par défaut du lien

        // Récupérer l'ID de la section ciblée
        const targetId = link.getAttribute('href').substring(1); // Enlève le '#' du href
        const targetSection = document.getElementById(targetId);

        // Effectuer un défilement animé vers la section
        targetSection.scrollIntoView({
            behavior: 'smooth', // Scroll fluide
            block: 'start' // Aligner en haut de la page
        });
    });
});


window.onscroll = function() {
  updateProgressBar();
};

function updateProgressBar() {
  let scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
  let scrollHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
  let progress = (scrollTop / scrollHeight) * 100;

  document.querySelector(".progress-indicator").style.width = progress + "%";
}
