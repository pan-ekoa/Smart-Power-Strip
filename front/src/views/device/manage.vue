<template>
  <div class="device-manage-section">
    <div style="margin: 24px 0">
      <select v-model="selectedDevice">
        <option value="all">全部设备</option>
        <option value="1">设备1</option>
        <option value="2">设备2</option>
      </select>
    </div>
    <div v-if="selectedDevice === 'all' || selectedDevice === '1'" class="device-box">
      <h3>设备1</h3>
      <!-- 这里可以放设备1的详细信息或操作 -->
    </div>
    <div v-if="selectedDevice === 'all' || selectedDevice === '2'" class="device-box">
      <h3>设备2</h3>
      <!-- 这里可以放设备2的详细信息或操作 -->
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
const selectedDevice = ref("all");
</script>

<style scoped>
.device-manage-section {
  margin: 40px auto 0 auto;
  width: 800px;
  background: #fff;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  padding: 32px;
}
.device-box {
  margin-top: 24px;
  padding: 16px;
  border: 1px solid #eee;
  border-radius: 8px;
}
</style>
