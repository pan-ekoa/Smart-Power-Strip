<template>
  <div class="main-wrapper">
    <div class="socket-box">
      <div class="socket-left">
        <div class="device-title"><span class="device-label">Device</span><span class="device-num">1</span></div>
        <div class="switch-circle" :class="{ on: device1Data.Status === 1, off: device1Data.Status !== 1 }"></div>
        <div class="switch-toggle" @click="toggleDeviceStatus(1)"></div>
      </div>
      <div class="socket-content">
        <div class="socket-item">
          <div class="item-label">电压</div>
          <div class="item-value">{{ device1Data.Voltage }} <span class="unit">V</span></div>
        </div>
        <div class="socket-item">
          <div class="item-label">电流</div>
          <div class="item-value">{{ device1Data.Current }} <span class="unit">A</span></div>
        </div>
        <div class="socket-item">
          <div class="item-label">功率</div>
          <div class="item-value">
            {{ isNaN(Number(device1Data.Power)) ? "--" : Number(device1Data.Power).toFixed(2) }} <span class="unit">W</span>
          </div>
        </div>
        <div class="socket-item energy-item">
          <div class="item-label">电能</div>
          <div class="item-value">{{ device1Data.Energy }} <span class="unit">kWh</span></div>
        </div>
      </div>
    </div>
    <div class="socket-box socket-box-2">
      <div class="socket-left">
        <div class="device-title"><span class="device-label">Device</span><span class="device-num">2</span></div>
        <div class="switch-circle" :class="{ on: device2Data.Status === 1, off: device2Data.Status !== 1 }"></div>
        <div class="switch-toggle" @click="toggleDeviceStatus(2)"></div>
      </div>
      <div class="socket-content">
        <div class="socket-item">
          <div class="item-label">电压</div>
          <div class="item-value">{{ device2Data.Voltage }} <span class="unit">V</span></div>
        </div>
        <div class="socket-item">
          <div class="item-label">电流</div>
          <div class="item-value">{{ device2Data.Current }} <span class="unit">A</span></div>
        </div>
        <div class="socket-item">
          <div class="item-label">功率</div>
          <div class="item-value">
            {{ isNaN(Number(device2Data.Power)) ? "--" : Number(device2Data.Power).toFixed(2) }} <span class="unit">W</span>
          </div>
        </div>
        <div class="socket-item energy-item">
          <div class="item-label">电能</div>
          <div class="item-value">{{ device2Data.Energy }} <span class="unit">kWh</span></div>
        </div>
      </div>
    </div>
    <div class="content-row">
      <!-- 这里可以放置后续每个指标的内容或图表 -->
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import axios from "axios";

const device1Data = ref({
  Voltage: "--",
  Current: "--",
  Power: "--",
  Energy: "--",
  Status: 0
});
const device2Data = ref({
  Voltage: "--",
  Current: "--",
  Power: "--",
  Energy: "--",
  Status: 0
});

const fetchDeviceData = async () => {
  // Device 1
  try {
    const { data } = await axios.get("http://localhost:6007/device", { params: { id: 1 } });
    console.log("Device:", data);
    if (data && data.message === "success" && data.data) {
      device1Data.value = data.data;
    }
  } catch (e) {
    // 可选：错误处理
  }
  // Device 2
  try {
    const { data } = await axios.get("http://localhost:6007/device", { params: { id: 2 } });
    console.log("Device:", data);
    if (data && data.message === "success" && data.data) {
      device2Data.value = data.data;
    }
  } catch (e) {
    // 可选：错误处理
  }
};

const toggleDeviceStatus = async (deviceId: number) => {
  // 1. 根据 deviceId 选择对应的数据对象（device1Data 或 device2Data）
  const deviceData = deviceId === 1 ? device1Data : device2Data;

  // 2. 计算新的状态：如果当前 Status 是 1（开），就变成 0（关）；如果是 0（关），就变成 1（开）
  const newStatus = deviceData.value.Status === 1 ? 0 : 1;

  try {
    // 3. 发送 GET 请求到后端，告知要切换的插座 id 以及新的 status
    await axios.get("http://localhost:6007/command", { params: { id: deviceId, status: newStatus } });

    // 4. 前端本地也同步更新 status，保证界面立即响应
  } catch (e) {
    // 5. 如果请求失败，可以在这里做错误处理（比如弹窗提示等）
  }
};
// function toggleDeviceStatus(deviceId) {
//   const deviceData = deviceId === 1 ? device1Data : device2Data;
//   const newStatus = deviceData.value.Status === 1 ? 0 : 1;

