/* ============================================
   PRIME PORTFOLIO - INTERACTIVE JAVASCRIPT
   ============================================ */

// Wait for DOM to be ready
document.addEventListener('DOMContentLoaded', () => {
    // Initialize all modules
    initParticles();
    initCustomCursor();
    initNavigation();
    initScrollAnimations();
    initTiltEffect();
    initMagneticEffect();
    initCounterAnimation();
    initSkillBars();
    initContactForm();
    initSmoothScroll();
    initMagicBento();
});

/* ============================================
   LENIS SMOOTH SCROLL
   ============================================ */
function initSmoothScroll() {
    const lenis = new Lenis({
        duration: 2.0,
        easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
        direction: 'vertical',
        gestureDirection: 'vertical',
        smooth: true,
        mouseMultiplier: 0.6,
        smoothTouch: false,
        touchMultiplier: 1.2,
        infinite: false,
    });

    function raf(time) {
        lenis.raf(time);
        requestAnimationFrame(raf);
    }

    requestAnimationFrame(raf);

    // Update anchor links to work with Lenis
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                lenis.scrollTo(target, {
                    offset: 0,
                    duration: 2.0,
                });
            }
        });
    });
}

/* ============================================
   PARTICLE BACKGROUND SYSTEM
   ============================================ */
function initParticles() {
    const canvas = document.getElementById('particles');
    const ctx = canvas.getContext('2d');

    let particles = [];
    let mouseX = 0;
    let mouseY = 0;

    // Set canvas size
    function resizeCanvas() {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    }

    resizeCanvas();
    window.addEventListener('resize', resizeCanvas);

    // Track mouse position
    document.addEventListener('mousemove', (e) => {
        mouseX = e.clientX;
        mouseY = e.clientY;
    });

    // Particle class
    class Particle {
        constructor() {
            this.reset();
        }

        reset() {
            this.x = Math.random() * canvas.width;
            this.y = Math.random() * canvas.height;
            this.size = Math.random() * 2 + 1;
            this.baseSize = this.size;
            this.speedX = (Math.random() - 0.5) * 0.5;
            this.speedY = (Math.random() - 0.5) * 0.5;
            this.opacity = Math.random() * 0.5 + 0.2;

            // Random color from prime palette
            const colors = ['#00d4ff', '#8b5cf6', '#ff0080'];
            this.color = colors[Math.floor(Math.random() * colors.length)];
        }

        update() {
            this.x += this.speedX;
            this.y += this.speedY;

            // Mouse interaction
            const dx = mouseX - this.x;
            const dy = mouseY - this.y;
            const distance = Math.sqrt(dx * dx + dy * dy);

            if (distance < 150) {
                const force = (150 - distance) / 150;
                this.x -= dx * force * 0.02;
                this.y -= dy * force * 0.02;
                this.size = this.baseSize + force * 3;
            } else {
                this.size = this.baseSize;
            }

            // Wrap around edges
            if (this.x < -10) this.x = canvas.width + 10;
            if (this.x > canvas.width + 10) this.x = -10;
            if (this.y < -10) this.y = canvas.height + 10;
            if (this.y > canvas.height + 10) this.y = -10;
        }

        draw() {
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
            ctx.fillStyle = this.color;
            ctx.globalAlpha = this.opacity;
            ctx.fill();
            ctx.globalAlpha = 1;
        }
    }

    // Create particles (reduced count for performance)
    const particleCount = Math.min(50, Math.floor(window.innerWidth / 30));
    for (let i = 0; i < particleCount; i++) {
        particles.push(new Particle());
    }

    // Draw connections between nearby particles (optimized with distance² check)
    function drawConnections() {
        const maxDist = 120;
        const maxDistSq = maxDist * maxDist;
        for (let i = 0; i < particles.length; i++) {
            for (let j = i + 1; j < particles.length; j++) {
                const dx = particles[i].x - particles[j].x;
                const dy = particles[i].y - particles[j].y;
                const distSq = dx * dx + dy * dy;

                if (distSq < maxDistSq) {
                    const distance = Math.sqrt(distSq);
                    ctx.beginPath();
                    ctx.moveTo(particles[i].x, particles[i].y);
                    ctx.lineTo(particles[j].x, particles[j].y);
                    ctx.strokeStyle = `rgba(0, 212, 255, ${0.1 * (1 - distance / maxDist)})`;
                    ctx.lineWidth = 1;
                    ctx.stroke();
                }
            }
        }
    }

    // Animation loop
    function animate() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        particles.forEach(particle => {
            particle.update();
            particle.draw();
        });

        drawConnections();

        requestAnimationFrame(animate);
    }

    animate();
}

