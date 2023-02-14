import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)
let router = new Router({
    mode:"history",
    routes: [
        
        {
            path: '/',
            name: "HomePage",
            component: () => import('./components/HelloWorld'),
            meta : {
                requiresAuth: false
            }
        },
        {
            path: '*',
            name: "404Page",
            component:()=>import('./components/Others/404Page'),
           
        },
        {
            path: '/ServerError',
            name: "ServerError",
            component:() => import('./components/Others/500Page'),
           
        },
        
    ]
});

// router.beforeEach((to,from,next) => {
//    if(to.matched.some(route => route.meta.requiresAuth == true) && !localStorage.getItem("token"))
//    {
//        next({name : 'LoginPage'});
//        return
//    }
//    if(to.matched.some(route => route.meta.requiresAuth == false) && localStorage.getItem("token"))
//    {
//        next({name : 'HomePage'});
//        return
//    }
//     next();
// });


export default router
