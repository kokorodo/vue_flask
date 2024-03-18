<template>
  <lay-layer
    v-model="_p.dlgVisible"
    :shadeClose="false"
    :title="_p.title"
    :shade="true"
    :area="['500px', '450px']"
    :btn="action11"
    :close="clsDlg"
  >
    <div class="m-4 container mx-auto px-10">
      <label class="block my-2">
        <span class="inline-block w-20">Name: </span>
        <input type="text" class="form-input px-4 py-1 w-80" v-model="name" />
      </label>
      <label class="block my-2">
        <span class="inline-block w-20">Gender: </span>
        <select class="px-4 py-1 w-80" v-model="gender">
          <option value=""></option>
          <option value="male">male</option>
          <option value="female">famale</option>
        </select>
      </label>
    </div>
  </lay-layer>
</template>

<script lang="ts" setup>
import { ref,defineExpose  } from "vue";
import { layer } from "@layui/layui-vue";
import service from "../api/index.js";

const uid = ref(0);
const name = ref("");
const gender = ref("");

const _p = defineProps({
  dlgVisible: {
    type: Boolean,
    default: false,
  },
  title: {
    type: String,
    default: "User Information",
  },
});

const emit = defineEmits(["update:dlgVisible","refreshTable"]);

const refreshParentTable = () => {
  emit("refreshTable");
}

const clsDlg = () => {
  layer.confirm("Are you sure?", {
    title:'Message',
    btn: [
      {
        text: "Yes",
        callback: (id) => {
          layer.close(id);
          emit("update:dlgVisible", false);
        },
      },
      {
        text: "No",
        callback: (id) => {
          layer.close(id);
        },
      },
    ],
  });
};

const action11 = ref([
  {
    text: "Confirm",
    callback: () => {
      // layer.confirm(
      //   "确认操作 name : " + name.value + ", gender : " + gender.value,
      //   { shade: false }
      // );
      saveUser();
    },
  },
  {
    text: "Cancel",
    callback: () => {
      layer.confirm("Are you sure?", {
        title:'Message',
        btn: [
          {
            text: "Yes",
            callback: (id) => {
              layer.close(id);
              emit("update:dlgVisible", false);
            },
          },
          {
            text: "No",
            callback: (id) => {
              layer.close(id);
            },
          },
        ],
      });
    },
  },
]);


const initUI = (obj) =>{
  if(typeof(obj) == 'undefined' || null == obj){
    name.value = '';
    gender.value = '';
  } else {
    uid.value = obj.uid
    name.value = obj.name;
    gender.value = obj.gender;
  }

}

const saveUser = () => {
  let url = "/add_user";
  let data = {name : name.value, gender : gender.value};
  if(typeof(uid.value) != 'undefined' && uid.value != 0){
    url = '/edit_user';
    data['uid'] = uid.value;
  }


  // console.log('let url ' + url)
  let layIndex = layer.load(0);
  service.post(url, data).then((res) => {
    layer.close(layIndex);
    if(res.code == 200){
      layer.confirm('Save User Success',{title:'Message'})
      emit("update:dlgVisible", false);
      refreshParentTable()
    } else {
      layer.confirm(res.msg,{title:'Message'})
    }
  }).catch((err) => {
    layer.close(layIndex);
    console.log(err)
    layer.confirm(err,{title:'Message'})
  })
};

// 将父组件要调用的方法抛出去
defineExpose({ initUI })
</script>

<style>
</style>