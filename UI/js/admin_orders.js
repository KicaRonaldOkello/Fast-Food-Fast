function admin_orders(){
    var x = sessionStorage.getItem('Token');
    if (x == null){
        window.location.href = 'index.html';
    };
    var myurl = 'https://fast-food-challenge-3.herokuapp.com/api/v1/orders';

    var myheader = {
        'Content-Type': 'application/json',
        'Authorization': sessionStorage.getItem('Token')
    };

    var init = {
        method: 'GET',
        headers: myheader 
        
    };
    fetch(myurl, init)
    .then(function(res){
        return res.json();
    })
    .then(function(data){
        for (let i = 0 , l = data.orders.length; i < l; i++){
            var par1 = document.createElement("p");
            var order_id = document.createTextNode('ORDER NO: #'+data.orders[i].order_id);
            par1.appendChild(order_id);
            var par2 = document.createElement("p");
            var food_name = document.createTextNode('ORDER: '+data.orders[i].food_name);
            par2.appendChild(food_name);
            var par3 = document.createElement("p");
            var amount = document.createTextNode('AMOUNT: '+data.orders[i].amount+" pieces");
            par3.appendChild(amount);
            var par4 = document.createElement("p");
            var order_status = document.createTextNode('ORDER STATUS: '+data.orders[i].order_status);
            par4.appendChild(order_status);
            var par5 = document.createElement("p");
            var time = document.createTextNode('TIME: '+data.orders[i].time);
            par5.appendChild(time);
            var par6 = document.createElement("p");
            var username = document.createTextNode('USERNAME: '+data.orders[i].username);
            par6.appendChild(username);

            var admin_orders = document.createElement("div");
            admin_orders.id = "admin-orders";
            admin_orders.appendChild(par1);
            admin_orders.appendChild(par2);
            admin_orders.appendChild(par3);
            admin_orders.appendChild(par4);
            admin_orders.appendChild(par5);
            admin_orders.appendChild(par6);

            var button1 = document.createElement("button");
            button1.name = "Processing";
            button1.value = data.orders[i].order_id;
            var button1_name = document.createTextNode('PROCESSING');
            button1.appendChild(button1_name);
            button1.addEventListener("click", function(){change_status(this);});

            var button2 = document.createElement("button");
            button2.name = "Complete";
            button2.value = data.orders[i].order_id;
            var button2_name = document.createTextNode('COMPLETE');
            button2.appendChild(button2_name);
            button2.addEventListener("click", function(){change_status(this);});

            var button3 = document.createElement("button");
            button3.name = "Cancelled";
            button3.value = data.orders[i].order_id;
            var button3_name = document.createTextNode('CANCELLED');
            button3.appendChild(button3_name);
            button3.addEventListener("click", function(){change_status(this);});

            var admin_buttons = document.createElement("div"); 
            admin_buttons.className = "order-display";
            admin_buttons.appendChild(button1);
            admin_buttons.appendChild(button2);
            admin_buttons.appendChild(button3);

            var order_div = document.createElement("div");
            order_div.id = "order";
            order_div.appendChild(admin_orders);
            order_div.appendChild(admin_buttons);

            var admin_div = document.getElementById("admin");
            admin_div.appendChild(order_div);
            
        }
    })

}