export default {
    props: ["objekat", "drzave", "opstine", "mesta", "atributi", "tekst"],
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
            <template v-if="atr != 'iddrzava'">
                <template v-if="atr != 'idopstina'">
                    <template v-if="atr != 'idmesto'">
                        <label>{{atr}}: <input class="form-control" aria-label="Small" type="text" v-model="noviObjekat[atr]" required></label>
                    </template>
                </template>
            </template>
        </div>
        <div>
            <label>Drzava:
                <select class="form-select" aria-label="Default select example" v-model="noviObjekat['iddrzava']" required>
                    <option v-for="obj in drzave" v-bind:value="obj.iddrzava">{{obj.drzava}}</option>
                </select>
            </label>
        </div>
        <div>
            <label>Opstina:
                <select class="form-select" aria-label="Default select example" v-model="noviObjekat['idopstina']" required>
                    <option v-for="obj in opstine" v-bind:value="obj.idopstina">{{obj.opstina}}</option>
                </select>
            </label>
        </div>
        <div>
            <label>Mesto:
                <select class="form-select" aria-label="Default select example" v-model="noviObjekat['idmesto']" required>
                    <option v-for="obj in mesta" v-bind:value="obj.idmesto">{{obj.mesto}}</option>
                </select>
            </label>
        </div>
        <div>
            <input class="btn btn-primary" type="submit" v-on:click="$emit('dodaj', {...noviObjekat})" value="Dodaj">
            <input class="btn btn-primary" hidden="true" id="izmena" type="submit" v-on:click="$emit('izmeni', {...noviObjekat})" value="Izmeni"> 
            <input class="btn btn-primary" type="button" v-on:click="pretraga" value="Pretraga">
        </div>
    </form>
    `
}