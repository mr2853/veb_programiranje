export default {
    props: ["objekti", "atributi"],
    emits: ["izmena", "uklanjanje"],
    data() {
        return {}
    },
    template: `
    <table class="table">
    <thead class="thead-dark">
    <tr>
        <th v-for="naziv in atributi" scope="col">{{naziv}}</th>
        <th scope="col">Akcije</th>
    </tr>
</thead>
<tbody>
    <tr v-for="obj in objekti" scope="row">
        <template v-for="i in atributi.length">
            <td>{{obj[atributi[i-1]]}}</td>
        </template>
        <td><button type="button" class="btn btn-secondary" v-on:click="$emit('izmena', {...obj})">Izmeni</button>
        <button type="button" class="btn btn-secondary" v-on:click="$emit('uklanjanje', obj['idmesto'])">Ukloni</button></td>
    </tr>
</tbody>
</table>
    `
}