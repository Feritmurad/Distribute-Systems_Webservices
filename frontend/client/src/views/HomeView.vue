<script>
import axios from 'axios'
import { ref } from 'vue'

export default {
  setup() {
    const myData = ref(null)
    const message = ref('Loading data...')
    const amount = ref(null)
    const MovieDelete = ref(null)

    async function fetchData(amount) {
      try {
        const response = await axios.get(`http://127.0.0.1:5000/api/movies?limit=${amount}`)
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

    async function deleteMovie(MovieDelete) {
      try {
        const response = await axios.delete(`http://127.0.0.1:5000/api/movies/${MovieDelete}`)
        if (response.status === 200) {
          message.value = 'Movie unliked successfully'
        } else {
          message.value = `Error: ${response.status}`
        }
      } catch (error) {
        message.value = 'Error unliking movie'
      } 
    }


    function onSubmit() {
      if (amount.value !== null && !isNaN(amount.value)) {
        fetchData(amount.value)
      }
    }

    function onSubmitDelete() {
      if (MovieDelete.value !== null) {
        deleteMovie(MovieDelete.value)
      }
    }

    return {
      myData,
      message,
      amount,
      onSubmit,
      MovieDelete,
      onSubmitDelete
    }
  }
}
</script>

<template>


<div class="flex justify-center">
  <form @submit.prevent="onSubmit">   
    <label for="amount" class="mb-2 text-sm font-medium  sr-only text-white">Amount</label>
    <div class="relative">
      <div class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
        <svg aria-hidden="true" class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
      </div>
      <input id="amount" class="block pr-20 p-4 pl-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50  bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-green-500 focus:border-green-500" placeholder="Amount" required v-model="amount">
      <button type="submit" class="text-white absolute right-2.5 bottom-2.5 bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-3 py-2 bg-blue-600 hover:bg-blue-700 focus:ring-blue-800">Submit</button>
    </div>
    </form>
    <form @submit.prevent="onSubmitDelete">   
    <label for="movie-delete" class="mb-2 text-sm font-medium  sr-only text-white">MovieDelete</label>
    <div class="relative">
      <div class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
        <svg aria-hidden="true" class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
      </div>
      <input  id="movie-delete" class="block pr-20 p-4 pl-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50  bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-green-500 focus:border-green-500" placeholder="Movie" required v-model="MovieDelete">
      <button type="submit" class="text-white absolute right-2.5 bottom-2.5 bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-3 py-2 bg-blue-600 hover:bg-blue-700 focus:ring-blue-800">Delete</button>
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
            </tr>
        </thead>
        <tbody>
        <tr v-for="(item, index) in myData" :key="index" class="border-b">
          <th scope="row" class="px-6 py-4 font-medium whitespace-nowrap text-white white-text">
            {{ index + 1 }}
          </th>
          <td class="px-6 py-4 font-medium whitespace-nowrap text-white">
            {{ item.title }}
          </td>
        </tr>
      </tbody>
    </table>
</div>
</div>


</template>
