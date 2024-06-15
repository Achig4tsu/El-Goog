const express = require('express');
const helmet = require('helmet');
const cors = require('cors');
const authRoutes = require('.//routes/auth');
const { sequelize } = require('.//config/db');
const dotenv = require('dotenv');

dotenv.config();

const app = express();

// Middlewares
app.use(helmet());
app.use(cors({
    origin: 'http://mariadb:3306',
    methods: ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'],
    allowedHeaders: ['Content-Type', 'Authorization'],
    credentials: true
}));
app.use(express.json());

// Sequelize Connection
sequelize.authenticate()
    .then(() => console.log('Database connected...'))
    .catch(err => console.log('Error: ' + err));

// Routes
app.use('/api/auth', authRoutes);

// Handle OPTIONS requests
app.options('*', cors());

// Start Server
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
