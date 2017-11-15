'use strict'
function ajax(method, url, callback, reqBody){
    let x = new XMLHttpRequest();
    x.open(method, url, true);
    x.setRequestHeader("Content-Type", "application/json");
    x.onload = function(){
        console.log({"callback": x.responseText});
        let data = JSON.parse(x.responseText);
        callback(data);
    };
    let postdata = null;
    if (reqBody){
        postdata = JSON.stringify(reqBody);
    };
    console.log(postdata);
    x.send(postdata);  
};