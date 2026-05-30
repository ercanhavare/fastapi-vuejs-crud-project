<script setup lang="ts">

import {ref, watch} from 'vue'
import { Hero } from './types';

/**
 * Props definition for the HeroModal component. It expects a hero object of type Hero or null to be passed as a prop from the parent component (App.vue). This allows the modal to be used for both creating a new hero (when hero is null) and editing an existing hero (when hero is not null).
 */
const props = defineProps<{
    hero: Hero | null
}>();

/**
 * State variables for the HeroModel component
 */
const age = ref<string>('');
const name = ref<string>('');
const secretName = ref<string>('');

/**
 * Emits the 'close' event to notify the parent component to close the modal
 */
const emits = defineEmits(['close', 'saved', 'error']);

/**
 * Watch for changes in the hero prop to populate the form fields when editing an existing hero. If the hero prop is null, it means we are creating a new hero, so we reset the form fields to empty values.
 */
watch(()=>props.hero, (h) => {
    if (h) {
        name.value = h.name;
        age.value = h.age ? h.age.toString() : '';
        secretName.value = h.secret_name || '';
    } else {
        name.value = '';
        age.value = '';
        secretName.value = '';
    }
}, { immediate: true })

/**
 * Saves the new hero data. In a real application, this would involve sending the data to the backend API.
 */
const save=async () => {
   const payload = {
       name: name.value,
       age: age.value ? parseInt(age.value) : undefined,
       secret_name: secretName.value || undefined
   }

   try {
    let response;

    /**
     * If the hero prop is not null, it means we are editing an existing hero, so we send a PUT request to update the hero. If the hero prop is null, it means we are creating a new hero, so we send a POST request to create the hero. After successfully creating a new hero, we emit the 'saved' event with the newly created hero data to notify the parent component to update the list of heroes.
     */
    if (props.hero) {
        response = await fetch(`http://localhost:8000/heroes/${props.hero.id}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(payload)
        });
    } else {
        response = await fetch('http://localhost:8000/heroes/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(payload)
        });
    }

    if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
    }

    const result = await response.json();
    emits('saved', result);
    emits('close');
   } catch (err: any) {
       emits('error', err.message || 'Failed to save hero.');
       console.error('Error saving hero:', err.message);
   }

}

</script>
<template>
    <div class="fixed inset-0 z-50 flex items-center justify-center bg-slate-900/50 p-4 backdrop-blur-sm">
        <div class="w-full max-w-xl rounded-[28px] bg-white p-8 shadow-2xl ring-1 ring-slate-200">

            <div class="mb-6 flex items-start justify-between gap-4">
                <div>
                    <div class="mb-3 flex h-12 w-12 items-center justify-center rounded-2xl bg-sky-500/10 text-sky-600">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="h-6 w-6">
                            <path d="M12 2a7 7 0 00-7 7v3c0 2.93 2.42 5.32 5.4 5.48a1 1 0 01.95.97V21h2v-2.55a1 1 0 01.95-.97A7.001 7.001 0 0019 12V9a7 7 0 00-7-7zm0 2a5 5 0 015 5v3a5 5 0 11-10 0V9a5 5 0 015-5z" />
                        </svg>
                    </div>
                    <h2 class="text-3xl font-semibold tracking-tight text-slate-900">{{ props.hero ? 'Edit Hero' : 'Add Hero' }}</h2>
                    <p class="mt-2 text-sm leading-6 text-slate-500">{{ props.hero ? 'Update the hero details and save changes.' : 'Create a new hero profile and add it to the list.' }}</p>
                </div>
                <button class="h-11 w-11 rounded-2xl border border-slate-200 bg-slate-50 text-slate-500 transition hover:bg-slate-100" @click="emits('close')" aria-label="Close modal">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="h-5 w-5">
                        <path d="M18.3 5.71a1 1 0 00-1.42 0L12 10.59 7.12 5.7A1 1 0 105.7 7.12L10.59 12l-4.88 4.88a1 1 0 001.42 1.42L12 13.41l4.88 4.89a1 1 0 001.42-1.42L13.41 12l4.89-4.88a1 1 0 000-1.41z" />
                    </svg>
                </button>
            </div>

            <div class="space-y-4">
                <label class="block text-sm font-medium text-slate-700">
                    Hero Name
                    <input class="mt-2 w-full rounded-2xl border border-slate-200 bg-slate-50 px-4 py-3 text-slate-900 placeholder:text-slate-400 focus:border-sky-500 focus:outline-none focus:ring-2 focus:ring-sky-100" type="text" placeholder="Enter hero name" v-model="name" />
                </label>

                <label class="block text-sm font-medium text-slate-700">
                    Age
                    <input class="mt-2 w-full rounded-2xl border border-slate-200 bg-slate-50 px-4 py-3 text-slate-900 placeholder:text-slate-400 focus:border-sky-500 focus:outline-none focus:ring-2 focus:ring-sky-100" type="number" placeholder="Age (optional)" v-model="age" />
                </label>

                <label class="block text-sm font-medium text-slate-700">
                    Secret Name
                    <input class="mt-2 w-full rounded-2xl border border-slate-200 bg-slate-50 px-4 py-3 text-slate-900 placeholder:text-slate-400 focus:border-sky-500 focus:outline-none focus:ring-2 focus:ring-sky-100" type="text" placeholder="Enter secret name" v-model="secretName" />
                </label>
            </div>

            <div class="mt-6 flex flex-col gap-3 sm:flex-row sm:justify-end">
                <button class="rounded-2xl border border-slate-200 bg-white px-5 py-3 text-sm font-medium text-slate-700 transition hover:border-slate-300 hover:bg-slate-50" @click="emits('close')">Cancel</button>
                <button class="rounded-2xl bg-slate-900 px-5 py-3 text-sm font-semibold text-white transition hover:bg-slate-800" @click="save">{{ props.hero ? 'Update Hero' : 'Create Hero' }}</button>
            </div>
        </div>
    </div>
</template>