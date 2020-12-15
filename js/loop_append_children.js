const num_carousel = 20;
const num_image = 30;

let request = new XMLHttpRequest();
request.open("GET", 'data/data.json', false);
request.send(null);
let data_j = JSON.parse(request.responseText);
request.open("GET", 'data/url.json', false);
request.send(null);
let url_j = JSON.parse(request.responseText);


// Create carousels
let body = document.body;
for (let i=1; i<num_carousel+1; i++){
    let wrapper = document.createElement("div");
    wrapper["id"] = "wide-wrapper-" + i.toString();
    let carousel = document.createElement("ul");
    carousel["id"] = "carousel-" + i.toString();
    wrapper.innerHTML += carousel.outerHTML;
    body.appendChild(wrapper);
}

// Add images to each carousel
for (let i=1; i<num_carousel+1; i++){
    let carousel = document.getElementById("carousel-" + i.toString());
    for (let j=1; j<num_image+1; j++){
        let entry_id = num_image * (i-1) + j;

        let li = document.createElement("li");

        let a = document.createElement("a");
        a["href"] = url_j[entry_id];
        a["target"] = "_blank";
        let img = document.createElement("img");
        img["src"] = "icons/" + entry_id.toString() + ".jpg";
        img["alt"] = "";
        a.innerHTML += img.outerHTML;
        li.innerHTML += a.outerHTML;

        let div = document.createElement("div");
        div.classList.add("tooltip");
        div.innerHTML = data_j[entry_id];
        li.innerHTML += div.outerHTML;

        carousel.appendChild(li);
    }

}


