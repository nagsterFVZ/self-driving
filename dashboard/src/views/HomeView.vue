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
  await fetch("http://127.0.0.1:8080/stats", {
    method: "GET",
  }).then((response) => {
    console.log(response);
    stats.value = response;
  });
}
</script>
