$(function () {
    var color="";
    $("tr").mouseenter(function () {
        color=$(this).css("background-color");
        $(this).css("background-color","#D9EDF7");
    });
    $("tr").mouseleave(function () {
        $(this).css("background-color",color);
    });
        //
   /* function delTr(){
    /!*var table = obj.parentNode.parentNode.parentNode.parentNode;
    var tr = obj.parentNode.parentNode.parentNode;
    table.removeChild(tr);*!/
    alert("删除了");
    }*/
    $("a").click(function () {
        alert("删除了");
    });
    //点击确定获取servledemo1中的响应内容
    $("#button-show").click(function () {
     var prov_v = $("#prov").val();
        var city_v = $("#city").val();
        var country_v = $("#country").val();
        //console.log(provice[prov_v].name+provice[prov_v]["city"][city_v].name+
        // provice[prov_v]["city"][city_v].districtAndCounty[country_v]);
        $.ajax({
            url:"/tsxs/servletdemo1",
            dataType:"json",
            type:"post",
           /* data:{"prov":provice[prov_v].name,"city":provice[prov_v]["city"][city_v].name,
                "country":provice[prov_v]["city"][city_v].districtAndCounty[country_v]},*/
           data:{"prov":prov_v,"city":city_v,"country":country_v},
            success:function(result){
                //遍历获得的json
                for(var i=0;i<result.length;i++){
                    //json里的字段
                    var id = result[i].id;
                    var province = result[i].province;
                    var city = result[i].city;
                    var cityarea = result[i].city_area;
                    var title = result[i].title;
                    var content = result[i].content;
                    var reflectingTime = result[i].reflecting_time;
                    var replyUnit = result[i].reply_unit;
                    var replyTime = result[i].reply_time;
                    var replyOption = result[i].reply_option;
                    var datetime = result[i].datetime;
                    //加入表格中
                    $("table tbody").append(' <tr>\n' +
                        '         <td><div>'+title+'</div></td>\n' +
                        '        <td><div>'+content+'</div></td>\n' +
                        '        <td><div>'+replyUnit+'</div></td>\n' +
                        '        <td><div>'+datetime+'</div></td>\n' +
                        '        <td><div><a href="javascript:void(0);" style="text-decoration:none;">移交</a></td>\n'+
                        '    </tr>\n');
                }
            },
            error:function(e){
                console.log(e);
            }
        });
    });
});
