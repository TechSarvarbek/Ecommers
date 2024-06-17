<template>
  <div class="card w-full sm:w-72 bg-base-100 shadow-xl relative">
    <figure>
      <img :src="imageSrc" :alt="imageAlt" />
    </figure>
    <button class="btn m-2 absolute top-2 right-2" @click="handleBuyNow">
      <i class="mdi mdi-cart"></i>
    </button>
    
    <div class="card-body">
      <h2 class="card-title">{{ title }}</h2>
      <p>{{ truncateDescription(description) }}</p>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    imageSrc: {
      type: String,
      required: true,
    },
    imageAlt: {
      type: String,
      default: 'Product Image',
    },
    title: {
      type: String,
      required: true,
    },
    description: {
      type: String,
      required: true,
    },
  },
  methods: {
    handleBuyNow() {
      this.$emit('buy-now'); // Emitting an event to notify the parent component
    },
    truncateDescription(description) {
      if (description.length > 100) {
        return description.substring(0, 100) + '...';
      }
      return description;
    }
  },
};
</script>

<style scoped>
/* Scoped styles for the component */
</style>
