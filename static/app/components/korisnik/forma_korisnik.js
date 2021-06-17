export default {
    props: ["objekat", "atributi", "tekst", "tip_korisnika"],
    emits: ["dodaj", "izmeni", "pretraga"],
    data() {
        return {
            noviObjekat: this.objekat ? {...this.objekat} : {}
        }
    },
    watch: {
         objekat: function(newValue, oldValue) {
            this.noviObjekat = {...this.objekat};
            if (Object.keys(this.noviObjekat).length !== 0)
            {
                document.getElementById("izmena").hidden = false
            }
         }
    },
    methods: {
        pretraga: function pretraga(){
            this.$emit('pretraga', {...this.noviObjekat})
        }
    },
    template: `
    <form>
        <div v-for="atr in atributi">
            <label>{{atr}}: <input class="form-control" aria-label="Small" type="text" v-model="noviObjekat[atr]" required></label>
        </div>
        <label>Tip korisnika:
            <select class="form-select" aria-label="Default select example" v-model="noviObjekat['idtip_korisnika']" required>
                <option v-for="obj in tip_korisnika" v-bind:value="obj.idtip_korisnika">{{obj.tip_korisnika}}</option>
            </select>
        </label>
        <div>
            <input class="btn btn-primary" type="submit" v-on:click="$emit('dodaj', {...noviObjekat})" value="Dodaj">
            <input class="btn btn-primary" hidden="true" id="izmena" type="submit" v-on:click="$emit('izmeni', {...noviObjekat})" value="Izmeni"> 
            <input class="btn btn-primary" type="button" v-on:click="pretraga" value="Pretraga">
        </div>
    </form>
    `
}