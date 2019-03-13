let yearlyAqi;
let yearlyDate;

$.get('/yearly-pred',(data)=>{
  console.log(data)
    yearlyAqi = data.aqi;
    yearlyDate = data.date;

})

$(document).ready(function(){
    var trace1 = {
    type: "scatter",
    mode: "lines",
    name: 'AQI',
    x: yearlyDate,
    y: yearlyAqi,
    line: {color: '#17BECF'}
  }





  var data = [trace1];

  var layout = {
    title: 'Yearly AQI Prediction',
    xaxis: {
      autorange: true,
      range: ['2015-02-17', '2017-02-16'],
        rangeslider: {range: ['2014-02-17', '2015-02-16']},
      type: 'date'
    },
    yaxis: {
      autorange: true,
      range: [0, 1000],
      type: 'linear'
    }
  };

  Plotly.newPlot('yearlyPredDiv', data, layout);
});





