export default {
    props: ["objekat", "drzave", "opstine", "mesta", "atributi", "tekst"],
    emits: ["dodaj", "izmeni", "pretraga"],
    data() {
        this.drzava_id = 'drzave_'+this.tekst;
        this.opstine_id = 'opstine_'+this.tekst;
        this.mesta_id = 'mesta_'+this.tekst;
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
            if(drzave.selectedIndex != -1){
                var iddrzava = drzave.options[drzave.selectedIndex].value
            }

            for(let i=0; i < opstine.options.length; i++)
            {
                opstine.removeChild(opstine.firstChild)
            }
            try{
                opstine.removeChild(opstine.firstChild)
            }catch(TypeError){}

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
            this.nadjiMesta(0, 0)
        },
        nadjiMesta: function nadjiOpstine(rowId, event) {
            let drzave = document.getElementById(this.drzava_id)
            let opstine = document.getElementById(this.opstine_id)
            let mesta = document.getElementById(this.mesta_id)
            if(opstine.selectedIndex != -1){
                var idopstina = opstine.options[opstine.selectedIndex].value
            }
            if(drzave.selectedIndex != -1){
                var iddrzava = drzave.options[drzave.selectedIndex].value
            }
            
            for(let i=0; i < mesta.options.length; i++)
            {
                mesta.removeChild(mesta.firstChild)
            }
            try{
                mesta.removeChild(mesta.firstChild)
            }catch(TypeError){}

            for(let i=0; i < this.mesta.length; i++)
            {
                if(this.mesta[i]['idopstina'] == idopstina && this.mesta[i]['iddrzava'] == iddrzava)
                {
                    let opt = document.createElement('option');
                    opt.appendChild( document.createTextNode(this.mesta[i]['mesto']) );
                    opt.value = this.mesta[i]['idmesto'];
                    mesta.appendChild(opt);
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
            <template v-if="atr != 'idadresa'">
                <label>{{atr}}: <input type="text" class="form-control" aria-label="Small" v-model="noviObjekat[atr]" required></label>
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
                <select class="form-select" aria-label="Default select example" v-bind:id="opstine_id" v-model="noviObjekat['idopstina']" required v-on:change='nadjiMesta(rowId, $event)'>
                    <option v-for="obj in opstine" v-bind:value="obj.idopstina">{{obj.opstina}}</option>
                </select>
            </label>
        </div>
        <div>
            <label>Mesto:
                <select class="form-select" aria-label="Default select example" v-bind:id="mesta_id" v-model="noviObjekat['idmesto']" required>
                    <option v-for="obj in mesta" v-bind:value="obj.idmesto">{{obj.mesto}}</option>
                </select>
            </label>
        </div>
        <div>
            <input type="submit" class="btn btn-primary" v-on:click="$emit('dodaj', {...noviObjekat})" value="Dodaj">
            <input hidden="true" id="izmena" type="submit" class="btn btn-primary" v-on:click="$emit('izmeni', {...noviObjekat})" value="Izmeni">
            <input type="button" class="btn btn-primary" v-on:click="pretraga" value="Pretraga">
        </div>
    </form>
    `
}