export default {
    template: `
    <div class="alert alert-danger" role="alert" v-if="neuspesanLogin">
  Neuspesna prijava na sistem!
</div>
    <form v-on:submit.prevent="login()">
  <div class="mb-3">
    <label class="form-label">Korisničko ime</label>
    <input type="text" v-model="noviObjekat.korisnicko_ime" class="form-control" required>
  </div>
  <div class="mb-3">
    <label class="form-label">Lozinka</label>
    <input type="password" v-model="noviObjekat.lozinka" class="form-control" required>
  </div>
  <button type="submit" class="btn btn-primary">Login</button>
</form>
    `,
    props: ["naziv", "atributi"],
    emits: ["sacuvaj"],
    data() {
        return {
            noviObjekat: {
                "korisnicko_ime" : "",
                "lozinka" : ""
            },
            neuspesanLogin: false
        }
    },
    methods: {
        login: function() {
            axios.post(`api/login`, this.noviObjekat).then((response) => {
                localStorage.setItem("token", response.data[0]);
                localStorage.setItem("tip_korisnika", response.data[1]);
                this.$router.push("/investitor");
            }, _ => {
                this.neuspesanLogin = true;
            });
        }
    }
}