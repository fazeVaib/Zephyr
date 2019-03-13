(function() {

    $.get('/statistics-data',(data)=>{
        console.log("*******");
        NallData = data.allstate_so2_no2_rspm_spm;
        console.log("ALL DATA",data)
    allStateGraph(NallData);

    })

})();


function allStateGraph(allData)
{
    let margin = {left: 100, bottom: 150, right: 10, top: 10}

    let width = 2400 - margin.left - margin.right;
    let height = 600 - margin.top - margin.bottom;


    let div3 = d3.select('#div3')
        .append('svg')
        .attr('height', height + margin.top + margin.bottom)
        .attr('width', width + margin.left + margin.right)

    //x-label
        div3.append("text")
            .attr("class", "x axis-label")
            .attr("x",(width/2)+50)
            .attr("y",height+124)
            .attr("font-size","20px")
            .attr("text-anchor","middle")
            .text("States");

    //ylabel
        div3.append("text")
            .attr("class","y axis-label")
            .attr("x",-(height/2))
            .attr("y",+60)
            .attr("font-color","black")
            .attr("font-size","20px")
            .attr("text-anchor","middle")
            .attr("transform","rotate(-90)")
            .text("Level of Pollutant (ug/m3)");

    let g = div3.append('g')
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")")
    let cityName = allData[0];
    let so2 = allData[1];
    let no2 = allData[2];
    let co2 = allData[3];
    let pm2 = allData[4];

    console.log(cityName.length, so2.length, no2.length, co2.length, pm2.length);

    let newData = cityName.map((x, i) => {
        return {
            name: x,
            height: so2[i]
        }
    })


    let x = d3.scaleBand()
        .domain(newData.map((d) => {
            console.log("DNAME", d.name)
            return d.name
        }))
        .range([0, width])
        .paddingInner(0.3)
        .paddingOuter(0.3);
    console.log(x.bandwidth)

    let y = d3.scaleLinear()
        .domain([0, d3.max(newData, (d) => {
            return d.height;
        })])
        .range([height, 0])


    let xAxis = d3.axisBottom(x);
    g.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(0," + height + ")")
        .call(xAxis)
        .selectAll("text")
        .attr("y", "10")
        .attr("x", "-5")
        .attr("text-anchor", "end")
        .attr("font-color","black")
        .attr("transform", "rotate(-40)")

    let yAxis = d3.axisLeft(y);
    g.append("g")
        .attr("class", "y-axis")
        .call(yAxis);

    let rect = g.selectAll('rect')
        .data(newData)

    rect.enter()
        .append('rect')
        .attr('x', (d) => {
            console.log(x(d.name))
            return x(d.name);
        })
        .attr('y', (d) => {
            return y(d.height)
        })
        .attr('height', (tempD) => {
            return height - y(tempD.height)
        })
        .attr('width', x.bandwidth)

        .attr('fill', '#238acb')
}
