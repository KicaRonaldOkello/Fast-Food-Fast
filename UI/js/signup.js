function signup() {
    var mybody = JSON.stringify({
        'name': document.getElementById('name').value,
        'username': document.getElementById('username').value,
        'email': document.getElementById('email').value,
        'password': document.getElementById('password').value
    });
    var myurl = 'https://fast-food-challenge-3.herokuapp.com/v1/auth/signup';

    var myheader = {
        'Content-Type': 'application/json'
    };

    var init = {
        method: 'POST',
        headers: myheader, 
        body: mybody
    };

    fetch(myurl, init)
    .then(function(res){
        return res.json();
    })
    .then(function(data){
            console.log(data);
            return False

            if (data.access_token && data.role == 'user'){
                sessionStorage.setItem('Token', 'Bearer '+data.access_token);
                window.location.href = 'orders.html';
            }
            else{
                var par = document.getElementById("login_error");
                par.style.color = "pink";
                var message = document.createTextNode("*"+data.Error);
                par.appendChild(message);
            }
            
        });
    return true
}
    

function login() {
    var login_body = JSON.stringify({
        'username': document.getElementById('LoginUsername').value,
        'password': document.getElementById('LoginPassword').value
    });
    var login_url = 'https://fast-food-challenge-3.herokuapp.com/api/v1/auth/login';

    var myheader = {
        'Content-Type': 'application/json'
    };

    var init = {
        method: 'POST',
        headers: myheader,
        body: login_body
    };

    fetch(login_url, init)
        .then(function (response) {
            return response.json();
        })
        .then(function (json) {
            if (json.access_token && json.role == 'user') {
                sessionStorage.setItem('Token', 'Bearer '+json.access_token);
                window.location.href = 'orders.html';
            }
            else if (json.access_token && json.role == 'admin'){
                sessionStorage.setItem('Token', 'Bearer '+json.access_token);
                window.location.href = 'admin.html';
            }
            else {
                var par = document.getElementById("login_error");
                par.style.color = "pink";
                var message = document.createTextNode("*"+json.Error);
                par.appendChild(message);
            }
        });
}