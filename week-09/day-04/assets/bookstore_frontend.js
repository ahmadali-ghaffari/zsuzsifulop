let xml = new XMLHttpRequest();
let body = document.querySelector('body');
url = 'http://localhost:3000';
    
function talkToAPI(method, resource){
    xml.open(method, url + resource, true);
    xml.onload = function(){
      let div = document.createElement('div');
      div.innerHTML = xml.response;
      body.appendChild(div);
    }
    xml.send();
  }
  talkToAPI('GET', '/list')