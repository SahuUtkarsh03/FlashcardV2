<template>
    <div class="main-form">
        <center><h1 class="display-1">Register Yourself</h1></center>
        <form @submit.prevent="onSubmit">
            <div v-if="errorMsg">
                <br>
                <p class="alert alert-danger" > {{errorMsg}}</p>
            </div>
            <input class="form-control" type="text" v-model="firstname" placeholder="FirstName" >
            <br>
            <input class="form-control" type="text" v-model="lastname" placeholder="LastName" >
            <br>
            <input class="form-control" type="text" v-model="username" placeholder="Username" >
            <br>
            <input class="form-control" type="email" v-model="email" placeholder="Email">
            <br>
            <input class="form-control" type="password" v-model="password" placeholder="Password" autocomplete="on">
            <br>
            <p class="alert alert-danger" v-if="!$v.password.minLength || !$v.password.maxLength" > 
                Password must be more than 8 characters & less than 20 characters.
            </p>
            <input class="form-control" type="password" v-model="checkpassword" placeholder="Check Password" autocomplete="on">
            <br v-if="!$v.checkpassword.$error">
            <p class="alert alert-danger" v-if="!$v.checkpassword.sameAs" > Passwords must be identical.</p>
            <br>
            <button class="form-control btn btn-primary" type="submit" >Submit</button>
        </form>
        <br>
        <h3 style="text-align: center;">Already have an account? Login please!!  
            <router-link class="nav-link" to="/login">Click here to Login</router-link>
        </h3>
    </div>
</template>

<script>
import {required,email,maxLength,minLength,sameAs} from 'vuelidate/lib/validators';
import router from '../router';

export default {
    name: "UserRegister",
    data:()=>{
        return {
            firstname : null,
            lastname : null,
            password : null,
            checkpassword : null,
            username : null,
            email : null,
            errorMsg : null
        }
    },
    validations: ()=>{
        return{
            firstname : {required},
            lastname : {required},
            password : {required,maxLength:maxLength(20),minLength:minLength(8)},
            checkpassword : {required,maxLength : maxLength(20),minLength : minLength(8), sameAs: sameAs("password")},
            username : {required},
            email: {required,email}
        }
    },
    methods:{
        async onSubmit(){
            this.$v.$touch();
            if (!this.$v.$error){
                const data = {
                    firstname: this.firstname,
                    lastname:this.lastname,
                    email: this.email,
                    password: this.password,
                    username: this.username
                }
                console.log(data);
                await fetch('http://127.0.0.1:5000/user',{
                    method:"POST",
                    body:JSON.stringify(data),
                    headers:{'Content-Type': 'application/json'}
                })
                .then( response => response.json())
                .then(data => { 
                    if (data.error_message) this.errorMsg = data.error_message;
                    else router.push("/login");
                })
                .catch(err=>console.log(err.response.data));
            
            }else alert("form not submmitted");
            
        }
    }
};
</script>

<style scoped>
    .main-form{
        margin-left: 25%; 
        margin-right: 25%;
    }
</style>
