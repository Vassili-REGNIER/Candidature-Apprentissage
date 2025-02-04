// Menu
const toggle = document.getElementById('menu-toggle');
const menu = document.querySelector('.menu');

toggle.addEventListener('click', (event) => {
  menu.classList.toggle('show');
  event.stopPropagation(); // Empêche la propagation du clic vers le document
});

// Cache le menu lorsqu'on clique autre part que sur le bouton menu
document.addEventListener('click', (event) => {
  if (!toggle.contains(event.target)) {
    menu.classList.remove('show');
  }
});


// Bouton pour remonter
window.addEventListener("scroll", function () {
  const scrollToTopButton = document.getElementById("scrollToTopButton");

  if (window.scrollY > 100) {
    scrollToTopButton.style.display = "flex"; // Affiche le bouton
  } else {
    scrollToTopButton.style.display = "none"; // Cache le bouton quand on est en haut
  }
});

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


/* Barre nav mobile */
// Sélectionner tous les liens de navigation
const menuItems = document.querySelectorAll('.menu li a');

function updateCurrentPage() {
    let currentSection = 'presentation-section';

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










document.querySelectorAll('.links-wrapper a').forEach(anchor => {
  anchor.addEventListener('click', function(e) {
      e.preventDefault();
      
      const slidesContainer = document.querySelector('.slides');
      const slides = document.querySelectorAll('.slide');
      const slideWidth = slides[0].offsetWidth + parseInt(getComputedStyle(slidesContainer).gap); 
      
      const index = Array.from(document.querySelectorAll('.links-wrapper a')).indexOf(this);
      const scrollPosition = index * slideWidth;
      
      slidesContainer.scrollTo({
          left: scrollPosition,
          behavior: 'smooth'
      });
  });
});

/* Support Swipe (Mobile) */
const slidesContainer = document.querySelector('.slides');
let startX = 0;
let scrollLeftStart = 0;

slidesContainer.addEventListener('touchstart', (e) => {
  startX = e.touches[0].pageX;
  scrollLeftStart = slidesContainer.scrollLeft;
});

slidesContainer.addEventListener('touchmove', (e) => {
  const deltaX = e.touches[0].pageX - startX;
  slidesContainer.scrollLeft = scrollLeftStart - deltaX;
});



document.addEventListener("DOMContentLoaded", function () {
  // Sélection de tous les liens dans .links-wrapper
  const links = document.querySelectorAll(".links-wrapper a");

  links.forEach(link => {
      link.addEventListener("click", function () {
          // Supprimer la classe 'selected' de tous les liens
          links.forEach(l => l.classList.remove("selected"));

          // Ajouter la classe 'selected' au lien cliqué
          this.classList.add("selected");
      });
  });
});
