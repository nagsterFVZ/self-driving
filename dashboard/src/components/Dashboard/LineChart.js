import { defineComponent, h } from "vue";

import { Line } from "vue-chartjs";
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  LineElement,
  LinearScale,
  PointElement,
  CategoryScale,
} from "chart.js";

ChartJS.register(
  Title,
  Tooltip,
  Legend,
  LineElement,
  LinearScale,
  PointElement,
  CategoryScale
);

export default defineComponent({
  name: "LineChart",
  components: {
    Line,
  },
  props: {
    chartId: {
      type: String,
      default: "line-chart",
    },
    width: {
      type: Number,
      default: 400,
    },
    height: {
      type: Number,
      default: 400,
    },
    cssClasses: {
      default: "",
      type: String,
    },
    styles: {
      type: Object,
      default: () => {},
    },
    plugins: {
      type: Array,
      default: () => [],
    },
    chartData: {
      type: Object,
      required: true,
    },
  },
  setup(props) {

    //console.log("Graph", props.chartData)
    // const chartData = {
    //   labels: ["10:00", "10:15", "10:30", "10:45", "11:00", "11:15", "11:30"],
    //   datasets: [
    //     {
    //       label: "CPU Temp",
    //       backgroundColor: "#f87979",
    //       data: [56, 63, 62, 59, 57, 58, 60],
    //       tension: 0.4,
    //     },
    //   ],
    // };

    const chartOptions = {
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        y: {
          // min: 3.7,
          // max: 3.8,
          ticks: {
            stepSize: 1,
            // callback: function (value: string) {
            //   return value + "°C";
            // },
          },
        },
        x: {
          // type: "time"
        }
      },
    };

    return () =>
      h(Line, {
        chartData: props.chartData,
        chartOptions,
        chartId: props.chartId,
        width: props.width,
        height: props.height,
        cssClasses: props.cssClasses,
        styles: props.styles,
        plugins: props.plugins,
      });
  },
});
