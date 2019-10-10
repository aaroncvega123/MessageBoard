var cookie_dict;

function get_cookie_dict(){
    var cookies = (document.cookie.replace(' ', '')).split(';');
    var dict = {};
    cookies.forEach(function(cookie){
        cookie = cookie.split('=');
        var name = cookie[0];
        var data = cookie[1];
        dict[name] = data;
    });
    cookie_dict = dict;
}

function set_nav_account_button(){
    if (cookie_dict['auth_key']) {
        var topnav = $('.topnav');
        var profile_button = $("<a id='account_button' class='right'>");  
        profile_button.text(cookie_dict['email']);
        profile_button.appendTo(topnav);      
    }
}

window.addEventListener("load", function(){
    get_cookie_dict();
    set_nav_account_button();
});