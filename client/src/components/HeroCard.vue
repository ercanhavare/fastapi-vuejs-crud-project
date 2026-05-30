<template>
    <div class="bg-white rounded-3xl border border-slate-200 p-6 shadow-sm transition-shadow duration-200 hover:shadow-lg">
        <div class="flex items-center gap-3 pb-4 border-b border-slate-200">
            <div class="flex h-12 w-12 items-center justify-center rounded-2xl bg-sky-500/10 text-sky-600">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="h-6 w-6">
                    <path d="M12 12a4 4 0 100-8 4 4 0 000 8zm0 2c-3.33 0-10 1.67-10 5v3h20v-3c0-3.33-6.67-5-10-5z" />
                </svg>
            </div>
            <div>
                <div class="text-xl font-semibold text-slate-900">{{ hero.name }}</div>
                <div class="text-sm text-slate-500">Hero profile</div>
            </div>
        </div>

        <div class="mt-5 space-y-4 text-sm text-slate-600">
            <div class="flex items-center gap-2 rounded-2xl bg-slate-50 p-3">
                <div class="flex h-8 w-8 items-center justify-center rounded-2xl bg-slate-200 text-slate-700">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="h-4 w-4">
                        <path d="M12 12a4 4 0 100-8 4 4 0 000 8zm6-4a6 6 0 11-12 0 6 6 0 0112 0z" />
                    </svg>
                </div>
                <div><span class="font-medium text-slate-800">Secret Name:</span> {{ hero.secret_name }}</div>
            </div>
            <div class="flex items-center gap-2 rounded-2xl bg-slate-50 p-3">
                <div class="flex h-8 w-8 items-center justify-center rounded-2xl bg-slate-200 text-slate-700">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="h-4 w-4">
                        <path d="M12 2a10 10 0 100 20 10 10 0 000-20zm1 14.5h-2V12h2v4.5zm0-6.5h-2V7h2v3z" />
                    </svg>
                </div>
                <div><span class="font-medium text-slate-800">Age:</span> {{ hero.age ?? 'N/A' }}</div>
            </div>
        </div>

        <div class="flex flex-wrap gap-3 mt-6">
            <button class="inline-flex items-center justify-center gap-2 rounded-2xl bg-sky-600 px-4 py-2 text-sm font-medium text-white shadow-sm transition hover:bg-sky-700" v-on:click="()=>{emits('edit', hero)}">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="h-4 w-4">
                    <path d="M5 20h14v-2H5v2zm4.41-11.41l1.17 1.17L7 14.34V16h1.66l3.58-3.58 1.17 1.17L10 17.17 5.83 13 9.41 9.59z" />
                </svg>
                Edit
            </button>
            <button class="inline-flex items-center justify-center gap-2 rounded-2xl bg-rose-600 px-4 py-2 text-sm font-medium text-white shadow-sm transition hover:bg-rose-700" v-on:click="()=>{emits('delete', hero.id)}">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="h-4 w-4">
                    <path d="M9 3h6v2H9V3zm-2 4h10l-1 12H8L7 7zm3 2v8h2V9H10z" />
                </svg>
                Delete
            </button>
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
