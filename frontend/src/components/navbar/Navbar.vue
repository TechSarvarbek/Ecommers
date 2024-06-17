<template>
  <nav class="bg-white">
    <div class="container mx-auto px-4 flex justify-between items-center py-3 md:px-12 px-10">
      <div class="flex items-center md:w-[50%] w-[75%]">
        <img src="/logo.png" alt="Logo" class="w-14">
        <input
          type="text"
          placeholder="Что ты ищешь?"
          class="ml-4 p-2 pl-5 bg-gray-100 rounded-3xl w-[80%]  focus:outline-none font-sans"
        >
      </div>
      <div class="flex items-center space-x-4">
        <button class="text-gray-700 hover:text-blue-500 hidden sm:inline">корзина</button>
        <button class="text-gray-700 hover:text-blue-500 hidden sm:inline">Войти</button>
        <button class="bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600">Регистрация</button>
        <button
          class="text-gray-700 hover:text-blue-500 sm:hidden"
          @click="toggleMobileMenu"
        >
          ☰
        </button>
      </div>
    </div>
    <div
      class="bg-white sm:hidden"
      :class="{ 'block': isMobileMenuOpen, 'hidden': !isMobileMenuOpen }"
    >
      <!-- Mobile menu content goes here -->
      <button class="block mx-auto w-full hover:bg-blue-500 hover:text-white text-gray-700 hover:text-blue-500 py-2 px-4">Войти</button>
      <button class="block mx-auto w-full hover:bg-blue-500 hover:text-white text-gray-700 hover:text-blue-500 py-2 px-4">корзина</button>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'nav',
  data() {
    return {
      isMobileMenuOpen: false,
    }
  },
  methods: {
    toggleMobileMenu() {
      this.isMobileMenuOpen = !this.isMobileMenuOpen;
    },
  },
}
</script>