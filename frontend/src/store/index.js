import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import jwt from 'jsonwebtoken'
import router from '../router'

Vue.use(Vuex)

const SERVER = 'http://localhost:8000/api/v1'

export default new Vuex.Store({
  state: {
    reports: [],
    token: sessionStorage.getItem('token') || null,
    profile: {}
  },
  getters: {
    loggedIn(state) {
      return state.token !== null
    },
    reports(state) {
      return state.reports
    }
  },
  mutations: {
    clearProfile(state) {
      state.profile = {}
    },
    deleteToken(state) {
      state.token = null
    },
    getProfile(state, profile) {
      state.profile = profile
    },
    getReports(state, reports) {
      state.reports = reports
    },
    obtainToken(state, token) {
      state.token = token
    }
  },
  actions: {
    clearProfile(context) {
      context.commit('clearProfile')
    },
    deleteToken(context) {
      if(context.getters.loggedIn) {
        return new Promise((resolve, reject) => {
          axios.post(`${SERVER}/rest-auth/logout/`)
            .then(res => {
              sessionStorage.removeItem('token')
              context.commit('deleteToken')
              resolve(res)
            })
            .catch(err => {
              sessionStorage.removeItem('token')  // removes the token if it's invalid
              context.commit('deleteToken')
              reject(err)
          })
        })
      }
    },
    getProfile(context) {
      let headers = {headers: {'Authorization': `JWT ${context.state.token}`}}
      axios.get(`${SERVER}/user`, headers)
        .then(res => {
          const profile = res.data
          context.commit('getProfile', profile)
        })
        .catch(err => {
          context.commit('clearProfile')
          window.console.log(err)
        })
    },
    getReports(context) {
      let headers = {headers: {'Authorization': `JWT ${context.state.token}`}}
      return new Promise((resolve, reject) => {
        axios.get(`${SERVER}`, headers)
        .then(res => {
          const reports = res.data
          context.commit('getReports', reports)
          resolve(res)
        })
        .catch(err => {
          window.console.log(err)
          reject(err)
        })
      })

    },
    obtainToken(context, credentials)  {
      return new Promise((resolve, reject) => {
        axios.post(`${SERVER}/api-token-auth/`, {
          username: credentials.username,
          password: credentials.password,
        })
          .then(res => {
            const token = res.data.token
            sessionStorage.setItem('token', token)
            context.commit('obtainToken', token)
            resolve(res)
          })
          .catch(err => {
            reject(err)
        })
      })     
    },
    checkToken(context) {
      // Check time for token to expire
      let token = context.state.token
      if(token) {
        const expirationTime = jwt.decode(token, {complete: true}).payload.exp
        const currentTime = new Date().getTime()/1000
        const minutesToExpire = (expirationTime - currentTime)/60
        window.console.log('minutesToExpire', minutesToExpire)
        // Refresh Token
        if(minutesToExpire <= 0) {
          context.commit('clearProfile')
          context.commit('deleteToken')
          router.push({name: 'login'})
        } else if (minutesToExpire < 2) {
          let headers = {"Content-Type": "application/json"}
          let data = {"token": token}
          axios.post(`${SERVER}/api-token-refresh/`, data, {headers})
            .then(res => {
              token = res.data.token
              sessionStorage.setItem('token', token)
              context.commit('obtainToken', token)
              window.console.log(res)
            })
            .catch(err => {
              window.console.log(err)
            })
        }
      }
    },
    registration(context, data) {
      return new Promise((resolve, reject) => {
        axios.post(`${SERVER}/rest-auth/registration/`, {
          username: data.username,
          email: data.email,
          password1: data.password,
          password2: data.password,
        })
          .then(res => {
            resolve(res)
          })
          .catch(err => {
            reject(err)
        })
      })
    }
  }
})