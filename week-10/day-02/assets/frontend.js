const Playlist = function(){
    var root = document.querySelector(".playlists")
    var rootsongs = document.querySelector(".songlists")
    var plus = document.querySelector(".plus");
    var firstline = document.querySelector(".firstline");
    plus.addEventListener("click", function(){
        window.prompt("New tracklist!")
    })
    
    function create(nameMe){
        ajax('POST', 'http://localhost:8080/playlist', console.log, {"playlist" :  nameMe });
    };

    function load(){
        ajax('GET', 'http://localhost:8080/favourite', render)
    };

    function load2(i){
        ajax('GET', 'http://localhost:8080/playlist/' + i, render2)
    }; 

    let render = function (response){
        while (root.firstChild){
            root.removeChild(root.firstChild);
        }
        console.log(response)
        response.forEach(function(element, i) {
            console.log(response)
            let li = document.createElement('li');
            li.innerHTML = element.playlist;  
            li.setAttribute('class', 'track song');      
            root.appendChild(li);
            let X = document.createElement("span");
            X.setAttribute('class', 'close');
            X.textContent="x"
            X.addEventListener('click', function(){
                alert("Plan to Close");
            });
            li.appendChild(X);
            li.addEventListener('click', function(){
                firstline.textContent = element.playlist;
                highlight(i);
                rootsongs.innerHTML="";
                load2(i+1);
                });
            }); 
    };

    function delete1(){
        ajax('PUT', 'http://localhost:8080/playlist', render);
    };
    
    function highlight(index){
        let myList = root.querySelectorAll(".track")
        console.log(myList)
        myList.forEach(function(element, i) {
            element.setAttribute('class', "track song")
            if (index === i){
                element.setAttribute('class', "track song blue")
            };
        });
    };

    function render2(response){
        response.forEach(function(element) {
            let li = document.createElement('li');
            li.innerHTML = element.path;  
            li.setAttribute('class', 'song');      
            rootsongs.appendChild(li);
            li.addEventListener('click', function(){
                var audio = document.querySelector(".playline")
                audio.setAttribute('src', element.path);
                var secondline = document.querySelector(".secondline");
                secondline.textContent = element.path;
            });
        });
    }; 

    return {
        render: render,
        highlight: highlight,
        delete1: delete1,
        create: create,
        load: load,
        render2: render2,
        load2: load2
    }
};
    
let playlistmodule =  Playlist();
playlistmodule.highlight();
playlistmodule.load();
playlistmodule.load2();
playlistmodule.highlight();

