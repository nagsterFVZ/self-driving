<template>
  <v-card
    height="150"
    width="150"
    elevation="4"
    class="card-button mr-4"
    style="text-align: center"
  >
    <div style="transform: translate(0%, 20%)">
      <v-icon v-if="!loading" size="100">mdi-power</v-icon>
      <v-progress-circular
        v-else
        color="primary"
        indeterminate
        :size="80"
        :width="7"
        class="mb-5"
      />
    </div>
    <p class="pt-2 text-h7">{{ title }}</p>
  </v-card>
</template>
<script setup>
defineProps({
  title: {
    type: String,
  },
  loading: {
    type: Boolean,
  },
});
</script>
