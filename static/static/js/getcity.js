var citys=new Array();
var countrys=new Array();
$(function(){
    var color="";
    $("tr").mouseenter(function () {
        color=$(this).css("background-color");
        $(this).css("background-color","#D9EDF7");
    });
    $("tr").mouseleave(function () {
        $(this).css("background-color",color);
    });
    $.ajax({
        url:"/tsxs/getcity",
        dataType:"json",
        type:"post",
        data:{},
        success:function(result){
            result.forEach(function (item, index) {    //数组的foreach方法对获得的json数据进行便利 item表示当时的元素 index表示索引
                if (citys.indexOf(item.city) === -1) {  //indexOf(value)	从前往后索引，获取 value 在数组中的第一个下标
                    citys.push(item.city);
                }
                if (countrys.indexOf(item.city_area) === -1) {
                    countrys.push(item.city_area);
        }
            })
           /* console.log(citys);
            console.log(countrys);*/
        },
        error:function(e){
            console.log(e);
            alert("失败了");
        }
    });
    $("#prov").change(function () {
        $("#button-show").attr("disabled",true);//按钮不可按
            for(var i=0;i<citys.length;i++){
                $("#city").append(' <option>\n' +     //动态添加option
                        citys[i]                  +
                        '</option>');
            };
        });
    $("#city").change(function () {
       $("#button-show").attr("disabled",true);
        for(var i=0;i<countrys.length;i++){         //动态添加option
            $("#country").append(' <option>\n' +
                countrys[i]                  +
                '</option>');
        };
    });
    $("#country").change(function () {
        var prov_v = $("#prov  option:selected").text();//获取select中选中的option的值
        var city_v = $("#city  option:selected").text();//获取select中选中的option的值
        if(prov_v!=null && city_v!=null){//
            $("#button-show").attr("disabled",false);//按钮可按
        }
    });
    $("#button-show").on('click',function () {      /*给按钮另加一个事件 用on 否则会出现覆盖问题*/
        $("#addr-show").val($("#prov  option:selected").text()+$("#city  option:selected").text()+
            $("#country  option:selected").text()); //获取select中选中的option的值
    });
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
                '        <td><div><a href="javascript:void(0);" style="text-decoration:none;" onclick="delTr(this)">移交</a></td>\n'+
                '    </tr>\n');
        }
    },
            error:function(e){
                console.log(e);
            }
        });
    });
});
function delTr(obj){
    var replyUnit = $(obj).parents("tr").children("td").eq(2).text();
    $(obj).parents("tr").remove();//jquery添加的东西需要另一行需要 把删除的函数放到$(function)外
    alert("已移交"+replyUnit);
}