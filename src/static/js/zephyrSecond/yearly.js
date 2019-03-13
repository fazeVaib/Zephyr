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
    line: {color: '#D8001F'}
  }





  var data = [trace1];

  var layout = {
    autosize: false,
  width: 1150,
  height: 601,
  margin: {
    l: 50,
    r: 50,
    b: 100,
    t: 100,
    pad: 4
  },
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





