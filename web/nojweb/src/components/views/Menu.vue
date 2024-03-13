<template>
    <div id="NavMenu">
      <el-menu
          :default-active="toIndex"
          class="el-menu-demo"
          text-color="#000000"
          active-text-color="#3989fa"
          mode="horizontal"
          @select="handleSelect"
      >
      <el-menu-item index="/">
      <el-icon>
        <Lollipop />
      </el-icon>
      首页
    </el-menu-item>
    <el-menu-item index="/user/login">
      <el-icon>
        <Lollipop />
      </el-icon>
      登录
    </el-menu-item>
    <el-menu-item index="/user/reg">
      <el-icon>
        <Lollipop />
      </el-icon>
      注册
    </el-menu-item>
      </el-menu>
      <el-main>
        <router-view></router-view>
      </el-main>
    </div>
  </template>
  
  <script>
  export default {
    name: "NavMenu",
    
    computed: {
      toIndex(){  // 根据路径绑定到对应的一级菜单，防止页面刷新重新跳回第一个
        return '/' + this.$route.path.split('/')[1];
      },
    },
    methods: {
      handleSelect(path){  // 切换菜单栏
        this.$router.push({
          path: path
        });
      },
    },
  
  };
  </script>
  
  <style scoped>
  </style>
  ./Menu.vue