/*****************************************/
/* Caroussel présentation section        */
/*****************************************/
let index = 0;
        const carousel = document.querySelector('.carousel');
        const carouselSections = document.querySelectorAll('.carousel-section');

        document.getElementById('next').addEventListener('click', () => {
            index = (index + 1) % carouselSections.length;
            carousel.style.transform = `translateX(${-index * 100}vw)`;
        });

        document.getElementById('prev').addEventListener('click', () => {
            index = (index - 1 + carouselSections.length) % carouselSections.length;
            carousel.style.transform = `translateX(${-index * 100}vw)`;
        });

// Positionne le carrousel correctement
carousel.style.transform = `translateX(${-index * 100}vw)`;




/*****************************************/
/* Formulaire de contact                 */
/*****************************************/
var form = document.getElementById("contact-form");
var button = document.getElementById("contact-form-button");

// Empêcher "Entrée" d'envoyer le message dans textarea
document.querySelector(".message-input").addEventListener("keydown", function(e) {
  if (e.key === "Enter") {
      e.preventDefault(); // Empêche l'envoi du formulaire
      this.value += "\n"; // Ajoute une nouvelle ligne
  }
});

async function handleSubmit(event) {
  event.preventDefault();
  
  // Récupérer le message dans le champ message
  var messageField = document.querySelector(".message-input");

  var data = new FormData(event.target);

  button.textContent = "Envoi en cours..."; // Change le texte pendant l'envoi
  await new Promise(resolve => setTimeout(resolve, 800));

  button.textContent = "Message envoyé !"; // Succès
  button.style.backgroundColor = "#4CAF50"; // Vert succès
  button.style.border = "none";
  button.style.color = "var(--background-color)";

  fetch(event.target.action, {
      method: form.method,
      body: data,
      headers: { 'Accept': 'application/json' }
  }).then(response => {
      if (response.ok) {
          button.textContent = "Message envoyé !"; // Succès
          button.style.backgroundColor = "#4CAF50"; // Vert succès
          button.style.border = "none";
          button.style.color = "var(--background-color)";
          form.reset();
      } else {
          response.json().then(data => {
              button.textContent = "Échec, réessayez"; // Échec
              button.style.backgroundColor = "#D32F2F"; // Rouge erreur
              button.style.border = "none";
              button.style.color = "var(--background-color)";
          });
      }
  }).catch(error => {
      button.textContent = "Échec, réessayez";
      button.style.backgroundColor = "#D32F2F";
      button.style.border = "none";
      button.style.color = "var(--background-color)";
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

  const heightIntervals = [450, 470, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050, 1200];
  const numberRows = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 18, 20, 22]

  for (let i = 0; i < heightIntervals.length; ++i) {
    if (screenHeight < heightIntervals[i]) {
      textarea.rows = numberRows[i];
      return;
    } 
  }

  textarea.rows = numberRows[numberRows.length - 1];
}

// Exécuter au chargement et à chaque redimensionnement
window.addEventListener("resize", updateTextareaRows);
window.addEventListener("DOMContentLoaded", updateTextareaRows);






/*****************************************/
/* Menu navigation                       */
/*****************************************/
const toggleMenu = document.getElementById('menu-toggle');
const menu = document.querySelector('.menu');

toggleMenu.addEventListener('click', (event) => {
  menu.classList.toggle('show');
  event.stopPropagation(); // Empêche la propagation du clic vers le document
});

// Cache le menu lorsqu'on clique autre part que sur le bouton menu
document.addEventListener('click', (event) => {
  if (!toggleMenu.contains(event.target)) {
    menu.classList.remove('show');
  }
});



/*****************************************/
/* Bouton d'anchrage                     */
/*****************************************/
window.addEventListener("scroll", function () {
  const scrollToTopButton = document.getElementById("scrollToTopButton");

  if (window.scrollY > 1000) {
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

// Fonction pour descendre jusqu'à whoami
function scrollToWhoami2() {
  const section = document.getElementById('presentation-section');
  if (section) {
      const sectionTop = section.offsetTop + windowHeight; // Position de la section
      window.scrollTo({
          top: sectionTop, // Décaler pour éviter que la navbar cache la section
          behavior: 'smooth' // Défilement fluide
      });
  }
}

function scrollToWhoami() {
  document.getElementById("link-to-whoami").addEventListener("click", function () {
    document.getElementById("presentation-section").scrollIntoView({ behavior: "smooth" });
  });
}





/*****************************************/
/* Bouton download cv                    */
/*****************************************/
window.addEventListener("scroll", function () {
  const cvButton = document.querySelector(".download-cv-button");
  let windowWidth = window.innerWidth;
  if (windowWidth > 1180) return;
  if (window.scrollY > 115 ) {
    cvButton.style.display = "flex"; // Affiche le bouton
  } else {
    cvButton.style.display = "none"; // Cache le bouton quand on est en haut
  }
});




const toggleTheme = document.getElementById('darkmode-toggle');
const body = document.body;
        
// Load theme from local storage or set default
const currentTheme = localStorage.getItem('theme');
if (currentTheme) {
    body.classList.add(currentTheme);
    body.attributeList
    toggleTheme.checked = currentTheme === 'dark';

}

// Switch theme and save in localStorage
toggleTheme.addEventListener('change', function() {
    if (toggleTheme.checked) {
        body.classList.add('dark');
        body.classList.remove('light');
        localStorage.setItem('theme', 'dark');
        
    } else {
        body.classList.add('light');
        body.classList.remove('dark');
        localStorage.setItem('theme', 'light');;
    }
});










/*****************************************/
/* Barre nav dynamique                   */
/*****************************************/

// Sélectionner tous les liens de navigation
const menuItems = document.querySelectorAll('.menu li a');
const sections = document.querySelectorAll('section');
const windowHeight = window.innerHeight;

function updateCurrentPage() {
    let currentSection = 'presentation-section'; // Par défaut, la première section

    let currentViewPos = window.scrollY + (windowHeight / 2); // Position actuelle dans la vue

    sections.forEach((section) => {
        // On ajoute windowHeight à sectionTop car les sections commencent à partir de 100vh 
        const sectionTop = section.offsetTop + windowHeight;
        const sectionHeight = section.offsetHeight;

        // Vérifier si currentViewPos est DANS la section
        if (currentViewPos >= sectionTop && currentViewPos < sectionTop + sectionHeight) {
          
      
          currentSection = section.id; // Mettre à jour la section active
        }
    });

    // Mettre à jour la classe 'current-page' sur les liens du menu
    
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

// Mettre à jour au chargement initial
window.addEventListener('load', updateCurrentPage);




/*****************************************/
/* Scrolls du menu animés                */
/*****************************************/
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



/*****************************************/
/* Barre de progression                  */
/*****************************************/
window.onscroll = function() {
  updateProgressBar();
};

function updateProgressBar() {
  let scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
  let scrollHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
  let progress = (scrollTop / scrollHeight) * 100;

  document.querySelector(".progress-indicator").style.width = progress + "%";
}









/*****************************************/
/* Caroussel de projets                  */
/*****************************************/



// Au chargement de la page, ajouter la classe 'selected' au premier lien
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



document.querySelectorAll('.links-wrapper a').forEach((link, index) => {
  link.addEventListener('click', (e) => {
      e.preventDefault(); // Empêche le comportement par défaut du lien

      const slidesContainer = document.querySelector('.slides');
      const slideWidth = slidesContainer.clientWidth;
      const targetSlide = document.querySelector(`#slide-${index + 1}`);
      const navbar = document.querySelector('.navbar');
      const navbarHeight = navbar ? navbar.offsetHeight : 0;

      // Défilement horizontal du carrousel
      slidesContainer.scrollTo({
          left: index * slideWidth,
          behavior: 'smooth'
      });

      // Vérification si la slide est visible dans la fenêtre
      const slideRect = targetSlide.getBoundingClientRect();
      const windowHeight = window.innerHeight;

      if (slideRect.top < 0 || slideRect.bottom > windowHeight) {
        // Scroll vertical pour centrer la slide dans l'écran
        const slideCenter = window.scrollY + slideRect.top - (windowHeight / 2) + (slideRect.height / 2) - (navbarHeight / 2);

        window.scrollTo({
            top: slideCenter,
            behavior: 'smooth'
        });
    }
  });
});

