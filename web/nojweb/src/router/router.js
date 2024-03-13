import { createRouter, createWebHistory } from "vue-router";
import userLogin from '@/components/views/userLogin'
import home from '@/components/views/home'
import userReg from '@/components/views/userReg'

const router = createRouter({
    history: createWebHistory(),
    routes: [
    {
        meta: {
            title: '用户登录',
            activeTitle: '/user/login'
        },
        path: '/user/login', component: userLogin,
    }, 
    {
        meta: {
            title: '首页',
            activeTitle: '/'
        },
        path: '/', component: home,
    }, 
    {
        meta: {
            title: '用户注册',
            activeTitle: '/user/reg'
        },
        path: '/user/reg', component: userReg,
    }  ],
    caseSensitive: true
});

export default router;
