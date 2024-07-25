document.addEventListener('DOMContentLoaded', () => {
    const cart = document.getElementById('cart');
    const cartCount = document.getElementById('cart-count');
    const addToCartButtons = document.querySelectorAll('.add-to-cart');

    addToCartButtons.forEach(button => {
        button.addEventListener('click', () => {
            let count = parseInt(cartCount.textContent);
            cartCount.textContent = count + 1;
            cart.classList.add('animate');
            setTimeout(() => {
                cart.classList.remove('animate');
            }, 200);
        });
    });
});
