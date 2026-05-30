<script setup lang="ts">

import {ref, onMounted} from 'vue'
import HeroModal from './components/HeroModal.vue';
import HeroCard from './components/HeroCard.vue';
import ConfirmModal from './components/ConfirmModal.vue';
import ToastContainer from './components/ToastContainer.vue';
import { Hero } from './components/types.js';

/**
 * State variables
 */
const loading = ref<boolean>(false);
const error = ref<string | null>(null);
const toasts = ref<Array<{ id: number; message: string; variant?: 'success' | 'error' | 'info' }>>([]);
const selectedHero = ref<Hero | null>(null);
const showModal = ref<boolean>(false);
const showDeleteConfirm = ref<boolean>(false);
const heroToDelete = ref<number | null>(null);
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
    addToast(error.value ?? 'Failed to load heroes.', 'error');
  } finally {
    loading.value = false;
  }
}

/**
 * handleDelete for removing a hero from the list. This function is called when a hero is deleted from the HeroCard component.
 */
const requestDelete = (id: number) => {
  heroToDelete.value = id;
  showDeleteConfirm.value = true;
}

const cancelDelete = () => {
  heroToDelete.value = null;
  showDeleteConfirm.value = false;
}

const addToast = (message: string, variant: 'success' | 'error' | 'info' = 'success') => {
  const id = Date.now() + Math.floor(Math.random() * 1000);
  toasts.value.push({ id, message, variant });
  setTimeout(() => { removeToast(id); }, 3000);
}

const removeToast = (id: number) => {
  toasts.value = toasts.value.filter((toast) => toast.id !== id);
}

const handleDelete = async () => {
  if (!heroToDelete.value) {
    return;
  }

  try {
    loading.value = true;
    const response = await fetch(`http://localhost:8000/heroes/${heroToDelete.value}`, {
      method: 'DELETE'
    });
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    heroes.value = heroes.value.filter(hero => hero.id !== heroToDelete.value);
    addToast('Hero successfully deleted.', 'success');
  } catch (err: any) {
    error.value = err.message;
    console.error('Error deleting hero:', error.value);
    addToast('Failed to delete hero.', 'error');
  } finally {
    loading.value = false;
    cancelDelete();
  }
}


/**
 * handleSave for updating the hero list after a hero is created or updated. This function is called when a hero is saved from the HeroModal component.
 * @param hero 
 */
const handleError = (message: string) => {
  addToast(message, 'error');
}

const handleSave = (hero: Hero) => {

  if (selectedHero.value) {
    const index = heroes.value.findIndex((h) => h.id === selectedHero.value?.id);

    if (index !== -1) {
      heroes.value[index] = hero;
    }
    addToast('Hero successfully updated.', 'success');
  } else {
    heroes.value.push(hero);
    addToast('Hero successfully added.', 'success');
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
  <div class="min-h-screen bg-slate-100 py-10">
    <div class="mx-auto max-w-6xl px-4">
      <header class="mb-8 rounded-[28px] bg-white p-6 shadow-sm ring-1 ring-slate-200 sm:flex sm:items-center sm:justify-between">
        <div>
          <p class="text-sm font-semibold uppercase tracking-[0.24em] text-sky-600">Hero Management</p>
          <h1 class="mt-2 text-4xl font-semibold tracking-tight text-slate-900">Hero's Journey</h1>
          <p class="mt-3 max-w-2xl text-sm leading-6 text-slate-600">Create, edit and manage your heroes with a clean and polished interface.</p>
        </div>
        <button class="mt-6 inline-flex items-center justify-center gap-2 rounded-2xl bg-sky-600 px-5 py-3 text-sm font-semibold text-white shadow-sm transition hover:bg-sky-700 sm:mt-0" v-on:click="()=>{ selectedHero = null; showModal = true; }">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="h-4 w-4">
            <path d="M12 5v14m7-7H5" stroke="currentColor" stroke-width="2" stroke-linecap="round" />
          </svg>
          Add Hero
        </button>
      </header>
      <ToastContainer :toasts="toasts" @dismiss="removeToast" />

      <div v-if="!loading && heroes.length === 0" class="rounded-3xl border border-dashed border-slate-200 bg-white p-10 text-center text-slate-600 shadow-sm">
        <p class="text-lg font-semibold text-slate-900">No heroes found yet</p>
        <p class="mt-2 text-sm leading-6">Click the “Add Hero” button to create a new hero profile.</p>
      </div>

      <div v-else class="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3">
        <HeroCard v-for="hero in heroes" v-bind:key="hero.id" :hero="hero" v-on:delete="requestDelete" v-on:edit="(h)=>{showModal = true; selectedHero = h}"/>
      </div>

      <HeroModal v-if="showModal" v-bind:hero="selectedHero" v-on:close="()=>{ showModal = false; selectedHero = null; }" v-on:saved="handleSave" v-on:error="handleError"/>
      <ConfirmModal v-if="showDeleteConfirm" title="Do you want to delete this hero?" description="This action cannot be undone. If you continue, the hero will be permanently removed." confirmText="Delete" cancelText="Cancel" v-on:confirm="handleDelete" v-on:close="cancelDelete" />
    </div>
  </div>

</template>

<style scoped>
</style>