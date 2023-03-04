import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
    state:{
        Color:"",
    },
    mutations:{
        MyColor(state, item){
            state.Color = item
        },
    }
});