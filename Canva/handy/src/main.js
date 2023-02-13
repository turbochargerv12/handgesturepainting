import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import router from './router'
import axios from 'axios'
import ServerError from './components/Others/500Page'


Vue.config.productionTip = false

Vue.component('ServerError',ServerError) 

// axios.defaults.baseURL="http://192.168.49.29:5555"
// Vue.prototype.baseURL="http://192.168.49.29:5555"

new Vue({
  router,
  vuetify,
  render: h => h(App)
}).$mount('#app')
