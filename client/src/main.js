import './assets/main.css'

import { createApp } from 'vue'
import router from "@/router/index.js"
import {Checkbox, InputPassword, Input, Table, Card, Drawer, Button} from "ant-design-vue"
import axios from 'axios'

window.axios = axios;

import App from './App.vue'

import { library } from '@fortawesome/fontawesome-svg-core'
import { fas } from '@fortawesome/free-solid-svg-icons'
import { fab } from '@fortawesome/free-brands-svg-icons'
import { far } from '@fortawesome/free-regular-svg-icons'
library.add(fas, fab, far)

import 'ant-design-vue/dist/reset.css';
import 'bootstrap/dist/css/bootstrap-grid.min.css'
import 'bootstrap/dist/css/bootstrap-utilities.min.css'
import {FontAwesomeIcon} from "@fortawesome/vue-fontawesome";

const app = createApp(App);
app.use(router);
app.component('font-awesome-icon', FontAwesomeIcon)
app.use(Card);
app.use(Checkbox);
app.use(Input);
app.use(InputPassword);
app.use(Table);
app.use(Drawer);
app.use(Button);
app.mount('#app');
