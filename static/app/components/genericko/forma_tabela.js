export default {
    props: ["naziv", "atributi"],
    template: `
<div>
    <forma v-on:sacuvaj="create" v-bind:atributi="atributi" v-bind:tekst="'Dodaj'"></forma>
    <forma v-bind:objekat="objekatZaIzmenu" v-bind:atributi="atributi" v-bind:tekst="'Izmeni'" v-on:sacuvaj="update"></forma>
    <tabela v-bind:objekti="objekti" v-bind:atributi="atributi" v-on:uklanjanje="remove" v-on:izmena="setObjekatZaIzmenu"></tabela>
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
                this.objekti = response.data;
            });
        },
        getForma() {
            axios.get(`api/${this.naziv}_forma`).then((response) => {
                this.objekti['dodatak_formi'] = response.data;
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
        this.getForma();
    }
}