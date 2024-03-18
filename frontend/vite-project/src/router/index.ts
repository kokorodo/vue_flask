import { createRouter, createWebHashHistory } from 'vue-router'
import HelloWorld from '../components/HelloWorld.vue'
import UserList from '../components/UserList.vue'
import UserForm from '../components/UserForm.vue'


const routes = [
  {
    path: '/',
    redirect: 'userList'
  },
  {
    name: 'helloWorld',
    path: '/helloWorld',
    meta: {
      title: 'HelloWorld'
    },
    component: HelloWorld,
    children: [

    ]
  },
  {
    name: 'userList',
    path: '/userList',
    meta: {
      title: '用户列表'
    },
    component: UserList,
    children: [

    ]
  },
  {
    name: 'userForm',
    path: '/userForm',
    meta: {
      title: '用户表单'
    },
    component: UserForm,
    children: [

    ]
  }
]
const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
