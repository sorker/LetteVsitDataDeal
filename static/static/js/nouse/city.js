
/*
$(function () {
    $.ajax({
        url:"/tsxs/getcity",
        dataType:"json",
        type:"post",
        success:function(result){
            for(var i=0;i<result.length;i++){
                var city = result[i].city;
                var cityArea = result[i].city_area;
                if(city="杭州"){
                    province[0].city
                }
            }
        },
        error:function(e){
            console.log(e);
        }
    });
});*/
var provice =[{
        name: "浙江省",
        city: [
            {
                name: "杭州",
                districtAndCounty: ["拱墅区", "上城区", "下城区", "江干区", "西湖区", "滨江区", "余杭区", "萧山区", "临安市", "富阳市", "建德市", "桐庐县", "淳安县", "千岛湖镇","经济技术开发区"]
            },
            {
                name: "湖州",
                districtAndCounty: ["吴兴区", "南浔区", "长兴县", "雉城镇", "德清县", "武康镇", "安吉县", "递铺镇","湖州度假区","湖州开发区"]
            },
            {
                name: "嘉兴",
                districtAndCounty: ["南湖区", "秀洲区", "平湖市", "海宁市", "桐乡市", "嘉善县", "魏塘镇", "海盐县", "武原镇","经济技术开发区","国际商务区"]
            },
            {
                name: "舟山",
                districtAndCounty: ["定海区", "普陀区", "岱山县", "高亭镇", "嵊泗县", "菜园镇"]
            },
            {
                name: "宁波",
                districtAndCounty: ["海曙区", "江东区", "江北区", "北仑区", "镇海区", "鄞州区", "慈溪市", "余姚市", "奉化市", "宁海县", "象山县"]
            },
            {
                name: "绍兴",
                districtAndCounty: ["越城区", "诸暨市", "上虞市", "嵊州市", "绍兴县", "新昌县", "城关镇"]
            },
            {
                name: "衢州",
                districtAndCounty: ["柯城区", "衢江区", "江山市", "常山县", "天马镇", "开化县", "城关镇", "龙游县"]
            },
            {
                name: "金华",
                districtAndCounty: ["婺城区", "金东区", "兰溪市", "永康市", "义乌市", "东阳市", "武义县", "浦江县", "磐安县", "安文镇"]
            },
            {
                name: "台州",
                districtAndCounty: ["椒江区", "黄岩区", "路桥区", "临海市", "温岭市", "三门县", "海游镇", "天台县", "仙居县", "玉环县", "珠港镇"]
            },
            {
                name: "温州",
                districtAndCounty: ["鹿城区", "龙湾区", "瓯海区", "瑞安市", "乐清市", "永嘉县", "上塘镇", "文成县", "大峃镇", "平阳县", "昆阳镇", "泰顺县", "罗阳镇", "洞头县", "北岙镇", "苍南县", "灵溪镇"]
            },
            {
                name: "丽水",
                districtAndCounty: ["莲都区", "龙泉市", "缙云县", "五云镇", "青田县", "鹤城镇", "云和县", "云和镇", "遂昌县", "妙高镇", "松阳县", "西屏镇", "庆元县", "松源镇", "景宁畲族自治县", "鹤溪镇"]
            }
        ]
}];
