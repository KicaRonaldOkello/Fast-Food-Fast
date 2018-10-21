function menu(){
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
            var element = document.createElement("p");
            var food = document.createTextNode(data.menu[i].food_name + " @ " + data.menu[i].price +" /=");
            element.appendChild(food);
            var input = document.createElement("input");
            input.setAttribute("type", "text");
            input.width = "3px";
            var label = document.createElement("label");
            var text = document.createTextNode(" pieces.");
            label.appendChild(text);
            var orders = document.getElementById("orders");
            var button = document.createElement("button");
            button.appendChild(document.createTextNode("Order"));
            var display = document.createElement("div");
            display.className = "order-display";
            var order = document.createElement("div");
            order.id = "order";
            var image = document.createElement("img");
            image.src = "img/"+data.menu[i].image_name;

            order.appendChild(image);
            display.appendChild(element);
            display.appendChild(input);
            display.appendChild(label);
            display.appendChild(button);
            order.appendChild(display);
            orders.appendChild(order);
        }

    });
}