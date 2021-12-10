// $.ajax({
//     type: "POST",
//     url: "~/pythoncode.py",
//     data: { param: text}
//   }).done(function( o ) {
//      // do something
//   });

// $('file').on('change', function() {
//     alert( this.value );
//   })

// $('search').on('input', function() {
// alert( this.value );
// })

let input = document.getElementById('search');
let log = document.getElementById('log');
let results = document.getElementById('results');
input.oninput = searchSuf;

function searchSuf(e) {
//   log.textContent = `Ingresaste
//       ${e.target.value} .`;
    results.innerHTML = "";
    var string = e.target.value + "$";
   
    const xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange= function() {
        if (this.readyState == 4 && this.status == 200) {
       // Typical action to be performed when the document is ready:
        //    JSON.parse(httpRequest.responseText)
        var resp = JSON.parse(this.responseText);
       

        log.textContent =""
        len =  Object.keys(resp).length;
        
        if(len == 0){
            console.log(len)
            results.innerHTML+="<option value='No hay coincidencias'>";
        }
        else{
            for (i=0;i< len;i++){
                
            results.innerHTML+="<option value='"+resp[i]+"'>";
            }
        } 
        }
    }
    if(string == "$"){
        log.textContent = "No has buscado nada";
    }
    else{
        xhttp.open("GET", "../cgi-bin/search_str.py?string="+string, true);
        xhttp.send();
    }
}