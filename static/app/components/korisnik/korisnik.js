export default {
    props: ["naziv", "atributi"],
    template: `
<div>
    <forma v-on:sacuvaj="create" v-bind:dodatni_objekti="dodatni_objekti" v-bind:atributi="atributi" v-bind:tekst="'Dodaj'"></forma>
    <forma v-bind:objekat="objekatZaIzmenu" v-bind:dodatni_objekti="dodatni_objekti" v-bind:atributi="atributi" v-bind:tekst="'Izmeni'" v-on:sacuvaj="update"></forma>
    <tabela v-bind:objekti="objekti" v-bind:atributi="atributi" v-on:uklanjanje="remove" v-on:izmena="setObjekatZaIzmenu"></tabela>
</div>
    `,
    data() {
        return {
            objekti: [],
            dodatni_objekti : [],
            objekatZaIzmenu: {},
        }
    },
    methods: {
        setObjekatZaIzmenu(objekat) {
            this.objekatZaIzmenu = { ...objekat };
        },
        refreshObjekti() {
            axios.get(`api/${this.naziv}`).then((response) => {
                let nadjen = 0
                console.log(response.data[1])
                for(let i=0; i < Object.keys([response.data][0][1]).length; i++)
                {
                    if([response.data][0][1][i] != undefined){
                        if([response.data][0][1][i].includes('id'))
                        {
                            this.objekti = [response.data][0][1];
                            this.dodatni_objekti = [response.data][0][2];
                            console.log(this.dodatni_objekti)
                            nadjen = 1
                            break
                        }
                    }
                }
                if(nadjen == 0){
                    console.log(response.data)
                    console.log([response.data][0][1])
                    this.objekti = [response.data][0][1];
                }
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