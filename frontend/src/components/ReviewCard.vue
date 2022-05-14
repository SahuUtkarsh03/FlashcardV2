<template>
    <div class="main-form">
        <center><h3 class="heading">Question : {{question}}</h3>
        <h3 class="heading">Answer: {{answer}}</h3></center>
        <form @submit.prevent="rate" >
            <select class="form-select" v-model="score" selected>
                <option value="0">--select--</option>
                <option value="15">Easy</option>
                <option value="10">Medium</option>
                <option value="5">Hard</option>
            </select>
            <br>
            <button class="form-control btn btn-primary" type="submit" >Rate</button>
        </form>
    </div>
</template>

<script>
import router from '@/router';
export default {
    name:"ReviewCard",

    data(){
        var token=localStorage.getItem('x-access-token');
        var requestOptions = {
        method: 'GET',
        headers:{"Access-Control-Expose-Headers": "Content-Disposition",
                    "Content-Disposition": "attachment",
                    "x-access-token": token,
                    "Access-Control-Allow-Origin":"*"},
        redirect: 'follow'
        };

        fetch(`http://127.0.0.1:5000/card/${this.$route.params.cardid}`, requestOptions)
        .then(response => response.json())
        .then(result => {
            console.log(result);
            this.score=result.cardscore;
            this.question=result.question;
            this.answer=result.answer;
            this.deckid=result.parent_deckid;
        })
        .catch(error => console.log('error', error));

        return {
            score:null,
            question:null,
            answer:null,
            deckid:null
        }
    },
    methods:{
        async rate(){
            var token=localStorage.getItem('x-access-token');
            await fetch(`http://127.0.0.1:5000/reviewcard/${this.$route.params.cardid}`,{
                method: 'POST',
                headers: {
                    "Content-Type": "application/json",
                    "x-access-token": token,
                    "Access-Control-Allow-Origin":"*"
                },
                body: JSON.stringify({"score":this.score}),
                redirect: 'follow'
                })
                .then(response => response.json())
                .then(result => console.log(result))
                .catch(error => console.log('error', error));

                router.push(`/viewcards/${this.deckid}`);
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