<script setup lang="ts">
const props = defineProps<{
  toasts: Array<{
    id: number
    message: string
    variant?: 'success' | 'error' | 'info'
  }>
}>()

const emit = defineEmits(['dismiss'])

const variantClasses = {
  success: 'bg-emerald-600 text-white',
  error: 'bg-rose-600 text-white',
  info: 'bg-slate-900 text-white'
}
</script>

<template>
  <div class="fixed right-6 top-6 z-50 flex flex-col gap-3">
    <div
      v-for="toast in toasts"
      :key="toast.id"
      class="min-w-[280px] max-w-sm overflow-hidden rounded-3xl border border-slate-200 shadow-2xl ring-1 ring-slate-200"
      :class="variantClasses[toast.variant ?? 'success']"
    >
      <div class="flex items-start gap-3 p-4">
        <div class="flex h-10 w-10 items-center justify-center rounded-2xl bg-white/15 text-white">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="h-5 w-5">
            <path d="M12 2a10 10 0 100 20 10 10 0 000-20zm-1 14.5l-4-4 1.4-1.4L11 13.67l5.6-5.6L18 9.5l-7 7z" />
          </svg>
        </div>
        <div class="min-w-0 flex-1">
          <p class="text-sm font-semibold leading-6 text-white">{{ toast.message }}</p>
        </div>
        <button
          class="rounded-full bg-white/15 p-2 text-white transition hover:bg-white/25"
          @click="emit('dismiss', toast.id)"
          aria-label="Dismiss notification"
        >
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="h-4 w-4">
            <path d="M18.3 5.7a1 1 0 00-1.4 0L12 10.6 7.1 5.7A1 1 0 105.7 7.1L10.6 12l-4.9 4.9a1 1 0 101.4 1.4L12 13.4l4.9 4.9a1 1 0 001.4-1.4L13.4 12l4.9-4.9a1 1 0 000-1.4z" />
          </svg>
        </button>
      </div>
    </div>
  </div>
</template>
