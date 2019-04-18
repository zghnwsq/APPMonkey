var back = "";
var getCpu = [];
var it = 0;
var it2 = 0;
var cpu = [];
var acpu = [];


    Highcharts.setOptions({
            global: {
                        useUTC: false
                }
        });
    var chart = Highcharts.chart('container', {
        chart: {
                type: 'spline',
                marginRight: 10,
        },
        title: {
                text: 'CPU Trend'
        },
        xAxis: {
                type: 'datetime',
                tickPixelInterval: 150
        },
        yAxis: {
                title: {
                        text: null
                }
        },
        tooltip: {
                formatter: function () {
                        return '<b>' + this.series.name + '</b><br/>' +
                                Highcharts.dateFormat('%Y-%m-%d %H:%M:%S', this.x) + '<br/>' +
                                Highcharts.numberFormat(this.y, 2);
                }
        },
        legend: {
                enabled: true
        },
        series: [{
                name: 'CPU',
                data: [0]
                },{
                name: 'APP',
                data: [0]
        }]
    });



$(document).ready(function(){
    new QWebChannel(qt.webChannelTransport, function(channel){
        window.share = channel.objects.share;
    });
});



function WebToQt() {
    var name = document.getElementById("username").value;
    window.share.WebToQt(name);
}
function QtToWeb(){
    window.share.QtToWeb(function(res){
        back = res;
        return res;
    });
    setTimeout(update, 1000);
}
function update(){
    document.getElementById("back").value = back;
}
function run(){
    var pkg = " -p " + document.getElementById("package").value
    var sed = " -s " + document.getElementById("seed").value
    var t = " --throttle " + document.getElementById("throttle").value
    var v = " " + document.getElementById("v").value
    var touch = " --pct-touch " + document.getElementById("touch").value
    var syskeys = " --pct-syskeys " + document.getElementById("syskeys").value
    var appswitch = " --pct-appswitch " + document.getElementById("appswitch").value
    var other = " " + document.getElementById("other").value
    var times = " " + document.getElementById("times").value
    var tmp = pkg + sed + t + v + touch + syskeys + appswitch + other + times
    window.share.Run(tmp);
}


function GetCpu(){
    var cc = [];
    var app = document.getElementById("package").value
    window.share.Cpu(app, function(res){
        cc = res;
        cpu.push(parseInt(cc[0]));
        acpu.push(parseInt(cc[1]))
    });
//    setTimeout(function(cc){updateCpu(cc)}, 3000);
}


function stopIt(){
    clearInterval(it);
    clearInterval(it2);
//    setTimeout(function(){clearInterval(it);}, 1000);
}

function monitor(){
    it = setInterval(GetCpu, 3000);
    it2 = setInterval(updateCpu, 3000);
//    it = setInterval(function(){GetCpu()}, 5000);
}

function updateCpu(){
//    cpu.push(parseInt(cc));
    chart.series[0].update({data:cpu});
    chart.series[1].update({data:acpu});
}