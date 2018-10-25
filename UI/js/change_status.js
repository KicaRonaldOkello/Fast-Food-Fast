function change_status(button){
    var myurl = 'http://localhost:5000/api/v1/orders/'+button.value;

    var myheader = {
        'Content-Type': 'application/json',
        'Authorization': sessionStorage.getItem('Token')
    };
    var mybody = JSON.stringify({
        'status': button.name
    });

    var init = {
        method: 'PUT',
        headers: myheader,
        body: mybody
        
    };
    fetch(myurl, init)
    .then(function(response){
        if (response.ok){
            alert("successful");
            window.location.reload();
        }
        else{
             response.json().then(function(res){
            alert(res.Error);}
            )
        }
    });
    
}