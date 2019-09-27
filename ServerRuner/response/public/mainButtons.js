
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
function jQ_append(id_of_input)
{
   var int_id=Cookies.get("id");
   data={"id":int_id,"getname":{"name":" "}};
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
    },
    error: function (request, status, error) {
        location.href='/login';
        alert(request.responseText);
    }
    //EСЛИ ОТЗЫВ ПУСТОЙ ТО ПЕРЕХОД НА ЛОГИН!!!
    })
}

function find_people_fielder(name,receiver_id){
        let founded_user_div=document.createElement('div');
        let founded_user_photo_div=document.createElement('div');
        let founded_user_name_div=document.createElement('div');
        let founded_username=document.createElement('div')
        let butt_div=document.createElement('div');
        let left_content_div=document.createElement('div');
        let trigger_chat=document.createElement('input');
        founded_user_div.className='founded_accs';
        founded_user_photo_div.className='founded_accs_photo';
        founded_user_name_div.className='founded_accs_name';//контейнер для имени и учасников
        founded_username.className="founded_username";//имя

        trigger_chat.className="trigger_chat";
        butt_div.id='butN'+receiver_id;

        butt_div.className="butt_div";
        left_content_div.className="left_content_div";
        founded_username.innerHTML=name;
        founded_user_name_div.append(founded_username);
        butt_div.append(trigger_chat);
        left_content_div.append(founded_user_photo_div);
        left_content_div.append(founded_user_name_div);
        founded_user_div.append(left_content_div);
        founded_user_div.append(butt_div);
        people_container.append(founded_user_div);
}
var group_div_id=0;
function find_group_fielder(name,chat_id,members){
        let founded_user_div=document.createElement('div');
        let founded_user_photo_div=document.createElement('div');
        let founded_user_name_div=document.createElement('div');
        let founded_username=document.createElement('div');
        let founded_list_members_div=document.createElement('div');
        founded_list_members_div.innerHTML=members;
        let butt_div=document.createElement('div');
        let left_content_div=document.createElement('div');
        let trigger_chat=document.createElement('input');

        butt_div.id='gbutN'+group_div_id;
        group_div_id++;

        founded_user_div.className='founded_accs';
        founded_user_photo_div.className='founded_accs_photo';
        founded_user_name_div.className='founded_accs_name';//контейнер для имени и учасников
        founded_username.className="founded_username";//имя
        founded_list_members_div.className="founded_list_members";
        trigger_chat.className="trigger_group_chat";
        butt_div.className="butt_div";
        left_content_div.className="left_content_div";
        founded_username.innerHTML=name;
        founded_user_name_div.append(founded_username);
        founded_user_name_div.append(founded_list_members_div);
        butt_div.append(trigger_chat);
        //butt_div.append(hidden_text);
        left_content_div.append(founded_user_photo_div);
        left_content_div.append(founded_user_name_div);
        founded_user_div.append(left_content_div);
        //founded_user_div.append(hidden_text);
        founded_user_div.append(butt_div);
        people_container.append(founded_user_div);
}

function delete_peopleInDiv(){
    $('.founded_accs').remove();
    //document.querySelector("#people_container").innerHTML = "";
}
$('#registbtn').on('click',function(){
    registration();
});

$('#enter').on('click',function (){
    logInitilization();
});
$('#entertest').on('click',function(){

})

$('#people_container').on('click','.trigger_chat',function(){
var int_my_id=Cookies.get("id");
var but_div=$(this).parent().attr('id');
var int_receiver_id=but_div.slice(4);
var receiver_name=Cookies.get(int_receiver_id);
data={"my_Id":int_my_id,"int_receiver":int_receiver_id,"name_receiver":receiver_name};

 $.ajax({
        type: "POST",
        url: "/api/create_chat",
        data: JSON.stringify(data),
        contentType: "application/json; charset=utf-8",
        success: function(msg){
            alert('success');
        if(local_page!='chatroom'){
            switchMainWindow(local_page,"chatroom");
            local_page="chatroom";
        }
        }
        })
})
$('#people_container').on('click','.trigger_group_chat',function(){//не всегда зайдет
if(local_page!='chatroom'){
    switchMainWindow(local_page,"chatroom");
    local_page="chatroom";
    }
})
$('#smsLogo').on('click',function(){
 if(local_page!='searchroom'){
    switchMainWindow(local_page,"searchroom");
    local_page="searchroom";
    }
})
$('#accLogo').on('click',function(){
if(local_page!="acc"){
    switchMainWindow(local_page,"acc");
    local_page="acc";
    }
})


$('#findbtn').on('click',function(){
     var username=jQuery('#find').val();
     data_group={"group_name":username,"group_names":[],"group_ids":[],'group_members':[]};
     var isFull=true;
     $.ajax({
        type: "POST",
        url: "/api/find_group",
        data: JSON.stringify(data_group),
        contentType: "application/json; charset=utf-8",
        success: function(msg){
        //если что т внутри
        try{
        delete_peopleInDiv();
        }
        catch(e){
        isFull=false;
        for(let i=0;i<msg["group_names"].length;i++){
        find_group_fielder(msg['group_names'][i],msg['group_ids'][i],"GroupMembersFunction");
        }}
        if(isFull==true){
        group_div_id=0;
        for(let i=0;i<msg["group_names"].length;i++){
        find_group_fielder(msg['group_names'][i],msg['group_ids'][i],"GroupMembersFunction");
        }
        }
         $(".trigger_group_chat").attr('type','button');
        }
        })
    data={"fusername":username,"name":[],'id':[]};
    $.ajax({
        type: "POST",
        url: "/api/find_person",
        data: JSON.stringify(data),
        contentType: "application/json; charset=utf-8",
        success: function(msg){
        if(isFull==true){
         for(let i=0;i<msg["name"].length;i++){
         Cookies.set(msg['id'][i],null);
         }
        }
        for(let i=0;i<msg["name"].length;i++){
        find_people_fielder(msg['name'][i],msg['id'][i]);
        Cookies.set(msg['id'][i],msg['name'][i]);

        //запоминаем имя и айди в массиве с индексом айди блока
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
