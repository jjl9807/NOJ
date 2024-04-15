<template>
    <el-menu mode="horizontal" :default-active="this.$store.state.activeTitle" :router="true">
      <el-menu-item index="/problem/ + this.$route.params.pid" >
        <el-icon>
          <Lollipop />
        </el-icon>
        描述
      </el-menu-item>
      <el-menu-item  index="/problem/+this.$route.params.pid+ /submission">
        <el-icon>
          <Files />
        </el-icon>
        提交
      </el-menu-item>
    </el-menu>
  </template>
  
  <script>
  
  export default {
    name: "problemMenu",
    data() {
      return {
        pid:this.$route.params.pid,
      }
    },
    methods: {
      logout() {
      },
    }
  }
  </script>
  
  <style>
  .icon {
    border-radius: 5px;
    width: 40px;
    height: 40px;
  }
  
  .pd .el-dialog__body {
    padding: 0;
  }
  
  .el-divider--horizontal {
    margin: 10px 0;
  }
  
  .el-menu--collapse .el-menu .el-submenu,
  .el-menu--popup {
    min-width: 100px !important;
    font-size: 10px;
  }
  
  .el-menu {
    justify-content: center;
  }
  </style>