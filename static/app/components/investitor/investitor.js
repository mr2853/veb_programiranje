export default {
    props: ["naziv", "atributi"],
    template: `
<div>
    <forma-investitor v-on:sacuvaj="create" v-bind:drzave="drzave" v-bind:opstine="opstine" v-bind:mesta="mesta" v-bind:adrese="adrese" v-bind:atributi="atributi" v-bind:tekst="'Dodaj'"></forma-investitor>
    <forma-investitor v-bind:objekat="objekatZaIzmenu" v-bind:drzave="drzave" v-bind:opstine="opstine" v-bind:mesta="mesta" v-bind:adrese="adrese" v-bind:atributi="atributi" v-bind:tekst="'Izmeni'" v-on:sacuvaj="update"></forma-investitor>
    <tabela-investitor v-bind:objekti="objekti" v-bind:atributi="atributi" v-on:uklanjanje="remove" v-on:izmena="setObjekatZaIzmenu"></tabela-investitor>
</div>
    `,
    data() {
        return {
            objekti: [],
            drzave : [],
            opstine : [],
            mesta : [],
            adrese : [],
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
                this.mesta = [response.data][0][4];
                this.adrese = [response.data][0][5];
            });
        },
        create(objekat) {
            axios.post(`api/${this.naziv}`, objekat).then((response) => {
                this.refreshObjekti();
            });
        },
        update(objekat) {
            axios.put(`api/${this.naziv}/${objekat['idinvestitor']}`, objekat).then((response) => {
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
        
        if(localStorage.getItem("tip_korisnika") != "administrator")
        {
            document.getElementById("korisnik").remove()
        }
    }
}