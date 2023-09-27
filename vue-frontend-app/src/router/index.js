import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import RegisterView from '../views/RegisterView.vue'
import NotFound from "../views/NotFound.vue"

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
    meta: {
      layout: "DashboardLayout",
    },
  },
  
  {
    path: '/login',
    name: 'login',
    component: LoginView,
    meta: {
      layout: "AuthLayout",
    },
  },
  {
    path: '/register',
    name: 'register',
    component: RegisterView,
    meta: {
      layout: "AuthLayout",
    },
  },
  {
    path: '/notfound',
    name: 'notfound',
    component: NotFound,
    meta: {
      layout: "FreeSpaceLayout",
    },
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
