<template>
    <div class="p-4 rounded-lg shadow border">
        <div class="h2 text-lx font-semibold">{{ hero.name }}</div>
        <p class="text-sm text-gray-600">Secret Name: {{ hero.secret_name }}</p>
         <p class="text-sm text-gray-600">Age: {{ hero.age }}</p>

            <div class="flex gap-2 mt-2">
                <button class="bg-blue-400 text-white px-3 py-1 rounded hover:bg-blue-600" v-on:click="()=>{emits('edit', hero.id)}">Edit</button>
                <button class="bg-red-400 text-white px-3 py-1 rounded hover:bg-red-600" v-on:click="()=>{emits('delete', hero.id)}">Delete</button>
            </div>
    </div>
</template>

<script setup lang="ts">
import { Hero } from './types.js';

/**
 * Props definition for the HeroCard component. It expects a hero object of type Hero to be passed as a prop from the parent component (App.vue).
 */
defineProps<{
    hero: Hero
}>()

/**
 * Emitting events for edit and delete actions. The component will emit 'edit' and 'delete' events with the hero's id when the respective buttons are clicked. The parent component (App.vue) will listen for these events to handle the editing and deleting of heroes.
 */
const emits = defineEmits(['edit', 'delete']);
</script>
