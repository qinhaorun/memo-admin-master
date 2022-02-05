import { createRouter, createWebHistory } from "vue-router";
import AvatarUpload from "./pages/AvatarUpload.vue";

export const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      redirect: '/avatar-upload'
    },
    {
      path: "/avatar-upload",
      component: AvatarUpload,
    },


  ],
});

 
