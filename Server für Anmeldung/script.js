document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    
    // Simulate a simple login check
    if (username === 'admin' && password === 'password123') {
        window.location.href = 'dashboard.html'; // Redirect to the dashboard or another page
    } else {
        document.getElementById('error-message').innerText = 'Invalid username or password';
    }
});
