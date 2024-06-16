<template>
  <a-card title="Users" style="width: 100%">
    <div class="row md-3">
      <div class="col-12 d-flex justify-content-end">
        <a-button type="primary">
          <router-link :to="{name: 'admin-users-create'}">
            <font-awesome-icon :icon="['fas', 'plus']" />
          </router-link>
        </a-button>
      </div>
    </div>
    <div class="row">
      <div class="col-12">
        <a-table :dataSource="users" :columns="columns" :scroll="{ x: 576}">
          <template #bodyCell="{column, record}">
            <template v-if="column.key==='action'">
              <router-link :to="{ name: 'admin-users-edit', params: { id: record.id }}" >
                <a-button type="primary" class="me-sm-2 mb-2">
                  <font-awesome-icon :icon="['far', 'pen-to-square']"/>
                </a-button>
              </router-link>
              <a-button type="primary" danger @click="deleteUser(record.id)">
                  <font-awesome-icon :icon="['fas', 'trash']" />
              </a-button>
            </template>
          </template>
        </a-table>
      </div>
    </div>
  </a-card>
</template>

<script>
  import { defineComponent, ref} from "vue";
  import dayjs from "dayjs";

  export default defineComponent( {
    setup(){
      const users = ref([]);

      const columns = [
          {
            title: 'Mã',
            dataIndex: 'id',
            key: 'id',
          },
          {
            title: 'Họ',
            dataIndex: 'first_name',
            key: 'first_name',
          },
          {
            title: 'Tên',
            dataIndex: 'last_name',
            key: 'last_name',
          },
          {
            title: 'SDT',
            dataIndex: 'phone_number',
            key: 'phone_number',
          },
          {
            title: 'Email',
            dataIndex: 'email',
            key: 'email',
          },
          {
            title: 'Công cụ',
            key: 'action',
            fixed: 'right',
          },
      ];

      const deleteUser = (id) =>{
        axios.delete(`http://127.0.0.1:8000/user/${id}`,{
        headers: {Authorization: `Bearer ${localStorage.getItem('token')}`}})
            .then(function (response) {
              if (response.status === 200) {
                getUsers();
              }
            })
            .catch(function (error) {
              console.log(error);
            })
      }
      const getUsers = () => {
        axios.get('http://127.0.0.1:8000/user/', {
        headers: {Authorization: `Bearer ${localStorage.getItem('token')}`}})
          .then(function (response) {
            users.value = response.data;
          })
          .catch(function (error) {
            console.log(error);
          });
      };

      getUsers();

      return {
        users,
        columns,
        deleteUser
      }
    }
  });
</script>
<style scoped>

</style>