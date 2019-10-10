var cookie_dict;

function get_cookie_dict(){
    var cookies = (document.cookie).split(';');
    var dict = {};
    cookies.forEach(function(cookie){
        cookie = cookie.split('=');
        var name = cookie[0];
        var data = cookie[1];
        dict[name] = data;
    });
    cookie_dict = dict;
}

function init(){
    get_cookie_dict();
    console.log(cookie_dict);
}

init();