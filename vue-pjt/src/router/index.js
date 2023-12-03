import { createRouter, createWebHistory } from 'vue-router'
import ArticleView from '@/views/ArticleView.vue'
import DetailView from '@/views/DetailView.vue'
import CreateView from '@/views/CreateView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LogInView from '@/views/LogInView.vue'
import KakaoMapView from '@/views/KakaoMapView.vue'
import ExchangeView from '@/views/ExchangeView.vue'
import ProfileView from '@/views/ProfileView.vue'
import LogOutView from '@/views/LogOutView.vue'
import DepositView from '@/views/DepositView.vue'
import SavingView from '@/views/SavingView.vue'
import DetailDepositView from '@/views/DetailDepositView.vue'
import UpdateView from '@/views/UpdateView.vue'
import DetailSavingView from '@/views/DetailSavingView.vue'
import ProfileUpdateView from '@/views/ProfileUpdateView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/articles',
      name: 'ArticleView',
      component: ArticleView
    },
    {
      path: '/articles/:id',
      name: 'DetailView',
      component: DetailView
    },
    {
      path: '/create',
      name: 'CreateView',
      component: CreateView
    },
    {
      path: '/signup',
      name: 'SignUpView',
      component: SignUpView
    },
    {
      path: '/login',
      name: 'LogInView',
      component: LogInView
    },
    {
      path: '/Maps',
      name : 'Maps',
      component: KakaoMapView
    },
    {
      path: '/Exchange',
      name: 'Exchange',
      component: ExchangeView
    },
    {
      path: '/profile',
      name: 'Profile',
      component: ProfileView
    },
    {
      path: '/LogOut',
      name: 'LogOut',
      component: LogOutView
    },
    {
      path: '/Deposit',
      name: 'Deposit',
      component: DepositView
    },
    {
      path: '/Saving',
      name : 'Saving',
      component: SavingView
    },
    {
      path: '/DetailDeposit/:id',
      name: 'DetailDepositView',
      component: DetailDepositView,
      props: true
    },
    {
      path: '/articles/:id/update',
      name: 'UpdateView',
      component: UpdateView
    },
    {
      path: '/DetailSaving/:id',
      name: 'DetailSavingView',
      component: DetailSavingView
    },
    {
      path: '/ProfileUpdate',
      name : 'ProfileUpdateView',
      component: ProfileUpdateView,
    }
  ]
})

import { useCounterStore } from '@/stores/counter'

router.beforeEach((to, from) => {
  const store = useCounterStore()
  if((to.name === 'CreateView' || to.name === 'Profile')&& !store.isLogin) {
    window.alert('로그인 필요')
    return {name: 'LogInView'}
  }
  if ((to.name === 'SignUpView' || to.name === 'LogInView') && (store.isLogin)) {
    window.alert('이미 로그인 완료')
    return { name : 'ArticleView'}
  }
})


export default router
