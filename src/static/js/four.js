(
    function() {
        console.log("*******");
        $.get('/statistics-data', (data) => {
            // console.log("FourthGet",data);
            NallData = data.loc_high_so2;
            // console.log(NallData);
            fourthGraph(NallData);

        })
    }
)();

function fourthGraph(data){

        let allData = data;
        console.log("Fourth",allData);
        let cityName = allData[0];
        let cityData = allData[1];
        let margin = {left:100,bottom:100, right:10,top:10};

        let width = 800 - margin.left - margin.right;
        let height = 500 - margin.top - margin.bottom;


        let div3 = d3.select('#fourth')
            .append('svg')
            .attr('height',height + margin.top+ margin.bottom)
            .attr('width',width+margin.left+margin.right);

        let g = div3.append('g')
            .attr("transform","translate("+margin.left+","+margin.top+")");



        let newData = cityName.map((x,i)=>{
            return{
                name:x,
                height:cityData[i]
            }
        })


        let x = d3.scaleBand()
            .domain(newData.map((d)=>{
                // console.log("DNAME",d.name)
                return d.name
            }))
            .range([0,width])
            .paddingInner(0.3)
            .paddingOuter(0.3);
        // console.log(x.bandwidth)

        let y =d3.scaleLinear()
            .domain([0,d3.max(newData,(d)=>{
                return d.height;
            })])
            .range([height,0]);


        let xAxis = d3.axisBottom(x);
        g.append("g")
            .attr("class","x axis")
            .attr("transform","translate(0,"+height+")")
            .call(xAxis)
            .selectAll("text")
            .attr("y","10")
            .attr("x","-5")
            .attr("text-anchor","end")
            .attr("transform","rotate(-40)");

        let yAxis = d3.axisLeft(y);
        g.append("g")
            .attr("class","y-axis")
            .call(yAxis);

        let rect = g.selectAll('rect')
            .data(newData)

        rect.enter()
            .append('rect')
            .attr('x',(d)=>{
                // console.log(x(d.name))
                return x(d.name);
            })
            .attr('y',(d)=>{
                return y(d.height)
            })
            .attr('height',(tempD)=>{
                return height-y(tempD.height)
            })
            .attr('width',x.bandwidth)

            .attr('fill','blue')

}
