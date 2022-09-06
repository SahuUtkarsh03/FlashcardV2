<template>
    <div class="mainpage">
        <center>
            <h1>Welcome to Flas(h/k) Cards <span class="Username">{{UserName}}</span></h1>
        </center>       
        <div v-if="errMsg" >
            <br>
            <div><button @click="setErr()" 
                class="alert alert-danger" 
                role="alert">
                {{errMsg}}
                <span aria-hidden="true"> &times;</span>
            </button> </div>
        </div>
        <h1 @click.prevent="addDeck" ><i class="bi bi-file-earmark-plus-fill"></i></h1>

        <div class="row">
            <DeckCard class="col-md-4 card _card"  v-for="deck in allDecks" :key="deck.deck_id" 
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
import { mapGetters , mapActions } from 'vuex';

export default {
    name: 'DashBoard',
    data(){
        var username=localStorage.getItem('UserName');
        
        return {
            UserName: username,
            // decks: decks,
            errMsg:null
        }      
    }, 
    methods:{
        addDeck(){
            router.push("/addDeck");
        },
        setErr(){
            this.errMsg=!this.errMsg;
        },
        ...mapActions(["fetchDecks"])
    },
    components: { DeckCard },
    created(){
        this.fetchDecks();
    },
    computed: mapGetters(['allDecks'])
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