//   axios({
//     method: "post",
//     url: "http://localhost:6006/command",
//     data: {
//       id: deviceId,
//       status: newStatus
//     },
//     headers: {
//       "Content-Type": "application/json"
//     },
//     responseType: "json"
//   })
//     .then(response => {
//       console.log(response);
//     })
//     .catch(error => {
//       console.log(error);
//     });
// }

onMounted(() => {
  fetchDeviceData();
});
</script>

<style scoped lang="scss">
.main-wrapper {
  display: flex;
  flex-direction: column;
  height: 100vh;
  width: 100%;
  background: #f7f7f7;
}

.socket-box {
  margin: 64px auto 32px auto;
  width: 800px;
  height: 220px;
  background: #fff;
  border-radius: 32px;
  box-shadow: 0 4px 24px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: row;
  align-items: stretch;
  padding: 0 48px;
  position: relative;
}

.socket-box-2 {
  margin-top: 40px;
}

.socket-left {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  width: 80px;
  padding-top: 16px;
  position: relative;
}

.device-title {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  display: flex;
  flex-direction: row;
  align-items: flex-end;
  justify-content: center;
  width: 100%;
  font-family: "Segoe UI", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", Arial, sans-serif;
  font-size: 1.2rem;
  font-weight: 700;
  letter-spacing: 1px;
  color: #333;
  margin-bottom: 0;
  margin-top: 0;
  text-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
  height: 36px;
  line-height: 36px;
}
.device-label,
.device-num {
  font-family: inherit;
  font-size: inherit;
  font-weight: inherit;
  color: inherit;
}
.device-label {
  margin-right: 2px;
}
.device-num {
  margin-left: 1px;
}

.switch-circle {
  width: 54px;
  height: 54px;
  border-radius: 50%;
  border: 4px solid #eee;
  background: #ccc;
  transition:
    background 0.3s,
    border-color 0.3s;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  display: flex;
  align-items: center;
  justify-content: center;
  margin-top: 48px;
  margin-bottom: 18px;
}
.switch-circle.on {
  background: #ff7875;
  border-color: #ff7875;
}
.switch-circle.off {
  background: #bbb;
  border-color: #eee;
}

.switch-toggle {
  width: 54px;
  height: 28px;
  border-radius: 14px;
  background: #e6f7ff;
  margin: 0 auto;
  box-shadow: 0 1px 4px rgba(0, 0, 0, 0.08);
  border: 1.5px solid #91d5ff;
}

.socket-content {
  display: flex;
  flex: 1;
  justify-content: space-between;
  align-items: center;
  height: 100%;
  margin-left: 40px;
  width: 660px;
}
.socket-item {
  width: 140px;
  height: 120px;
  background: #f2f2f2;
  border-radius: 16px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-size: 1.2rem;
  font-weight: 500;
  margin-left: 24px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
}
.socket-item:first-child {
  margin-left: 0;
}
.item-label {
  font-size: 1.3rem;
  font-weight: bold;
  margin-bottom: 18px;
  font-family: "Segoe UI", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", Arial, sans-serif;
  color: #444;
  letter-spacing: 1px;
}
.item-value {
  font-size: 2.1rem;
  font-weight: 600;
  color: #333;
  min-height: 36px;
  font-family: "Segoe UI", "Consolas", "Menlo", "Monaco", monospace;
}
.energy-item {
  width: 200px !important;
}

.content-row {
  flex: 1;
  /* 可根据需要添加内容或样式 */
}

.unit {
  font-size: 1.1rem;
  color: #888;
  margin-left: 2px;
}
</style>
