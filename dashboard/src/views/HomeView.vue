<template>
  <v-container fluid class="pa-8">
    <v-row>
      <h1>Dashboard</h1>
      <v-spacer />
      <v-range-slider
        v-if="charts[0]"
        class="pr-2 pt-1"
        v-model="dataRange"
        track-fill-color="primary"
        thumb-color="primary"
        thumb-label
        step="1"
        :max="maxRange"
        min="0"
        strict
      >
        <template v-slot:thumb-label="{ modelValue }">
          {{ charts[0].labels[modelValue] }}
        </template>
      </v-range-slider>
      <v-btn
        @click="setRange"
        variant="elevated"
        rounded="lg"
        color="primary"
        class="mr-2"
      >
        Range
      </v-btn>
      <v-btn variant="elevated" rounded="lg" color="primary" @click="getStats"
        >Refresh</v-btn
      >
    </v-row>
    <v-row>
      <v-col v-for="chart in charts" :key="chart.key" cols="4">
        <DashboardLineCard :chartData="chart" />
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref, onMounted } from "vue";
import DashboardLineCard from "../components/DashboardLineCard.vue";

onMounted(() => {
  getStats();
});

const charts = ref([]);
const stats = ref({});
const dataRange = ref([0, 300]);
const maxRange = ref(300);

function setRange() {
  console.log();
  for (const chart of charts.value) {
    chart.labels = chart.labels.slice(dataRange.value[0], dataRange.value[1]);
    chart.datasets[0].data = chart.datasets[0].data.slice(
      dataRange.value[0],
      dataRange.value[1]
    );
  }
}

async function getStats() {
  charts.value = [];
  await fetch("/api/stats", {
    method: "GET",
  }).then((response) => {
    response.json().then((data) => {
      stats.value = data;
      constructData(data);
    });
  });
}

function constructData(data) {
  //For each sensor in data
  for (const [key, value] of Object.entries(data)) {
    // Create Label
    const label = [];
    // Create datataset
    const dataset = {
      label: key,
      backgroundColor: "#FF9100",
      tension: 0.4,
      data: [],
    };
    // Put data into label and dataset
    value.forEach((element) => {
      label.push(msToTime(element[0]));
      dataset.data.push(element[1]);
    });
    // Create chart object with label and dataset
    const chart = {
      key: key,
      labels: label,
      datasets: [dataset],
    };
    // push chart to charts
    charts.value.push(chart);
  }
  maxRange.value = charts.value[0].labels.length - 1;
}

function msToTime(s) {
  var date = new Date(s);

  return date.toLocaleTimeString("it-IT");
}
</script>
