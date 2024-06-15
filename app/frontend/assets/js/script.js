document.addEventListener("DOMContentLoaded", () => {
    const loginModal = document.getElementById('loginModal');
    const settingsIcon = document.getElementById('settingsIcon');
    const settingsMenu = document.getElementById('settingsMenu');
    const darkModeToggle = document.getElementById('darkModeToggle');
    const body = document.body;

    settingsIcon.addEventListener('click', () => {
        settingsMenu.classList.toggle('show');
    });

    darkModeToggle.addEventListener('change', () => {
        body.classList.toggle('dark-mode');
    });

    document.getElementById('loginForm').addEventListener('submit', async (e) => {
        e.preventDefault();
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;

        console.log('Form submitted with', { email, password });

        try {
            const response = await fetch('http://localhost:5000/api/auth/login', { // Assurez-vous que l'URL est correcte
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ email, password })
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();
            console.log('Response from server:', data);

            if (data.success) {
                showSuccessAnimation();
                setTimeout(() => {
                    window.location.href = 'adminpanel.html';  // Remplacez par l'URL de votre nouvelle page
                }, 2000);
            } else {
                alert('Erreur de connexion');
            }
        } catch (error) {
            console.error('Erreur:', error);
        }
    });
});

function openLogin() {
    document.getElementById('loginModal').style.display = 'block';
}

function closeLogin() {
    document.getElementById('loginModal').style.display = 'none';
}

function showSuccessAnimation() {
    const successMessage = document.createElement('div');
    successMessage.className = 'success-animation';
    successMessage.innerText = 'Connexion réussie!';
    document.body.appendChild(successMessage);
    setTimeout(() => {
        successMessage.classList.add('fade-out');
        setTimeout(() => {
            document.body.removeChild(successMessage);
        }, 1000);
    }, 1000);
}
