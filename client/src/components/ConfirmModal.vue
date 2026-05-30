<script setup lang="ts">
const props = defineProps<{
  title: string
  description: string
  confirmText?: string
  cancelText?: string
}>()

const emits = defineEmits(['confirm', 'close'])
</script>

<template>
  <div class="fixed inset-0 z-50 flex items-center justify-center bg-slate-900/50 p-4 backdrop-blur-sm">
    <div class="w-full max-w-md rounded-[28px] bg-white p-6 shadow-2xl ring-1 ring-slate-200">
      <div class="mb-6 flex items-start justify-between gap-4">
        <div>
          <p class="text-sm font-semibold uppercase tracking-[0.24em] text-rose-600">Confirm Delete</p>
          <h2 class="mt-3 text-2xl font-semibold tracking-tight text-slate-900">{{ title }}</h2>
          <p class="mt-2 text-sm leading-6 text-slate-600">{{ description }}</p>
        </div>
        <button class="h-10 w-10 rounded-2xl border border-slate-200 bg-slate-50 text-slate-500 transition hover:bg-slate-100" @click="emits('close')" aria-label="Close confirmation">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="h-5 w-5">
            <path d="M18.3 5.71a1 1 0 00-1.42 0L12 10.59 7.12 5.7A1 1 0 105.7 7.12L10.59 12l-4.88 4.88a1 1 0 001.42 1.42L12 13.41l4.88 4.89a1 1 0 001.42-1.42L13.41 12l4.89-4.88a1 1 0 000-1.41z" />
          </svg>
        </button>
      </div>

      <div class="mt-4 flex flex-col gap-3 sm:flex-row sm:justify-end">
        <button class="rounded-2xl border border-slate-200 bg-white px-4 py-3 text-sm font-medium text-slate-700 transition hover:border-slate-300 hover:bg-slate-50" @click="emits('close')">{{ cancelText ?? 'Cancel' }}</button>
        <button class="rounded-2xl bg-rose-600 px-4 py-3 text-sm font-semibold text-white transition hover:bg-rose-700" @click="emits('confirm')">{{ confirmText ?? 'Delete' }}</button>
      </div>
    </div>
  </div>
</template>
