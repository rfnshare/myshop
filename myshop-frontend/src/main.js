// main.js or main.ts
import { createApp } from 'vue';
import App from './App.vue';
import router from './router';

// Import Bootstrap 5 CSS
import "bootstrap/dist/css/bootstrap.css";

// Import Bootstrap 5 JS
import "bootstrap/dist/js/bootstrap.bundle.min.js"; // bundle.js includes Popper.js, no need for jQuery

createApp(App).use(router).mount('#app');
