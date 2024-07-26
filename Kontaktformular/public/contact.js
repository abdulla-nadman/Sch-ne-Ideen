document.getElementById('contactForm').addEventListener('submit', async function(event) {
    event.preventDefault();

    const formData = {
        name: document.getElementById('name').value,
        email: document.getElementById('email').value,
        message: document.getElementById('message').value
    };

    try {
        const response = await fetch('/send-email', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        });

        if (response.ok) {
            alert('Nachricht erfolgreich gesendet!');
        } else {
            const errorText = await response.text();
            alert('Fehler beim Senden der Nachricht: ' + errorText);
        }
    } catch (error) {
        alert('Ein Fehler ist aufgetreten: ' + error.message);
    }
});
