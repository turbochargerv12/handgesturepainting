import Vue from 'vue';
import App from './App.vue';
import VueKonva from 'vue-konva';
import vuetify from './plugins/vuetify';
import router from './router';
import axios from 'axios'
// import vueElementLoading from 'vue-element-loading'
import ServerError from './components/Others/500Page'
import {WebCam} from 'vue-cam-vision'
import OwlCarousel from 'vue-owl-carousel'


Vue.component(WebCam.name, WebCam);
Vue.component('OwlCarousel',OwlCarousel);
Vue.use(VueKonva);
Vue.component('ServerError',ServerError); 
// Vue.component('VueElementLoading',vueElementLoading);

axios.defaults.baseURL="http://localhost:5000/"
Vue.prototype.baseURL="http://localhost:5000/"

Vue.config.productionTip = false

new Vue({
  vuetify,
  router,
  render: h => h(App)
}).$mount('#app')
