<template>
    <v-app>
      <!-- Admin Navigation Drawer -->
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
  
      <!-- Admin App Bar -->
      <v-app-bar app color="black" dark>
        <!-- <v-toolbar-title>Admin Dashboard</v-toolbar-title> -->
        <v-spacer></v-spacer>
          <span class="white--text text-h6">Admin - Dashboard</span>
        <v-spacer></v-spacer>
        <v-btn text color="red" @click="logout">Logout</v-btn>
      </v-app-bar>
  
      <!-- Main Content -->
      <v-main>
        <v-container>
          <v-card class="pa-5 mx-auto" max-width="600">
            <v-card-title class="text-center">Welcome, Admin</v-card-title>
            <v-card-text>
              <p>Manage users, review reports, and configure settings here.</p>
            </v-card-text>
          </v-card>
        </v-container>
      </v-main>
    </v-app>
  </template>
  
  <script>
  export default {
    methods: {
      logout() {
        localStorage.removeItem("token"); // Remove token
        this.$router.push("/admin/login"); // Redirect to Admin Login
      }
    }
  };
  </script>
    