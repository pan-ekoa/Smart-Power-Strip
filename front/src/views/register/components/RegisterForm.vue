<template>
  <div class="logo-container">
    <img src="@/assets/images/logo_with_name.png" alt="Logo" class="logo-image" />
  </div>

  <el-form ref="registerFormRef" :model="registerForm" :rules="registerRules" size="large">
    <el-form-item prop="username">
      <el-input v-model="registerForm.username" placeholder="请输入用户名">
        <template #prefix>
          <el-icon><User /></el-icon>
        </template>
      </el-input>
    </el-form-item>

    <el-form-item prop="password">
      <el-input v-model="registerForm.password" type="password" placeholder="请输入密码" show-password>
        <template #prefix>
          <el-icon><Lock /></el-icon>
        </template>
      </el-input>
    </el-form-item>

    <el-form-item prop="confirmPassword">
      <el-input v-model="registerForm.confirmPassword" type="password" placeholder="请确认密码" show-password>
        <template #prefix>
          <el-icon><Lock /></el-icon>
        </template>
      </el-input>
    </el-form-item>
  </el-form>

  <div class="buttons">
    <el-button :icon="Back" @click="goToLogin" round size="large" style="width: 180px">返回登录</el-button>
    <el-button
      :icon="Check"
      type="primary"
      :loading="loading"
      @click="register(registerForm)"
      round
      size="large"
      style="width: 180px"
    >
      注册
    </el-button>
  </div>
</template>

<script setup lang="ts">
import { ref, reactive } from "vue";
import { useRouter } from "vue-router";
import type { ElForm } from "element-plus";
import { User, Lock, Check, Back } from "@element-plus/icons-vue";
import { ElMessage } from "element-plus";

type FormInstance = InstanceType<typeof ElForm>;

const router = useRouter();
const loading = ref(false);
const registerFormRef = ref<FormInstance>();

const registerForm = reactive({
  username: "",
  password: "",
  confirmPassword: ""
});

const validateConfirmPassword = (rule: any, value: string, callback: any) => {
  if (!value) {
    callback(new Error("请确认密码")); // 为空
  } else if (value.length < 6) {
    callback(new Error("密码长度至少6位"));
  } else if (value !== registerForm.password) {
    callback(new Error("两次输入的密码不一致！")); // 和密码不一样
  } else {
    callback(); // 成功
  }
};

const registerRules = reactive({
  username: [{ required: true, message: "请输入用户名", trigger: "blur" }],
  password: [{ required: true, message: "请输入密码", trigger: "blur" }],
  confirmPassword: [{ validator: validateConfirmPassword, trigger: "blur" }]
});

const register = async (form: { username: string; password: string; confirmPassword: string }) => {
  if (!registerFormRef.value) return;

  try {
    await registerFormRef.value.validate(); // 如果validate失败，会抛异常，直接跳catch，不会往下执行
  } catch (validateError) {
    console.warn("表单校验未通过❌", validateError);
    ElMessage.warning("请完善表单信息🌟");
    return; // 校验失败后，直接return，不要继续请求接口
  }

  loading.value = true;

  try {
    const response = await fetch("http://localhost:6007/auth/register", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        username: form.username,
        password: form.password
      })
    });

    const data = await response.json();

    if (response.ok) {
      ElMessage.success(data.message);
      console.log("注册成功", data.user);
      router.push("/login");
    } else {
      ElMessage.error(data.message || "注册失败，请重试！");
    }
  } catch (error) {
    console.error("注册异常:", error);
    ElMessage.error("网络错误，无法连接到服务器！");
  } finally {
    loading.value = false;
  }
};

const goToLogin = () => {
  router.push("/login");
};
</script>

<style scoped lang="scss">
.logo-container {
  text-align: center;
  // margin-top: -50px;
}

.logo-image {
  max-width: 280px;
}

.el-form {
  max-width: 400px;
  padding: 30px;
  justify-content: center;
}

.buttons {
  display: flex;
  justify-content: center;
  gap: 20px;
  width: 100%;
  margin-top: -20px;
}
</style>
