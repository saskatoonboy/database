let entries = [];
class CardEntry {

    constructor(id, name, colour, rarity, edition) {

        this.id = id;
        this.name = name;
        this.colour = colour;
        this.rarity = rarity;
        this.edition = edition.toLowerCase();
        entries.push(this);

    }

    isValid(name, colour, rarity, edition) {
        if (name == "") {
            name = "any"
        }
        if (colour == "") {
            colour = "any"
        }
        if (rarity == "") {
            rarity = "any"
        }
        if (edition == "") {
            edition = "any"
        }
        if (name != "any" && !this.name.toLowerCase().includes(name)) {
            return false;

        } else if (!this.colour.toLowerCase().includes(colour) && colour != "any") {

            return false;

        } else if (!this.rarity.toLowerCase().includes(rarity) && rarity != "any") {

            return false;

        } else if (edition != "any" && !this.edition.includes(edition)) {

            return false;

        }
        return true;
    }

}