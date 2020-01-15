import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'
import vuetify from './plugins/vuetify';

Vue.config.productionTip = false

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    // this route requires auth, check if logged in
    // if not, redirect to login page.
    if (!store.getters.loggedIn) {
      next({name: 'login'})
    } else {
      next()
    }
  } else if (to.matched.some(record => record.meta.requiresVisitor)) {
    // if and authenticated user tries to visit login or register pages
    // then redirect to reports page.
    if (store.getters.loggedIn) {
      next({name: 'main'})
    } else {
      next()
    }
  }else {
    next() // make sure to always call next()!
  }
})

new Vue({
  store,
  router,
  vuetify,
  render: h => h(App)
}).$mount('#app')
