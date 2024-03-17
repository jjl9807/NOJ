<template>
    <div style="text-align: center; margin: 0 auto; max-width: 1200px">
      <!-- 正在进行或即将到来的比赛列表 -->
      <el-card class="box-card" shadow="hover">
        <template #header>
          <div class="card-header">
            正在进行或即将到来的比赛
          </div>
        </template>
        <el-table :data="ongoingContests" height="300px" :header-cell-style="{ textAlign: 'center' }"
          :cell-style="{ textAlign: 'center' }">
          <el-table-column prop="title" label="比赛名称" min-width="20%">
            <template #default="scope">
              <span>{{ scope.row.title }}</span>
            </template>
          </el-table-column>
          <el-table-column prop="start" label="开始时间" min-width="20%">
            <template #default="scope">
              <span>{{ scope.row.start }}</span>
            </template>
          </el-table-column>
          <el-table-column prop="length" label="时长" min-width="10%">
            <template #default="scope">
              <span>{{ scope.row.length }} min</span>
            </template>
          </el-table-column>
          <el-table-column prop="type" label="类型" min-width="10%">
            <template #default="scope">
              <span>{{ scope.row.type }}</span>
            </template>
          </el-table-column>
          <el-table-column prop="playerCnt" label="报名人数" min-width="10%">
            <template #default="scope">
              <span>{{ scope.row.playerCnt }}</span>
            </template>
          </el-table-column>
        </el-table>
      </el-card>
  
      <!-- 已结束的比赛列表 -->
      <el-card class="box-card" shadow="hover">
        <template #header>
          <div class="card-header">
            已结束的比赛
          </div>
        </template>
        <el-table :data="finishedContests" height="300px" :header-cell-style="{ textAlign: 'center' }"
          :cell-style="{ textAlign: 'center' }">
          <el-table-column prop="title" label="比赛名称" min-width="20%">
            <template #default="scope">
              <span>{{ scope.row.title }}</span>
            </template>
          </el-table-column>
          <el-table-column prop="start" label="开始时间" min-width="20%">
            <template #default="scope">
              <span>{{ scope.row.start }}</span>
            </template>
          </el-table-column>
          <el-table-column prop="length" label="时长" min-width="10%">
            <template #default="scope">
              <span>{{ scope.row.length }} min</span>
            </template>
          </el-table-column>
          <el-table-column prop="type" label="类型" min-width="10%">
            <template #default="scope">
              <span>{{ scope.row.type }}</span>
            </template>
          </el-table-column>
          <el-table-column prop="playerCnt" label="报名人数" min-width="10%">
            <template #default="scope">
              <span>{{ scope.row.playerCnt }}</span>
            </template>
          </el-table-column>
        </el-table>
      </el-card>
    </div>
  </template>
  
  <script>
  import { ElMessage } from 'element-plus';
  
  export default {
    name: 'ContestList',
    data() {
      return {
        ongoingContests: [], // 正在进行或即将到来的比赛
        finishedContests: [], // 已结束的比赛
      };
    },
    mounted() {
      this.fetchContests();
    },
    methods: {
      // 获取比赛列表数据
      async fetchContests() {
        try {
          // 模拟正在进行或即将到来的比赛数据（假设从接口获取）
          const ongoingData = await this.getOngoingContestsFromAPI();
          this.ongoingContests = ongoingData;
  
          // 模拟已结束的比赛数据（假数据）
          const finishedData = this.getFinishedContestsFakeData();
          this.finishedContests = finishedData;
        } catch (error) {
          ElMessage({
            message: '获取比赛列表失败' + error.message,
            type: 'error',
            duration: 2000,
          });
        }
      },
  
      // 获取正在进行或即将到来的比赛数据（假设从接口获取）
      async getOngoingContestsFromAPI() {
        // 假设从接口获取数据
      },
  
      // 获取已结束的比赛假数据
      getFinishedContestsFakeData() {
        return [
          {
            title: '已结束比赛1',
            start: '2024-03-15 10:00:00',
            length: 120,
            type: '编程',
            playerCnt: 50
          },
          {
            title: '已结束比赛2',
            start: '2024-03-14 09:00:00',
            length: 90,
            type: '数学竞赛',
            playerCnt: 30
          },
          // 可以根据需要添加更多假数据
        ];
      },
    },
  };
  </script>
  
  <!-- 样式部分略，保持原样式 -->
  