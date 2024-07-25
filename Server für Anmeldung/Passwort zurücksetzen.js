document.getElementById('resetPasswordForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const username = document.getElementById('reset-username').value;

    // Simple mock for password reset
    let users = JSON.parse(localStorage.getItem('users')) || {};
    if (users[username]) {
        // Simulate sending a password reset link
        alert('Password reset link sent to your email (mock)');
        window.location.href = 'index.html'; // Redirect to the login page
    } else {
        document.getElementById('reset-error-message').innerText = 'Username does not exist';
    }
});
