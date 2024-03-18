<template>
  <div class="m-4 container mx-auto px-10">
    <button
      @click="addUser"
      class="my-5 px-4 py-2 text-gray-100 text-bold bg-amber-600 hover:bg-amber-800 dark:bg-slate-800 dark:hover:bg-slate-700"
    >
      Add User
    </button>
    <data-table
      ref="myDataTable"
      :defaultSortBy="defaultSorting.by"
      :defaultSortDesc="defaultSorting.desc"
      :columns="columns"
      :is_ssp_mode="is_ssp_mode"
      :url="url"
    >
      <template v-slot:editBtn="{ data }">
        <a
          href="#"
          class="bg-amber-600 hover:bg-amber-800 mr-1 text-center inline-block p-1"
          @click="editUser(data)"
        >
          <PencilSquareIcon class="w-4 text-gray-100" />
        </a>
      </template>
    </data-table>
  </div>

  <user-form
    v-model:dlgVisible="_dlgVisible"
    :title="_title"
    ref="uf"
    @refreshTable="refreshTable"
  ></user-form>
</template>

<script lang="ts" setup>
import { ref, nextTick } from "vue";
// import DataTable from "vue-tailwind-datatable";
import DataTable from "./DataTable.vue";
import { PencilSquareIcon } from "@heroicons/vue/24/solid";
import { layer } from "@layui/layui-vue";
import UserForm from "./UserForm.vue";
import service from "../api/index.js";

const uf = ref();
const url = "/get_user_list";

const _dlgVisible = ref(false);
const _title = ref("Add User");

const myDataTable = ref(null);
const editUser = (obj) => {
  //alert('Now should showing edit form for User ID '+obj.uid+' name '+ obj.name+' gender '+ obj.gender);
  nextTick(() => {
    uf.value.initUI(obj);
    _dlgVisible.value = true;
  });
};

const addUser = () => {
  // layer.msg("成功消息", { icon : 1, time: 1000})
  // console.log(myDataTable)
  // myDataTable.value.reload()
  nextTick(() => {
    uf.value.initUI();
    _dlgVisible.value = true;
  });
};

const defaultSorting = reactive({
  by: "email",
  desc: true,
});

const columns = ref([
  {
    db: "uid",
    label: "ID",
    class: ["text-center"],
    sortable: false,
  },
  {
    db: "name",
    label: "Name",
    class: ["text-center"],
    sortable: false,
  },
  {
    db: "gender",
    label: "Gender",
    class: ["text-center"],
    sortable: false,
  },
  {
    db: "edit",
    label: "Edit",
    class: ["text-center"],
    sortable: false,
  },
]);

const is_ssp_mode = ref(true);

const data = ref([
  {
    uid: 2,
    name: "john",
    gender: "john@gmail.com",
    edit: [{ slotName: "editBtn", user_id: 2 }],
  },
]);


const refreshTable = () => {
  myDataTable.value.reload();
}


/*
const getUserList = () => {
  let url = "/get_user_list";
  let layIndex = layer.load(0);
  service.post(url, {}).then((res) => {
    layer.close(layIndex);
    if(res.code == 200){
      data.value = res.list
    } else {
      layer.confirm(res.msg,{title:'Message'})
    }
  }).catch((err) => {
    layer.close(layIndex);
    console.log(err)
    layer.confirm(err,{title:'Message'})
  })
}


onMounted(() => {
  getUserList();
})
*/
</script>


<style>
</style>