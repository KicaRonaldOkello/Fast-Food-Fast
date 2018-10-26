function add_menu (){

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