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
        <span class="white--text text-h6">Admin - User Register</span>
        <v-spacer></v-spacer>
        <v-btn text color="red" @click="logout">Logout</v-btn>
      </v-app-bar>
  
      <!-- Main Content -->
      <v-main>
        <v-container>
          <v-card class="pa-5 mx-auto" max-width="500">
            <v-card-title class="text-center">Register New User</v-card-title>
            <v-card-text>
              <v-form @submit.prevent="registerUser">
                <v-text-field label="Email" v-model="email" required></v-text-field>
                <v-text-field label="Username" v-model="username" required></v-text-field>
                <v-text-field label="Password" v-model="password" type="password" required></v-text-field>
                <v-btn type="submit" color="primary" block>Register</v-btn>
              </v-form>
              <p v-if="successMessage" class="green--text">{{ successMessage }}</p>
              <p v-if="errorMessage" class="red--text">{{ errorMessage }}</p>
            </v-card-text>
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
        email: "",
        username: "",
        password: "",
        successMessage: "",
        errorMessage: ""
      };
    },
    methods: {
      async registerUser() {
        this.successMessage = "";
        this.errorMessage = "";
  
        if (!this.email || !this.username || !this.password) {
          this.errorMessage = "All fields are required!";
          return;
        }
  
        try {
          // const response = await axios.post("http://127.0.0.1:5000/admin/register_user", {
          const response = await axios.post("http://127.0.0.1:5000/admin/register_user", {
            email: this.email,
            username: this.username,
            password: this.password
          });
  
          this.successMessage = response.data.message;
          this.email = "";
          this.username = "";
          this.password = "";
        } catch (error) {
          this.errorMessage = error.response?.data?.error || "Registration failed";
        }
      },
      logout() {
        localStorage.removeItem("token");
        this.$router.push("/admin/login");
      }
    }
  };
  </script>
  
  <style scoped>
  @import 'vuetify/styles';
  </style>
  