<script setup lang="ts">

import {ref} from 'vue'

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
        response = await fetch('http://localhost:8000/heroes/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(payload)
        })
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`)
        }
        const result = await response.json();
       emits('saved', result);
   } catch (err: any) {
       console.error('Error creating hero:', err.message)
   }

}

</script>
<template>
    <div class="fixed inset-0 bg-black opacity-30 flex items-center justify-center z-50">
        <div class="bg-white rounded-xl p-6 w-full max-w-md shadow-lg space-y-4">

            <h2 class="text-2xl font-bold mb-2 text-indigo-700">Add Hero</h2>

            <input class="w-full p-2 border rounded-lg" type="text" placeholder="Hero Name" v-model="name"/>

            <input class="w-full p-2 border rounded-lg" type="number" placeholder="Age (optional)" v-model="age"/>

            <input class="w-full p-2 border rounded-lg" type="text" placeholder="Secret Name" v-model="secretName"/>

            <div class="flex justify-end gap-3 pt-2">
                <button class="px-4 py-2 bg-gray-300 rounded hover:bg-gray-400" @click="emits('close')">Cancel</button>
                 <button class="px-4 py-2 bg-indigo-700 text-white rounded hover:bg-indigo-800" @click="save">Create</button>
            </div>
        </div>
    </div>
</template>