var citys=new Array();
var countrys=new Array();
$(function(){
    $.ajax({
        url:"/tsxs/getcity",
        dataType:"json",
        type:"post",
        data:{},
        success:function(result){
            result.forEach(function (item, index) {
                if (citys.indexOf(item.city) === -1) {
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
        }
    });
    $("#prov").change(function () {
            for(var i=0;i<citys.length;i++){
                $("#city").append(' <option>\n' +
                        citys[i]                  +
                        '</option>');
            };
        });
    $("#city").change(function () {
        for(var i=0;i<countrys.length;i++){
            $("#country").append(' <option>\n' +
                countrys[i]                  +
                '</option>');
        };
    });
});