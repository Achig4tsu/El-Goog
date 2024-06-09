const rateLimit = require('express-rate-limit');

const loginLimiter = rateLimit({
    windowMs: 15 * 60 * 1000, // 15 minutes
    max: 5, // Limite chaque IP à 5 requêtes par `window` (ici, par 15 minutes)
    message: "Trop de tentatives de connexion. Veuillez réessayer plus tard.",
    headers: true,
});

module.exports = loginLimiter;
