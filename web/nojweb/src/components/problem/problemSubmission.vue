<template>
  <div>
    <problemMenu />
  </div>
    <div>
      <el-form ref="submitForm" :model="submitForm" :rules="submitFormRules" label-width="100px">
        <el-form-item label="源文件：" prop="language">
          <el-select v-model="submitForm.language" placeholder="请选择语言">
            <el-option label="C" value="c"></el-option>
            <el-option label="C++" value="cpp"></el-option>
            <el-option label="Java" value="java"></el-option>
            <!-- 其他语言选项 -->
          </el-select>
        </el-form-item>
        <el-form-item label="语言：" prop="editorType">
          <el-radio v-model="submitForm.editorType" label="editor">使用编辑器上传</el-radio>
          <el-radio v-model="submitForm.editorType" label="file">从本地文件上传</el-radio>
        </el-form-item>
  
        <!-- 如果选择使用编辑器上传 -->
        <el-form-item v-if="submitForm.editorType === 'editor'" label="代码：">
          <el-input type="textarea" v-model="submitForm.code"></el-input>
        </el-form-item>
  
        <!-- 如果选择从本地文件上传 -->
        <el-form-item v-else label="选择文件：">
          <el-upload
            class="upload-demo"
            action="/upload"
            :on-success="handleFileUploadSuccess"
            :before-upload="beforeFileUpload"
            :file-list="fileList">
            <el-button size="small" type="primary">点击上传</el-button>
          </el-upload>
        </el-form-item>
  
        <el-form-item>
          <el-button type="primary" @click="submitFormValidate('submitForm')">提交</el-button>
        </el-form-item>
      </el-form>
    </div>
  </template>
  
  <script>
  import problemMenu from './problemMenu'
  export default {
    name: "problemSubmission",
    components:{
      problemMenu
    },
    data() {
      return {
        submitForm: {
          language: '',
          editorType: 'editor', // 默认使用编辑器上传
          code: '',
          file: null // 存储上传的文件
        },
        fileList: []
      };
    },
    methods: {
      handleFileUploadSuccess(response, file, fileList) {
        // 文件上传成功的回调
        this.submitForm.file = file;
        this.fileList = fileList;
      },
      beforeFileUpload(file) {
        // 限制文件类型
        const isAllowedType = ['.cpp', '.c', '.java'].includes(file.name.slice(file.name.lastIndexOf('.')));
        if (!isAllowedType) {
          this.$message.error('只能上传 .cpp/.c/.java 文件');
        }
        return isAllowedType;
      },
      submitFormValidate(formName) {
        this.$refs[formName].validate(valid => {
          if (valid) {
            // 提交表单逻辑
            console.log('提交表单');
            console.log(this.submitForm);
            // 这里可以使用router跳转
          } else {
            return false;
          }
        });
      }
    }
  };
  </script>
  
  <style>
  .upload-demo {
    display: inline-block;
    margin-bottom: 20px;
  }
  
  </style>
  