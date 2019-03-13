let dailyAqi;
let dailyDate;

$.get('/daily-pred',(data)=>{
  console.log(data)
    dailyAqi = data.aqi;
    dailyDate = data.date;

})

$(document).ready(function(){
    var trace1 = {
    type: "scatter",
    mode: "lines",
    name: 'AQI',
    x: dailyDate,
    y: dailyAqi,
    line: {color: '#17BECF'}
  }





  var data = [trace1];

  var layout = {
    title: 'Daily AQI Prediction',
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

  Plotly.newPlot('dailyPredDiv', data, layout);
});





