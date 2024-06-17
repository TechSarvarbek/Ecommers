<template>
  <div class="container mx-auto">
    <div class="grid grid-cols-2 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
      <Product
        v-for="product in products"
        :key="product.id"
        :image-src="product.imageSrc"
        :image-alt="product.imageAlt"
        :title="product.title"
        :description="product.description"
        :button-text="product.buttonText"
        :usb-settings="product.usbSettings"
        @buy-now="handleBuyNowEvent"
      />
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import Product from './Product.vue';

const products = ref([
  {
    id: 1,
    imageSrc: 'https://img.daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.jpg',
    imageAlt: 'Shoes',
    title: 'Shoes!',
    description: 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo',
  },
  {
    id: 2,
    imageSrc: 'https://img.daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.jpg',
    imageAlt: 'Shoes',
    title: 'Another Shoes!',
    description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
  },
  {
    id: 2,
    imageSrc: 'https://img.daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.jpg',
    imageAlt: 'Shoes',
    title: 'Another Shoes!',
    description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
  },
  {
    id: 2,
    imageSrc: 'https://img.daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.jpg',
    imageAlt: 'Shoes',
    title: 'Another Shoes!',
    description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
  },
  {
    id: 2,
    imageSrc: 'https://img.daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.jpg',
    imageAlt: 'Shoes',
    title: 'Another Shoes!',
    description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
  },
  {
    id: 2,
    imageSrc: 'https://img.daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.jpg',
    imageAlt: 'Shoes',
    title: 'Another Shoes!',
    description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
  },
  {
    id: 2,
    imageSrc: 'https://img.daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.jpg',
    imageAlt: 'Shoes',
    title: 'Another Shoes!',
    description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
  },
  {
    id: 2,
    imageSrc: 'https://img.daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.jpg',
    imageAlt: 'Shoes',
    title: 'Another Shoes!',
    description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
  },
  // Add more products as needed
]);

const handleBuyNowEvent = () => {
  alert('Buy Now button clicked!');
};
</script>

<style scoped>
/* Add any additional styling if needed */
</style>