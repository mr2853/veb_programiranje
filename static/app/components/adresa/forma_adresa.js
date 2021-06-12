export default {
    props: ["objekat", "drzave", "opstine", "mesta", "atributi", "tekst"],
    emits: ["sacuvaj"],
    data() {
        return {
            noviObjekat: this.objekat ? {...this.objekat} : {}
        }
    },
    watch: {
         objekat: function(newValue, oldValue) {
             this.noviObjekat = {...this.objekat};
         }
    },
    template: `
    <form v-on:submit.prevent="$emit('sacuvaj', {...noviObjekat})">
        <div v-for="atr in atributi">
            <template v-if="atr != 'iddrzava'">
                <template v-if="atr != 'idopstina'">
                    <template v-if="atr != 'idmesto'">
                        <label>{{atr}}: <input type="text" v-model="noviObjekat[atr]" required></label>
                    </template>
                </template>
            </template>
        </div>
        <div>
            <label>Drzava:
                <select v-model="noviObjekat['iddrzava']" required>
                    <option v-for="obj in drzave" v-bind:value="obj.iddrzava">{{obj.drzava}}</option>
                </select>
            </label>
        </div>
        <div>
            <label>Opstina:
                <select v-model="noviObjekat['idopstina']" required>
                    <option v-for="obj in opstine" v-bind:value="obj.idopstina">{{obj.opstina}}</option>
                </select>
            </label>
        </div>
        <div>
            <label>Mesto:
                <select v-model="noviObjekat['idmesto']" required>
                    <option v-for="obj in mesta" v-bind:value="obj.idmesto">{{obj.mesto}}</option>
                </select>
            </label>
        </div>
        <div>
            <input type="submit" v-bind:value="tekst">
        </div>
    </form>
    `
}