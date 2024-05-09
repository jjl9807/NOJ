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
            <el-table-column prop="status" label="状态">
  <template v-slot="{ row }">
    <span v-html="formatStatus(row)"></span>
  </template>
</el-table-column>

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
  let testCases = [];
  if (this.$route.params.sid == 1) {
    testCases = [
      { testCase: "Test#1", status: "Accepted", time: "1ms", memory: "6.43MB" },
      { testCase: "Test#2", status: "Accepted", time: "1ms", memory: "6.43MB" },
      { testCase: "Test#3", status: "Accepted", time: "1ms", memory: "6.43MB" },
      { testCase: "Test#4", status: "Accepted", time: "1ms", memory: "6.43MB" },
      { testCase: "Test#5", status: "Accepted", time: "1ms", memory: "6.43MB" },
      { testCase: "Test#6", status: "Accepted", time: "1ms", memory: "6.43MB" },
      { testCase: "Test#7", status: "Accepted", time: "1ms", memory: "6.43MB" },
      { testCase: "Test#8", status: "Accepted", time: "1ms", memory: "6.43MB" },
      { testCase: "Test#9", status: "Accepted", time: "1ms", memory: "6.43MB" },
      { testCase: "Test#10", status: "Accepted", time: "1ms", memory: "6.43MB" },
    ];
  } else if (this.$route.params.sid == 2) {
    testCases = [
      { testCase: "Test#1", status: "Wrong Answer", time: "1ms", memory: "5.22MB" },
      { testCase: "Test#2", status: "Wrong Answer", time: "1ms", memory: "5.22MB" },
      { testCase: "Test#3", status: "Wrong Answer", time: "1ms", memory: "5.22MB" },
      { testCase: "Test#4", status: "Wrong Answer", time: "1ms", memory: "5.22MB" },
      { testCase: "Test#5", status: "Wrong Answer", time: "1ms", memory: "5.22MB" },
      { testCase: "Test#6", status: "Wrong Answer", time: "1ms", memory: "5.22MB" },
      { testCase: "Test#7", status: "Wrong Answer", time: "1ms", memory: "5.22MB" },
      { testCase: "Test#8", status: "Wrong Answer", time: "1ms", memory: "5.22MB" },
      { testCase: "Test#9", status: "Wrong Answer", time: "1ms", memory: "5.22MB" },
      { testCase: "Test#10", status:"Wrong Answer", time: "1ms", memory: "5.22MB" },
    ];
  } else {
    testCases = [
      { testCase: "Test#1", status: "Time Limit Exceeded", time: "2001ms", memory: "9.84MB" },
      { testCase: "Test#2", status: "Time Limit Exceeded", time: "2001ms", memory: "9.84MB" },
      { testCase: "Test#3", status: "Time Limit Exceeded", time: "2001ms", memory: "9.84MB" },
      { testCase: "Test#4", status: "Time Limit Exceeded", time: "2001ms", memory: "9.84MB" },
      { testCase: "Test#5", status: "Time Limit Exceeded", time: "2001ms", memory: "9.84MB" },
      { testCase: "Test#6", status: "Time Limit Exceeded", time: "2001ms", memory: "9.84MB" },
      { testCase: "Test#7", status: "Time Limit Exceeded", time: "2001ms", memory: "9.84MB" },
      { testCase: "Test#8", status: "Time Limit Exceeded", time: "2001ms", memory: "9.84MB" },
      { testCase: "Test#9", status: "Time Limit Exceeded", time: "2001ms", memory: "9.84MB" },
      { testCase: "Test#10", status: "Time Limit Exceeded", time: "2001ms", memory: "9.84MB" },

    ];
  }

  return {
    submittedCode: this.$store.state.code,
    sid: this.$route.params.sid,
    testCases: testCases,
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
      formatStatus(row) {
    if (row.status === 'Accepted') {
      return '<span style="color: green;">' + row.status + '</span>';
    } else if(row.status == 'Time Limit Exceeded'){
      return '<span style="color: purple;">' + row.status + '</span>';
    }else{
      return '<span style="color: red;">' + row.status + '</span>';

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
    height: auto;
    overflow: auto;
  }
  
  .code-content {
    text-align: left;
  }
  </style>
  