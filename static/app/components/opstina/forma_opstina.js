export default {
    props: ["objekat", "drzave", "atributi", "tekst"],
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
                <label>{{atr}}: <input type="text" v-model="noviObjekat[atr]" required></label>
            </template>
        </div>

        <label>Drzava:
            <select v-model="noviObjekat['iddrzava']" required>
                <option v-for="obj in drzave" v-bind:value="obj.iddrzava">{{obj.drzava}}</option>
            </select>
        </label>
        <div>
            <input type="submit" v-bind:value="tekst">
        </div>
    </form>
    `
}