// Gère le scroll du carroussel
let index = 0;
        const carousel = document.querySelector('.carousel');
        const sections = document.querySelectorAll('.carousel-section');

        document.getElementById('next').addEventListener('click', () => {
            index = (index + 1) % sections.length;
            carousel.style.transform = `translateX(${-index * 100}vw)`;
        });

        document.getElementById('prev').addEventListener('click', () => {
            index = (index - 1 + sections.length) % sections.length;
            carousel.style.transform = `translateX(${-index * 100}vw)`;
        });

// Positionne le carrousel correctement
carousel.style.transform = `translateX(${-index * 100}vw)`;



// Formulaire de contact 
var form = document.getElementById("contact-form");
var button = document.getElementById("contact-form-button");

// Empêcher "Entrée" d'envoyer le message dans textarea
document.querySelector(".message-input").addEventListener("keypress", function(event) {
    if (event.key === "Enter" && !event.shiftKey) {
        event.preventDefault();
    }
});

async function handleSubmit(event) {
  event.preventDefault();
  var data = new FormData(event.target);
  
  button.textContent = "Envoi en cours..."; // Change le texte pendant l'envoi
  await new Promise(resolve => setTimeout(resolve, 800));

  button.textContent = "Message envoyé !"; // Succès
  button.style.backgroundColor = "#4CAF50"; // Vert succès
  button.style.border = "none"
  button.style.color = "var(--background-color)"

  fetch(event.target.action, {
      method: form.method,
      body: data,
      headers: { 'Accept': 'application/json' }
  }).then(response => {
      if (response.ok) {
          button.textContent = "Message envoyé !"; // Succès
          button.style.backgroundColor = "#4CAF50"; // Vert succès
          button.style.border = "none"
          button.style.color = "var(--background-color)"
          form.reset();
      } else {
          response.json().then(data => {
              button.textContent = "Échec, réessayez"; // Échec
              button.style.backgroundColor = "#D32F2F"; // Rouge erreur
              button.style.border = "none"
              button.style.color = "var(--background-color)"
          });
      }
  }).catch(error => {
      button.textContent = "Échec, réessayez";
      button.style.backgroundColor = "#D32F2F";
      button.style.border = "none"
      button.style.color = "var(--background-color)"
  });

  // On remet le style du bouton par défaut au bout de 7 secondes
  await new Promise(resolve => setTimeout(resolve, 7000));
  button.textContent = "Envoyer"; 
  if (document.body.classList.contains("dark")) { 
    button.style.backgroundColor = "var(--dark-theme-highlight)";
    button.style.border = "2px solid var(--dark-theme-highlight)";
    button.style.color = "var(--dark-theme-item)";
  } else { 
    button.style.backgroundColor = "var(--light-theme-highlight)";
    button.style.border = "2px solid var(--light-theme-highlight)";
    button.style.color = "var(--light-theme-item)";
  }
}

form.addEventListener("submit", handleSubmit);



// Redimensionne l'espace de texte dans la zone du message 
function updateTextareaRows() {
  const textarea = document.querySelector(".message-input");
  if (!textarea) return;

  const screenHeight = window.innerHeight;
  const minRows = 4; // Nombre de lignes minimum
  const maxRows = 15; // Nombre de lignes maximum
  const rowHeight = 20; // Hauteur approximative d'une ligne (ajuste selon le CSS)

  let newRows = Math.floor(screenHeight / rowHeight / 5); // Ajustement dynamique
  newRows = Math.max(minRows, Math.min(newRows, maxRows)); // Contraindre entre min/max

  textarea.rows = newRows;
}

// Exécuter au chargement et à chaque redimensionnement
window.addEventListener("resize", updateTextareaRows);
window.addEventListener("DOMContentLoaded", updateTextareaRows);







// Menu
const toggle_n = document.getElementById('menu-toggle');
const menu = document.querySelector('.menu');

toggle_n.addEventListener('click', (event) => {
  menu.classList.toggle('show');
  event.stopPropagation(); // Empêche la propagation du clic vers le document
});

// Cache le menu lorsqu'on clique autre part que sur le bouton menu
document.addEventListener('click', (event) => {
  if (!toggle_n.contains(event.target)) {
    menu.classList.remove('show');
  }
});


// Affichage du bouton pour remonter en haut de la page
window.addEventListener("scroll", function () {
  const scrollToTopButton = document.getElementById("scrollToTopButton");

  if (window.scrollY > 1000) {
    scrollToTopButton.style.display = "flex"; // Affiche le bouton
  } else {
    scrollToTopButton.style.display = "none"; // Cache le bouton quand on est en haut
  }
});


// Affichage du bouton pour télécharger le cv
window.addEventListener("scroll", function () {
  const cvButton = document.querySelector(".download-cv-button");
  let windowWidth = window.innerWidth;
  if (windowWidth > 1000) return;
  if (window.scrollY > 115 ) {
    cvButton.style.display = "flex"; // Affiche le bouton
  } else {
    cvButton.style.display = "none"; // Cache le bouton quand on est en haut
  }
});




const toggle = document.getElementById('darkmode-toggle');
const body = document.body;
        
// Load theme from local storage or set default
const currentTheme = localStorage.getItem('theme');
if (currentTheme) {
    body.classList.add(currentTheme);
    body.attributeList
    toggle.checked = currentTheme === 'dark';

}

// Switch theme and save in localStorage
toggle.addEventListener('change', function() {
    if (toggle.checked) {
        body.classList.add('dark');
        body.classList.remove('light');
        localStorage.setItem('theme', 'dark');
        
    } else {
        body.classList.add('light');
        body.classList.remove('dark');
        localStorage.setItem('theme', 'light');;
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
    window.scrollBy({
        top: window.innerHeight,  // Défiler de la hauteur de la fenêtre (100vh)
        behavior: 'smooth'        // Ajouter une transition fluide
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