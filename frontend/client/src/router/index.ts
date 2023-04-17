import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LikesView from '@/views/LikesView.vue'
import GenresView from '../views/GenresView.vue'
import ActorsView from '../views/ActorsView.vue'
import RuntimeView from '../views/RuntimeView.vue'
import AverageScoreViewVue from '@/views/AverageScoreView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/likes',
      name: 'likes',
      component: LikesView
    },
    {
      path: '/genres',
      name: 'genres',
      component: GenresView
    },
    {
      path: '/actors',
      name: 'actors',
      component: ActorsView
    },
    {
      path: '/runtime',
      name: 'runtime',
      component: RuntimeView
    },
    {
      path: '/average_score',
      name: 'average_score',
      component: AverageScoreViewVue
    },
  ]
})

export default router
