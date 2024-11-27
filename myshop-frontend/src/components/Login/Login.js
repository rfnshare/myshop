import axios from 'axios';
import config from '../../config/config';  // Import config

export default {
  name: "Login",
  data() {
    return {
      username: '',
      password: '',
      errorMessage: "",
    };
  },
  methods: {
    async handleLogin() {
      const payload = {
        username: this.username,
        password: this.password
      };
      try {
        const response = await axios.post(`${config.base_url}/users/login/`, payload);
        console.log(response.data)
        // Correct keys based on API response
        localStorage.setItem('access_token', response.data.access);  // Use 'access' key from API response
        localStorage.setItem('refresh_token', response.data.refresh);  // Use 'refresh' key from API response

        // Redirect to the dashboard on successful login
        if (response.data.is_staff === true)
        {
          await this.$router.push("/admin/dashboard");
        }
        else {
          await this.$router.push('/dashboard');
          console.log("Login successful as user");
        }

      } catch (error) {
        console.error("Login failed:", error.response?.data || error.message);
        this.errorMessage = error.response?.data?.message || "Login failed. Please try again.";
      }

    }
  }
};