<script>
import axios from 'axios'
import { ref } from 'vue'

export default {
  setup() {
    const myData = ref(null)
    const message = ref('Loading data...')
    const movies = ref(null)
    const image = ref(null)

    async function fetchData(movies) {
      try {
        const response = await axios.get(`http://127.0.0.1:5000/api/movies/average_score?movies=${movies}`)
        if (response.status === 200) {
          myData.value = response.data.data
          image.value = "data:image/png;base64," + myData.value
          message.value = 'Data loaded successfully'
        } else {
          message.value = `Error: ${response.status}`
        }
      } catch (error) {
        message.value = 'Error loading data'
      } 
    }

    function onSubmit() {
      if (movies.value !== null) {
        fetchData(movies.value)
      }
    }


    return {
      myData,
      message,
      onSubmit,
      movies,
      image
    }
  }
}


</script>

<template>


<div class="flex justify-center">
  <form @submit.prevent="onSubmit" >   
    <label for="movies" class="mb-2 text-sm font-medium sr-only  dark:text-white">Movies</label>
    <div class="relative">
      <div class=" absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none ">
        <svg aria-hidden="true" class=" w-5 h-5 dark:text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
      </div>
      <input id="movies" class="block pr-20  p-4 pl-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50  dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-green-500 dark:focus:border-green-500" placeholder="Movies" required v-model="movies">
      <button type="submit" class="text-white  absolute right-2.5 bottom-2.5 bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-3 py-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Submit</button>
    </div>
    </form>
  </div>

  <div class="flex justify-center">
    <img v-if="myData" :src="image" alt="Image">
  </div>

</template>
