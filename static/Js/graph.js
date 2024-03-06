document.addEventListener('DOMContentLoaded', function () {
  function updateGraph() {
    var data = [];
    if (document.getElementById('option1').checked) {
      // Ajoutez les données spécifiques à la data
    }
    if (document.getElementById('option2').checked) {
      // Ajoutez les données spécifiques à la data
    }
    // Utilisez Plotly pour redessiner le graphique
    Plotly.newPlot('graph', data);
  }

  // Ajoutez un écouteur d'événements à chaque checkbox pour redessiner le graphique à chaque changement
  var checkboxes = document.querySelectorAll('input[type=checkbox]');
  checkboxes.forEach(function(checkbox) {
    checkbox.addEventListener('change', updateGraph);
  });

  // Dessinez le graphique initialement
  updateGraph();
});