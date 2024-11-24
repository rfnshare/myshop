<template>
  <div class="profile">
    <div class="profile-card">
      <!-- Profile Picture -->
      <div class="profile-image-container">
        <img :src="userProfilePic || '@/assets/profile-icon.svg'"
        alt="Profile Picture"
        class="profile-image"
        />
      </div>

      <!-- User Info -->
      <div class="profile-info">
        <h2>{{ userFirstName || 'First Name not available' }} {{ userLastName || 'Last Name not available' }}</h2>
        <p><strong>Email:</strong> {{ userEmail }}</p>
        <p><strong>Phone:</strong> {{ userPhone }}</p>
      </div>

      <!-- Logout Button -->
      <button @click="logout" class="logout-btn">Logout</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import config from "../config/config";  // Import config to access base URL

export default {
  name: "Profile",
  data() {
    return {
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
      const accessToken = localStorage.getItem('access_token'); // Get access token

      if (!accessToken) {
        this.$router.push('/login'); // If no token, redirect to login
        return;
      }

      try {
        const response = await axios.get(`${config.base_url}/users/profile/`, {
          headers: {
            Authorization: `Bearer ${accessToken}`,  // Pass the access token in the header
          },
        });

        console.log(response);

        // Populate the data with the response from the API
        this.userFirstName = response.data.first_name || '';  // Update first name
        this.userLastName = response.data.last_name || '';    // Update last name
        this.userEmail = response.data.email || '';           // Update email
        this.userPhone = response.data.phone_number || '';    // Update phone number
        this.userProfilePic = response.data.profile_pic_url || ''; // Update profile picture

      } catch (error) {
        // Handle error if token is invalid or expired
        if (error.response?.data?.code === 'token_not_valid') {
          console.error('Invalid or expired token:', error.response.data.messages[0].message);
          this.$router.push('/login');  // Redirect to login if the token is invalid
        } else {
          console.error('Error fetching profile:', error.response?.data || error.message);
        }
      }
    },

    logout() {
      localStorage.removeItem('access_token');
      localStorage.removeItem('refresh_token');
      this.$router.push('/login');  // Redirect to login page after logout
    }
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
