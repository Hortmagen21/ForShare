$('document').ready(function(){
if(window.location.pathname=="/"){
jQ_append("textbox")
}

function jQ_append(id_of_input)
{
   var id=location.search;
   var sep_id=id.split("=");
   var int_id=sep_id[1];
   data={"id":int_id,"getname":{"name":" "}}
    //alert(id)
    //alert(typeof(int_id))
    $.ajax({
    type: "POST",
    url: "/",
    data: JSON.stringify(data),
    contentType: "application/json; charset=utf-8",
    success: function(msg){
    text=msg["getname"]["name"]
    var input_id="#"+id_of_input;
    $(input_id).val($(input_id).val()+text);

    }
    })





}
$('#registbtn').on('click',function(){

    var username;
    var password;
    username=jQuery('#username').val();
    password=jQuery('#password').val();
    var repassword=$('#repassword').val();
    if(username!="" && password!=""){
    if (repassword==password){
    var data={"username":username, "password":password,"gainId":{"id":0}}
    $.ajax({
    type: "POST",
    url: "/registration",
    data: JSON.stringify(data),
    contentType: "application/json; charset=utf-8",
    success: function(msg){
     location.href=`/?id=${msg["gainId"]["id"]}`;}
    })}
    else{
    alert("incorect password");
    }
    }
    else{
    alert("pls,fill the gaps");
    }




});

$('#enter').on('click',function(){

    var username;
    var password;
    username=jQuery('#username').val();
    password=jQuery('#password').val();
    if(username!="" && password!=""){
    var data={"username":username, "password":password,"gainId":{"id":0}}
    $.ajax({
    type: "POST",
    url: "/login",
    data: JSON.stringify(data),
    contentType: "application/json; charset=utf-8",
    success: function(msg){//msg change
     //alert(msg["gainId"]["id"]);
     location.href=`/?id=${msg["gainId"]["id"]}`}
    })
    }
    else{
    alert("incorect pass")
    }



});
$('#entertest').on('click',function(){


})
});
