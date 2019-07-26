$('document').ready(function(){
$('#enter').on('click',function(){
    var Loger;
    var Loger=new XMLHttpRequest();
    Loger.open('GET','database',false);
    Loger.send();
    if (Loger.status !=200){
	    location.href="/login";}
    else{
	    var jsoncontain;
	    var jsoncontain=JSON.parse(Loger.responseText);
	    //alert(jsoncontain);
	    //alert(Loger.responseText);
	    //alert(jsoncontain.username);
        var username;
        var password;
        username=jQuery('#username').val();
        password=jQuery('#password').val();
        alert(password);
        alert(username);
        if (jsoncontain.username==username && jsoncontain.password==password){
        location.href="/";}
        else{
        alert('error');}
        }}
);
});