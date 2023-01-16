<script setup lang="ts">
defineProps<{ label: string }>();
</script>

<template>
  <v-col cols="auto">
    <v-card elevation="3">
      <v-card-title>{{ label }}</v-card-title>
      <v-card-text><slot /></v-card-text>
    </v-card>
  </v-col>
</template>
