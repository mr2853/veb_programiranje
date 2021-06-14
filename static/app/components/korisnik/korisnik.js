export default {
    props: ["naziv", "atributi"],
    template: `
    <div>
        <forma-korisnik v-on:sacuvaj="create" v-bind:tip_korisnika="tip_korisnika" v-bind:atributi="atributi" v-bind:tekst="'Dodaj'"></forma-korisnik>
        <forma-korisnik v-bind:objekat="objekatZaIzmenu" v-bind:tip_korisnika="tip_korisnika" v-bind:atributi="atributi" v-bind:tekst="'Izmeni'" v-on:sacuvaj="update"></forma-korisnik>
        <tabela-korisnik v-bind:objekti="objekti" v-bind:atributi="atributi" v-on:uklanjanje="remove" v-on:izmena="setObjekatZaIzmenu"></tabela-korisnik>
    </div>
    `,
    data() {
        return {
            objekti: [],
            tip_korisnika: [],
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
                this.tip_korisnika = [response.data][0][2];
            });
        },
        create(objekat) {
            axios.post(`api/${this.naziv}`, objekat).then((response) => {
                this.refreshObjekti();
            });
        },
        update(objekat) {
            axios.put(`api/${this.naziv}/${objekat['idkorisnik']}`, objekat).then((response) => {
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