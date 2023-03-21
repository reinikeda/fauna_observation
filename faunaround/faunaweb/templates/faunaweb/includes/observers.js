var ctx = document.getElementById('observers-chart').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'pie',
    data: {
        labels: {{ observer_labels|safe }},
        datasets: [{
            data: {{ observer_data|safe }},
            backgroundColor: [
                '#609966',
                '#9DC08B',
                '#61876E',
                '#A6BB8D',
                '#BBD6B8',
                '#6e8661',
                '#6e8661',
                '#b9c08b',
                '#818661',
                '#6e8661'
            ]
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: true,
        legend: {
            position: 'right'
        }
    }
});