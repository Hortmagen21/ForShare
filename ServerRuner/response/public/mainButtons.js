
$('document').ready(function(){
local_page="acc";//default отображение main page при загрузке(СТРАНИЦА АККА)

if(window.location.pathname=="/"){
jQ_append("textbox");//запись имени в какойто обьект по айди
}
function switchMainWindow(current_window,desire_window){
switch(current_window){
case 'acc':
    $('#acc_window').hide();
    switch(desire_window){
    case 'searchroom':
        $('#input_space').show();
        break;
    case 'chatroom':
        $('#messager_container').show();
        break;
    }
break;
case 'searchroom':
    $('#input_space').hide();
    switch(desire_window)   {
        case 'acc':
            $('#acc_window').show();
            break;
        case 'chatroom':
            $('#messager_container').show();
            break;

    }
break;
case 'chatroom':
    $('#messager_container').hide();
    switch(desire_window){
        case 'acc':
            $('#acc_window').show();
            break;
        case 'searchroom':
            $('#input_space').show();
            break;



    }
break;
}
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
    url: "/api/login",
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
    url: "/api/registration",
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
    url: "/api/datafielder",
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
$('.trigger_chat').on('click',function(){
    alert("sss");
    switchMainWindow(local_page,"chatroom");
    local_page="chatroom";
});
$('#smsLogo').on('click',function(){
    switchMainWindow(local_page,"searchroom");
    local_page="searchroom";
})
$('#accLogo').on('click',function(){
    switchMainWindow(local_page,"acc");
    local_page="acc";
})
//var div_id=0;
function find_people_fielder(name,receiver_id){

        let founded_user_div=document.createElement('div');
        let founded_user_photo_div=document.createElement('div');
        let founded_user_name_div=document.createElement('div');
        let butt_div=document.createElement('div');
        let left_content_div=document.createElement('div');
        let trigger_chat=document.createElement('input');
        let hidden_text=document.createElement('div');
        hidden_text.className='hidden_text';
        hidden_text.innerHTML=receiver_id;
        founded_user_div.className='founded_accs';
        founded_user_photo_div.className='founded_accs_photo';
        founded_user_name_div.className='founded_accs_name';
        trigger_chat.className="trigger_chat";
        butt_div.className="butt_div";
        left_content_div.className="left_content_div";
        founded_user_name_div.innerHTML=name;
        butt_div.append(trigger_chat);
        left_content_div.append(founded_user_photo_div);
        left_content_div.append(founded_user_name_div);
        founded_user_div.append(left_content_div);
        founded_user_div.append(hidden_text);
        founded_user_div.append(butt_div);
        people_container.append(founded_user_div);

}
function delete_peopleInDiv(){
    $('.founded_accs').remove();
    //document.querySelector("#people_container").innerHTML = "";
}
$('#findbtn').on('click',function(){
    var username=jQuery('#find').val();
    data={"fusername":username,"name":[],'id':[]};
    $.ajax({
        type: "POST",
        url: "/api/find_person",
        data: JSON.stringify(data),
        contentType: "application/json; charset=utf-8",
        success: function(msg){
        var isFull=true;//если что т внутри
        try{
        for(let i=0;i<msg["name"].length;i++){
        delete_peopleInDiv();
        }}
        catch(e){
        isFull=false;
        for(let i=0;i<msg["name"].length;i++){
        find_people_fielder(msg['name'][i],msg['id'][i]);
        }}
        if(isFull==true){
        for(let i=0;i<msg["name"].length;i++){
        find_people_fielder(msg['name'][i],msg['id'][i]);
        }
        }
         $(".trigger_chat").attr('type','button');//чтоб все инпути (искуств)стали кнопками
        }
        })


    })




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
