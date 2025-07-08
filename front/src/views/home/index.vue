<template>
  <div class="main-wrapper">
    <div class="socket-box">
      <div class="socket-left">
        <div class="device-title"><span class="device-label">Device</span><span class="device-num">1</span></div>
        <div class="switch-circle" :class="{ on: status === 1, off: status !== 1 }"></div>
        <div class="switch-toggle"></div>
      </div>
      <div class="socket-content">
        <div class="socket-item">
          <div class="item-label">电压</div>
          <div class="item-value">--</div>
        </div>
        <div class="socket-item">
          <div class="item-label">电流</div>
          <div class="item-value">--</div>
        </div>
        <div class="socket-item">
          <div class="item-label">功率</div>
          <div class="item-value">--</div>
        </div>
        <div class="socket-item">
          <div class="item-label">电能</div>
          <div class="item-value">--</div>
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
// 页面只展示四个标题，无需 JS 逻辑
// 假设后端返回的Status
const status = ref(0); // 默认0，后续可用后端数据替换

// 示例：模拟后端请求Status
const fetchStatus = async () => {
  // 这里用setTimeout模拟异步请求，实际可用axios等替换
  setTimeout(() => {
    status.value = 1; // 1为红色，0为灰色
  }, 1000);
};

onMounted(() => {
  fetchStatus();
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
  margin-left: 20px;
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

.content-row {
  flex: 1;
  /* 可根据需要添加内容或样式 */
}
</style>
