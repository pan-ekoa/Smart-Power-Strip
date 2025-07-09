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
        <div>
          <h3 class="device-title device-title--deep">Device 1</h3>
          <div v-if="device1LastUpdate" class="update-time">{{ getUpdateText(device1LastUpdate) }}{{ now && "" }}</div>
        </div>
        <div class="device-actions">
          <el-switch v-model="device1On" @change="handleSwitch(1)" active-text="开" inactive-text="关" />
          <el-button size="small" type="primary" @click="openTimeDialog(1)">
            <el-icon><Clock /></el-icon>
            设置时间
          </el-button>
        </div>
      </div>
      <div class="charts-row">
        <div class="chart-box">
          <EChartsLine :data="device1Voltage" :time="device1TimeArray" title="电压变化趋势图" />
        </div>
        <div class="chart-box">
          <EChartsLine :data="device1Current" :time="device1TimeArray" title="电流变化趋势图" />
        </div>
      </div>
      <div class="charts-row">
        <div class="chart-box">
          <EChartsLine :data="device1Power" :time="device1TimeArray" title="功率变化趋势图" />
        </div>
        <div class="chart-box">
          <EChartsLine :data="device1Energy" :time="device1TimeArray" title="电能变化趋势图" />
        </div>
      </div>
      <!-- 这里可以放设备1的详细信息或操作 -->
      <div class="advice-section">
        <el-button size="small" @click="toggleAdvice(1)">
          <el-icon><InfoFilled /></el-icon>
          查看用电建议
        </el-button>
        <el-card v-if="adviceVisible1" shadow="never" style="margin-top: 12px">
          <div v-if="adviceLoading1" style="text-align: center; padding: 24px 0">
            <el-icon class="is-loading" style="font-size: 28px"><Loading /></el-icon>
          </div>
          <div v-else>
            <div v-if="adviceList1">
              <span v-html="adviceList1" class="advice-text advice-inline" />
            </div>
            <div v-else class="advice-text">暂无建议</div>
          </div>
        </el-card>
      </div>
      <el-dialog v-model="timeDialogVisible1" title="设置定时开关时间" width="340px" align-center>
        <div style="margin-bottom: 16px; color: #666">请选择设备的定时开关时间</div>
        <el-time-picker v-model="device1TimePicker" placeholder="选择时间" style="width: 100%" arrow-control />
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
        <div>
          <h3 class="device-title device-title--deep">Device 2</h3>
          <div v-if="device2LastUpdate" class="update-time">{{ getUpdateText(device2LastUpdate) }}{{ now && "" }}</div>
        </div>
        <div class="device-actions">
          <el-switch v-model="device2On" @change="handleSwitch(2)" active-text="开" inactive-text="关" />
          <el-button size="small" type="primary" @click="openTimeDialog(2)">
            <el-icon><Clock /></el-icon>
            设置时间
          </el-button>
        </div>
      </div>
      <div class="charts-row">
        <div class="chart-box">
          <EChartsLine :data="device2Voltage" :time="device2TimeArray" title="电压变化趋势图" />
        </div>
        <div class="chart-box">
          <EChartsLine :data="device2Current" :time="device2TimeArray" title="电流变化趋势图" />
        </div>
      </div>
      <div class="charts-row">
        <div class="chart-box">
          <EChartsLine :data="device2Power" :time="device2TimeArray" title="功率变化趋势图" />
        </div>
        <div class="chart-box">
          <EChartsLine :data="device2Energy" :time="device2TimeArray" title="电能变化趋势图" />
        </div>
      </div>
      <!-- 这里可以放设备2的详细信息或操作 -->
      <div class="advice-section">
        <el-button size="small" @click="toggleAdvice(2)">
          <el-icon><InfoFilled /></el-icon>
          查看用电建议
        </el-button>
        <el-card v-if="adviceVisible2" shadow="never" style="margin-top: 12px">
          <div v-if="adviceLoading2" style="text-align: center; padding: 24px 0">
            <el-icon class="is-loading" style="font-size: 28px"><Loading /></el-icon>
          </div>
          <div v-else>
            <div v-if="adviceList2">
              <span v-html="adviceList2" class="advice-text advice-inline" />
            </div>
            <div v-else class="advice-text">暂无建议</div>
          </div>
        </el-card>
      </div>
      <el-dialog v-model="timeDialogVisible2" title="设置定时开关时间" width="340px" align-center>
        <div style="margin-bottom: 16px; color: #666">请选择设备的定时开关时间</div>
        <el-time-picker v-model="device2TimePicker" placeholder="选择时间" style="width: 100%" arrow-control />
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
import { ref, onMounted, onUnmounted } from "vue";
import { Clock, InfoFilled, Loading } from "@element-plus/icons-vue";
import axios from "axios";
import EChartsLine from "@/components/ECharts/EChartsLine.vue";
const selectedDevice = ref("all");
const device1On = ref(false);
const device2On = ref(false);
const timeDialogVisible1 = ref(false);
const timeDialogVisible2 = ref(false);
const device1TimePicker = ref("");
const device2TimePicker = ref("");
const adviceVisible1 = ref(false);
const adviceVisible2 = ref(false);

