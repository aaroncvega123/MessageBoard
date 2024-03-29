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
        var topnav = $('.navbar-nav');
        var profile_button = $('<li class="nav-item">')
            .append($("<a class='nav-link' class='right' href=''>").text(cookie_dict['email']));
        var log_out_button = $('<li class="nav-item">')
            .append($("<a class='nav-link' class='right' href=''>").text('Log out'));

        log_out_button.appendTo(topnav);
        profile_button.appendTo(topnav);  
        log_out_button.on('click', function(){
            log_out();
        });
    }
    else{
        var topnav = $('.navbar-nav');
        var login_button = $('<li class="nav-item">')
            .append($("<a class='nav-link' class='right' href='/login'>").text('Log in'));
        var sign_up_button = $('<li class="nav-item">')
            .append($("<a class='nav-link' class='right' href='/create_account'>").text('Sign up'));
        login_button.appendTo(topnav);
        sign_up_button.appendTo(topnav); 
    }
}

window.addEventListener("load", function(){
    get_cookie_dict();
    set_nav_bar_buttons();
});