<template>
    <div class="mainpage">
        <button @click="addcard(deckid)" class="card-link btn btn-primary" ><i class="bi bi-plus-circle-fill"></i></button>
        <br><br>
        <div class="row">
            <CardBody class="col-md-4 card _card"  v-for="card in cards"
            :id_= card.id
            :deckid_ = card.deck_id
            :answer_ = card.answer
            :question_ = card.question
            :last_ = card.last_reviewed
            :score_ = card.card_score
            :key="card.id"
            />
        </div>
    </div>
</template>

<script>
import CardBody from './CardBody.vue';
import router from '../router';

export default {
    name:'ViewCards',
    data(){
        var token=this.$store.getters.getToken;
        var deckid = this.$route.params.deckid
        var requestOptions = {
        method: 'GET',
        headers: {"Access-Control-Expose-Headers": "Content-Disposition",
                    "Content-Disposition": "attachment",
                    "x-access-token": token,
                    "Access-Control-Allow-Origin":"*"},
        redirect: 'follow'
        };

        fetch(`http://127.0.0.1:5000/getcards/${deckid}`, requestOptions)
        .then(r=>r.json()).then(data=>this.cards=data);
        
        return{
            cards:null,
            deckid:this.$route.params.deckid
        }
    },
    methods:{
        addcard(id_){
            router.push(`/addCard/${id_}`);
        }
    },
    components : {
        CardBody 
    },

}
</script>


<style scoped>
._card{
    padding: 1%;
}
.mainpage{
    margin:2%;
}

</style>