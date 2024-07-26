const express = require('express');
const nodemailer = require('nodemailer');
const bodyParser = require('body-parser');

const app = express();
const port = 3000;

// Middleware
app.use(bodyParser.json());
app.use(express.static('public'));

// E-Mail-Konfiguration
const transporter = nodemailer.createTransport({
    service: 'gmail',
    auth: {
        user: 'your-email@gmail.com', // Ersetzen Sie dies mit Ihrer E-Mail-Adresse
        pass: 'your-email-password'   // Ersetzen Sie dies mit Ihrem E-Mail-Passwort
    }
});

// Route zum Senden der E-Mail
app.post('/send-email', (req, res) => {
    const { name, email, message } = req.body;

    const mailOptions = {
        from: email,
        to: 'your-email@gmail.com', // Ihre E-Mail-Adresse
        subject: 'Neue Kontaktformularnachricht',
        text: `Name: ${name}\nE-Mail: ${email}\nNachricht: ${message}`
    };

    transporter.sendMail(mailOptions, (error, info) => {
        if (error) {
            console.error('Fehler beim Senden der Nachricht:', error);
            return res.status(500).send('Fehler beim Senden der Nachricht.');
        }
        res.status(200).send('Nachricht erfolgreich gesendet.');
    });
});

app.listen(port, () => {
    console.log(`Server l„uft auf http://localhost:${port}`);
});
