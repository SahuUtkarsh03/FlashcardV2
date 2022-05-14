<template>
    <div v-if="!isDeleted">
        <div class="card-body">
            <h1 class="heading">{{ question_}}</h1> 
            <p class="card-text"> Last Reviewed : {{ last_ }} </p>
            <p class="card-text"> Card Score : {{ score_ }} </p>
            
            <button  @click="deletecard(id_)" class="card-link btn btn-primary" ><i class="bi bi-trash"></i></button>
            <button @click="ReviewCard(id_)" class="card-link btn btn-primary" ><i class="bi bi-pen-fill"></i></button>
            
        </div>
    </div>
</template>

<script>
import router from '@/router';
export default {
    name: 'CardBody',
    props:['id_','question_','answer_','last_','score_','deckid_'],
    methods:{
        async ReviewCard(id_){
            router.push(`/reviewcard/${id_}`)
        },
        async deletecard(id_){
            var token=localStorage.getItem('x-access-token');
            var requestOptions = {
            method: 'DELETE',
            headers:{"Access-Control-Expose-Headers": "Content-Disposition",
                    "Content-Disposition": "attachment",
                    "x-access-token": token,
                    "Access-Control-Allow-Origin":"*"},
            redirect: 'follow'
            };

            await fetch(`http://127.0.0.1:5000/card/${id_}`, requestOptions)
            .then(response => response.json())
            .then(result => {console.log(result);
                            this.isDeleted=true;
                            delete this.$parent.$data.cards[`${id_}`]
                            })
            .catch(error => console.log('error', error));
            
            router.push(`/viewcards/${this.deckid_}`);
            
            console.log(id_);
        }
        
    },
    data(){
        return{
            isDeleted:false
        }
    }
}
</script>
