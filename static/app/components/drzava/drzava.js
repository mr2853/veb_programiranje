export default {
    props: ["naziv", "atributi"],
    template: `
<div>
    <forma-drzava v-on:sacuvaj="create" v-bind:atributi="atributi" v-bind:tekst="'Dodaj'"></forma-drzava>
    <forma-drzava v-bind:objekat="objekatZaIzmenu" v-bind:atributi="atributi" v-bind:tekst="'Izmeni'" v-on:sacuvaj="update"></forma-drzava>
    <tabela-drzava v-bind:objekti="objekti" v-bind:atributi="atributi" v-on:uklanjanje="remove" v-on:izmena="setObjekatZaIzmenu"></tabela-drzava>
</div>
    `,
    data() {
        return {
            objekti: [],
            objekatZaIzmenu: {},
        }
    },
    methods: {
        setObjekatZaIzmenu(objekat) {
            this.objekatZaIzmenu = { ...objekat };
        },
        refreshObjekti() {
            axios.get(`api/${this.naziv}`).then((response) => {
                this.objekti = response.data
            });
        },
        create(objekat) {
            axios.post(`api/${this.naziv}`, objekat).then((response) => {
                this.refreshObjekti();
            });
        },
        update(objekat) {
            axios.put(`api/${this.naziv}/${objekat[this.atributi[0]]}`, objekat).then((response) => {
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