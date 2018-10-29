var x;
function pick_input(input){
    x = input.value;
};

function add_order(menu_id) {
    var v = sessionStorage.getItem('Token');
    if (v == null){
        window.location.href = 'index.html';
    };   
    var order_body = JSON.stringify({
        'amount': x,
        'food': menu_id.value
    });
    var add_order_url = 'https://fast-food-challenge-3.herokuapp.com/api/v1/users/orders';

    var myheader = {
        'Content-Type': 'application/json',
        'Authorization': sessionStorage.getItem('Token')
    };

    var init = {
        method: 'POST',
        headers: myheader,
        body: order_body
    };
    fetch(add_order_url, init)
    .then(function(response){
        if (response.ok){
            var res = document.getElementById("order-message");
            var par = document.createElement("p");
            par.style.color = "green";
            par.style.fontFamily = "Impact,Charcoal,sans-serif";
            par.style.fontSize = "20px";
            par.appendChild(document.createTextNode("* Order has been succesfully sent"));
            res.appendChild(par);
        }
        else{
            return response.json().then(function(data){
                alert(data.Error);
            })
        }
    });
}