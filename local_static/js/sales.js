$(document).ready(function(){
  function renderChart(id, data, labels){
    var ctx = $('#' + id)
    var myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: 'Sales',
                data: data,
                backgroundColor: 'rgba(0, 158, 29, 0.45)',
                borderColor:'rgba(0, 158, 29, 1)',
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero:true
                    }
                }]
            },
            backgroundColor: 'rgba(75, 192, 192, 1)'
        }
    })
  }

  function getSalesData(id, type){
    var url = '/analytics/sales/data/'
    var method = 'GET'
    var data = {'type': type}

    $.ajax({
      url: url,
      method: method,
      data: data,
      success: function(responseData){
        renderChart(id, responseData.data, responseData.labels)
      },
      error: function(error){
        console.log(url)
        console.log(data)
        console.log(method)
        $.alert("An error occurred")
      }
    })
  }

  var chartsToRender = $('.ecommerce-render-chart')
  $.each(chartsToRender, function(index, html){
    var $this = $(this)
    var id = $this.attr('id')
    var dataType = $this.attr('data-type')
    if (id && dataType){
      getSalesData(id, dataType)
    }
  })
})