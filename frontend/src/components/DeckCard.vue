<template>
    <div v-if="!isDeleted">
        <div class="card-body">
            <h1 class="heading">{{ title_ }} <i @click="viewCards(id_)" class="bi bi-arrow-up-right-square"></i> </h1>
            <p>Last Reviewed this deck at: {{ lastrev_ }}</p>
            <p>Deck Score: {{ score_ }}</p>
            <button @click="deleteDeck(id_)" class="card-link btn btn-primary" ><i class="bi bi-trash"></i></button>
            <button @click="exportDeck(id_)" class="card-link btn btn-primary" ><i class="bi bi-file-arrow-down-fill"></i></button>
            <button @click="addcard(id_)" class="card-link btn btn-primary" ><i class="bi bi-plus-circle-fill"></i></button>
        </div>
    </div>
</template>

<script>
import router from '@/router';
import {saveAs} from 'file-saver'

export default({

    name : "DeckCard",
    props : ['title_','score_','lastrev_','id_'],
    data(){
        return{
            isDeleted:false
        }
    },
    methods : {

        async deleteDeck(id_){
            var token=this.$store.getters.getToken
            var requestOptions = {
            method: 'DELETE',
            redirect: 'follow',
            headers:{
                        "Content-Type": "application/json",
                        "x-access-token": token,
                        "Access-Control-Allow-Origin":"http://127.0.0.1:5000"              
                    }
            };

            await fetch(`http://127.0.0.1:5000/deck/${id_}`, requestOptions)
            .then(response => response.json())
            .then(result => {
                console.log(result,id_);
                if (!result.error_message){
                    this.isDeleted=true

                    delete this.$parent.$data.decks[id_]

                    console.log("deleted Deck",id_);
                }else{
                    this.$parent.$data.errMsg=result.error_message
                }
            })
            .catch(error => {
                console.log(error);
            });

            
        },
        async exportDeck(id_){
            var token=this.$store.getters.getToken

            var requestOptions = {
            method: 'GET',
            redirect: 'follow',
            headers:{"Access-Control-Expose-Headers": "Content-Disposition",
                    "Content-Disposition": "attachment",
                    "x-access-token": token,
                    "Access-Control-Allow-Origin":"*"}
            };

            const res = await fetch(`http://127.0.0.1:5000//senddeck/${id_}`, requestOptions);
                
            if (res.ok){
                const blob = await res.blob();

                console.log(res);
                console.log(blob);

                saveAs(blob,`${this.title_}.csv`)
            }else console.log(res.json())
            console.log("export Deck",id_);
        },
        addcard(id_){
            router.push(`/addCard/${id_}`);
        },
        async viewCards(id_){
            console.log(id_);
            router.push(`/viewcards/${id_}`);
        }
    }
})
</script>

<style scoped>
.heading{
    text-align: center;
}
</style>