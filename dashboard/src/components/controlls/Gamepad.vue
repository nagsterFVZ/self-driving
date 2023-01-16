<script setup lang="ts">
import { computed } from "vue";
import Item from "./Item.vue";
import Controller from "./Controller.vue";

const props = defineProps<{ gamepad: Gamepad }>();

const supportsVibration = computed(
  () => props.gamepad.hapticActuators.length > 0
);
const vibrate = () => {
  if (supportsVibration.value) {
    const actuator: any = props.gamepad.hapticActuators[0];
    actuator.playEffect("dual-rumble", {
      startDelay: 0,
      duration: 1000,
      weakMagnitude: 1,
      strongMagnitude: 1,
    });
  }
};
</script>

<template>
  <div
    bg="dark:dark-500 light-100"
    shadow="~ md"
    border="rounded"
    max-w="screen-lg"
    mx="auto"
    overflow="hidden"
    grid="~"
    class="grid-cols-[2fr,1fr]"
  >
    <div p="4">
      <h2>{{ gamepad.id }}</h2>
      <v-row>
        <Item label="Index">
          {{ gamepad.index }}
        </Item>
        <Item label="Connected">
          {{ gamepad.connected }}
        </Item>
        <Item label="Mapping">
          {{ gamepad.mapping || "N/A" }}
        </Item>
        <Item label="Timestamp">
          {{ gamepad.timestamp.toFixed(0) }}
        </Item>
      </v-row>

      <h2>Buttons</h2>
      <v-row>
        <Item
          v-for="(button, index) in gamepad.buttons"
          :key="index"
          p="x-2 y-1"
          border="rounded"
          bg="dark:dark-700 light-500"
          :label="`B${index}`"
        >
          {{ button.value.toFixed(2) }}
        </Item>
      </v-row>

      <h2>Axes</h2>
      <v-row>
        <Item
          v-for="(axis, index) in gamepad.axes"
          :key="index"
          p="x-2 y-1"
          border="rounded"
          bg="dark:dark-700 light-500"
          :label="`Axis ${index}`"
        >
          {{ axis.toFixed(2) }}
        </Item>
      </v-row>

      <v-btn :disabled="!supportsVibration" @click="vibrate">Vibrate</v-btn>
    </div>
    <v-card width="600px" class="pa-4">
      <template v-if="gamepad.mapping === 'standard'">
        <Controller
          :gamepad="gamepad"
          text="dark-100 opacity-70 dark:(light-900 opacity-70)"
        />
      </template>
      <template v-else>
        <span font-medium text="dark:(light-900 opacity-70)">
          Unknown Controller Type
        </span>
      </template>
    </v-card>
  </div>
</template>
