<template>
  <el-menu mode="horizontal" :default-active="this.$store.state.activeTitle" :router="true">
    <img src = "@/assets/favicon.png" style="margin-top: 10px; margin-right: 20px"  class="icon">
    <el-menu-item index="/">
      <el-icon>
        <Lollipop />
      </el-icon>
      首页
    </el-menu-item>
    <el-menu-item v-if="this.$store.state.uid" index="/problem">
      <el-icon>
        <Files />
      </el-icon>
      题库
    </el-menu-item>
    <el-menu-item v-if="this.$store.state.uid" index="/contest">
      <el-icon>
        <Trophy />
      </el-icon>
      比赛
    </el-menu-item>
    <el-menu-item v-if="this.$store.state.uid" index="/submission">
      <el-icon>
        <DataAnalysis />
      </el-icon>
      提交记录
    </el-menu-item>
    <el-menu-item v-if="!this.$store.state.uid" index="/user/login">
      <el-icon>
        <User />
      </el-icon>
      登录
    </el-menu-item>
    <el-menu-item v-if="!this.$store.state.uid" index="/user/reg">
      <el-icon>
        <CircleCheck />
      </el-icon>
      注册
    </el-menu-item>
    <el-sub-menu index="/user" v-if="this.$store.state.uid">
      <template #title>
        <el-icon>
          <User />
        </el-icon>
        {{ this.$store.state.name }}
      </template>
      <el-menu-item :index="/user/ + this.$store.state.uid">
        <el-icon>
          <UserFilled />
        </el-icon>
        个人主页
      </el-menu-item>
      <el-menu-item index="/user/userEdit">
        <el-icon>
          <Edit />
        </el-icon>
        编辑资料
      </el-menu-item>
      <span @click="logout">
        <el-menu-item>
          <el-icon>
            <Close />
          </el-icon>
          退出登录
        </el-menu-item>
      </span>
    </el-sub-menu>
  </el-menu>
</template>

<script>
import axios from 'axios';
export default {
  name: "NavMenu",
  data() {
    return {
      uid: 0,
      name: "/",
      gid: 1,
      money: 50,
      curPath: '',
      
    }
  },
  methods: {
    logout() {
     axios.get('http://127.0.0.1:8000/logout').then(() => {
        window.sessionStorage.clear();
        localStorage.setItem('uid',0);
        this.$store.commit('setUid', 0);
        this.$store.commit('setName','/');
     });
     this.$router.push('/');
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