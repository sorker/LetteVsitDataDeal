$(function () {
   $("#submit").click(function () {
       var city = $("#city").val();
       var country = $("#country").val();
       var title = $("#title").val();
       var content = $("#content").val();
       $.ajax({
           url:"/tsxs/getinput",
           dataType:"json",
           type:"post",
           data:{"city":city,"country":country,"title":title,"content":content},
           success:function(result){
               location.href="../templates/xuandepartment.html";
               //alert(result);
           },
           error:function(e){
               console.log(e);
           }
       });
   })
});