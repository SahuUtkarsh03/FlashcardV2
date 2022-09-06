import Vue from 'vue'
import App from './App.vue'
import Vuelidate from 'vuelidate'
import store from './store';


import router from './router'


Vue.use(Vuelidate)
Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')