/* ============================================
   CUSTOM CURSOR
   ============================================ */
function initCustomCursor() {
    const cursor = document.querySelector('.cursor');
    const follower = document.querySelector('.cursor-follower');

    if (!cursor || !follower) return;

    // Check if touch device
    if ('ontouchstart' in window) {
        cursor.style.display = 'none';
        follower.style.display = 'none';
        return;
    }

    let cursorX = 0;
    let cursorY = 0;
    let followerX = 0;
    let followerY = 0;

    document.addEventListener('mousemove', (e) => {
        cursorX = e.clientX;
        cursorY = e.clientY;
    });

    // Smooth follower animation
    function animateCursor() {
        // Cursor follows immediately
        cursor.style.left = cursorX + 'px';
        cursor.style.top = cursorY + 'px';

        // Follower has smooth delay
        followerX += (cursorX - followerX) * 0.15;
        followerY += (cursorY - followerY) * 0.15;
        follower.style.left = followerX + 'px';
        follower.style.top = followerY + 'px';

        requestAnimationFrame(animateCursor);
    }

    animateCursor();

    // Hover effects
    const hoverElements = document.querySelectorAll('a, button, .magnetic, .tilt-card');

    hoverElements.forEach(el => {
        el.addEventListener('mouseenter', () => {
            cursor.classList.add('hover');
            follower.classList.add('hover');
        });

        el.addEventListener('mouseleave', () => {
            cursor.classList.remove('hover');
            follower.classList.remove('hover');
        });
    });
}

/* ============================================
   NAVIGATION
   ============================================ */
function initNavigation() {
    const navbar = document.querySelector('.navbar');
    const navToggle = document.querySelector('.nav-toggle');
    const navLinks = document.querySelector('.nav-links');
    const links = document.querySelectorAll('.nav-link');

    // Throttled scroll handler using rAF
    let scrollTicking = false;

    function onScroll() {
        if (!scrollTicking) {
            requestAnimationFrame(() => {
                const currentScroll = window.scrollY;

                if (currentScroll > 50) {
                    navbar.classList.add('scrolled');
                } else {
                    navbar.classList.remove('scrolled');
                }

                highlightNavLink(currentScroll);
                scrollTicking = false;
            });
            scrollTicking = true;
        }
    }

    window.addEventListener('scroll', onScroll, { passive: true });

    // Mobile toggle
    navToggle.addEventListener('click', () => {
        navToggle.classList.toggle('active');
        navLinks.classList.toggle('open');
    });

    // Close mobile menu on link click
    links.forEach(link => {
        link.addEventListener('click', () => {
            navToggle.classList.remove('active');
            navLinks.classList.remove('open');
        });
    });

    // Active link on scroll
    const sections = document.querySelectorAll('section[id]');

    function highlightNavLink(scrollY) {
        const scrollPosition = (scrollY || window.scrollY) + 100;

        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.offsetHeight;
            const sectionId = section.getAttribute('id');

            if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
                links.forEach(link => {
                    link.classList.remove('active');
                    if (link.getAttribute('href') === `#${sectionId}`) {
                        link.classList.add('active');
                    }
                });
            }
        });
    }
}

/* ============================================
   SCROLL ANIMATIONS
   ============================================ */
function initScrollAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('revealed');

                // Stagger animation for grid items
                if (entry.target.classList.contains('skill-card') ||
                    entry.target.classList.contains('project-card')) {
                    const siblings = entry.target.parentElement.children;
                    const index = Array.from(siblings).indexOf(entry.target);
                    entry.target.style.transitionDelay = `${index * 0.1}s`;
                }
            }
        });
    }, observerOptions);

    // Observe elements
    const elementsToAnimate = document.querySelectorAll(
        '.reveal-text, .about-text, .skill-card, .project-card, .stat-item'
    );

    elementsToAnimate.forEach(el => observer.observe(el));
}

/* ============================================
   3D TILT EFFECT
   ============================================ */
function initTiltEffect() {
    const tiltCards = document.querySelectorAll('.tilt-card');

    tiltCards.forEach(card => {
        card.addEventListener('mousemove', (e) => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;

            const centerX = rect.width / 2;
            const centerY = rect.height / 2;

            const rotateX = (y - centerY) / 10;
            const rotateY = (centerX - x) / 10;

            card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateZ(10px)`;
        });

        card.addEventListener('mouseleave', () => {
            card.style.transform = 'perspective(1000px) rotateX(0) rotateY(0) translateZ(0)';
        });
    });
}

/* ============================================
   MAGNETIC EFFECT
   ============================================ */
function initMagneticEffect() {
    const magneticElements = document.querySelectorAll('.magnetic');

    magneticElements.forEach(el => {
        el.addEventListener('mousemove', (e) => {
            const rect = el.getBoundingClientRect();
            const x = e.clientX - rect.left - rect.width / 2;
            const y = e.clientY - rect.top - rect.height / 2;

            el.style.transform = `translate(${x * 0.3}px, ${y * 0.3}px)`;
        });

        el.addEventListener('mouseleave', () => {
            el.style.transform = 'translate(0, 0)';
        });
    });
}

/* ============================================
   COUNTER ANIMATION
   ============================================ */
function initCounterAnimation() {
    const counters = document.querySelectorAll('.stat-number');

    const observerOptions = {
        threshold: 0.5
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const counter = entry.target;
                const target = parseInt(counter.getAttribute('data-target'));
                const duration = 2000;
                const step = target / (duration / 16);
                let current = 0;

                const updateCounter = () => {
                    current += step;
                    if (current < target) {
                        counter.textContent = Math.floor(current);
                        requestAnimationFrame(updateCounter);
                    } else {
                        counter.textContent = target;
                    }
                };

                updateCounter();
                observer.unobserve(counter);
            }
        });
    }, observerOptions);

    counters.forEach(counter => observer.observe(counter));
}

/* ============================================
   SKILL BARS ANIMATION
   ============================================ */
function initSkillBars() {
    const skillBars = document.querySelectorAll('.skill-progress');

    const observerOptions = {
        threshold: 0.5
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const bar = entry.target;
                const progress = bar.getAttribute('data-progress');
                bar.style.width = progress + '%';
                observer.unobserve(bar);
            }
        });
    }, observerOptions);

    skillBars.forEach(bar => observer.observe(bar));
}

/* ============================================
   CONTACT FORM
   ============================================ */
function initContactForm() {
    const form = document.getElementById('contactForm');
    const submitBtn = form.querySelector('.btn-submit');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        // Add loading state
        submitBtn.classList.add('loading');

        // Get form values
        const name = document.getElementById('name').value;
        const email = document.getElementById('email').value;
        const phone = document.getElementById('phone').value;
        const message = document.getElementById('message').value;

        try {
            const response = await fetch("https://formsubmit.co/ajax/sahidafridi.56786@gmail.com", {
                method: "POST",
                headers: { 
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                body: JSON.stringify({
                    name: name,
                    email: email,
                    phone: phone,
                    message: message
                })
            });

            const data = await response.json();

            if (data.success) {
                // Show success message
                showNotification('Message sent successfully!', 'success');
                // Reset form
                form.reset();
            } else {
                showNotification('Something went wrong. Please try again.', 'error');
            }
        } catch (error) {
            showNotification('Error sending message. Please try again later.', 'error');
            console.error(error);
        } finally {
            // Remove loading state
            submitBtn.classList.remove('loading');
        }
    });
}

/* ============================================
   NOTIFICATION SYSTEM
   ============================================ */
function showNotification(message, type = 'success') {
    // Create notification element
    const notification = document.createElement('div');
    notification.className = `notification ${type}`;
    notification.innerHTML = `
        <i class="fas ${type === 'success' ? 'fa-check-circle' : 'fa-exclamation-circle'}"></i>
        <span>${message}</span>
    `;

    // Add styles
    notification.style.cssText = `
        position: fixed;
        bottom: 30px;
        right: 30px;
        padding: 16px 24px;
        background: ${type === 'success' ? 'linear-gradient(135deg, #00d4ff, #8b5cf6)' : 'linear-gradient(135deg, #ff0080, #ff4d4d)'};
        color: white;
        border-radius: 12px;
        display: flex;
        align-items: center;
        gap: 12px;
        font-size: 15px;
        font-weight: 500;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.3);
        z-index: 10000;
        transform: translateX(120%);
        transition: transform 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    `;

    document.body.appendChild(notification);

    // Animate in
    setTimeout(() => {
        notification.style.transform = 'translateX(0)';
    }, 100);

    // Remove after delay
    setTimeout(() => {
        notification.style.transform = 'translateX(120%)';
        setTimeout(() => notification.remove(), 400);
    }, 4000);
}



/* ============================================
   TYPING EFFECT (For hero subtitle)
   ============================================ */
const typingText = document.querySelector('.typing-text');
if (typingText) {
    const originalText = typingText.textContent;
    typingText.textContent = '';

    let charIndex = 0;

    function typeChar() {
        if (charIndex < originalText.length) {
            typingText.textContent += originalText.charAt(charIndex);
            charIndex++;
            setTimeout(typeChar, 80);
        }
    }

    // Start typing after hero title animation
    setTimeout(typeChar, 1500);
}

/* ============================================
   PAGE LOAD ANIMATION
   ============================================ */
window.addEventListener('load', () => {
    document.body.classList.add('loaded');
});

/* ============================================
   MAGIC BENTO EFFECTS
   ============================================ */
function initMagicBento() {
    if (typeof gsap === 'undefined') return;

    const bentoGrids = document.querySelectorAll('.bento-grid');
    if (!bentoGrids.length) return;

    const DEFAULT_PARTICLE_COUNT = 12;
    const DEFAULT_SPOTLIGHT_RADIUS = 300;
    const DEFAULT_GLOW_COLOR = '132, 0, 255';
    
    // Convert hex color to RGB helper
    function hexToRgb(hex) {
        if (!hex) return null;
        hex = hex.replace(/^#/, '');
        if (hex.length === 3) {
            hex = hex.split('').map(c => c + c).join('');
        }
        const num = parseInt(hex, 16);
        return `${num >> 16 & 255}, ${num >> 8 & 255}, ${num & 255}`;
    }

    bentoGrids.forEach(grid => {
        // Global Spotlight logic
        const spotlight = document.createElement('div');
        spotlight.className = 'global-spotlight';
        document.body.appendChild(spotlight);
        
        let isInsideSection = false;
        const cards = grid.querySelectorAll('.bento-card');

        // Set up each card with variables
        cards.forEach(card => {
            // Try to extract card color from inline style to use as glow color
            let glowColor = DEFAULT_GLOW_COLOR;
            const style = card.getAttribute('style') || '';
            const match = style.match(/--card-color:\s*(#[0-9A-Fa-f]{3,6})/);
            if (match && match[1]) {
                glowColor = hexToRgb(match[1]) || DEFAULT_GLOW_COLOR;
            }
            card.style.setProperty('--glow-color', glowColor);
            card.dataset.glowColor = glowColor; // store for particle and ripple
        });

        const updateCardGlowProperties = (card, mouseX, mouseY, glow, radius) => {
            const rect = card.getBoundingClientRect();
            const relativeX = ((mouseX - rect.left) / rect.width) * 100;
            const relativeY = ((mouseY - rect.top) / rect.height) * 100;

            card.style.setProperty('--glow-x', `${relativeX}%`);
            card.style.setProperty('--glow-y', `${relativeY}%`);
            card.style.setProperty('--glow-intensity', glow.toString());
            card.style.setProperty('--glow-radius', `${radius}px`);
        };

        const handleGridMouseMove = (e) => {
            const rect = grid.getBoundingClientRect();
            isInsideSection = (
                e.clientX >= rect.left && e.clientX <= rect.right && 
                e.clientY >= rect.top && e.clientY <= rect.bottom
            );

            if (!isInsideSection) {
                gsap.to(spotlight, { opacity: 0, duration: 0.3, ease: 'power2.out' });
                cards.forEach(card => card.style.setProperty('--glow-intensity', '0'));
                return;
            }

            const proximity = DEFAULT_SPOTLIGHT_RADIUS * 0.5;
            const fadeDistance = DEFAULT_SPOTLIGHT_RADIUS * 0.75;
            let minDistance = Infinity;

            cards.forEach(card => {
                const cardRect = card.getBoundingClientRect();
                const centerX = cardRect.left + cardRect.width / 2;
                const centerY = cardRect.top + cardRect.height / 2;
                const distance = Math.hypot(e.clientX - centerX, e.clientY - centerY) - Math.max(cardRect.width, cardRect.height) / 2;
                const effectiveDistance = Math.max(0, distance);

                minDistance = Math.min(minDistance, effectiveDistance);

                let glowIntensity = 0;
                if (effectiveDistance <= proximity) {
                    glowIntensity = 1;
                } else if (effectiveDistance <= fadeDistance) {
                    glowIntensity = (fadeDistance - effectiveDistance) / (fadeDistance - proximity);
                }

                updateCardGlowProperties(card, e.clientX, e.clientY, glowIntensity, DEFAULT_SPOTLIGHT_RADIUS);
            });

            gsap.to(spotlight, {
                left: e.clientX,
                top: e.clientY,
                duration: 0.1,
                ease: 'power2.out'
            });

            const targetOpacity = minDistance <= proximity ? 0.8 : 
                minDistance <= fadeDistance ? ((fadeDistance - minDistance) / (fadeDistance - proximity)) * 0.8 : 0;

            gsap.to(spotlight, {
                opacity: targetOpacity,
                duration: targetOpacity > 0 ? 0.2 : 0.5,
                ease: 'power2.out'
            });
        };

        const handleGridMouseLeave = () => {
            isInsideSection = false;
            cards.forEach(card => card.style.setProperty('--glow-intensity', '0'));
            gsap.to(spotlight, { opacity: 0, duration: 0.3, ease: 'power2.out' });
        };

        document.addEventListener('mousemove', handleGridMouseMove);
        document.addEventListener('mouseleave', handleGridMouseLeave);

        // Particle and Hover logic for each card
        cards.forEach(card => {
            let particlesRef = [];
            let timeoutsRef = [];
            let isHovered = false;
            let magnetismAnimation = null;
            const glowColor = card.dataset.glowColor;

            const createParticleElement = (x, y) => {
                const el = document.createElement('div');
                el.className = 'particle';
                el.style.cssText = `
                    position: absolute;
                    width: 4px;
                    height: 4px;
                    border-radius: 50%;
                    background: rgba(${glowColor}, 1);
                    box-shadow: 0 0 6px rgba(${glowColor}, 0.6);
                    pointer-events: none;
                    z-index: 100;
                    left: ${x}px;
                    top: ${y}px;
                `;
                return el;
            };

            const clearAllParticles = () => {
                timeoutsRef.forEach(clearTimeout);
                timeoutsRef = [];
                if (magnetismAnimation) magnetismAnimation.kill();

                particlesRef.forEach(particle => {
                    gsap.to(particle, {
                        scale: 0,
                        opacity: 0,
                        duration: 0.3,
                        ease: 'back.in(1.7)',
                        onComplete: () => {
                            if (particle.parentNode) particle.parentNode.removeChild(particle);
                        }
                    });
                });
                particlesRef = [];
            };

            const animateParticles = () => {
                const { width, height } = card.getBoundingClientRect();
                const particleCount = DEFAULT_PARTICLE_COUNT;
                
                for(let i = 0; i < particleCount; i++) {
                    const timeoutId = setTimeout(() => {
                        if (!isHovered) return;
                        
                        const clone = createParticleElement(Math.random() * width, Math.random() * height);
                        card.appendChild(clone);
                        particlesRef.push(clone);

                        gsap.fromTo(clone, { scale: 0, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.3, ease: 'back.out(1.7)' });

                        gsap.to(clone, {
                            x: (Math.random() - 0.5) * 100,
                            y: (Math.random() - 0.5) * 100,
                            rotation: Math.random() * 360,
                            duration: 2 + Math.random() * 2,
                            ease: 'none',
                            repeat: -1,
                            yoyo: true
                        });

                        gsap.to(clone, {
                            opacity: 0.3,
                            duration: 1.5,
                            ease: 'power2.inOut',
                            repeat: -1,
                            yoyo: true
                        });
                    }, i * 100);
                    timeoutsRef.push(timeoutId);
                }
            };

            card.addEventListener('mouseenter', () => {
                isHovered = true;
                animateParticles();
                
                gsap.to(card, {
                    rotateX: 5,
                    rotateY: 5,
                    duration: 0.3,
                    ease: 'power2.out',
                    transformPerspective: 1000
                });
            });

            card.addEventListener('mouseleave', () => {
                isHovered = false;
                clearAllParticles();
                
                gsap.to(card, {
                    rotateX: 0,
                    rotateY: 0,
                    x: 0,
                    y: 0,
                    duration: 0.3,
                    ease: 'power2.out'
                });
            });

            card.addEventListener('mousemove', (e) => {
                const rect = card.getBoundingClientRect();
                const x = e.clientX - rect.left;
                const y = e.clientY - rect.top;
                const centerX = rect.width / 2;
                const centerY = rect.height / 2;

                const rotateX = ((y - centerY) / centerY) * -10;
                const rotateY = ((x - centerX) / centerX) * 10;

                gsap.to(card, {
                    rotateX,
                    rotateY,
                    duration: 0.1,
                    ease: 'power2.out',
                    transformPerspective: 1000
                });

                const magnetX = (x - centerX) * 0.05;
                const magnetY = (y - centerY) * 0.05;

                magnetismAnimation = gsap.to(card, {
                    x: magnetX,
                    y: magnetY,
                    duration: 0.3,
                    ease: 'power2.out'
                });
            });

            card.addEventListener('click', (e) => {
                const rect = card.getBoundingClientRect();
                const x = e.clientX - rect.left;
                const y = e.clientY - rect.top;

                const maxDistance = Math.max(
                    Math.hypot(x, y),
                    Math.hypot(x - rect.width, y),
                    Math.hypot(x, y - rect.height),
                    Math.hypot(x - rect.width, y - rect.height)
                );

                const ripple = document.createElement('div');
                ripple.className = 'magic-ripple';
                ripple.style.cssText = `
                    position: absolute;
                    width: ${maxDistance * 2}px;
                    height: ${maxDistance * 2}px;
                    border-radius: 50%;
                    background: radial-gradient(circle, rgba(${glowColor}, 0.4) 0%, rgba(${glowColor}, 0.2) 30%, transparent 70%);
                    left: ${x - maxDistance}px;
                    top: ${y - maxDistance}px;
                    pointer-events: none;
                    z-index: 1000;
                `;

                card.appendChild(ripple);

                gsap.fromTo(ripple, { scale: 0, opacity: 1 }, {
                    scale: 1,
                    opacity: 0,
                    duration: 0.8,
                    ease: 'power2.out',
                    onComplete: () => ripple.remove()
                });
            });
        });
    });
}
