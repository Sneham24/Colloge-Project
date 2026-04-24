// Homepage.js - Main JavaScript for Parent Bless Homepage

// Wait for DOM to load
document.addEventListener('DOMContentLoaded', function() {
    console.log('Parent Bless Homepage loaded successfully');
    
    // Initialize any homepage-specific functionality
    initializeHomepage();
});

function initializeHomepage() {
    // Add smooth scrolling for navigation
    const navLinks = document.querySelectorAll('nav a[href^="#"]');
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });
    
    // Add mobile menu toggle if needed
    const navbar = document.getElementById('navbar');
    if (navbar) {
        // You can add mobile menu functionality here if needed
        console.log('Navigation bar initialized');
    }
}

// Service scrolling functionality (already in HTML but keeping for consistency)
function scrollServices(direction) {
    const container = document.getElementById('servicesContainer');
    if (container) {
        const scrollAmount = 300;
        container.scrollBy({
            left: direction * scrollAmount,
            behavior: 'smooth'
        });
    }
}
