<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Navbar from './components/navbar/Navbar.vue'
import Footer from './components/Footer.vue'
</script>

<template>
  <header>
    <Navbar />
  </header>

  <RouterView />

  <Footer />
</template>

<style scoped>
</style>
