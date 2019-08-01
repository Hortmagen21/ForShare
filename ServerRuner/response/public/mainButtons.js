$('document').ready(function(){
$('#registbtn').on('click',function(){
    var username;
    var password;
    username=jQuery('#username').val();
    password=jQuery('#password').val();
    var data={"username":username, "password":password}
    $.ajax({
    type: "POST",
    url: "/registration",
    data: JSON.stringify(data),
    contentType: "application/json; charset=utf-8",
    success: function(msg){
    location.href="/";}
    })




});

$('#enter').on('click',function(){
    var username;
    var password;
    username=jQuery('#username').val();
    password=jQuery('#password').val();
    var data={"username":username, "password":password}
    $.ajax({
    type: "POST",
    url: "/login",
    data: JSON.stringify(data),
    contentType: "application/json; charset=utf-8",
    success: function(msg){
    location.href="/";}
    })

    //

});
});