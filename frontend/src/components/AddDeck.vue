<template>
    <div class="main-form">
        <center><h1 class="display-1">Add a Deck</h1></center>
        <div v-if="errMsg">
                <br>
                <p class="alert alert-danger" > {{errMsg}}</p>
            </div>
        <form @submit.prevent="handleSubmit">
            <input class="form-control" type="text" v-model="deckname" placeholder="DeckName" >
            <br>
            <button class="form-control btn btn-primary" type="submit" >Submit</button>
        </form>
    </div>
</template>

<script>
import router from '@/router';
import {required} from 'vuelidate/lib/validators';

export default {
    name:"AddDeck",
    data(){
        return{
            deckname:null,
            errMsg:null
        }
    },
    validations(){
        return{
            deckname:{required}
        }
    },
    methods:{
        async handleSubmit(){
            var token=localStorage.getItem('x-access-token');
            this.$v.$touch();
            if (!this.$v.$error){
                await fetch("http://127.0.0.1:5000/createDeck",{
                    method:'POST',redirect:"follow",
                    body:JSON.stringify({"deckname":this.deckname}),
                    headers:{
                        "Content-Type": "application/json",
                        "x-access-token": token,
                        "Access-Control-Allow-Origin":"*"
                    }
                }).then(response => response.json())
                .then(result => {
                    console.log(result);

                    if(result.errMsg){
                        this.errMsg=result.errMsg;
                        this.deckname=null    
                    }
                    else router.push("/dashboard");
                })
                .catch(error => console.log('error', error));
                // .then(response => {                    
                //     if(response.status==201){
                //         const r= response.json();
                //         console.log(response);
                //         if(r.Msg)router.push("/dashboard");
                //     }else {
                //         console.log(response);
                //         console.log(response.status);
                //         console.log(response.text());
                //     }
                // })
                // .then(response => {
                //     if(response.status==201){
                //         console.log(response);
                //         const r = response.json();
                //         console.log(r);
                //         console.log(r.Msg);
                //         r.Msg && router.push("/dashboard");
                //     }else{
                //         console.log(response);
                //         const r = response.json();
                //         console.log(r);
                //         console.log(r.errMsg);
                //     }
                //     })
                //     .catch(error => console.log('error', error));

            }else alert("Form not Submitted");
        }
    }
}
</script>

<style scoped>
    .main-form{
        margin-left: 25%; 
        margin-right: 25%;
    }
</style>