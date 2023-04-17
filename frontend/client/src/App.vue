<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import navbar from './components/NavbarComponent.vue'
</script>

<template>

<div class="grid grid-cols-1 gap-4 ">
  <div class="mb-20"><navbar></navbar>  </div>
  <div ><RouterView/></div>
</div>

  
</template>