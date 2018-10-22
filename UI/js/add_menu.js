function add_menu (){
    sessionStorage.setItem('Token', 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTU0MDE0MTg1MSwiZXhwIjoxNTQwMTQyNzUxLCJpZGVudGl0eSI6eyJ1c2VybmFtZSI6InJvbm55IiwicGFzc3dvcmQiOiJwYmtkZjI6c2hhMjU2OjUwMDAwJFd2S0ZSRjM2JDlhMjViYWYxOWVkYjUwMmMyYjIwNDQ0ODdmYWFmZDFjMTVmM2Y1NjhmOGJmOTYyYzBmYjg2ZTk0ZDE4OGExNjEiLCJyb2xlIjoiYWRtaW4iLCJ1c2VyX2lkIjo0NH0sInR5cGUiOiJhY2Nlc3MiLCJqdGkiOiI4YzY0NDlhYS0wOTg4LTQxMzUtOGFhMi04MDFjZWRiNGFiYmIiLCJuYmYiOjE1NDAxNDE4NTF9.-0gqxGU0X5eR6q9OIkDhN4tqf3aVuwng1Hi8CRqDZB8');
    var menu_body = JSON.stringify({
        'name': document.getElementById("add_food").value,
        'price': document.getElementById("add_price").value,
        'image_name': document.getElementById("upload").files[0].name
    })
    var myurl = 'http://localhost:5000/api/v1/menu';
    var myheader = {
        'Content-Type': 'application/json',
        'Authorization': sessionStorage.getItem('Token')
    };

    var init = {
        method: 'POST',
        headers: myheader, 
        body: menu_body
    };
    fetch(myurl, init)
    .then(function(response){
        if (response.ok){
            var par = document.getElementById("res");
            var message = document.createTextNode("* Adding item to menu was successful");
            par.appendChild(message);
        }
        else{
            return response.json().then(function(res){
            var par = document.getElementById("res");
            par.style.color = "red";
            var message = document.createTextNode("*"+ res.Error);
            par.appendChild(message);
            })
        }
    });
    var  img_body = JSON.stringify({
        'image_name': document.getElementById("upload").files[0]
    });
    var img_header = {
        'Authorization': sessionStorage.getItem('Token')
    };
    var img_init = {
        method: 'POST',
        headers: img_header, 
        body: img_body
    }

    fetch("/img", img_init)
    .then(res=> res.json());

}