import { createApp } from 'vue'
import './tailwind.css'
import App from './App.vue'

import Layui from '@layui/layui-vue'
import '@layui/layui-vue/lib/index.css'

import router from './router/index'


createApp(App).use(Layui).use(router).mount('#app')
