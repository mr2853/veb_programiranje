export default {
    props: ["objekat", "atributi", "tekst"],
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
        <div>
            <input type="submit" v-bind:value="tekst">
        </div>
    </form>
    `
}