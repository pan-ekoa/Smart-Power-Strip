<template>
  <div class="device-manage-section">
    <div style="margin: 24px 0; display: flex; align-items: center; justify-content: flex-start">
      <el-select v-model="selectedDevice" placeholder="请选择设备" class="device-select">
        <el-option label="全部设备" value="all"><i class="el-icon-menu"></i> 全部设备</el-option>
        <el-option label="Device 1" value="1"><i class="el-icon-cpu"></i> Device 1</el-option>
        <el-option label="Device 2" value="2"><i class="el-icon-cpu"></i> Device 2</el-option>
      </el-select>
    </div>
    <div v-if="selectedDevice === 'all' || selectedDevice === '1'" class="device-box">
      <div class="device-header">
        <h3 class="device-title device-title--deep">Device 1</h3>
        <div class="device-actions">
          <el-switch v-model="device1On" @change="handleSwitch(1)" active-text="开" inactive-text="关" />
          <el-button size="small" type="primary" @click="openTimeDialog(1)">
            <el-icon><Clock /></el-icon>
            设置时间
          </el-button>
        </div>
      </div>
      <div class="charts-row">
        <div class="chart-box">图表1</div>
        <div class="chart-box">图表2</div>
      </div>
      <div class="charts-row">
        <div class="chart-box">图表3</div>
        <div class="chart-box">图表4</div>
      </div>
      <!-- 这里可以放设备1的详细信息或操作 -->
      <div class="advice-section">
        <el-button size="small" @click="toggleAdvice(1)">
          <el-icon><InfoFilled /></el-icon>
          查看用电建议
        </el-button>
        <el-card v-if="adviceVisible1" shadow="never" style="margin-top: 12px">
          用电建议：建议合理安排用电时间，避免高峰期。
        </el-card>
      </div>
      <el-dialog v-model="timeDialogVisible1" title="设置定时开关时间" width="340px" align-center>
        <div style="margin-bottom: 16px; color: #666">请选择设备的定时开关时间</div>
        <el-time-picker v-model="device1Time" placeholder="选择时间" style="width: 100%" arrow-control />
        <template #footer>
          <div style="text-align: center">
            <el-button @click="timeDialogVisible1 = false">取消</el-button>
            <el-button type="primary" @click="saveTime(1)">保存</el-button>
          </div>
        </template>
      </el-dialog>
    </div>
    <div v-if="selectedDevice === 'all' || selectedDevice === '2'" class="device-box">
      <div class="device-header">
        <h3 class="device-title device-title--deep">Device 2</h3>
        <div class="device-actions">
          <el-switch v-model="device2On" @change="handleSwitch(2)" active-text="开" inactive-text="关" />
          <el-button size="small" type="primary" @click="openTimeDialog(2)">
            <el-icon><Clock /></el-icon>
            设置时间
          </el-button>
        </div>
      </div>
      <div class="charts-row">
        <div class="chart-box">图表1</div>
        <div class="chart-box">图表2</div>
      </div>
      <div class="charts-row">
        <div class="chart-box">图表3</div>
        <div class="chart-box">图表4</div>
      </div>
      <!-- 这里可以放设备2的详细信息或操作 -->
      <div class="advice-section">
        <el-button size="small" @click="toggleAdvice(2)">
          <el-icon><InfoFilled /></el-icon>
          查看用电建议
        </el-button>
        <el-card v-if="adviceVisible2" shadow="never" style="margin-top: 12px">
          用电建议：建议合理安排用电时间，避免高峰期。
        </el-card>
      </div>
      <el-dialog v-model="timeDialogVisible2" title="设置定时开关时间" width="340px" align-center>
        <div style="margin-bottom: 16px; color: #666">请选择设备的定时开关时间</div>
        <el-time-picker v-model="device2Time" placeholder="选择时间" style="width: 100%" arrow-control />
        <template #footer>
          <div style="text-align: center">
            <el-button @click="timeDialogVisible2 = false">取消</el-button>
            <el-button type="primary" @click="saveTime(2)">保存</el-button>
          </div>
        </template>
      </el-dialog>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { Clock, InfoFilled } from "@element-plus/icons-vue";
const selectedDevice = ref("all");
const device1On = ref(false);
const device2On = ref(false);
const timeDialogVisible1 = ref(false);
const timeDialogVisible2 = ref(false);
const device1Time = ref("");
const device2Time = ref("");
const adviceVisible1 = ref(false);
const adviceVisible2 = ref(false);

function handleSwitch(_device: number) {
  // 这里可以处理开关逻辑
  _device === 1;
}
function openTimeDialog(device: number) {
  if (device === 1) timeDialogVisible1.value = true;
  else if (device === 2) timeDialogVisible2.value = true;
}
function saveTime(device: number) {
  // 这里可以处理保存时间逻辑
  if (device === 1) timeDialogVisible1.value = false;
  else if (device === 2) timeDialogVisible2.value = false;
}

function toggleAdvice(device: number) {
  if (device === 1) adviceVisible1.value = !adviceVisible1.value;
  else if (device === 2) adviceVisible2.value = !adviceVisible2.value;
}
</script>

<style scoped>
.device-manage-section {
  margin: 40px auto 0 auto;
  width: 1000px;
  background: #fff;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  padding: 48px 40px;
}
.device-select {
  width: 220px;
  font-size: 1.1rem;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
  background: #f7f9fa;
}
.device-box {
  margin-top: 32px;
  padding: 32px 24px;
  border: 1.5px solid #eee;
  border-radius: 14px;
  min-height: 220px;
}
.charts-row {
  display: flex;
  gap: 24px;
  margin-top: 24px;
}
.chart-box {
  flex: 0 0 48%;
  height: 240px;
  min-width: 220px;
  background: #f5f7fa;
  border-radius: 10px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.1rem;
  color: #888;
}
.device-title {
  color: #218a5a;
  margin-top: 0;
  margin-bottom: 18px;
  font-weight: bold;
}
.device-title--deep {
  color: #176143;
  margin-top: -18px;
  margin-bottom: 18px;
}
.device-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 8px;
}
.device-actions {
  display: flex;
  align-items: center;
  gap: 12px;
}
.advice-section {
  margin-top: 24px;
}
</style>
