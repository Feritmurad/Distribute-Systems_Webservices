<script>
import axios from 'axios'
import { ref } from 'vue'

export default {
  setup() {
    const myData = ref(null)
    const message = ref('Loading data...')
    const movie = ref(null)

    async function fetchData(movie) {
      try {
        const response = await axios.get(`http://127.0.0.1:5000/api/movies/similar_actors?movie=${movie}`)
        if (response.status === 200) {
          myData.value = response.data.data.map(item => ({
            title: item.title,
            actors: item.actors
          }))
          message.value = 'Data loaded successfully'
        } else {
          message.value = `Error: ${response.status}`
        }
      } catch (error) {
        message.value = 'Error loading data'
      } 
    }


    function onSubmit() {
      if (movie.value !== null) {
        fetchData(movie.value)
      }
    }

    return {
      myData,
      message,
      movie,
      onSubmit,
    }
  }
}
</script>

<template>

<div class="flex justify-center">
  <form @submit.prevent="onSubmit">   
    <label for="movie" class="mb-2 text-sm font-medium  sr-only text-white">Movie</label>
    <div class="relative">
      <div class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
        <svg aria-hidden="true" class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
      </div>
      <input id="movie" class="block pr-20 p-4 pl-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50  bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-green-500 focus:border-green-500" placeholder="Movie" required v-model="movie">
      <button type="submit" class="text-white absolute right-2.5 bottom-2.5 bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-3 py-2 bg-blue-600 hover:bg-blue-700 focus:ring-blue-800">Submit</button>
    </div>
    </form>
  </div>



<div class="flex justify-center">
<div class="relative overflow-x-auto " >
    <table class=" text-sm text-left">
        <thead class="text-xs  uppercase   ">
            <tr>
                <th scope="col " class="px-6 py-3 text-white">
                    Rank
                </th>
                <th scope="col " class="px-6 py-3 text-white">
                    Movie
                </th>
                <th scope="col " class="px-6 py-3 text-white">
                    Similar actors
                </th>
            </tr>
        </thead>
        <tbody>
        <tr v-for="(item, index) in myData" :key="index" class="border-b">
          <th scope="row" class="px-6 py-4 font-medium whitespace-nowrap text-white">
            {{ index + 1 }}
          </th>
          <td class="px-6 py-4 font-medium whitespace-nowrap text-white">
            {{ item.title }}
          </td>
          <td class="px-6 py-4 font-medium whitespace-nowrap text-white">
            {{ item.actors }}
          </td>
        </tr>
      </tbody>
    </table>
</div>
</div>


</template>
