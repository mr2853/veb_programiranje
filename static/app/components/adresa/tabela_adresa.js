export default {
    props: ["objekti", "atributi"],
    emits: ["izmena", "uklanjanje"],
    data() {
        this.brojac_kolone = -1
        return {}
    },
    template: `
<table>
<thead>
    <tr>
        <th v-for="naziv in atributi">{{naziv}}</th>
        <th>Akcije</th>
    </tr>
</thead>
<tbody>
    <tr v-for="obj in objekti">
        <template v-for="i in atributi.length">
            <td>{{obj[atributi[i-1]]}}</td>
        </template>
        <td><button v-on:click="$emit('izmena', {...obj})">Izmeni</button><button
                v-on:click="$emit('uklanjanje', obj['idadresa'])">Ukloni</button></td>
    </tr>
</tbody>
</table>
    `
}