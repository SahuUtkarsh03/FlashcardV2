import Vuex from 'vuex';
import Vue from 'vue';
import deck from "./modules/deck";
import user from "./modules/user";
import createPersistedState from 'vuex-persistedstate';


Vue.use(Vuex);

export default new Vuex.Store({
        modules: {
            deck,user
        },
        plugins:[
            createPersistedState()
        ]
    });