import {createRouter, createWebHistory} from 'vue-router';
import Home from '../views/Home.vue';
import Login from '../views/Login.vue';
import Register from '../views/Register.vue';
import Dashboard from '../views/Dashboard.vue';
import Profile from '../views/Profile.vue';

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home,
        meta: {title: 'iFutureBD - Home'},
    },
    {
        path: '/login',
        name: 'Login',
        component: Login,
        meta: {title: 'iFutureBD - Login'},
    },
    {
        path: '/register',
        name: 'Register',
        component: Register,
        meta: {title: 'iFutureBD - Register'},
    },
    {
        path: '/dashboard',
        name: 'Dashboard',
        component: Dashboard,
        meta: {title: 'iFutureBD - Dashboard'},
        beforeEnter: (to, from, next) => {
            const accessToken = localStorage.getItem('access_token');
            if (accessToken) {
                next();  // Allow access to the dashboard if access token exists
            } else {
                next('/login');  // Redirect to login if access token is missing
            }
        }
    },
    {
        path: '/profile',
        name: 'Profile',
        component: Profile,  // Add Profile route
        meta: {title: 'iFutureBD - Profile'},
        beforeEnter: (to, from, next) => {
            const accessToken = localStorage.getItem('access_token');
            if (accessToken) {
                next();
            } else {
                next('/login');
            }
        }
    },
    {
        path: "/profile/update",
        name: "ProfileUpdate",
        component: () => import("@/views/ProfileUpdate.vue"),
    },

];

const router = createRouter({
    history: createWebHistory(),
    routes
});
router.beforeEach((to, from, next) => {
    // Check if the route has a meta title and set it
    if (to.meta.title) {
        document.title = to.meta.title;
    }
    next();
});


export default router;
