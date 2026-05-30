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
const emits = defineEmits(['close', 'saved']);

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
       console.error('Error saving hero:', err.message);
   }

}

</script>
<template>
    <div class="fixed inset-0 bg-black opacity-30 flex items-center justify-center z-50">
        <div class="bg-white rounded-xl p-6 w-full max-w-md shadow-lg space-y-4">

            <h2 class="text-2xl font-bold mb-2 text-indigo-700">{{ props.hero ? 'Edit Hero' : 'Add Hero' }}</h2>

            <input class="w-full p-2 border rounded-lg" type="text" placeholder="Hero Name" v-model="name"/>

            <input class="w-full p-2 border rounded-lg" type="number" placeholder="Age (optional)" v-model="age"/>

            <input class="w-full p-2 border rounded-lg" type="text" placeholder="Secret Name" v-model="secretName"/>

            <div class="flex justify-end gap-3 pt-2">
                <button class="px-4 py-2 bg-gray-300 rounded hover:bg-gray-400" @click="emits('close')">Cancel</button>
                 <button class="px-4 py-2 bg-indigo-700 text-white rounded hover:bg-indigo-800" @click="save">{{ props.hero ? 'Update' : 'Create' }}</button>
            </div>
        </div>
    </div>
</template>