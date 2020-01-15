import Vue from 'vue'
import VueRouter from 'vue-router'
import About from '../views/About'
import Main from '../views/Main'
import Login from '../components/auth/Login'
import Register from '../components/auth/Register'
import ReportDetail from '../views/ReportDetail'
import Logout from '../components/auth/Logout'
import Profile from '../views/Profile'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'main',
    component: Main,
    meta: {requiresAuth: true}
  },
  {
    // path: '/report',
    path: '/report/:id',
    name: 'report',
    component: ReportDetail,
    meta: {requiresAuth: true}
  },
  {
    path: '/about',
    name: 'about',
    component: About
  },
  {
    path: '/login',
    name: 'login',
    component: Login,
    meta: {requiresVisitor: true}
  },
  {
    path: '/register',
    name: 'register',
    component: Register,
    meta: {requiresVisitor: true}
  },
  {
    path: '/logout',
    name: 'logout',
    component: Logout
  },
  {
    path: '/profile',
    name: 'profile',
    component: Profile,
    meta: {requiresAuth: true}
  },
]

const router = new VueRouter({
  routes,
  mode: 'history'
})

export default router