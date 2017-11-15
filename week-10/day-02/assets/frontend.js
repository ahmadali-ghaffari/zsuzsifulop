const Playlist = function(){
    var root = document.querySelector(".playlists")
    var plus = document.querySelector(".plus");
    plus.addEventListener("click", function(){
        window.prompt("New tracklist!")
    })
    function showCreateDialog(){
    };
    
    function create(nameMe){
        ajax('POST', 'http://localhost:8080/playlist', console.log, {"playlist" :  nameMe });
    };

    let render = function (response){
        while (root.firstChild){
            root.removeChild(root.firstChild);
        }
        response.forEach(function(element, i) {
            console.log(response)
            let li = document.createElement('li');
            li.innerHTML = element.playlist;  //sima listánál element.title volt
            li.setAttribute('class', 'song');      
            root.appendChild(li);
            let X = document.createElement("span");
            X.setAttribute('class', 'close');
            X.textContent="x"
            X.addEventListener('click', function(){
                alert("Plan to Close");
            });
            li.appendChild(X);
            li.addEventListener('click', function(){
                highlight(i)});
            }); 
    };
    function delete1(){
        ajax('PUT', 'http://localhost:8080/playlist', render);
    };
    
    function highlight(index){
        let myList = root.querySelectorAll("li")
        console.log(myList)
        myList.forEach(function(element, i) {
            element.setAttribute('class', "song")
            if (index === i){
                element.setAttribute('class', "song blue")
            };
        });
    };

    function addEvents(){
    }; 

    function load(){
        ajax('GET', 'http://localhost:8080/favourite', render)
    };

    function clickHandles(){
    }; 

    return {
        render: render,
        highlight: highlight,
        addEvents: addEvents,
        delete1: delete1,
        create: create,
        load: load
    }
};

let playlistmodule =  Playlist();
playlistmodule.load() 
playlistmodule.highlight()
playlistmodule.create("Zsuzsi")
