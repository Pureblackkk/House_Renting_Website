import Vue from 'vue'
import Router from 'vue-router'
// import Vue Component
import Login from '@/components/login'
import Basic from '@/components/basic'
import Map from '@/components/map'
import Host from '@/components/host/host'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/page',
      name: 'content',
      component: Basic
    },
    {
      path: '/map',
      name: 'map',
      component: Map
    },
    {
      path: '/',
      name: 'login',
      component: Login
    },
    {
      path: '/host',
      name: 'host',
      component: Host
    }
  ]
})
