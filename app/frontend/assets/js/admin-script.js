document.addEventListener('DOMContentLoaded', () => {
    const userName = document.getElementById('user-name');
    const temperatureValue = document.getElementById('temperature-value');
    const crawlersValue = document.getElementById('crawlers-value');
    const speedValue = document.getElementById('speed-value');
    const siteDownsValue = document.getElementById('site-downs-value');

    // Fetch user name
    axios.get('/api/user')
        .then(response => {
            userName.textContent = response.data.name;
        })
        .catch(error => {
            console.error('Error fetching user data:', error);
        });

    // Fetch dashboard data
    axios.get('/api/dashboard')
        .then(response => {
            const data = response.data;
            temperatureValue.textContent = data.temperature || '--';
            crawlersValue.textContent = data.crawlers || '--';
            speedValue.textContent = data.speed ? `${data.speed} Mbs` : '--';
            siteDownsValue.textContent = data.siteDowns || '--';

            // Chart.js data
            const ctx = document.getElementById('crawlerChart').getContext('2d');
            new Chart(ctx, {
                type: 'line',
                data: {
                    labels: data.crawlerInfo.labels,
                    datasets: [{
                        label: 'Crawler Data',
                        data: data.crawlerInfo.data,
                        borderColor: 'rgba(255, 255, 255, 0.7)',
                        backgroundColor: 'rgba(255, 255, 255, 0.1)',
                    }]
                },
                options: {
                    scales: {
                        x: {
                            beginAtZero: true,
                            ticks: {
                                color: 'rgba(255, 255, 255, 0.7)',
                            }
                        },
                        y: {
                            beginAtZero: true,
                            ticks: {
                                color: 'rgba(255, 255, 255, 0.7)',
                            }
                        }
                    },
                    plugins: {
                        legend: {
                            labels: {
                                color: 'rgba(255, 255, 255, 0.7)'
                            }
                        }
                    }
                }
            });
        })
        .catch(error => {
            console.error('Error fetching dashboard data:', error);
        });
});


document.addEventListener('DOMContentLoaded', function() {
    const searchBar = document.querySelector('.search-login input');
    searchBar.addEventListener('keyup', function(event) {
        if (event.key === "Enter") {
            console.log("Searching for:", this.value); // Remplacer par la fonction de recherche réelle
        }
    });

    // Supposons que l'utilisateur soit récupéré via une API
    fetch('/api/user')
        .then(response => response.json())
        .then(data => {
            document.getElementById('user-name').textContent = data.username;
        })
        .catch(error => console.error('Failed to load user data', error));
});
