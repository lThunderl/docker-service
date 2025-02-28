import { createRouter, createWebHistory } from 'vue-router'
import Services from '../components/Services.vue';
import Tasks from '../components/Tasks.vue';
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Services',
      component: Services,
    },
	{
      path: '/tasks',
      name: 'Tasks',
      component: Tasks,
    },
  ],
})

export default router
