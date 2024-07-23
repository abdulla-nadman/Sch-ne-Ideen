document.addEventListener('DOMContentLoaded', function() {
    const canvas = document.getElementById('canvas');
    const ctx = canvas.getContext('2d');
    const lightImg = document.getElementById('light-img');
    
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
  
    const particles = [];
    const numParticles = 100;
    const particleSize = 20;
  
    for (let i = 0; i < numParticles; i++) {
      particles.push({
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height,
        speedX: (Math.random() - 0.5) * 4,
        speedY: (Math.random() - 0.5) * 4
      });
    }
  
    function draw() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      
      particles.forEach(particle => {
        particle.x += particle.speedX;
        particle.y += particle.speedY;
  
        if (particle.x < 0 || particle.x > canvas.width) particle.speedX *= -1;
        if (particle.y < 0 || particle.y > canvas.height) particle.speedY *= -1;
  
        ctx.drawImage(lightImg, particle.x, particle.y, particleSize, particleSize);
      });
  
      requestAnimationFrame(draw);
    }
  
    draw();
  });
  