import GeodetskaFirma from './components/geodetska_firma.js'
import Tabela from './components/genericko/tabela.js'
import Forma from './components/genericko/forma.js'
import Forma_Tabela from './components/genericko/forma_tabela.js'

const router = VueRouter.createRouter({
    history: VueRouter.createWebHashHistory(),
    props: true,
    routes: [
        {path: "/drzava_view", component: Forma_Tabela, props: { naziv:'drzava_view', atributi:['drzava']}},
        {path: "/opstina_view", component: Forma_Tabela, props: { naziv:'opstina_view', atributi:['opstina', 'iddrzava']}},
        {path: "/mesto_view", component: Forma_Tabela, props: { naziv:'mesto_view', atributi:['mesto', 'postanski_broj', 'idopstina']}},
        {path: "/katastarska_opstina_view", component: Forma_Tabela, props: { naziv:'katastarska_opstina_view', atributi:['katastarska_opstina','idopstina']}},
        {path: "/korisnik_view", component: Forma_Tabela, props: { naziv:'korisnik_view', atributi:['korisnicko_ime', 'lozinka', 'tip_korisnika']}},
        {path: "/investitor_view", component: Forma_Tabela, props: { naziv:'investitor_view', atributi:['ime','prezime','jmbg','broj_mobilnog','email','iddrzava','idopstina','idmesto','postanski_broj','ulica','broj']}},
    ], 
});

const app = Vue.createApp(GeodetskaFirma);
app.component('tabela', Tabela);
app.component('forma', Forma);
app.use(router);
app.mount("#app");