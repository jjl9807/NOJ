<template>
  <div class="login">
    <el-card class="box-card" shadow="hover">
      <template #header>
        <div class="card-header">
          登录
        </div>
      </template>
      <el-form :model="userInfo">
        <el-form-item label="用户名" prop="name" style="margin-left: 15px">
          <el-input v-model="userInfo.name" type="text" />
        </el-form-item>
        <el-form-item label="密码" prop="pass" style="margin-left: 28px">
          <el-input v-model="userInfo.pwd" type="password" @keyup.enter="submit" />
        </el-form-item>
        <el-button type="primary" @click="submit" style="width: 250px;">登录</el-button>
      </el-form>
      <el-divider />
      <el-button type="info" plain @click="this.$router.push('/user/reg')"
        style="width: 100%; height: 40px;">新用户？点此注册</el-button>
    </el-card>
  </div>
</template>
  
  <script>
  export default {
    name: "userLogin",
    data() {
    return {
      userInfo: {
        name: "",
        pwd: "",
      },
    }
  },
    methods: {
      login() {
        // 在这里可以编写登录逻辑，例如发送登录请求到后端接口
        // 然后根据后端返回的结果进行相应的处理
        console.log('Username:', this.userInfo.name);
        console.log('Password:', this.userInfo.pwd);
        // 这里只是简单地输出用户名和密码到控制台
      },
      submit(){
        this.$store.commit('setUid', 1);
        this.$router.push('/')
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