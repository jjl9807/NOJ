/*import { createStore } from 'vuex'

export default createStore({
    state: {
        uid: 1,
        name: "/",
        gid: 0,
        ip: '',
        path: '',
    },
    mutations: {},
    actions: {},
    modules: {}
})
*/

import { createStore } from 'vuex'

// 从本地存储中读取初始状态
const initialState = {
  uid: localStorage.getItem('uid') || 0,
  name: localStorage.getItem('name') || '/',
  gid: localStorage.getItem('gid') || 0,
  ip: localStorage.getItem('ip') || '',
  path: localStorage.getItem('path') || '',
};

export default createStore({
  state: initialState,
  mutations: {
    // 在 mutations 中定义修改状态的方法，并在其中更新状态的同时保存到本地存储
    setUid(state, uid) {
      state.uid = uid;
      localStorage.setItem('uid', uid);
      localStorage.uid = uid;
    },
    setName(state, name) {
      state.name = name;
      localStorage.setItem('name', name);
    },
    setGid(state, gid) {
      state.gid = gid;
      localStorage.setItem('gid', gid);
    },
    setIp(state, ip) {
      state.ip = ip;
      localStorage.setItem('ip', ip);
    },
    setPath(state, path) {
      state.path = path;
      localStorage.setItem('path', path);
    },
  },
  actions: {},
  modules: {}
})
