export default {
    props: ["objekat", "drzave", "opstine", "atributi", "tekst"],
    emits: ["dodaj", "izmeni", "pretraga"],
    data() {
        this.select_iddrzava = -1;
        this.drzava_id = 'drzave_'+this.tekst;
        this.opstine_id = 'opstine_'+this.tekst;
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
        nadjiOpstine: function nadjiOpstine(rowId, event) {
            let drzave = document.getElementById(this.drzava_id)
            let opstine = document.getElementById(this.opstine_id)
            let iddrzava = drzave.options[drzave.selectedIndex].value

            for(let i=0; i < opstine.options.length; i++)
            {
                opstine.removeChild(opstine.options[i]); 
            }
            for(let i=0; i < this.opstine.length; i++)
            {
                if(this.opstine[i]['iddrzava'] == iddrzava)
                {
                    let opt = document.createElement('option');
                    opt.appendChild( document.createTextNode(this.opstine[i]['opstina']) );
                    opt.value = this.opstine[i]['idopstina'];
                    opstine.appendChild(opt);
                }
            }
        },
        pretraga: function pretraga(){
            this.$emit('pretraga', {...this.noviObjekat})
        }
    },
    template: `
    <form>
        <div v-for="atr in atributi">
            <template v-if="atr != 'iddrzava'">
                <template v-if="atr != 'idopstina'">
                    <label>{{atr}}: <input class="form-control" aria-label="Small" type="text" v-model="noviObjekat[atr]" required></label>
                </template>
            </template>
        </div>
        <div>
            <label>Drzava:
                <select class="form-select" aria-label="Default select example" v-bind:id="drzava_id" v-model="noviObjekat['iddrzava']" required v-on:change='nadjiOpstine(rowId, $event)'>
                    <option v-for="obj in drzave" v-bind:value="obj.iddrzava">{{obj.drzava}}</option>
                </select>
            </label>
        </div>
        <div>
            <label>Opstina:
                <select class="form-select" aria-label="Default select example" v-bind:id="opstine_id" v-model="noviObjekat['idopstina']" required>
                    <option v-for="obj in opstine" v-bind:value="obj.idopstina">{{obj.opstina}}</option>
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