import axios from "axios";
import { layer } from "@layui/layui-vue";

let debounceTime = 0;

// 创建axios实例
const service = axios.create({
  baseURL: import.meta.env.VITE_API,
  timeout: 30000,
  validateStatus: (status) => status === 200, // 200 外的状态码都认定为失败
});

// 添加请求拦截器
service.interceptors.request.use(
  (config) => {
    // if (store.getters.token) {
    //   config.headers["Authentication"] = getCookie("token");
    // }
    config.headers['Access-Control-Allow-Origin'] = '*';
    return config;
    },
  (error) => Promise.reject(error)
);

// 添加响应拦截器
service.interceptors.response.use(
  (response) => {
    console.log(response)
    const res = response.data;

    if (response.status !== 200) {
      const { data, url, method, params } = response.config;

      const errorInfo = `错误消息：${res.msg}；失败Code：${res.code}；失败接口地址：${url}；参数：${method === "get" ? JSON.stringify(params) : data}；`;
      //layer.alert(res.msg);
      layer.notify({
        title:"Message",
        content:res.msg,
        icon:1
      })

      return Promise.reject(new Error(errorInfo || "Error"));
    }
    if (res.status === "error") {
      // alert(res.message);
      layer.notify({
        title:"Message",
        content:res.msg,
        icon:1
      })
    } else {
      // res.msg && alert(res.message);
      return res;
    }
  },
  (error) => {
    const { status, data } = error.response;
    // const {status, config, data} = error.response
    console.log(error.response);

    debounceTime && clearTimeout(debounceTime);
    debounceTime = setTimeout(() => {
      // 401 没token
      if (status === 401) {
        // alert(`Message：${status}，Current Request hava not token`);
        layer.notify({
          title:"Message",
          content:`Message：${status}，Current Request hava not token`,
          icon:1
        })
      } else if (status === 402) {
        // 402 被登出
        // removeCookie('token');
      }
    }, 100);
    return Promise.reject(error);
  }
);

export default service;
