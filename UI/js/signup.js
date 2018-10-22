function signup() {
    var mybody = JSON.stringify({
        'name': document.getElementById('name').value,
        'username': document.getElementById('username').value,
        'email': document.getElementById('email').value,
        'password': document.getElementById('password').value
    });
    var myurl = 'http://localhost:5000/api/v1/auth/signup';

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
            if (data.access_token){
                sessionStorage.setItem('access_token', data.access_token);
                window.location.href = 'orders.html';
            }
            else{
                alert(data.Error);
            }
            
        });
}
    

function login() {
    var login_body = JSON.stringify({
        'username': document.getElementById('LoginUsername').value,
        'password': document.getElementById('LoginPassword').value
    });
    var login_url = 'http://localhost:5000/api/v1/auth/login';

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
            if (json.access_token) {
                sessionStorage.setItem('Token', json.access_token);
                window.location.href = 'orders.html';
            }
            else {
                var par = document.getElementById("login_error");
                par.style.color = "pink";
                var message = document.createTextNode("*"+json.Error);
                par.appendChild(message);
            }
        })
        .catch((error)=> {
            console.log(error);
        });
}