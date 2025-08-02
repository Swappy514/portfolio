// Initialize AOS animations
AOS.init({
  duration: 1000,
  once: true,
});

// Dark Mode Toggle Logic with persistence
const toggle = document.getElementById('darkModeToggle');
const body = document.getElementById('body');

// Load saved theme from localStorage
const savedTheme = localStorage.getItem('theme');
if (savedTheme === 'dark') {
  body.classList.add('dark-mode');
  toggle.checked = true;
} else {
  body.classList.remove('dark-mode');
  toggle.checked = false;
}

// Listen for toggle changes
toggle.addEventListener('change', () => {
  if (toggle.checked) {
    body.classList.add('dark-mode');
    localStorage.setItem('theme', 'dark');
  } else {
    body.classList.remove('dark-mode');
    localStorage.setItem('theme', 'light');
  }
});

// Typed.js animation for hero subtext
const roles = ['Web Developer', 'Python Developer', 'Responsive Web Design', 'Flask Developer', 'Cloud Enthusiast'];
let typedIndex = 0;
let charIndex = 0;
let isDeleting = false;
const typedText = document.getElementById('typed-text');
const typingSpeed = 100;
const deletingSpeed = 50;
const delayBetween = 2000;

function type() {
  const currentRole = roles[typedIndex];
  if (isDeleting) {
    charIndex--;
    typedText.textContent = currentRole.substring(0, charIndex);
    if (charIndex === 0) {
      isDeleting = false;
      typedIndex = (typedIndex + 1) % roles.length;
      setTimeout(type, 1);
    } else {
      setTimeout(type, deletingSpeed);
    }
  } else {
    charIndex++;
    typedText.textContent = currentRole.substring(0, charIndex);
    if (charIndex === currentRole.length) {
      isDeleting = true;
      setTimeout(type, delayBetween);
    } else {
      setTimeout(type, typingSpeed);
    }
  }
}

// Start typing effect if element present
if (typedText) {
  type();
}


// Project Filtering
const filterButtons = document.querySelectorAll('.filter-btn');
const projectCards = document.querySelectorAll('.project-card');

// Filter button click
filterButtons.forEach(btn => {
  btn.addEventListener('click', function () {
    filterButtons.forEach(b => b.classList.remove('active'));
    this.classList.add('active');

    const filter = this.getAttribute('data-filter');
    projectCards.forEach(card => {
      if (filter === 'all' || card.getAttribute('data-category').includes(filter)) {
        card.style.display = '';
      } else {
        card.style.display = 'none';
      }
    });
  });
});

// Project card click: open GitHub (update data-link attribute as you add projects)
document.querySelectorAll('.project-card').forEach(card => {
  card.addEventListener('click', function () {
    const link = this.getAttribute('data-link');
    if (link) window.open(link, '_blank');
  });
});

// Education & Certification Tabs
const eduTabBtn = document.getElementById('eduTab');
const certTabBtn = document.getElementById('certTab');
const eduContent = document.getElementById('educationContent');
const certContent = document.getElementById('certificationsContent');

if (eduTabBtn && certTabBtn && eduContent && certContent) {
  eduTabBtn.addEventListener('click', () => {
    eduTabBtn.classList.add('active');
    certTabBtn.classList.remove('active');
    eduContent.classList.remove('d-none');
    certContent.classList.add('d-none');
  });
  certTabBtn.addEventListener('click', () => {
    certTabBtn.classList.add('active');
    eduTabBtn.classList.remove('active');
    certContent.classList.remove('d-none');
    eduContent.classList.add('d-none');
  });
}
