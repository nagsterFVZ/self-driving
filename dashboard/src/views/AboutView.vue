<template>
  <div>
    <div
      v-if="!isSupported"
      flex="~ row"
      place="items-center content-center"
      items="center"
      space="x-4"
    >
      <i i-carbon-error text="5xl" opacity="50" />
      <div flex="~ col">
        <span text="2xl">Gamepad is not supported on this device.</span>
        <span opacity="70"
          >It seems your device does not support the Gamepad API. Check
          <a href="https://caniuse.com/gamepad">here</a> for a list supported
          devices.</span
        >
      </div>
    </div>
    <div
      v-else-if="gamepads.length === 0"
      flex="~ row"
      place="items-center content-center"
      items="center"
      space="x-4"
    >
      <i i-carbon-game-console text="5xl" opacity="50" />
      <div flex="~ col">
        <span text="2xl">No Gamepad Detected</span>
        <span opacity="50"
          >Ensure your gamepad is connected and press a button to wake it
          up.</span
        >
      </div>
    </div>
    <div v-else space="y-4">
      <Gamepad
        v-for="gamepad in gamepads"
        :key="gamepad.id"
        :gamepad="gamepad"
      />
    </div>
    <v-card
      ><v-card-title>Socket Status</v-card-title
      ><v-card-text>{{ socketStatus }}</v-card-text></v-card
    >
    <v-card
      ><v-card-title>Controller</v-card-title
      ><v-card-text>{{ controller.status }}</v-card-text></v-card
    >
  </div>
</template>
<script setup>
import { useGamepad } from "@vueuse/core";
import Gamepad from "../components/controlls/Gamepad.vue";
import { io } from "socket.io-client";
import { ref, shallowRef } from "@vue/reactivity";
import { watch } from "@vue/runtime-core";

const { isSupported, gamepads } = useGamepad();
const socket = io("http://192.168.178.192:5000");

const socketStatus = ref(false);
const controller = ref({ buttons: [], axes: [] });

socket.on("connect", () => {
  socketStatus.value = true;
  console.log("🟢 Socket Connected"); // true
});

socket.on("disconnect", () => {
  socketStatus.value = false;
  console.log("🔴 Socket Disconnected"); // false
});

//socket.emit("control", { throttle: 0.0 });

watch(
  () => gamepads,
  (newValue) => {
    const prev = JSON.parse(JSON.stringify(controller));

    controller.value.buttons[0] = newValue.value[0].buttons[14];
    controller.value.buttons[1] = newValue.value[0].buttons[15];
    controller.value.buttons[2] = newValue.value[0].buttons[2];
    controller.value.buttons[3] = newValue.value[0].buttons[1];
    controller.value.axes[0] = newValue.value[0].axes[0];
    controller.value.axes[1] = newValue.value[0].buttons[7].value;
    controller.value.axes[2] = newValue.value[0].buttons[6].value;
    if (prev._value?.buttons?.length > 0) {
      const payload = [];
      controller.value.buttons.forEach((button, index) => {
        if (
          button.pressed != prev._value.buttons[index].pressed &&
          button.pressed
        ) {
          payload.push({ button: button, id: index });
        }
      });
      controller.value.axes.forEach((axe, index) => {
        if (axe >= 0.05 || axe <= -0.05) {
          payload.push({ axes: axe, id: index });
        }
      });
      if (payload.length > 0) {
        socket.emit("control", payload);
      }
    }

    // if (controller.value.buttons.some((element) => element.pressed)) {
    //   controller.value.status = "Button Press";
    //   socket.emit("control", controller.value);
    // } else {
    //   controller.value.status = "";
    // }
  },
  { deep: true }
);
</script>
