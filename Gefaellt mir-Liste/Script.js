document.addEventListener('DOMContentLoaded', () => {
    const likedProductsList = document.getElementById('liked-products');
    const likeButtons = document.querySelectorAll('.like-button');

    likeButtons.forEach(button => {
        button.addEventListener('click', (event) => {
            const product = event.target.closest('.product');
            const productId = product.dataset.id;
            const productName = product.querySelector('h2').textContent;

            // šberprfen, ob das Produkt bereits in der Liste ist
            if (![...likedProductsList.children].some(item => item.dataset.id === productId)) {
                const listItem = document.createElement('li');
                listItem.textContent = productName;
                listItem.dataset.id = productId;
                likedProductsList.appendChild(listItem);
            }
        });
    });
});
