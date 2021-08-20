
let validEntries = [];

let nameElement = document.getElementById("name");
let colourElement = document.getElementById("colour");
let rarityElement = document.getElementById("rarity");
let editionElement = document.getElementById("edition");

function checkEntries() {
    let name = nameElement.value;
    let colour = colourElement.value;
    let rarity = rarityElement.value;
    let edition = editionElement.value;

    validEntries = [];

    for (entry of entries) {

        if (entry.isValid(name, colour, rarity, edition)) {
            validEntries.push(entry);
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
