import GeodetskaFirma from './components/geodetska_firma.js'
import Tabela from './components/genericko/tabela.js'
import Forma from './components/genericko/forma.js'
import Forma_Tabela from './components/genericko/forma_tabela.js'
// import TabelaProizvoda from './components/tabelaProizvoda.js';
// import Proizvodi from './components/proizvodi.js'
// import Proizvod from './components/proizvod.js'
// component: Forma_Tabela, naziv:'drzava', atributi:['iddrzava', 'drzava']},
const router = VueRouter.createRouter({
    history: VueRouter.createWebHashHistory(),
    props: true,
    routes: [
        {path: "/", component: Forma_Tabela, props: { naziv:'drzava', atributi:['iddrzava', 'drzava']}},
        // {path: "/proizvodi", component: Proizvodi},
        // {path: "/proizvodi/:id", component: Proizvod}
    ], 
});

const app = Vue.createApp(GeodetskaFirma);
app.component('tabela', Tabela);
// app.component('tabela-proizvoda', TabelaProizvoda);
app.component('forma', Forma);
app.use(router);
app.mount("#app");