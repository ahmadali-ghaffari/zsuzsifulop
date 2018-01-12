'use strict';

function ajax(method, url, callback, reqBody) {
    let xhr = new XMLHttpRequest();
    xhr.open(method, url, true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onload = function () {
        console.log({"callback": xhr.responseText});
        let data = JSON.parse(xhr.responseText);
        callback(data);
    };
    let postdata = null;
    if (reqBody) {
        postdata = JSON.stringify(reqBody);
    }
    console.log(postdata);
    xhr.send(postdata);
}