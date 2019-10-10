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

function log_out(){
    document.cookie = "auth_key=;";
    document.cookie = "email=;";
    location.reload();
}

function set_nav_bar_buttons(){
    if (cookie_dict['auth_key']) {
        var topnav = $('.topnav');
        var profile_button = $("<a id='account_button' class='right'>");  
        var log_out_button = $("<a id='log_out_button' class='right'>");
        profile_button.text(cookie_dict['email']);
        log_out_button.text('Log out');
        log_out_button.appendTo(topnav);
        profile_button.appendTo(topnav);  
        log_out_button.on('click', function(){
            log_out();
        });
    }
}

window.addEventListener("load", function(){
    get_cookie_dict();
    set_nav_bar_buttons();
});