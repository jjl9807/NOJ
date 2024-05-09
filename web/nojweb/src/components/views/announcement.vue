<template>
  <el-row style="margin: auto; max-width: 1500px;">
    <el-col :xs="24" :sm="24" :md="16">
      <el-card class="box-card" shadow="hover">
        <template #header>
          <div class="card-header">
            公告栏
          </div>
        </template>
        <el-scrollbar wrap-class="announcement-scroll">
          <el-table :data="announcements" v-loading="loading" height="100%">
            <el-table-column prop="title" label="标题" min-width="60%">
              <template #default="scope">
                <span class="rlink" @click="$router.push('/announcement/' + scope.row.aid)">
                  {{ scope.row.title }}
                </span>
              </template>
            </el-table-column>
            <el-table-column prop="time" label="发布时间" min-width="40%" />
          </el-table>
        </el-scrollbar>
      </el-card>
    </el-col>
    <el-col :xs="24" :sm="24" :md="8">
      <div class="image-container">
        <img src="@/assets/logo.png" alt="Image" />
      </div>
    </el-col>
  </el-row>
</template>

<script>
export default {
  name: 'myAnnoucement',
  data() {
    return {
      announcements: [], // 公告数据
      loading: true // 加载状态
    };
  },
  methods: {
    // 模拟加载公告数据
    async fetchAnnouncements() {
      // 模拟异步加载数据，此处应替换为实际的数据获取方式
      await new Promise(resolve => setTimeout(resolve, 100)); // 模拟异步加载延迟
      this.announcements = [
        { aid: 1, title: "NOJ征题公告", time: "2024-03-16" },
        { aid: 2, title: "竞赛公告", time: "2024-03-15" },
        { aid: 3, title: "系统维护通知", time: "2024-03-14" }
        // 添加更多公告数据
      ];
      this.loading = false; // 加载完成
    }
  },
  mounted() {
    this.fetchAnnouncements(); // 页面加载时加载公告数据
  }
};
</script>

<style>
.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 20px;
  font-weight: bolder;
  /* font-size: 18px;
  font-weight: bold;
  padding: 20px; */
}

.announcement-scroll {
  /* height: calc(100% - 40px); 公告栏占据屏幕的垂直三分之一减去标题栏的高度 */
  overflow: auto;
}

.rlink {
  cursor: pointer;
}

.image-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 33vh; /* 占据屏幕的垂直三分之一 */
}

.image-container img {
  max-width: 100%;
  max-height: 100%;
}
</style>
