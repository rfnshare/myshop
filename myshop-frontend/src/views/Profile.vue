<template>
  <div class="profile">
    <div class="profile-card">
      <!-- Profile Picture -->
      <div class="profile-image-container">
        <img :src='userProfilePic'
        alt="Profile Picture"
        class="profile-image"
        />
      </div>

      <!-- User Info -->
      <div class="profile-info">
        <h2>{{userName}}</h2>
        <p><strong>Name:</strong>{{ userFirstName || 'First Name not available' }} {{ userLastName || 'Last Name not available' }}</p>
        <p><strong>Email:</strong> {{ userEmail }}</p>
        <p><strong>Phone:</strong> {{ userPhone }}</p>
      </div>

      <div class="profile-actions">
      <button class="btn btn-update" @click="navigateToUpdateProfile">
        Update Profile
      </button>
      <button @click="logout" class="btn btn-danger">Logout</button>
    </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import config from "../config/config";

export default {
  name: "Profile",
  data() {
    return {
      userName: "",
      userFirstName: "",  // First Name fetched from API
      userLastName: "",   // Last Name fetched from API
      userEmail: "",      // Email fetched from API
      userPhone: "",      // Phone fetched from API
      userProfilePic: "", // Profile picture URL fetched from API
    };
  },
  created() {
    this.fetchProfile();
  },
  methods: {
    async fetchProfile() {
      const accessToken = localStorage.getItem("access_token");

      if (!accessToken) {
        await this.$router.push("/login");
        return;
      }

      try {
        const response = await axios.get(`${config.base_url}/users/profile/`, {
          headers: {
            Authorization: `Bearer ${accessToken}`,
          },
        });

        // Populate the profile data
        this.userName = response.data.username
        this.userFirstName =  response.data.first_name
        this.userLastName =  response.data.last_name
        this.userEmail = response.data.email;
        this.userPhone = response.data.phone_number;

        // Update profile picture if available (optional)
        if (response.data.profile_pic_url) {
          this.userProfilePic = response.data.profile_pic_url;
        }
      } catch (error) {
        if (error.response?.data?.code === "token_not_valid") {
          console.error("Invalid token:", error.response.data.messages[0].message);
          await this.$router.push("/login");
        } else {
          console.error("Error fetching profile:", error.response?.data || error.message);
        }
      }
    },
    navigateToUpdateProfile() {
      this.$router.push("/profile/update");
    },
    async logout() {
      const accessToken = localStorage.getItem("access_token");
      const refreshToken = localStorage.getItem("refresh_token");

      if (!accessToken || !refreshToken) {
        console.error("No tokens found for logout");
        return;
      }

      try {
        await axios.post(
          `${config.base_url}/users/logout/`,
          { refresh: refreshToken },
          {
            headers: {
              Authorization: `Bearer ${accessToken}`,
            },
          }
        );

        // Clear tokens and redirect to login
        localStorage.removeItem("access_token");
        localStorage.removeItem("refresh_token");
        await this.$router.push("/login");
        console.log("Logged out successfully");
      } catch (error) {
        console.error("Logout failed:", error.response?.data || error.message);
      }
    },
  },
};
</script>

<style scoped>
.profile {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #f4f4f4;  /* Light background color for the page */
}
.profile-actions {
  display: flex;
  justify-content: space-between;
  margin-top: 20px;
}
.profile-card {
  background-color: #fff;
  border-radius: 10px;
  padding: 30px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  width: 320px;
  text-align: center;
}

.profile-image-container {
  margin-bottom: 20px;
}

.profile-image {
  width: 100px;
  height: 100px;
  border-radius: 50%; /* Makes the image round */
  object-fit: cover;
  border: 3px solid #e74c3c; /* Red border around the profile picture */
}

.profile-info h2 {
  font-size: 1.5rem;
  color: #333;
  margin: 10px 0;
}

.profile-info p {
  font-size: 1rem;
  color: #777;
  margin: 5px 0;
}

.logout-btn {
  background-color: #e74c3c;
  color: white;
  padding: 10px 20px;
  border: none;
  cursor: pointer;
  border-radius: 5px;
  margin-top: 20px;
  width: 100%;
}

.logout-btn:hover {
  background-color: #c0392b;
}
</style>
