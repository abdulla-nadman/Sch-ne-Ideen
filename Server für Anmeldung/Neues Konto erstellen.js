document.getElementById('registerForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const username = document.getElementById('new-username').value;
    const password = document.getElementById('new-password').value;

    // Simple validation and mock registration
    if (username && password) {
        // Normally, you would send this data to your server
        // For this example, we simply store it in local storage
        let users = JSON.parse(localStorage.getItem('users')) || {};
        if (users[username]) {
            document.getElementById('register-error-message').innerText = 'Username already exists';
        } else {
            users[username] = password;
            localStorage.setItem('users', JSON.stringify(users));
            alert('Account created successfully!');
            window.location.href = 'index.html'; // Redirect to the login page
        }
    } else {
        document.getElementById('register-error-message').innerText = 'Please fill out all fields';
    }
});
