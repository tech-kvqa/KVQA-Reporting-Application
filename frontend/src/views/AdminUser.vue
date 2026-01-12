<template>
    <v-app>
      <!-- Navigation Drawer -->
      <v-navigation-drawer app>
        <v-list>
          <v-list-item link to="/admin/dashboard">
            <v-list-item-content>
              <v-list-item-title>Dashboard</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
  
          <v-list-item link to="/admin/users">
            <v-list-item-content>
              <v-list-item-title>Manage Users</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
  
          <v-list-item link to="/admin/application">
            <v-list-item-content>
              <v-list-item-title>Manage Applications</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-navigation-drawer>
  
      <!-- App Bar -->
      <v-app-bar app color="black" dark>
        <!-- <v-toolbar-title>Admin Dashboard</v-toolbar-title> -->
        <v-spacer></v-spacer>
            <span class="white--text text-h6">Admin - User</span>
        <v-spacer></v-spacer>
        <v-btn text color="red" @click="logout">Logout</v-btn>
      </v-app-bar>
  
      <!-- Main Content -->
      <v-main>
        <v-container>
            <v-card class="pa-5 mx-auto" max-width="800">
                <!-- <v-card-title class="text-center">Registered Users</v-card-title> -->
                <v-card-title class="white--text" style="background-color: #A00; padding: 10px;">
                    Registered User
                </v-card-title>
                <v-data-table
                :headers="headers"
                :items="users"
                class="elevation-1"
                dense
                >
                    <template #[`item.delete`]="{ item }">
                        <v-btn color="red" text @click="deleteApplication(item.id)">Delete</v-btn>
                    </template>
                </v-data-table>

                <v-btn color="primary" class="mt-3" @click="goToRegister">Register User</v-btn>
            </v-card>
        </v-container>
      </v-main>
    </v-app>
  </template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      users: [],
      headers: [
        { title: "ID", key: "id", align: "center", width: "10%" },
        { title: "Username", key: "username", align: "center", width: "10%" },
        { title: "Email", key: "email", align: "center", width: "10%" },
        { title: "Delete", key: "delete", align: "center", width: "10%"}
      ],
    };
  },
  methods: {
    async fetchUsers() {
      try {
        // const response = await axios.get("http://127.0.0.1:5000/admin/users");
        const response = await axios.get("https://kvqa-reporting-application.onrender.com/admin/users");
        this.users = response.data.users;
      } catch (error) {
        console.error("Error fetching users:", error);
      }
    },
    goToRegister() {
      this.$router.push("/admin/register"); // Navigate to registration page
    },

    logout() {
        localStorage.removeItem("token");
        this.$router.push("/admin/login");
    }, 

    async deleteApplication(userId) {
        if (!confirm("Are you sure you want to delete this user?")) return;

        try {
            // await axios.delete(`http://127.0.0.1:5000/admin/users/${userId}`);
            await axios.delete(`https://kvqa-reporting-application.onrender.com/admin/users/${userId}`);
            this.users = this.users.filter(user => user.id !== userId);
            alert("User deleted successfully!");
        } catch (error) {
            console.error("Error deleting user:", error);
            alert("Failed to delete user.");
        }
    }
  },
  mounted() {
    this.fetchUsers();
  },
};
</script>

<style scoped>
.v-data-table th {
  text-align: center !important; /* Align headers */
}

.v-data-table td {
  text-align: center !important; /* Align table data */
}
</style>

  