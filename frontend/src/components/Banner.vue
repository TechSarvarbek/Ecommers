<template>
  <div class="carousel rounded-xl w-full">
    <div v-for="(slide, index) in slides" :key="slide.id" :id="'slide' + (index + 1)" class="carousel-item relative w-full">
      <img :src="slide.src" class="w-full rounded-xl h-66" />
      <div class="absolute inset-0 flex flex-col justify-center items-center bg-black bg-opacity-50 text-white pb-10 pt-5 text-center">
        <h2 class="text-xl sm:text-2xl md:text-3xl lg:text-4xl mb-2 mt-5">{{ slide.title }}</h2>
        <p class="mb-4 text-sm sm:text-base md:text-lg lg:text-xl w-[75%]">{{ slide.description }}</p>
        <a :href="slide.link" class="bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600">{{ slide.buttonText }}</a>
      </div>
      <div class="absolute flex justify-between transform -translate-y-1/2 left-5 right-5 top-1/2">
        <a :href="'#slide' + (index === 0 ? slides.length : index)" class="btn btn-circle">❮</a> 
        <a :href="'#slide' + (index === slides.length - 1 ? 1 : index + 2)" class="btn btn-circle">❯</a>
      </div>
    </div>
  </div>
</template>


<script>
export default {
  data() {
    return {
      slides: [
        {
          id: 1,
          src: "https://img.daisyui.com/images/stock/photo-1625726411847-8cbb60cc71e6.jpg",
          title: "Slide 1 Title",
          description: "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo",
          link: "#",
          buttonText: "Learn More"
        },
        {
          id: 2,
          src: "https://img.daisyui.com/images/stock/photo-1609621838510-5ad474b7d25d.jpg",
          title: "Slide 2 Title",
          description: "This is the description for slide 2.",
          link: "#",
          buttonText: "Learn More"
        },
        {
          id: 3,
          src: "https://img.daisyui.com/images/stock/photo-1414694762283-acccc27bca85.jpg",
          title: "Slide 3 Title",
          description: "This is the description for slide 3.",
          link: "#",
          buttonText: "Learn More"
        },
        {
          id: 4,
          src: "https://img.daisyui.com/images/stock/photo-1665553365602-b2fb8e5d1707.jpg",
          title: "Slide 4 Title",
          description: "This is the description for slide 4.",
          link: "#",
          buttonText: "Learn More"
        }
      ]
    };
  }
};
</script>
