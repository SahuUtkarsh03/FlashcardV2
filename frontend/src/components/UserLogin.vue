<template>
<div class="main-form">
    <center><h1 class="display-1">Login Yourself</h1></center>
        <form @submit.prevent="handleLogin">
            <div v-if="errorMsg">
                <br>
                <p class="alert alert-danger" > {{errorMsg}}</p>
            </div>
            <input class="form-control" type="text" v-model="username" placeholder="Username" >
            <br>
            <input class="form-control" type="password" v-model="password" placeholder="Password" autocomplete="on" >
            <br>
            <button class="form-control btn btn-primary" type="submit" >Login</button>
        </form>
</div>
</template>

<script>
import router from '@/router';
import base64 from 'base-64';
import {required,maxLength,minLength} from 'vuelidate/lib/validators';

export default {
    name:'UserLogin',
    data:()=>{
        return {
            username : null,
            password : null,
            errorMsg : null
        }
    },
    validations: ()=>{
        return{
            username : {required},
            password : {required,maxLength: maxLength(20),minLength:minLength(8)}
        }
    },
    methods:{
        async handleLogin(){   
            this.$v.$touch();
            if (!this.$v.$error){
            var myHeaders = new Headers();
            myHeaders.append("Authorization", 'Basic '+ base64.encode(this.username + ":" + this.password));
            myHeaders.append("Content-Type", "application/json");

            var raw = JSON.stringify({
            "username": this.username,
            "password": this.password
            });

            var requestOptions = {
            method: 'POST',
            headers: myHeaders,
            body: raw,
            redirect: 'follow'
            };

            await fetch("http://127.0.0.1:5000/login", requestOptions)
            .then(response => {console.log(response.status);return response.text()})
            .then(token => {console.log(token)
                if (!token.includes("Could not verify")){
                localStorage.setItem("x-access-token",token);
                localStorage.setItem("UserName",this.username);
                this.$parent.$data.isLogin=true;
                this.$parent.$children[0].$data.isLogin=!this.$parent.$children[0].$data.isLogin;
                this.$parent.$children[0].$data.isLogout=!this.$parent.$children[0].$data.isLogout;
                router.push("/dashboard");
                }else {this.errorMsg=token;
                    this.username=null;
                    this.password=null;
                }
                })
            .catch(error => console.log('error', error));
            } else alert("form not submmitted");       
            
        }
    },
    
}
</script>

<style scoped>
    .main-form{
        margin-left: 25%; 
        margin-right: 25%;
    }
</style>