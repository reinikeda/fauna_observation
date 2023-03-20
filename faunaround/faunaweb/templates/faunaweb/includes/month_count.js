var ctx = document.getElementById('observation-month-chart').getContext('2d');
var chart = new Chart(ctx, {
  type: 'bar',
  data: {
    labels: {{ month_labels|safe }},
    datasets: [{
      label: 'Observation count',
      data: {{ month_data|safe }},
      backgroundColor: '#609966',
      borderColor: '#064420',
      borderWidth: 1
    }]
  },
  options: {
    scales: {
      yAxes: [{
        ticks: {
          beginAtZero: true
        }
      }]
    }
  }
});