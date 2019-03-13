let goodAqi = ['All outdoor activities','Safe for all','Safe for aged and children'];
let sensitiveAqi = ['Unsafe for children', 'Unsafe for asthma patients'];
let unhealthyAqi = ['Avoid outdoor activities','Unsafe for all patients'];
let veryUnhealthyAqi = ['Avoid all outdoor exertion'];
let harazdousAqi = ['Unsafe for all','Avoid at all cost'];

let precaution = $('#precautionDiv');

$.get('/live-data',(data)=>{
        let aqi = data.aqi;
        if(aqi <= 50){
            createPrecaution(goodAqi)
        }
        
        if((aqi > 50)&&(aqi <= 150)){
            createPrecaution(sensitiveAqi)
        }
        if((aqi > 150)&&(aqi <= 200)){
            createPrecaution(unhealthyAqi)
        }
        if((aqi > 200)&&(aqi <= 300)){
            createPrecaution(veryUnhealthyAqi)
        }
        if(aqi > 300){
            createPrecaution(harazdousAqi)
        }
    
    

    
})

function createPrecaution(data){
    for(let i of data){
        let tempDiv =  createDiv(i);
        precaution.append(tempDiv);

    }
}

function createDiv(data){
    let newDiv = $(`<div class="row"><div class="col s12"><label style="font-size:24pt">${data}</label></div></div></div>`);
    return newDiv;
}
