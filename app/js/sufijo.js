let input_suf = document.getElementById('search_suf');
let log_suf = document.getElementById('log_suf');
let results_suf = document.getElementById('results_suf');
input_suf.oninput = searchSuf0;

function searchSuf0(e) {
//   log.textContent = `Ingresaste
//       ${e.target.value} .`;
    results_suf.innerHTML = "";
    var string = e.target.value + "$";
   
    const xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange= function() {
        if (this.readyState == 4 && this.status == 200) {
       // Typical action to be performed when the document is ready:
        //    JSON.parse(httpRequest.responseText)
        console.log(this.responseText);
        var resp = JSON.parse(this.responseText);
       

        log_suf.textContent =""
        len =  Object.keys(resp).length;
        

    
            results_suf.innerHTML="<option value=' Ha encontrado "+String(len)+" ocurrencias'>"
            for (i=0;i< len;i++){
            results_suf.innerHTML+="<option value='"+resp[i]+"'>";
            
        } 
        }
    }
    if(string == "$"){
        log_suf.textContent = "No has buscado nada";
    }
    else{
        xhttp.open("GET", "../cgi-bin/search_suf.py?string="+string, true);
        xhttp.send();
    }
}