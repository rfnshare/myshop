import axios from "axios";
import config from "../../config/config"; // Import config for base_url

export default {
  name: "Register",
  data() {
    return {
      userName: "",
      firstName: "",  // First name for registration
      lastName: "",   // Last name for registration
      email: "",      // Email for registration
      phone_number: "", // Phone number for registration
      password: "",   // Password for registration
      profilePic: null, // Profile picture file
    };
  },
  methods: {
    handleFileUpload(event) {
      this.profilePic = event.target.files[0]; // Save the uploaded file to data
    },
    async handleRegister() {
      const formData = new FormData(); // Create FormData for file upload
      formData.append("username", this.userName);
      formData.append("first_name", this.firstName);
      formData.append("last_name", this.lastName);
      formData.append("phone_number", this.phone_number); // Fixed: use phone_number
      formData.append("email", this.email);
      formData.append("password", this.password);
      if (this.profilePic) {
        formData.append("profile_pic", this.profilePic);
      }

      try {
        const response = await axios.post(`${config.base_url}/users/register/`, formData, {
          headers: {
            "Content-Type": "multipart/form-data", // Ensure correct content type for file upload
          },
        });
        console.log("Registration successful:", response.data);

        // Redirect to login page on successful registration
        this.$router.push("/login");
      } catch (error) {
        console.error("Registration failed:", error.response?.data || error.message);
      }
    },
  },
};
