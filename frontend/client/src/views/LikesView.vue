<script>
import axios from 'axios'
import { ref } from 'vue'

export default {
  setup() {
    const myData = ref(null)
    const message = ref('Loading data...')
    const movielike = ref(null)
    const movieunlike = ref(null)

    async function fetchData() {
      try {
        const response = await axios.get(`http://127.0.0.1:5000/api/movies/likes`)
        if (response.status === 200) {
          myData.value = response.data.data.map(item => ({
            title: item.title
          }))
          message.value = 'Data loaded successfully'
        } else {
          message.value = `Error: ${response.status}`
        }
      } catch (error) {
        message.value = 'Error loading data'
      } 
    }

    async function postMovie(movielike) {
      try {
        const response = await axios.post(`http://127.0.0.1:5000/api/movies/likes?movie=${movielike}`)
        if (response.status === 200) {
          message.value = 'Movie liked successfully'
          fetchData()
        } else {
          message.value = `Error: ${response.status}`
        }
      } catch (error) {
        message.value = 'Error liking movie'
      } 
    }

    async function deleteMovie(movieunlike) {
      try {
        const response = await axios.delete(`http://127.0.0.1:5000/api/movies/likes?movie=${movieunlike}`)
        if (response.status === 200) {
          message.value = 'Movie unliked successfully'
          fetchData()
        } else {
          message.value = `Error: ${response.status}`
        }
      } catch (error) {
        message.value = 'Error unliking movie'
      } 
    }

    fetchData(10)
    function onSubmitGetandPost() {
      if (movielike.value !== null ) {
        postMovie(movielike.value)
      }
    }

    function onSubmitGetandDelete() {
      if (movieunlike.value !== null ) {
        deleteMovie(movieunlike.value)
      }
    }

    return {
      myData,
      message,
      movielike,
      movieunlike,
      onSubmitGetandDelete,
      onSubmitGetandPost
    }
  }
}
</script>

<template>


<div class="flex justify-center">
  <form @submit.prevent="onSubmitGetandPost">   
    <label for="movie-like" class="mb-2 text-sm font-medium  sr-only dark:text-white">MovieLike</label>
    <div class="relative">
      <div class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
        <svg aria-hidden="true" class="w-5 h-5 dark:text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
      </div>
      <input  id="movie-like" class="block pr-20 p-4 pl-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50  dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-green-500 dark:focus:border-green-500" placeholder="Movie" required v-model="movielike">
      <button type="submit" class="text-white absolute right-2.5 bottom-2.5 bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-3 py-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Like</button>
    </div>
  </form>
  <form @submit.prevent="onSubmitGetandDelete">   
    <label for="movie-unlike" class="mb-2 text-sm font-medium  sr-only dark:text-white">MovieUnlike</label>
    <div class="relative">
      <div class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
        <svg aria-hidden="true" class="w-5 h-5 dark:text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
      </div>
      <input  id="movie-unlike" class="block pr-20 p-4 pl-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50  dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-green-500 dark:focus:border-green-500" placeholder="Movie" required v-model="movieunlike">
      <button type="submit" class="text-white absolute right-2.5 bottom-2.5 bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-3 py-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Unlike</button>
    </div>
  </form>
</div>

<div class="flex justify-center">
<div class="relative overflow-x-auto " >
    <table class=" text-sm text-left">
        <thead class="text-xs  uppercase   ">
            <tr>
                <th scope="col " class="px-6 py-3 dark:text-white">
                    Rank
                </th>
                <th scope="col " class="px-6 py-3 dark:text-white">
                    Movie
                </th>
            </tr>
        </thead>
        <tbody>
        <tr v-for="(item, index) in myData" :key="index" class="border-b">
          <th scope="row" class="px-6 py-4 font-medium whitespace-nowrap dark:text-white">
            {{ index + 1 }}
          </th>
          <td class="px-6 py-4 font-medium whitespace-nowrap dark:text-white">
            {{ item.title }}
          </td>
        </tr>
      </tbody>
    </table>
</div>
</div>


</template>
