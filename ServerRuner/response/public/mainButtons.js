$('document').ready(function(){
$('#enter').on('click',function(){
    var enterbtn;
    enterbtn=document.getElementById("enter");//взяли кнопку с айди enter
    var Loger;
    var Loger=new XMLHttpRequest();
    Loger.open('GET','database',true);//database путь в router
    Loger.send();
    Loger.onreadystatechange=function(){
    if (Loger.readyState !=4)return;
    if (Loger.status !=200){
        alert(Loger.status)
	    location.href="/login";
	    enterbtn.disabled=false;
	    }
    else{
	    var jsoncontain;
	    var jsoncontain=JSON.parse(Loger.responseText);//храним переработаный JSON
	    //alert(jsoncontain);
	    //alert(Loger.responseText);
	    //alert(jsoncontain.username);
        var username;
        var password;
        username=jQuery('#username').val();//берем переменные с полей
        password=jQuery('#password').val();
        //alert(password);
        //alert(username);
        if (jsoncontain.username==username && jsoncontain.password==password){
        location.href="/";}
        else{
        alert('wrong password or username');
        enterbtn.disabled=false;
        }
        }}
        enterbtn.disabled=true;
});
});