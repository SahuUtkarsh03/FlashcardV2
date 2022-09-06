<template>
    <nav class="navbar navbar-expand-md navbar-dark bg-dark sticky-top" style="margin-bottom: 10px;">
    <button class="navbar-toggler navbar-toggler-right" type="button"
        data-toggle="collapse" data-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent" aria-expanded="false"
        aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
    </button>
    <span class="navbar-brand">Flas(h/k) Card</span>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav mr-auto">
                <li class="nav-item">
                    <router-link class="nav-link" to= "/" >Home</router-link>
                </li>
                <li v-if="!getToken" class="nav-item">
                    <router-link class="nav-link" to= "/register" >Register</router-link>
                </li>
                <li v-if="!getToken" class="nav-item">
                    <router-link class="nav-link" to="/login">login</router-link>
                </li>
                <li v-if="getToken" class="nav-item">
                    <router-link class="nav-link" to="/dashboard" >Dashboard</router-link>
                </li>
                <li v-if="getToken" class="nav-item">
                    <span @click="logout" class="nav-link" >Logout</span>
                </li>

            </ul>
        </div>
    </nav>
</template>

<script>
import router from '@/router';
import { mapGetters ,mapActions} from 'vuex';

export default {
    name: 'NavBar',
    methods:{
        ...mapActions(['clearToken','']),
        logout(){
            localStorage.removeItem("x-access-token");
            localStorage.removeItem("UserName");
            this.clearToken();
            router.push("/login");
            console.log("CLear Token");

        }
    },
    computed:mapGetters(['getToken'])
}
</script>

