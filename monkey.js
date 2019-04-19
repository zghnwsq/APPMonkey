var back = "";
var getCpu = [];
var it = 0;
var it2 = 0;
var cpu = [];
var acpu = [];
var vss = [];
var rss = [];


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
                        text: '%'
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
        credits:{
            enabled: false // 禁用版权信息
        },
        exporting:{
            enabled: false //禁用导出
        },
        series: [{
                name: 'CPU',
                data: [0]
                },{
                name: 'APP',
                color: '#8085e9',
                data: [0]
        }]
    });

var chart2 = Highcharts.chart('mem', {
        chart: {
                type: 'spline',
                marginRight: 10,
        },
        title: {
                text: 'APP Mem Trend'
        },
        xAxis: {
                type: 'datetime',
                tickPixelInterval: 150
        },
        yAxis: {
                title: {
                        text: 'MB'
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
        credits:{
            enabled: false // 禁用版权信息
        },
        exporting:{
            enabled: false //禁用导出
        },
        series: [{
                name: 'VSS',
                color: '#90ed7d',
                data: [0]
                },{
                name: 'RSS',
                color: '#f7a35c',
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
    var motion = " --pct-motion " + document.getElementById("motion").value
    var syskeys = " --pct-syskeys " + document.getElementById("syskeys").value
    var appswitch = " --pct-appswitch " + document.getElementById("appswitch").value
    var other = " " + document.getElementById("other").value
    var times = " " + document.getElementById("times").value
    var tmp = pkg + sed + t + v + touch + motion + syskeys + appswitch + other + times
    window.share.Run(tmp);
}


function GetCpu(){
    var cc = [];
    var app = document.getElementById("package").value
    window.share.Cpu(app, function(res){
        cc = res;
        cpu.push(parseInt(cc[0]));
        acpu.push(parseInt(cc[1]));
        vss.push(parseFloat(cc[2]));
        rss.push(parseFloat(cc[3]));
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
    it2 = setInterval(updateChart, 3000);
//    it = setInterval(function(){GetCpu()}, 5000);
}

function updateChart(){
//    cpu.push(parseInt(cc));
    chart.series[0].update({data:cpu});
    chart.series[1].update({data:acpu});
    chart2.series[0].update({data:vss});
    chart2.series[1].update({data:rss});
}