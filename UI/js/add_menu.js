function add_menu (){

    var menu_body = JSON.stringify({
        'name': document.getElementById("add_food").value,
        'price': document.getElementById("add_price").value,
        'description': document.getElementById("descri").value
    })
    var myurl = 'https://fast-food-challenge-3.herokuapp.com/api/v1/menu';
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
            par.style.color = "green";
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
    

}