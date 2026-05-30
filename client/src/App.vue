<script setup lang="ts">

import {ref, onMounted} from 'vue'
import HeroModel from './components/HeroModel.vue';

/**
 * Hero interface representing the structure of a hero object
 */
interface Hero {
  id: number;
  name: string;
  age?: number;
  secret_name?: string;
}

/**
 * State variables
 */
const loading = ref<boolean>(false);
const error = ref<string | null>(null);
const showModal = ref<boolean>(false);
const heroes = ref<Hero[]>([]);

/**
 * Fetch heroes from the backend API
 */
const fetchHeroes = async () => {
  loading.value = true;
  try {
    const response = await fetch('http://localhost:8000/heroes/?offset=0&limit=100')
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`)
    }
    heroes.value = await response.json();
  } catch (err: any) {
    error.value = err.message;
    console.error('Error fetching heroes:', error.value)
  } finally {
    loading.value = false;
  }
}

/**
 * Fetch heroes when the component is mounted
 */
onMounted(() => {
  fetchHeroes();
})
</script>

<template>
  <div class="p-6 mx-w-4xl mx">
    <header class="flex justify-between items-center mb-6">
      <h1 class="text-3xl font-bold text-indigo-700"> Hero's Journey</h1>
      <button class="bg-indigo-700 text-white px-4 py-2 rounded shadow" v-on:click="()=>{showModal = true}">Add Hero</button>
    </header>

    <div class="grid grid-cols-1 sm:gid-cols-2 lg:grid-cols-3 gap-4">
      <div v-for="hero in heroes" v-bind:key="hero.id">{{ hero.name }}</div>
    </div>

    <HeroModel v-if="showModal" v-on:close="()=>{showModal = false}"/>
  </div>

</template>

<style scoped>
</style>