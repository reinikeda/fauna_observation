var lang = {
    en: {
        species_count: 'Species count',
        observed_species_count: 'Observed species count'
    },
    lt: {
        species_count: 'Rūšių skaičius',
        observed_species_count: 'Užfiksuotų rūšių skaičius'
    }
};

var browserLang = navigator.language || navigator.userLanguage;

var language = lang[browserLang] ? lang[browserLang] : lang['en'];

var ctx = document.getElementById('species-chart').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: {{ animal_class_labels|safe }},
        datasets: [{
            label: language.species_count,
            data: {{ species_count_data|safe }},
            backgroundColor: '#609966',
            borderColor: '#064420',
            borderWidth: 1
        }, {
            label: language.observed_species_count,
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