import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

export default new Vuex.Store({
    state:{
        Color:"",
        // myRole:"",
        // isloggdin : !!localStorage.getItem("token")
    },
    mutations:{
        MyColor(state, item){
            state.Color = item
        },
        // UserName(state, item){
        //     state.myName = item
        // },
        // assignToken(state, item){
        //     localStorage.setItem("token",item)
        // },
    }
});