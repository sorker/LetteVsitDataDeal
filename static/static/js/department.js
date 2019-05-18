$(function(){
    $("#goto").attr("disabled",true);
    var num;
    $("#complaints").click(function () {
        $("#d_form").show().siblings().hide();
});
$("#query").click(function () {
    $("#d_table").show().siblings().hide();
});
$("#querymessage").click(function () {
    $("tbody tr").remove();
    num=0;
    $.ajax({
        url:"/tsxs/getdepartmentmessage",
        dataType:"json",
        type:"post",
        data:{"replyUnit":"教育部","nums": num },
        success:function(result) {
            //遍历获得的json
            //console.log(result.length);
            for (var i = 0; i < result.length; i++) {
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
                    '         <td><div>' + title + '</div></td>\n' +
                    '        <td><div>' + content + '</div></td>\n' +
                    '        <td><div>' + replyUnit + '</div></td>\n' +
                    '        <td><div>' + datetime + '</div></td>\n' +
                    '        <td><div><a href="javascript:void(0);" style="text-decoration:none;" onclick="delTr(this)">处理</a></td>\n' +
                    '    </tr>\n');
            }
        },
        error:function(e){
            console.log(e);
        }
    });
});
$("#last").click(function () {
    if(num===0 || typeof num === 'undefined'){
        alert("不能到上一页，此页是第一页");
    }else{
        num=num-6;
        if(num>=0){
            $("tbody tr").remove();
            $.ajax({
                url:"/tsxs/getdepartmentmessage",
                dataType:"json",
                type:"post",
                data:{"replyUnit":"教育部","nums": num },
                success:function(result) {
                    //遍历获得的json
                    //console.log(result.length);
                    for (var i = 0; i < result.length; i++) {
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
                            '         <td><div>' + title + '</div></td>\n' +
                            '        <td><div>' + content + '</div></td>\n' +
                            '        <td><div>' + replyUnit + '</div></td>\n' +
                            '        <td><div>' + datetime + '</div></td>\n' +
                            '        <td><div><a href="javascript:void(0);" style="text-decoration:none;" onclick="delTr(this)">处理</a></td>\n' +
                            '    </tr>\n');
                    }
                },
                error:function(e){
                    console.log(e);
                }
            });
        }else{
            alert("不能到上一页，此页是第一页");
        }
    }
});
$("#next").click(function () {
    num=num+6;
    if(typeof num === 'undefined'){
        alert("不能到下一页，此页是最后一页");
    }else{
        $.ajax({
            url:"/tsxs/getdepartmentmessage",
            dataType:"json",
            type:"post",
            data:{"replyUnit":"教育部","nums": num },
            success:function(result) {
                if(result.length === 0){
                    alert("后面没有数据了");
                }else{
                    $("tbody tr").remove();
                    //遍历获得的json
                    //console.log(result.length);
                    for (var i = 0; i < result.length; i++) {
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
                            '         <td><div>' + title + '</div></td>\n' +
                            '        <td><div>' + content + '</div></td>\n' +
                            '        <td><div>' + replyUnit + '</div></td>\n' +
                            '        <td><div>' + datetime + '</div></td>\n' +
                            '        <td><div><a href="javascript:void(0);" style="text-decoration:none;" onclick="delTr(this)">处理</a></td>\n' +
                            '    </tr>\n');
                    }
                }

            },
            error:function(e){
                console.log(e);
            }
        });
    }
});
$("#text").focus(function () {
    $("#goto").attr("disabled",false);
})
function isNumber(val) {
        var regPos = /^\d+(\.\d+)?$/; //非负浮点数
        var regNeg = /^(-(([0-9]+\.[0-9]*[1-9][0-9]*)|([0-9]*[1-9][0-9]*\.[0-9]+)|([0-9]*[1-9][0-9]*)))$/; //负浮点数
        if(regPos.test(val) || regNeg.test(val)) {
            return true;
        } else {
            return false;
        }
    }
$("#goto").click(function () {
    var inputnum = $("#text").val();
    var actionnum= (inputnum-1)*6;
    if(isNumber(inputnum)===false){
        alert("只能输入数字");
    }else if(inputnum<1){
        alert("数字不能小于1");
    }else{
        $.ajax({
            url:"/tsxs/getdepartmentmessage",
            dataType:"json",
            type:"post",
            data:{"replyUnit":"教育部","nums": actionnum },
            success:function(result) {
                if(result.length === 0){
                    alert("跳转的页面没有数据");
                }else{
                    $("tbody tr").remove();
                    //遍历获得的json
                    //console.log(result.length);
                    for (var i = 0; i < result.length; i++) {
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
                            '         <td><div>' + title + '</div></td>\n' +
                            '        <td><div>' + content + '</div></td>\n' +
                            '        <td><div>' + replyUnit + '</div></td>\n' +
                            '        <td><div>' + datetime + '</div></td>\n' +
                            '        <td><div><a href="javascript:void(0);" style="text-decoration:none;" onclick="delTr(this)">处理</a></td>\n' +
                            '    </tr>\n');
                    }
                }

            },
            error:function(e){
                console.log(e);
            }
        });
    }
})
});
function delTr(obj){
    var replyUnit = $(obj).parents("tr").children("td").eq(2).text();
    var title= $(obj).parents("tr").children("td").eq(0).text();
    var content = $(obj).parents("tr").children("td").eq(1).text();
    $(obj).parents("tr").remove();//jquery添加的东西需要另一行需要 把删除的函数放到$(function)外
    $.ajax({
        url:"/tsxs/deletedr",
        type:"post",
        dataType:"text",
        data:{"title":title,"content":content},
        success:function(result){
            var res = parseInt(result);
            if(res>0){
                alert(replyUnit+"已处理事件");
            }else{
                alert("处理失败");
            }
        },
        error:function(e){
            console.log(e);
        }
    });

}