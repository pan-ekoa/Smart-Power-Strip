<template>
  <div ref="chartRef" style="width: 100%; height: 100%"></div>
</template>

<script setup lang="ts">
import { ref, watch, onMounted, onBeforeUnmount } from "vue";
import * as echarts from "echarts";

const props = defineProps<{
  data: number[];
  time: (string | number)[];
  title: string;
}>();

const chartRef = ref<HTMLDivElement | null>(null);
let chart: echarts.ECharts | null = null;

function renderChart() {
  if (!chartRef.value) return;
  if (!chart) chart = echarts.init(chartRef.value);
  chart.setOption({
    title: {
      text: props.title,
      left: "center",
      top: 24, // 标题下移
      textStyle: {
        fontSize: 16,
        fontWeight: 600,
        color: "#333"
      }
    },
    tooltip: { trigger: "axis" },
    grid: { left: 40, right: 30, top: 60, bottom: 40 }, // 网格整体下移
    xAxis: {
      type: "category",
      data: props.time,
      axisLabel: { fontSize: 12, color: "#666", margin: 16 },
      axisLine: { lineStyle: { color: "#ccc" } },
      axisTick: { show: false }
    },
    yAxis: {
      type: "value",
      axisLabel: { fontSize: 12, color: "#666" },
      splitLine: { lineStyle: { color: "#eee" } },
      axisLine: { show: false },
      axisTick: { show: false }
    },
    series: [
      {
        data: props.data,
        type: "line",
        smooth: true,
        showSymbol: false,
        areaStyle: {
          color: "rgba(33, 138, 90, 0.08)"
        },
        lineStyle: {
          color: "#218a5a",
          width: 2
        }
      }
    ]
  });
}

watch(() => [props.data, props.time], renderChart, { deep: true });
onMounted(renderChart);
onBeforeUnmount(() => {
  chart?.dispose();
});
</script>

<style scoped>
div {
  width: 100%;
  height: 100%;
}
</style>
