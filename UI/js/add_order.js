var x;
function pick_input(input){
    x = input.value;
}

function add_order(menu_id) {
    var order_body = JSON.stringify({
        'amount': x,
        'food': menu_id.value
    });
    var add_order_url = 'http://localhost:5000/api/v1/users/orders';

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
            alert("Successful");
        }
        else{
            return response.json().then(function(data){
                alert(data.Error);
            })
        }
    });
}