<template>
    <div class="mainpage">
        <center>
            <h1>Welcome to Flas(h/k) Cards <span class="Username">{{UserName}}</span></h1>
        </center>       
        <div v-if="errMsg">
            <br>
            <p class="alert alert-danger">{{errMsg}}</p>  
        </div>
        <h1 @click.prevent="addDeck" ><i class="bi bi-file-earmark-plus-fill"></i></h1>

        <div class="row">
            <DeckCard class="col-md-4 card _card"  v-for="deck in decks" :key="deck.deck_id" 
            :title_= deck.deck_name 
            :lastrev_ = deck.last_reviewed 
            :score_ = deck.deck_score 
            :id_ = deck.deck_id
            />
        </div>   

    </div> 
</template>


<script>

import DeckCard from './DeckCard.vue';
import router from '../router';

export default {
    name: 'DashBoard',
    data(){
        var username=localStorage.getItem('UserName');
        var token=localStorage.getItem('x-access-token')
        var requestOptions = {
        method: 'GET',
        redirect: 'follow',
        headers:{"x-access-token":token,"Access-Control-Allow-Origin":"*"}
        };
        var decks= fetch("http://127.0.0.1:5000/getdecks", requestOptions)
                    .then(response => response.json())
                    .then(result => {
                        console.log(result);
                        if(!result.message)this.decks= result;
                    })
                    .catch(error => console.log('error', error));
        
        return {
            UserName: username,
            decks: decks,
            errMsg:null
        }      
    }, 
    methods:{
        addDeck(){
            router.push("/addDeck");
        }
    },
    components: { DeckCard }
}
</script>

<style scoped>
.Username{
    color: blue;
}
._card{
    padding: 1%;
}
.mainpage{
    margin:2%;
}

</style>