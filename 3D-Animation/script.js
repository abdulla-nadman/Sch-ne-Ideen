const carousel = document.getElementById('carousel');
const products = document.querySelectorAll('.product');

products.forEach(product => {
  product.addEventListener('mouseenter', () => {
    carousel.style.animationPlayState = 'paused';
  });
  product.addEventListener('mouseleave', () => {
    carousel.style.animationPlayState = 'running';
  });
});