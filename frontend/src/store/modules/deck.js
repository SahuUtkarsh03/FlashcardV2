const state ={
    decks:[]
};

const getters={
    allDecks:(state)=> state.decks
};

const actions={
    fetchDecks:async (context)=>{
        var token=localStorage.getItem('x-access-token')
        var requestOptions = {
        method: 'GET',
        redirect: 'follow',
        headers:{"x-access-token":token,"Access-Control-Allow-Origin":"*"}
        };
        await fetch("http://127.0.0.1:5000/getdecks", requestOptions)
                    .then(response => response.json())
                    .then(result => {
                        console.log(result);
                        context.commit('setDecks',result);
                    })
                    .catch(error => console.log('error', error));        
    },
    clearDecks:(context)=> context.commit.delDecks()
    
};

const mutations={
setDecks: (state,decks)=> state.decks=decks,
delDecks:(state)=>state.decks=[]
};

export default {
    state,
    getters,
    actions,
    mutations
};