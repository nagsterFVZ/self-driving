<template>
  <v-card>
    <v-toolbar density="compact">
      <v-toolbar-title>{{ chartData.key }}</v-toolbar-title>

      <v-spacer></v-spacer>
    </v-toolbar>
    <LineChart :chartData="chartData" />
  </v-card>
</template>
<script setup>
import LineChart from "./Dashboard/LineChart";

defineProps({
  chartData: {
    type: Object,
    required: true,
  },
});
</script>
