<template>
    <div class="change-info">
      <!-- 大标题 -->
      <h1 class="title">更改个人信息</h1>
  
      <!-- 身份验证 -->
      <div class="auth">
        <h2>请输入您的密码进行身份验证</h2>
        <el-form :model="authForm" label-width="120px">
          <el-form-item label="密码：" prop="password">
            <el-input type="password" v-model="authForm.password"></el-input>
          </el-form-item>
        </el-form>
      </div>
  
      <!-- 新个人信息 -->
      <div class="new-info">
        <h2>请输入新的个人信息</h2>
        <el-form :model="infoForm" label-width="140px">
          <el-form-item label="新密码：" prop="newPassword">
            <el-input type="password" v-model="infoForm.newPassword"></el-input>
          </el-form-item>
          <el-form-item label="重新输入新密码：" prop="confirmPassword">
            <el-input type="password" v-model="infoForm.confirmPassword"></el-input>
          </el-form-item>
          <el-form-item label="Email：" prop="email">
            <el-input v-model="infoForm.email"></el-input>
          </el-form-item>
          <el-form-item label="QQ：" prop="qq">
            <el-input v-model="infoForm.qq"></el-input>
          </el-form-item>
          <el-form-item label="性别：" prop="gender">
            <el-select v-model="infoForm.gender" placeholder="请选择">
              <el-option label="男" value="male"></el-option>
              <el-option label="女" value="female"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="格言：" prop="motto">
            <el-input type="textarea" v-model="infoForm.motto"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="submitForm">提交</el-button>
          </el-form-item>
        </el-form>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        authForm: {
          password: ''
        },
        infoForm: {
          newPassword: '',
          confirmPassword: '',
          email: '',
          qq: '',
          gender: '',
          motto: ''
        }
      };
    },
    methods: {
      submitForm() {
        // 提交表单逻辑
        console.log('提交表单', this.authForm, this.infoForm);
      }
    }
  };
  </script>
  
  <style scoped>
  .change-info {
    margin: 20px auto;
    max-width: 600px;
    text-align: left; /* 设置整体内容左对齐 */
  }
  
  .title {
    text-align: left; /* 设置大标题左对齐 */
  }
  
  .auth,
  .new-info {
    margin-top: 20px;
  }
  
  h2 {
    font-size: 18px;
    margin-bottom: 10px;
  }
  
  .el-form-item {
    text-align: left !important; /* 设置表单项左对齐 */
  }
  </style>
  