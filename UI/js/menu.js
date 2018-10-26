function menu(){
    const x = sessionStorage.getItem('Token');
    if (x == null){
        window.location.href = 'index.html';
    };
    var myurl = 'http://localhost:5000/api/v1/menu';

    var myheader = {
        'Content-Type': 'application/json'
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
        for(let i = 0, l = data.menu.length; i< l; i++){
            var elem = document.createElement("span");
            elem.class = "menu_id";
            var menu_id = document.createTextNode(data.menu[i].menu_id);
            elem.appendChild(menu_id);
            var element = document.createElement("p");
            var food = document.createTextNode(data.menu[i].food_name);
            element.appendChild(food);

            var element2 = document.createElement("p");
            var price = document.createTextNode(data.menu[i].price +" /=");
            element2.appendChild(price);

            var element3 = document.createElement("p");
            var description = document.createTextNode(data.menu[i].description);
            element3.appendChild(description);

            var display2 = document.createElement("div");
            display2.id = "description1";

            var input = document.createElement("input");
            input.setAttribute("type", "text");
            input.width = "3px";
            input.addEventListener("input", function(){pick_input(this);});
            var label = document.createElement("label");
            var text = document.createTextNode(" pieces.");
            label.appendChild(text);
            var orders = document.getElementById("orders");
            var button = document.createElement("button");
            button.value = data.menu[i].menu_id;
            button.addEventListener("click", function(){add_order(this);});
            button.appendChild(document.createTextNode("Order"));
            var display = document.createElement("div");
            display.id = "description";
            var order = document.createElement("div");
            order.id = "order";

    
            display2.appendChild(elem);
            display2.appendChild(element);
            display2.appendChild(element2);
            display.appendChild(element3);
            display.appendChild(input);
            display.appendChild(label);
            display.appendChild(button);
            order.appendChild(display2);
            order.appendChild(display);
            orders.appendChild(order);
        }

    });
}