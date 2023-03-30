import { createRouter, createWebHistory } from 'vue-router'
import HomePage from './components/HomePage.vue'
import TestPage from './components/TestPage.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomePage,
  },
  {
    path: '/test',
    name: 'test',
    component: TestPage,
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
