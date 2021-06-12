import GeodetskaFirma from './components/geodetska_firma.js'

import TabelaDrzava from './components/drzava/tabela_drzava.js'
import FormaDrzava from './components/drzava/forma_drzava.js'
import Drzava from './components/drzava/drzava.js'

import TabelaOpstina from './components/opstina/tabela_opstina.js'
import FormaOpstina from './components/opstina/forma_opstina.js'
import Opstina from './components/opstina/opstina.js'

import TabelaKorisnik from './components/korisnik/tabela_korisnik.js'
import FormaKorisnik from './components/korisnik/forma_korisnik.js'
import Korisnik from './components/korisnik/korisnik.js'

import TabelaMesto from './components/mesto/tabela_mesto.js'
import FormaMesto from './components/mesto/forma_mesto.js'
import Mesto from './components/mesto/mesto.js'

import TabelaKatastarskaOpstina from './components/katastarska_opstina/tabela_katastarska_opstina.js'
import FormaKatastarskaOpstina from './components/katastarska_opstina/forma_katastarska_opstina.js'
import KatastarskaOpstina from './components/katastarska_opstina/katastarska_opstina.js'

import TabelaAdresa from './components/adresa/tabela_adresa.js'
import FormaAdresa from './components/adresa/forma_adresa.js'
import Adresa from './components/adresa/adresa.js'

import TabelaInvestitor from './components/investitor/tabela_investitor.js'
import FormaInvestitor from './components/investitor/forma_investitor.js'
import Investitor from './components/investitor/investitor.js'

const router = VueRouter.createRouter({
    history: VueRouter.createWebHashHistory(),
    props: true,
    routes: [
        {path: "/drzava_view", component: Drzava, props: { naziv:'drzava_view', atributi:['drzava']}},
        {path: "/opstina_view", component: Opstina, props: { naziv:'opstina_view', atributi:['opstina', 'iddrzava']}},
        {path: "/mesto_view", component: Mesto, props: { naziv:'mesto_view', atributi:['mesto', 'postanski_broj', 'idopstina']}},
        {path: "/katastarska_opstina_view", component: KatastarskaOpstina, props: { naziv:'katastarska_opstina_view', atributi:['katastarska_opstina','idopstina']}},
        {path: "/korisnik_view", component: Korisnik, props: { naziv:'korisnik_view', atributi:['korisnicko_ime', 'lozinka', 'tip_korisnika']}},
        {path: "/adresa_view", component: Adresa, props: { naziv:'adresa_view', atributi:['idmesto', 'ulica', 'broj']}},
        {path: "/investitor_view", component: Investitor, props: { naziv:'investitor_view', atributi:['ime','prezime','jmbg','broj_mobilnog','email','postanski_broj','ulica','broj']}},
    ], 
});

const app = Vue.createApp(GeodetskaFirma);

app.component('tabela-investitor', TabelaInvestitor);
app.component('forma-investitor', FormaInvestitor);

app.component('tabela-adresa', TabelaAdresa);
app.component('forma-adresa', FormaAdresa);

app.component('tabela-katastarska-opstina', TabelaKatastarskaOpstina);
app.component('forma-katastarska-opstina', FormaKatastarskaOpstina);

app.component('tabela-drzava', TabelaDrzava);
app.component('forma-drzava', FormaDrzava);

app.component('tabela-opstina', TabelaOpstina);
app.component('forma-opstina', FormaOpstina);

app.component('tabela-korisnik', TabelaKorisnik);
app.component('forma-korisnik', FormaKorisnik);

app.component('tabela-mesto', TabelaMesto);
app.component('forma-mesto', FormaMesto);

app.use(router);
app.mount("#app");