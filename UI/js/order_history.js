function order_history(){
    var x = sessionStorage.getItem('Token');
    if (x == null){
        window.location.href = 'index.html';
    };

    var myurl = 'http://localhost:5000/api/v1/users/orders';

    var myheader = {
        'Content-Type': 'application/json',
        'Authorization': sessionStorage.getItem('Token')
    };

    var init = {
        method: 'GET',
        headers: myheader 
        
    };
    fetch(myurl, init)
    .then(function(response){
        return response.json();
    })
    .then(function(data){
        for (let i = 0 , l = data.Orders.length; i < l; i++){
            var par1 = document.createElement("p");
            var order_id = document.createTextNode('ORDER NO: #'+data.Orders[i].order_id);
            par1.appendChild(order_id);
            var par2 = document.createElement("p");
            var food_name = document.createTextNode('ORDER: '+data.Orders[i].food_name);
            par2.appendChild(food_name);
            var par3 = document.createElement("p");
            var amount = document.createTextNode('AMOUNT: '+data.Orders[i].amount+" pieces");
            par3.appendChild(amount);
            var par4 = document.createElement("p");
            var order_status = document.createTextNode('ORDER STATUS: '+data.Orders[i].order_status);
            par4.appendChild(order_status);
            var par5 = document.createElement("p");
            var time = document.createTextNode('TIME: '+data.Orders[i].time);
            par5.appendChild(time);

            var order_class = document.createElement("div");
            order_class.className = "order-no";
            order_class.appendChild(par1);
            order_class.appendChild(par2);
            order_class.appendChild(par3);
            order_class.appendChild(par4);
            order_class.appendChild(par5);

            var wrap_order = document.createElement("div");
            wrap_order.id = "order";
            wrap_order.appendChild(order_class);

            var history = document.getElementById("order_history");
            history.appendChild(wrap_order);

        }
    });

}
