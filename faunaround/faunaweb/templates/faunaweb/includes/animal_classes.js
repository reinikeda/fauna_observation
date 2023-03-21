var ctx = document.getElementById('species-chart').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: {{ animal_class_labels|safe }},
        datasets: [{
            label: 'Species count',
            data: {{ species_count_data|safe }},
            backgroundColor: '#609966',
            borderColor: '#064420',
            borderWidth: 1
        }, {
            label: 'Observed species count',
            data: {{ observed_species_data|safe }},
            backgroundColor: '#9DC08B',
            borderColor: '#064420',
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});