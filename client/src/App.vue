<script setup lang="ts">

import {ref, onMounted} from 'vue'
import HeroModal from './components/HeroModal.vue';
import HeroCard from './components/HeroCard.vue';
import { Hero } from './components/types.js';

/**
 * State variables
 */
const loading = ref<boolean>(false);
const error = ref<string | null>(null);
const selectedHero = ref<Hero | null>(null);
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
 * handleDelete for removing a hero from the list. This function is called when a hero is deleted from the HeroCard component.
 */
const handleDelete = async (id: number) => {
  try {
    loading.value = true;
    const response = await fetch(`http://localhost:8000/heroes/${id}`, {
      method: 'DELETE'
    });
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
   heroes.value = heroes.value.filter(hero => hero.id !== id);
  } catch (err: any) {
    error.value = err.message;
    console.error('Error deleting hero:', error.value);
  } finally {
    loading.value = false;
  }
}


/**
 * handleSave for updating the hero list after a hero is created or updated. This function is called when a hero is saved from the HeroModal component.
 * @param hero 
 */
const handleSave = (hero: Hero) => {

  if (selectedHero.value) {
    const index = heroes.value.findIndex((h) => h.id === selectedHero.value?.id);

    if (index !== -1) {
      heroes.value[index] = hero;
    }
  } else {
    heroes.value.push(hero);
  }

  showModal.value = false;
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
      <button class="bg-indigo-700 text-white px-4 py-2 rounded shadow" v-on:click="()=>{ selectedHero = null; showModal = true; }">Add Hero</button>
    </header>

    <div class="grid grid-cols-1 sm:gid-cols-2 lg:grid-cols-3 gap-4">
      <HeroCard v-for="hero in heroes" v-bind:key="hero.id" :hero="hero" v-on:delete="handleDelete" v-on:edit="(h)=>{showModal = true; selectedHero = h}"/>
    </div>

    <HeroModal v-if="showModal" v-bind:hero="selectedHero" v-on:close="()=>{ showModal = false; selectedHero = null; }" v-on:saved="handleSave"/>
  </div>

</template>

<style scoped>
</style>