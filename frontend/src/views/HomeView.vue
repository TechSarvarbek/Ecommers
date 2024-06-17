<template>
  <div>
      <div class="container mx-auto md:px-16 px-2 py-6">
        <Banner />
      </div>
      <div class="container mx-auto md:px-16 px-2 py-6">
        <ProductList />
      </div>
  </div>

</template>

<script>
import Banner from '../components/Banner.vue'
import ProductList from '../components/ProductList.vue'

export default {
  name: 'App',
  components: {
    Banner,
    ProductList
  },
}
</script>

<style>
/* Add any additional custom styles here */
</style>