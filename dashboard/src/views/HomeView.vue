<template>
  <temp-card />
</template>

<script lang="ts">
import { defineComponent } from 'vue';

// Components
import TempCard from '../components/Dashboard/LineChart';

export default defineComponent({
  name: 'HomeView',

  components: {
    TempCard,
  },
});
</script>
