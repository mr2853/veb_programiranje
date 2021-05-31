export default {
    template: `
<div>
    <korisnik-forma v-on:sacuvaj="create" v-bind:tekst="'Dodaj'"></korisnik-forma>
    <korisnik-forma v-bind:kupac="kupacZaIzmenu" v-bind:tekst="'Izmeni'" v-on:sacuvaj="update"></korisnik-forma>
    <tabela-korisnika v-bind:kupci="kupci" v-on:uklanjanje="remove" v-on:izmena="setKupacZaIzmenu"></tabela-korisnika>
</div>
    `,
    data() {
        return {
            kupci: [],
            kupacZaIzmenu: {},
        }
    },
    methods: {
        setKupacZaIzmenu(kupac) {
            this.kupacZaIzmenu = { ...kupac };
        },
        refreshKupci() {
            axios.get("api/kupci").then((response) => {
                this.kupci = response.data;
            });
        },
        create(kupac) {
            axios.post("api/kupci", kupac).then((response) => {
                this.refreshKupci();
            });
        },
        update(kupac) {
            console.log(kupac);
            axios.put(`api/kupci/${kupac.id}`, kupac).then((response) => {
                this.refreshKupci();
            });
        },
        remove(id) {
            axios.delete(`api/kupci/${id}`).then((response) => {
                this.refreshKupci();
            });
        }
    },
    created() {
        this.refreshKupci();
    }
}