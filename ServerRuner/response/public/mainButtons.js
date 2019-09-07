
$('document').ready(function(){

if(window.location.pathname=="/"){
jQ_append("textbox")
}
function logInitilization(){
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
     //alert(typeof(msg["gainId"]["id"]));
     var id_giver=msg["gainId"]["id"];
     //location.href=`/?id=${msg["gainId"]["id"]}`
     Cookies.set("id",id_giver,{expires:1});
     location.href="/";
     }
    })
    }
    else{
    alert("incorect pass")
    }
}
function registration(){
    var username=jQuery('#username').val();
    var password=jQuery('#password').val();
   //var isAcceptRules=$('#Rulesconfirm').val();//string(on-is true)
    //alert(isAcceptRules);
    var repassword=$('#repassword').val();
    if(username!="" && password!=""){
    if (repassword==password){
    if ($('#Rulesconfirm').is(":checked")){
    var data={"username":username, "password":password,"gainId":{"id":0}}
    $.ajax({
    type: "POST",
    url: "/registration",
    data: JSON.stringify(data),
    contentType: "application/json; charset=utf-8",
    success: function(msg){
        var id_giver=msg["gainId"]["id"];
        //location.href=`/?id=${msg["gainId"]["id"]}`;
        Cookies.set("id",id_giver,{expires:1});
        location.href="/";
     }
    })
    //isAcceptRules
    }
    else{
    alert("pls,confirm Site's Rules")
    }
    //repass!=pass
    }
    else{
    alert("password isn't equal repassword");
    }
    //empty user or pass
    }
    else{
    alert("pls,fill the gaps");
    }
}


$('#registbtn').on('click',function(){
    registration();
});

$('#enter').on('click',function (){
    logInitilization();
});
$('#entertest').on('click',function(){
    //var a="2";
    //alert(Cookies.set("idr","rt"));
    //Cookies.set("idr",a);
    //alert(Cookies.get("idr"));
})
function jQ_append(id_of_input)
{
   //var id=location.search;
   //var sep_id=id.split("=");
   //var int_id=sep_id[1];
   var int_id=Cookies.get("id");
   data={"id":int_id,"getname":{"name":" "}};
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
    if($(input_id).val()==" "){
    $(input_id).val($(input_id).val()+text);
    }
    }
    })
}

$("body").keydown(function (e){
    if(e.keyCode == 13){
    if(window.location.pathname=="/login"){
        logInitilization();
        }
    else if(window.location.pathname=="/registration"){
        registration();
        }
    else{
    //для других страниц
    }
    }
});
});
