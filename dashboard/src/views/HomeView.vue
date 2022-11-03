<template>
  <temp-card />
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import TempCard from "../components/Dashboard/LineChart";

onMounted(() => {
  getStats();
});

const stats = ref({});
async function getStats() {
  await fetch("/api/stats", {
    method: "GET",
  }).then((response) => {
    response.json().then((data) => {
      stats.value = data;
      console.log(stats.value);
    });
  });
}
</script>
