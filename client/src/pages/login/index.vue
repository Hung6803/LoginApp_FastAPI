<template>
  <form @submit.prevent="Login()">
    <a-card title="Đăng nhập" style="width: 100%">
      <div class="row mb-3">
        <div class="col-12 col-sm-3 text-start text-sm-end">
          <label>
            <span class="text-danger me-1">*</span>
            <span>Email:</span>
          </label>
        </div>
        <div class="col-12 col-sm-5">
          <a-input placeholder="Email" allow-clear v-model:value="email"/>
          <div class="w-100"></div>
          <small>{{error_email}}</small>
        </div>
      </div>
      <div class="row mb-3">
        <div class="col-12 col-sm-3 text-start text-sm-end">
          <label>
            <span class="text-danger me-1">*</span>
            <span>Mật khẩu:</span>
          </label>
        </div>
        <div class="col-12 col-sm-5">
          <a-input-password placeholder="Mật khẩu" allow-clear v-model:value="password"/>
          <div class="w-100"></div>
          <small>{{error_password}}</small>
        </div>
      </div>

      <div class="row mb-3">
        <div class="col-12 d-sm-flex justify-content-center">
          <a-button type="primary" html-type="submit"><span>Login</span></a-button>
        </div>
      </div>

      <div class="row mb-3">
        <div class="col-12 d-sm-flex justify-content-right">
          Or
          <a>
            <router-link :to="{name: 'login-register'}">
              <span>register now!</span>
            </router-link>
          </a>
        </div>
      </div>
    </a-card>
  </form>
</template>

<script>
import {defineComponent, ref, reactive, toRefs} from "vue";
import {message} from "ant-design-vue";
import {useRouter} from "vue-router";

export default defineComponent({
  setup(){
    const formState = reactive({
      email: '',
      password: '',
      remember: true,
    });
    const router = useRouter();
    const error_password = ref("")
    const error_email = ref("")
    const Login = () =>{
      if (formState.email === ""){
        error_email.value = "Vui lòng nhập Email!";
      }
      else if (formState.password === ""){
        error_password.value = "Vui lòng nhập mật khẩu!";
        error_email.value = "";
      }
      else {
        axios.get(`http://127.0.0.1:8000/user/login/${formState.email}/${formState.password}`)
            .then(function (response) {
              if (response.data) {
                message.success("Đăng nhập thành công!");
                router.push({name: 'admin-users'});
              } else{
                message.error("Tài khoản hoặc mật khẩu không đúng!");
              }
            })
            .catch(function (error) {
              message.error("Tài khoản hoặc mật khẩu không đúng!")
            });
      }
    };

    return {
      Login,
      ...toRefs(formState),
      error_email,
      error_password,
    };
  },
})
</script>
