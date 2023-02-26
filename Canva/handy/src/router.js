import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)
let router = new Router({
    mode: "history",
    routes: [
        
        {
            path:'/',
            name:"Master",
            component: () => import('@/pages/MasteR'),
            meta: { requiresAuth: false},
            children:[      
                
                {
                    path:'/cam',
                    name:"Cam",
                    props:true,
                    component: () => import('@/components/WebCam'),
                    meta: { requiresAuth: false}
                },
                
            ]
            
        },
        {
            path:'/home',
            name:"Canvas",
            props:true,
            component: () => import('@/components/CanvaS'),
            meta: { requiresAuth: false}
        },
        {
            path:'/500',
            name:"ServerError",
            component: () => import('@/components/Others/500Page'),
            meta: { requiresAuth: false}
        },
        {
            path:'*',
            name:"404Page",
            component: () => import('@/components/Others/404Page'),
            meta: { requiresAuth: false}
        }
    ]
});
export default router;