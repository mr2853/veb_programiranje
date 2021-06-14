export default {
    props: ["objekat", "atributi", "tekst", "tip_korisnika"],
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
            <label>{{atr}}: <input type="text" v-model="noviObjekat[atr]" required></label>
        </div>
        <label>Tip korisnika:
            <select v-model="noviObjekat['idtip_korisnika']" required>
                <option v-for="obj in tip_korisnika" v-bind:value="obj.idtip_korisnika">{{obj.tip_korisnika}}</option>
            </select>
        </label>
        <div>
            <input type="submit" v-bind:value="tekst">
        </div>
    </form>
    `
}