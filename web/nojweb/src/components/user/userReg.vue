<template>
  <div class="login">
    <el-card class="box-card" shadow="hover">
      <template #header>
        <div class="card-header">
          注册
        </div>
      </template>
      <el-form :model="registerForm" ref="registerForm" :rules="rules">
        <el-form-item label="邮箱" prop="email" style="margin-left: 15px">
          <el-input v-model="registerForm.email" type="text" />
        </el-form-item>
        <el-form-item label="用户名" prop="username" style="margin-left: 28px">
          <el-input v-model="registerForm.username" type="text" />
        </el-form-item>
        <el-form-item label="密码" prop="password" style="margin-left: 28px">
          <el-input v-model="registerForm.password" type="password" />
        </el-form-item>
        <el-form-item label="确认密码" prop="confirmPassword" style="margin-left: 28px">
          <el-input v-model="registerForm.confirmPassword" type="password" />
        </el-form-item>
        <el-button type="primary" @click="submit" style="width: 250px;">注册</el-button>
      </el-form>
      <el-divider />
      <el-button type="info" plain @click="showLoginForm" style="width: 100%; height: 40px;">已有账号？点此登录</el-button>
    </el-card>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: "userRegister",
  data() {
    return {
      registerForm: {
        email: "",
        username: "",
        password: "",
        confirmPassword: ""
      },
      rules: {
        email: [{ required: true, message: "请输入邮箱", trigger: "blur" }],
        username: [{ required: true, message: "请输入用户名", trigger: "blur" }],
        password: [{ required: true, message: "请输入密码", trigger: "blur" }],
        confirmPassword: [{ required: true, message: "请确认密码", trigger: "blur" }]
      }
    };
  },
  methods: {
    submit() {
      this.$refs.registerForm.validate(valid => {
        if (valid) {
          if (this.registerForm.password === this.registerForm.confirmPassword) {
            // 进行注册逻辑，例如发送注册请求到后端接口
        axios.post('http://127.0.0.1:8000/register', {
        username: this.username,
        email: this.email,
        password:this.password
      }).then(res => {
        console.log('注册成功', res.data);
        // 可以根据实际需求处理注册成功后的逻辑
      }).catch(err => {
        console.error('注册失败', err);
        // 可以根据实际需求处理注册失败后的逻辑
      });
          } else {
            this.$message.error("密码不一致");
          }
        } else {
          this.$message.error("请输入完整信息");
        }
      });
    },
    showLoginForm() {
      // 显示登录表单
      console.log("显示登录表单");
      this.$router.push("/user/login");
    }
  }
};
</script>

<style scoped>
.login {
  text-align: center;
  margin: 50px auto; /* 修改垂直居中 */
  max-width: 500px;
}

.card-header {
  font-weight: bold;
  font-size: 24px; /* 修改标题字体大小 */
  margin-bottom: 20px; /* 增加标题与表单之间的间距 */
}

.el-card__body {
  padding: 30px; /* 增加卡片内边距 */
}

.el-form-item {
  margin-bottom: 20px; /* 增加表单项之间的间距 */
}

.el-input {
  width: 100%; /* 表单输入框宽度100% */
}

.el-button {
  margin-top: 20px; /* 增加按钮与表单之间的间距 */
}
</style>
