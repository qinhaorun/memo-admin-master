<script setup lang="ts">
import { NConfigProvider, NMessageProvider, NGlobalStyle } from "naive-ui";
import App from "./App.vue";
</script>

<template>
  <NConfigProvider>
    <NMessageProvider>
      <App />
      <NGlobalStyle />
    </NMessageProvider>
  </NConfigProvider>
</template>
