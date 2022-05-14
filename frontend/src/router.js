import Vue from "vue";
import Router from 'vue-router'

import HomePage from './components/HomePage'
import UserRegister from "./components/UserRegister";
import UserLogin from "./components/UserLogin";
import DashBoard from './components/DashBoard';
import AddDeck from './components/AddDeck';
import AddCard from './components/AddCard';
import ViewCards from './components/ViewCards';
import ReviewCard from './components/ReviewCard';

Vue.use(Router);

export default new Router({
    mode:'history',
    routes:[
        {path: '/' , component: HomePage},
        {path: '/register' , component: UserRegister},
        {path: '/login' , component: UserLogin},
        {path: '/dashboard', component: DashBoard},
        {path: '/addDeck', component: AddDeck},
        {path: '/addCard/:deckid', component: AddCard},
        {path: '/viewcards/:deckid', component: ViewCards},
        {path: '/reviewcard/:cardid', component: ReviewCard, props:true}

    ]
});