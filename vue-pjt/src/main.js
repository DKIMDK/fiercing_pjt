import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
import { createApp } from 'vue'
import { createPinia, defineStore } from 'pinia'
import App from './App.vue'
import router from './router'
import { Toast } from 'bootstrap'
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'

const app = createApp(App)
const pinia = createPinia()

pinia.use(piniaPluginPersistedstate)
app.use(pinia)
app.use(router)
app.provide('toast', Toast);

app.mount('#app')
