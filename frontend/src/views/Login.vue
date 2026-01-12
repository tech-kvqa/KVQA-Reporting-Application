<!-- <template>
  <v-app>
    <v-container>
    <v-app-bar app color="black" dark>
        <v-toolbar-title>KVQA</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-btn color="error" @click="adminlogin">Admin Login</v-btn>
      </v-app-bar>
    </v-container>
    <v-container>
      <v-card class="pa-5 mx-auto" max-width="400">
        <v-card-title class="text-center">User Login</v-card-title>
        <v-card-text>
          <v-form @submit.prevent="login">
            <v-text-field label="Email" v-model="email" required></v-text-field>
            <v-text-field label="Password" v-model="password" type="password" required></v-text-field>
            <v-btn type="submit" color="primary" block>Login</v-btn>
          </v-form>
          <p v-if="errorMessage" class="red--text">{{ errorMessage }}</p>
        </v-card-text>
      </v-card>
    </v-container>
  </v-app>
  </template>
  
  <script>
  import axios from "axios";
  
  export default {
    data() {
      return {
        email: "",
        password: "",
        errorMessage: ""
      };
    },
    methods: {
      async login() {
        try {
          // const response = await axios.post("http://127.0.0.1:5000/login", {
          const response = await axios.post("http://127.0.0.1:5000/login", {
            email: this.email,
            password: this.password
          });
  
          localStorage.setItem("token", response.data.token);
          this.$router.push("/dashboard"); // Redirect after login
        } catch (error) {
          this.errorMessage = error.response?.data?.error || "Login failed";
        }
      },

      adminlogin () {
        this.$router.push('/admin/login')
      }
    }
  };
  </script>
  
  <style scoped>
  @import 'vuetify/styles';
  /* .v-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
  } */
  </style>
   -->

<template>
  <v-app>
    <v-app-bar app color="black" dark>
      <v-toolbar-title>KVQA</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn color="error" @click="adminlogin">Admin Login</v-btn>
    </v-app-bar>

    <v-container class="login-container user-login-bg">
      <v-card class="login-card user-card">
        <v-card-title class="login-card-title">User Login</v-card-title>

        <v-card-text>
          <v-form @submit.prevent="login">
            <v-text-field label="Email" v-model="email" required></v-text-field>
            <v-text-field label="Password" v-model="password" type="password" required></v-text-field>

            <v-btn type="submit" color="primary" block class="login-btn">
              Login
            </v-btn>
          </v-form>

          <p v-if="errorMessage" class="login-error">{{ errorMessage }}</p>
        </v-card-text>
      </v-card>
    </v-container>
  </v-app>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      email: "",
      password: "",
      errorMessage: ""
    };
  },
  methods: {
    async login() {
      try {
        const response = await axios.post("http://127.0.0.1:5000/login", {
          email: this.email,
          password: this.password
        });
        localStorage.setItem("token", response.data.token);
        this.$router.push("/dashboard");
      } catch (error) {
        this.errorMessage = error.response?.data?.error || "Login failed";
      }
    },
    adminlogin() {
      this.$router.push("/admin/login");
    }
  }
};
</script>

<style scoped>
@import 'vuetify/styles';

/* Full-page gradient */
.user-login-bg {
  display: flex;
  justify-content: center;
  align-items: center;
  height: calc(100vh - 64px); /* Full height minus app-bar */
  background: linear-gradient(135deg, #a1c4fd, #c2e9fb);
}

/* Login Card */
.login-card {
  max-width: 400px;
  width: 100%;
  padding: 2rem;
  border-radius: 12px;
  box-shadow: 0px 10px 25px rgba(0, 0, 0, 0.2);
  transition: all 0.3s ease-in-out;
  border-top: 5px solid #2196f3; /* Blue accent */
}

.login-card:hover {
  transform: translateY(-4px);
  box-shadow: 0px 15px 30px rgba(0, 0, 0, 0.3);
}

/* Card title */
.login-card-title {
  text-align: center;
  font-weight: 700;
  font-size: 1.6rem;
  margin-bottom: 1.5rem;
  color: #2196f3;
}

/* Buttons */
.login-btn {
  margin-top: 1rem;
  transition: all 0.2s ease;
}

.login-btn:hover {
  background-color: #1976d2 !important;
}

/* Error text */
.login-error {
  color: #d32f2f;
  margin-top: 0.5rem;
  text-align: center;
}
</style>