// Device 1数据更新时间
const device1LastUpdate = ref(0);
const device2LastUpdate = ref(0);
// Device 1数据
const device1Energy = ref<number[]>([]);
const device1Current = ref<number[]>([]);
const device1Voltage = ref<number[]>([]);
const device1Power = ref<number[]>([]);
const device1TimeArray = ref<string[] | number[]>([]);
// Device 2数据
const device2Energy = ref<number[]>([]);
const device2Current = ref<number[]>([]);
const device2Voltage = ref<number[]>([]);
const device2Power = ref<number[]>([]);
const device2TimeArray = ref<string[] | number[]>([]);

const adviceList1 = ref<string>("");
const adviceList2 = ref<string>("");
const adviceLoading1 = ref(false);
const adviceLoading2 = ref(false);

const now = ref(Date.now());

onMounted(() => {
  const timer = setInterval(() => {
    now.value = Date.now();
  }, 30000); // 每30秒刷新一次
  onUnmounted(() => clearInterval(timer));
});

async function fetchDeviceArrays(deviceId: number) {
  try {
    const { data } = await axios.get("http://localhost:6007/device/strip", { params: { id: deviceId } });
    if (data && data.message === "success" && data.data) {
      const now = Date.now();
      if (deviceId === 1) {
        device1Energy.value = data.data.energy || [];
        device1Current.value = data.data.current || [];
        device1Voltage.value = data.data.voltage || [];
        device1Power.value = data.data.power || [];
        device1TimeArray.value = data.data.time || [];
        device1LastUpdate.value = now;
      } else if (deviceId === 2) {
        device2Energy.value = data.data.energy || [];
        device2Current.value = data.data.current || [];
        device2Voltage.value = data.data.voltage || [];
        device2Power.value = data.data.power || [];
        device2TimeArray.value = data.data.time || [];
        device2LastUpdate.value = now;
      }
    }
  } catch (e) {
    // 可选：错误处理
  }
}

async function fetchAdvice(device: number) {
  if (device === 1) adviceLoading1.value = true;
  else if (device === 2) adviceLoading2.value = true;
  try {
    const { data } = await axios.get("http://localhost:6007/device/advice", { params: { id: device } });
    if (data && data.message === "success") {
      if (device === 1) adviceList1.value = data.data.message;
      else if (device === 2) adviceList2.value = data.data.message;
    }
  } catch (e) {
    // 可选：错误处理
  } finally {
    if (device === 1) adviceLoading1.value = false;
    else if (device === 2) adviceLoading2.value = false;
  }
}

fetchDeviceArrays(1);
fetchDeviceArrays(2);

// const mock60 = Array.from({ length: 60 }, (_, i) => i + 1);
// device1Voltage.value = mock60.map(x => 220 + Math.sin(x / 10) * 10);
// device1Current.value = mock60.map(x => 5 + Math.cos(x / 8) * 2);
// device1Power.value = mock60.map(x => 1000 + Math.sin(x / 7) * 100);
// device1Energy.value = mock60.map(x => 10 + x * 0.1 + Math.random() * 0.2);
// device1TimeArray.value = mock60.map(x => `${x < 10 ? "0" : ""}${x}:00`);

function handleSwitch(device: number) {
  // 1. 计算新状态
  const isOn = device === 1 ? device1On.value : device2On.value;
  const newStatus = isOn ? 1 : 0;

  // 2. 发送请求到后端
  axios.get("http://localhost:6007/command", { params: { id: device, status: newStatus } }).catch(() => {
    // 可选：错误处理，比如弹窗提示
  });
}
function openTimeDialog(device: number) {
  if (device === 1) timeDialogVisible1.value = true;
  else if (device === 2) timeDialogVisible2.value = true;
}
function saveTime(device: number) {
  // 这里可以处理保存时间逻辑
  let time = device === 1 ? device1TimePicker.value : device2TimePicker.value;
  // 发送请求到后端
  axios.get("http://localhost:6007/command/time", { params: { id: device, time } }).catch(() => {
    // 可选：错误处理，比如弹窗提示
  });
  if (device === 1) timeDialogVisible1.value = false;
  else if (device === 2) timeDialogVisible2.value = false;
}

function toggleAdvice(device: number) {
  if (device === 1) {
    adviceVisible1.value = !adviceVisible1.value;
    if (adviceVisible1.value) {
      adviceList1.value = "";
      fetchAdvice(1);
    }
  } else if (device === 2) {
    adviceVisible2.value = !adviceVisible2.value;
    if (adviceVisible2.value) {
      adviceList2.value = "";
      fetchAdvice(2);
    }
  }
}

function getUpdateText(ts: number) {
  if (!ts) return "";
  const diff = Math.floor((Date.now() - ts) / 1000);
  if (diff < 60) return `刚刚更新了数据`;
  if (diff < 3600) return `${Math.floor(diff / 60)}分钟前更新了数据`;
  if (diff < 86400) return `${Math.floor(diff / 3600)}小时前更新了数据`;
  return `很久以前更新了数据`;
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
.update-time {
  color: #999;
  font-size: 0.95rem;
  margin-top: 8px;
  margin-bottom: 0;
}
.advice-text {
  font-size: 1rem;
  color: #666;
}
.advice-item {
  margin: 2px 0;
  line-height: 1.4;
  font-size: 1rem;
}
.advice-inline {
  display: inline-block;
  margin: 0 2px;
  line-height: 1.5;
  font-size: 1rem;
  white-space: pre-line;
}
</style>
