<template>
    <div class="oj-page">
      <!-- 已提交的代码显示区域 -->
      <div class="code-display" ref="codeDisplay">
        <el-card>
          <template #header>
            <span>已提交的代码</span>
          </template>
          <pre class="code-content">{{ submittedCode }}</pre>
        </el-card>
      </div>
  
      <!-- 测试用例列表 -->
      <div class="test-cases" ref="testCases">
        <el-card>
          <template #header>
            <span>测试用例</span>
          </template>
          <el-table :data="testCases" border>
            <el-table-column prop="testCase" label="测试用例"></el-table-column>
            <el-table-column prop="status" label="状态"></el-table-column>
            <el-table-column prop="time" label="时间"></el-table-column>
            <el-table-column prop="memory" label="内存"></el-table-column>
          </el-table>
        </el-card>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name:"submissionDetail",
    data() {
      return {
        submittedCode: `#include <iostream>
  using namespace std;
  
  int main() {
      cout << "Hello, World!";
      return 0;
  }`, // 模拟已提交的代码
        testCases: [
          { testCase: "Test#1", status: "Accepted", time: "100ms", memory: "10MB" },
          { testCase: "Test#2", status: "Wrong Answer", time: "-", memory: "-" },
          // 可以根据需要添加更多的测试用例数据
        ],
      };
    },
    mounted() {
    this.mounted = true;
    this.sid = this.$route.params.sid;
      // 添加滚动条
      this.$refs.codeDisplay.addEventListener('scroll', this.handleScroll);
      this.$refs.testCases.addEventListener('scroll', this.handleScroll);
    },
    beforeUnmount() {
      // 移除滚动条监听事件
      this.$refs.codeDisplay.removeEventListener('scroll', this.handleScroll);
      this.$refs.testCases.removeEventListener('scroll', this.handleScroll);
    },
    methods: {
      handleScroll(event) {
        // 在这里处理滚动事件，例如同步滚动两个区域
        const target = event.target;
        if (target === this.$refs.codeDisplay) {
          this.$refs.testCases.scrollTop = target.scrollTop;
        } else if (target === this.$refs.testCases) {
          this.$refs.codeDisplay.scrollTop = target.scrollTop;
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .oj-page {
    display: flex;
    justify-content: space-around;
    margin-top: 20px;
  }
  
  .code-display,
  .test-cases {
    width: 45%;
    height: 300px;
    overflow: auto;
  }
  
  .code-content {
    text-align: left;
  }
  </style>
  