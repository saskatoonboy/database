
let validEntries = [];

let nameElement = document.getElementById("name");
let colourElement = document.getElementById("colour");
let rarityElement = document.getElementById("rarity");
let editionElement = document.getElementById("edition");
let displayElement = document.getElementById("display");

function createCardItem(ID, name) {
    let li = document.createElement("li");
    let a = document.createElement("a");
    a.href = ID+"/";
    a.textContent = name;
    li.appendChild(a);
    return li;

}

function checkEntries() {
    let name = nameElement.value;
    let colour = colourElement.value;
    let rarity = rarityElement.value;
    let edition = editionElement.value;

    validEntries = [];
    displayElement.innerHTML = '';


    for (entry of entries) {

        if (entry.isValid(name, colour, rarity, edition)) {
            validEntries.push(entry);
            displayElement.appendChild(createCardItem(entry.id, entry.name));
        }

    }

}

nameElement.addEventListener("input", function (e) {
    checkEntries();
});

colourElement.addEventListener("input", function (e) {
    checkEntries();
});

rarityElement.addEventListener("input", function (e) {
    checkEntries();
});

editionElement.addEventListener("input", function (e) {
    checkEntries();
});
