const User = require('../models/User');
const { validationResult } = require('express-validator');
const crypto = require('crypto');
const fs = require('fs');

// Lire la clé publique
const publicKey = fs.readFileSync('public.pem', 'utf8');

exports.loginUser = async (req, res) => {
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
        return res.status(400).json({ errors: errors.array() });
    }

    const { email, password } = req.body;

    try {
        console.log(`Recherche de l'utilisateur avec l'email : ${email}`);

        let user = await User.findOne({
            where: { email },
            attributes: ['password']
        });

        if (!user) {
            console.log('Utilisateur non trouvé');
            return res.status(400).json({ success: false, message: 'Identifiants invalides' });
        }

        console.log(`Utilisateur trouvé. Mot de passe haché : ${user.password}`);

        // Vérifier le mot de passe avec la clé publique
        const verify = crypto.createVerify('SHA256');
        verify.update(password);
        verify.end();
        const isMatch = verify.verify(publicKey, user.password, 'hex');

        console.log(`Mot de passe entré : ${password}`);
        console.log(`Résultat de la comparaison : ${isMatch}`);

        if (!isMatch) {
            console.log('Mot de passe incorrect');
            return res.status(400).json({ success: false, message: 'Identifiants invalides' });
        }

        console.log('Connexion réussie');
        return res.status(200).json({ success: true, message: 'Connexion réussie' });
    } catch (error) {
        console.error('Erreur du serveur:', error.message);
        res.status(500).send('Erreur du serveur');
    }
};
