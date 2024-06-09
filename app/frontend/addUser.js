const crypto = require('crypto');
const fs = require('fs');
const { sequelize } = require('./server/config/db');
const User = require('./server/models/User');

// Lire la clé privée
const privateKey = fs.readFileSync('private.pem', 'utf8');

async function addUser(email, password) {
    try {
        await sequelize.authenticate();
        console.log('Connection has been established successfully.');

        // Hacher le mot de passe avec la clé privée
        const hash = crypto.createSign('SHA256');
        hash.update(password);
        hash.end();
        const hashedPassword = hash.sign(privateKey, 'hex');

        console.log('Mot de passe haché pour l\'utilisateur:', hashedPassword);

        const user = await User.create({ email, password: hashedPassword });
        console.log('User created:', user.email);
    } catch (error) {
        console.error('Unable to connect to the database:', error);
    } finally {
        await sequelize.close();
    }
}

const args = process.argv.slice(2);
if (args.length !== 2) {
    console.error('Please provide email and password as arguments');
    process.exit(1);
}

const [email, password] = args;

addUser(email, password);
