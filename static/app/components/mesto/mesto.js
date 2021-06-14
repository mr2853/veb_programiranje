export default {
    props: ["naziv", "atributi"],
    template: `
<div>
    <forma-mesto v-on:sacuvaj="create" v-bind:drzave="drzave" v-bind:opstine="opstine" v-bind:atributi="atributi" v-bind:tekst="'Dodaj'"></forma-mesto>
    <forma-mesto v-bind:objekat="objekatZaIzmenu" v-bind:drzave="drzave" v-bind:opstine="opstine" v-bind:atributi="atributi" v-bind:tekst="'Izmeni'" v-on:sacuvaj="update"></forma-mesto>
    <tabela-mesto v-bind:objekti="objekti" v-bind:atributi="atributi" v-on:uklanjanje="remove" v-on:izmena="setObjekatZaIzmenu"></tabela-mesto>
</div>
    `,
    data() {
        return {
            objekti: [],
            drzave : [],
            opstine : [],
            objekatZaIzmenu: {},
        }
    },
    methods: {
        setObjekatZaIzmenu(objekat) {
            this.objekatZaIzmenu = { ...objekat };
        },
        refreshObjekti() {
            axios.get(`api/${this.naziv}`).then((response) => {
                this.objekti = [response.data][0][1];
                this.drzave = [response.data][0][2];
                this.opstine = [response.data][0][3];
            });
        },
        create(objekat) {
            axios.post(`api/${this.naziv}`, objekat).then((response) => {
                this.refreshObjekti();
            });
        },
        update(objekat) {
            axios.put(`api/${this.naziv}/${objekat['idmesto']}`, objekat).then((response) => {
                this.refreshObjekti();
            });
        },
        remove(id) {
            axios.delete(`api/${this.naziv}/${id}`).then((response) => {
                this.refreshObjekti();
            });
        }
    },
    created() {
        this.refreshObjekti();
    }
}