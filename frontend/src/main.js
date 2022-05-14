import Vue from 'vue'
import App from './App.vue'
import Vuelidate from 'vuelidate'



import router from './router'


Vue.use(Vuelidate)
Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
