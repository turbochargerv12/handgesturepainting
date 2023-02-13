import Vue from 'vue'
import Vuex from 'vuex'
//import router from "./router"
Vue.use(Vuex);

export default new Vuex.Store({
    state:{
        myName:"",
        myRole:"",
        isloggdin : !!localStorage.getItem("token")
    },
    mutations:{
        UserRole(state, item){
            state.myRole = item
        },
        UserName(state, item){
            state.myName = item
        },
        assignToken(state, item){
            localStorage.setItem("token",item)
        },
    }
});