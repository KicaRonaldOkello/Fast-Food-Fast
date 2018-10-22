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
    var mybody = JSON.stringify({
        'username': document.getElementById('LoginUsername').value,
        'password': document.getElementById('LoginPassword').value
    });
    var myurl = 'http://localhost:5000/api/v1/auth/login';

    var myheader = {
        'Content-Type': 'application/json'
    };

    var init = {
        method: 'POST',
        headers: myheader,
        body: mybody
    };

    fetch(myurl, init)
        .then(function (response) {
            return response.json();
        })
        .then(function (data) {
            var par = document.getElementById("error_message");
            if (data.access_token) {
                sessionStorage.setItem('Token', 'Bearer '+data.access_token);
                window.location.href = 'orders.html';
            }
            else if (par.value == data.Error){
                return False;
            }
            else {
                
                par.style.color = "red";
                var message = document.createTextNode(data.Error);
                par.appendChild(message);
            }
        });
}