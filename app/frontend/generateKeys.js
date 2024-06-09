const crypto = require('crypto');
const fs = require('fs');

// Générer une paire de clés RSA
const { publicKey, privateKey } = crypto.generateKeyPairSync('rsa', {
  modulusLength: 2048,
  publicKeyEncoding: {
    type: 'spki',
    format: 'pem'
  },
  privateKeyEncoding: {
    type: 'pkcs8',
    format: 'pem'
  }
});

// Sauvegarder les clés dans des fichiers
fs.writeFileSync('private.pem', privateKey);
fs.writeFileSync('public.pem', publicKey);

console.log('Clés générées et sauvegardées dans private.pem et public.pem');
