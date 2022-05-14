<template>
    <div class="main-form">
        <center><h1 class="display-1">Add Card</h1></center>
            <div v-if="errMsg">
                <br>
                <p class="alert alert-danger" > {{errMsg}}</p>
            </div>
            <form @submit.prevent="handleSubmit">
                <input class="form-control" type="text" v-model="question" placeholder="Question" >
                <br>
                <input class="form-control" type="text" v-model="answer" placeholder="Answer" >
                <br>
                <button class="form-control btn btn-primary" type="submit" >Submit</button>
            </form>
    </div> 
</template>

<script>
import router from '../router';
import {required} from 'vuelidate/lib/validators';

export default ({
    name:"AddCard",
    data(){
        return{
            errMsg:null,
            question:null,
            answer:null
        }
    },
    validations(){
        return{
            question:{required},
            answer:{required}
        }
    },
    methods:{
        async handleSubmit(){

            var token = localStorage.getItem('x-access-token');
            var deckid = this.$route.params.deckid
            this.$v.$touch();
            if (!this.$v.$error){
                var raw = JSON.stringify({
                "question":this.question,
                "answer": this.answer,
                "deckid": deckid
                });

                var requestOptions = {
                method: 'POST',
                headers: {
                    "Content-Type":"application/json",
                    "x-access-token": token
                },
                body: raw,
                redirect: 'follow'
                };

                await fetch("http://127.0.0.1:5000/card", requestOptions)
                .then(response => response.text())
                .then(result => {
                    console.log(result);  
                    router.push(`/viewcards/${deckid}`);
                })
                .catch(error => console.log('error', error));
            }else alert("Form not Submitted!");
            
        }
    }
})
</script>

<style scoped>
.main-form{
        margin-left: 25%; 
        margin-right: 25%;
    }
</style>