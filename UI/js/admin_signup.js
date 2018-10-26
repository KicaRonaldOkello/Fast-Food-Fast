function admin_signup() {
    var mybody = JSON.stringify({
        'name': document.getElementById('name').value,
        'username': document.getElementById('username').value,
        'email': document.getElementById('email').value,
        'password': document.getElementById('password').value
    });
    var myurl = 'http://localhost:5000/api/v1/auth/admin';

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
                window.location.href = 'admin.html';
            }
            else{
                var par = document.getElementById("login_error");
                par.style.color = "pink";
                var message = document.createTextNode("*"+json.Error);
                par.appendChild(message);
            }
            
        });
}