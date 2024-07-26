const express = require('express');
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.json());

let likedItems = [];

app.post('/like', (req, res) => {
    const { item } = req.body;
    if (!likedItems.includes(item)) {
        likedItems.push(item);
    }
    res.json({ message: `${item} wurde zur Gef„llt mir Liste hinzugefgt.` });
});

app.get('/likes', (req, res) => {
    res.json(likedItems);
});

const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Server l„uft auf http://localhost:${PORT}`);
});
