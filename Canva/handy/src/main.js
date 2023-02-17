import Vue from 'vue';
import App from './App.vue';
import VueKonva from 'vue-konva';
import vuetify from './plugins/vuetify';
import router from './router';
// import vueElementLoading from 'vue-element-loading'
import ServerError from './components/Others/500Page'

Vue.use(VueKonva);
Vue.component('ServerError',ServerError); 
// Vue.component('VueElementLoading',vueElementLoading);

Vue.config.productionTip = false

new Vue({
  vuetify,
  router,
  render: h => h(App)
}).$mount('#app')
