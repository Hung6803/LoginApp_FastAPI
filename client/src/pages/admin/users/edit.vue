<template>
  <form @submit.prevent="editUsers()">
    <a-card title="Cập nhật tài khoản" style="width: 100%">
    <div class="row mb-3">
      <div class="col-12 col-sm-3 text-start text-sm-end">
        <label>
          <span class="text-danger me-1">*</span>
          <span>Họ:</span>
        </label>
      </div>
      <div class="col-12 col-sm-5">
        <a-input placeholder="Họ và tên đệm" allow-clear v-model:value="first_name"/>
      </div>
    </div>
    <div class="row mb-3">
      <div class="col-12 col-sm-3 text-start text-sm-end">
        <label>
          <span class="text-danger me-1">*</span>
          <span>Tên:</span>
        </label>
      </div>
      <div class="col-12 col-sm-5">
        <a-input placeholder="Tên" allow-clear v-model:value="last_name"/>
      </div>
    </div>
    <div class="row mb-3">
      <div class="col-12 col-sm-3 text-start text-sm-end">
        <label>
          <span class="text-danger me-1">*</span>
          <span>Số điện thoại:</span>
        </label>
      </div>
      <div class="col-12 col-sm-5">
        <a-input placeholder="Số điện thoại" allow-clear v-model:value="phone_number"/>
      </div>
    </div>
    <div class="row mb-3">
      <div class="col-12 col-sm-3 text-start text-sm-end">
        <label>
          <span class="text-danger me-1">*</span>
          <span>Email:</span>
        </label>
      </div>
      <div class="col-12 col-sm-5">
        <a-input placeholder="Email" allow-clear v-model:value="email"/>
      </div>
    </div>
    <div class="row mb-3">
      <div class="col-12 col-sm-3 text-start text-sm-end">

      </div>
      <div class="col-12 col-sm-5">
        <a-checkbox v-model:checked="change_password">
          Đổi mật khẩu
        </a-checkbox>
      </div>
    </div>
    <div class="row mb-3" v-if="change_password == true">
      <div class="col-12 col-sm-3 text-start text-sm-end">
        <label>
          <span class="text-danger me-1">*</span>
          <span>Mật khẩu mới:</span>
        </label>
      </div>
      <div class="col-12 col-sm-5">
        <a-input-password placeholder="Mật khẩu" allow-clear v-model:value="password"/>
      </div>
    </div>
    <div class="row mb-3" v-if="change_password == true">
      <div class="col-12 col-sm-3 text-start text-sm-end">
        <label>
          <span class="text-danger me-1">*</span>
          <span>Xác nhận mật khẩu:</span>
        </label>
      </div>
      <div class="col-12 col-sm-5">
        <a-input-password placeholder="Xác nhận mật khẩu" allow-clear v-model:value="password_confirmation"/>
        <div class="w-100"></div>
        <small>{{error_password}}</small>
      </div>
    </div>
    <div class="row mb-3">
      <div class="col-12 d-sm-flex justify-content-center">
        <a-button class="me-2">
          <router-link :to="{name: 'admin-users'}">
            <span>Hủy</span>
          </router-link>
        </a-button>
        <a-button type="primary" html-type="submit"><span>Lưu</span></a-button>
      </div>
    </div>

  </a-card>
  </form>
</template>

<script>
import {defineComponent, ref, reactive,toRefs} from "vue";
import {message} from "ant-design-vue";
import {useRouter} from "vue-router";
import {useRoute} from "vue-router";

export default defineComponent({
  setup(){
    const password_confirmation = reactive({
      password_confirmation: ""
    });
    const change_password = ref(false)
    const error_password = ref("")
    const router = useRouter();
    const route = useRoute();
    const users = reactive({
      first_name: "",
      last_name: "",
      phone_number: "",
      email: "",
      password: ""
    });
    const getUsersbyID = () =>{
      axios.get(`http://127.0.0.1:8000/user/${route.params.id}`)
          .then(function (response) {
            console.log(response);
            users.first_name = response.data.first_name;
            users.last_name = response.data.last_name;
            users.phone_number = response.data.phone_number;
            users.email = response.data.email;
          })
          .catch(function (error) {
            console.log(error);
          })
    }
    const editUsers = () =>{
      if(users["password"] === password_confirmation["password_confirmation"]) {
        axios.put(`http://127.0.0.1:8000/user/edit/${route.params.id}`, users)
        .then(function (response) {
          if (response) {
            message.success("Sửa thông tin thành công!");
            router.push({name: 'admin-users'});
          }
        })
        .catch(function (error) {
          console.log(error);
        });
      } else{
        error_password.value = "Không trùng với mật khẩu!";
      }
    };

    getUsersbyID();

    return {
      editUsers,
      ...toRefs(users),
      ...toRefs(password_confirmation),
      error_password,
      change_password
    };
  },
})
</script>