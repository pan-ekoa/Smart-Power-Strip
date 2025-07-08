<template>
  <el-dialog class="dialg" v-model="dialogVisible" title="个人信息" width="500px" draggable>
    <div class="avatar-section">
      <img :src="avatarUrl" alt="默认头像" class="avatar-image" />
    </div>
    <el-form label-width="100px" class="custom-form">
      <el-form-item label="用户ID">
        <div class="info-text">{{ userId }}</div>
      </el-form-item>
      <el-form-item label="用户名">
        <template v-if="!isEditing">
          <div class="info-text">{{ username }}</div>
        </template>
        <template v-else>
          <el-input v-model="username" />
        </template>
      </el-form-item>
    </el-form>

    <template #footer>
      <span class="dialog-footer">
        <el-button @click="dialogVisible = false">关闭</el-button>
      </span>
    </template>
  </el-dialog>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { useUserInfoStore } from "@/stores/modules/userInfo";

const dialogVisible = ref(false);
const isEditing = ref(false);
const email = ref("");
const username = ref("");
const userId = ref("");
const avatarUrl = ref("");

const userInfoStore = useUserInfoStore();

// 打开弹窗并加载用户数据
const openDialog = () => {
  const { email: e, username: u, user_id: id, avatar: a } = userInfoStore;
  email.value = e;
  username.value = u;
  userId.value = id.toString();
  avatarUrl.value = a;
  isEditing.value = false;
  dialogVisible.value = true;
};

defineExpose({ openDialog });
</script>

<style scoped lang="scss">
.avatar-section {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 20px;

  .avatar-image {
    width: 120px;
    height: 120px;
    border-radius: 50%;
    object-fit: cover;
    margin-bottom: 15px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  }

  .upload-avatar {
    text-align: center;
  }
}

.custom-form {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: left;
  width: 80%;
}

.el-form-item {
  width: 60%; /* 可以调整此值来控制表单宽度 */
}

.info-text {
  margin-left: 15px;
}

.dialog-footer {
  text-align: right;
}
</style>
