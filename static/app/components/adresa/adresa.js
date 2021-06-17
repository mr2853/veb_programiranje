export default {
    props: ["naziv", "atributi"],
    template: `
<div>
    <forma-adresa v-bind:objekat="objekatZaIzmenu" v-bind:drzave="drzave" v-bind:opstine="opstine" v-bind:mesta="mesta" v-bind:atributi="atributi" v-on:dodaj="create" v-on:izmeni="update" v-on:pretraga="pretraga"></forma-adresa>
    <tabela-adresa v-bind:objekti="objekti" v-bind:atributi="atributi" v-on:uklanjanje="remove" v-on:izmena="setObjekatZaIzmenu"></tabela-adresa>
</div>
    `,
    data() {
        return {
            objekti: [],
            drzave : [],
            opstine : [],
            mesta : [],
            objekatZaIzmenu: {},
        }
    },
    methods: {
        pretraga(objekat) {
            axios.post(`api/${this.naziv}/pretraga`, objekat).then((response) => {
                this.objekti = response.data
            });
        },
        setObjekatZaIzmenu(objekat) {
            this.objekatZaIzmenu = { ...objekat };
        },
        refreshObjekti() {
            axios.get(`api/${this.naziv}`).then((response) => {
                this.objekti = [response.data][0][1];
                this.drzave = [response.data][0][2];
                this.opstine = [response.data][0][3];
                this.mesta = [response.data][0][4];
            });
        },
        create(objekat) {
            axios.post(`api/${this.naziv}`, objekat).then((response) => {
                this.refreshObjekti();
            });
        },
        update(objekat) {
            axios.put(`api/${this.naziv}/${objekat['idadresa']}`, objekat).then((response) => {
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