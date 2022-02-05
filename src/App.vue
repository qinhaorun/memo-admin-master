<script setup lang="ts">
import { RouterView, useRoute, useRouter } from "vue-router";
import {
  NLayout,
  NLayoutSider,
  NMenu,
  NH3,
  NLayoutHeader,
  NIcon,
  MenuOption,
} from "naive-ui";
import { ArrowUpload16Regular } from "@vicons/fluent";
import { h } from "vue";


const menuData: MenuOption[] = [

  {
    label: " Avatar Upload",
    key: "/avatar-upload",
    // icon: () => h(NIcon, null, { default: () => h(ArrowUpload16Regular) }),
  },

];

const router = useRouter();

const route = useRoute();
</script>

<template>
  <NLayoutHeader
    style="padding: 0 32px; height: 64px; display: flex; align-items: center"
    bordered
  >
    <NH3 style="padding: 0; margin: 0">Memo Admin</NH3>
  </NLayoutHeader>
  <NLayout position="absolute" class="app" has-sider style="top: 64px">
    <NLayoutSider class="app-sider" bordered>
      <NMenu
        :options="menuData"
        :value="route.fullPath"
        @update-value="(value) => router.push(value)"
      />
    </NLayoutSider>
    <NLayout class="app-main" embedded>
      <RouterView />
    </NLayout>
  </NLayout>
</template>

<style>
body {
  overflow: hidden;
}

.app-sider {
  height: 100%;
}

.app-main {
  height: 100%;
  padding: 24px 32px;
}
</style>
