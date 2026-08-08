// Hamburger Menu Toggle
const hamburger = document.getElementById('hamburger');
const navDesktop = document.getElementById('nav-desktop');
const mobileNav = document.getElementById('nav-mobile');

if (hamburger) {
    hamburger.addEventListener('click', () => {
        hamburger.classList.toggle('active');
        if (mobileNav) {
            mobileNav.classList.toggle('hidden');
        }
    });
}

// Close mobile menu when clicking a link
if (mobileNav) {
    document.querySelectorAll('#nav-mobile a').forEach(link => {
        link.addEventListener('click', () => {
            hamburger.classList.remove('active');
            mobileNav.classList.add('hidden');
        });
    });
}

// Prevent dropdown toggle default behavior
document.querySelectorAll('.nav-dropdown-toggle').forEach(toggle => {
    toggle.addEventListener('click', (e) => {
        e.preventDefault();
    });
});
