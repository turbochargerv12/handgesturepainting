import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

export default new Vuex.Store({
    state:{
        picker:"",
        // myRole:"",
        // isloggdin : !!localStorage.getItem("token")
    },
    mutations:{
        // UserRole(state, item){
        //     state.myRole = item
        // },
        // UserName(state, item){
        //     state.myName = item
        // },
        // assignToken(state, item){
        //     localStorage.setItem("token",item)
        // },
    }
});