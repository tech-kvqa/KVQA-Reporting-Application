<!-- <template>
  <v-app>
    <v-container>
    <v-app-bar color="black" dark>
        <v-spacer></v-spacer>
        <span class="white--text text-h6">Welcome to dashboard User!</span>
        <v-spacer></v-spacer>
        <v-btn text color="blue" @click="logout">Logout</v-btn>
        <v-btn color="primary" @click="goBack">Cancel</v-btn>
      </v-app-bar>
    </v-container>
    <v-container>
      <v-card class="pa-5 mt-3 mx-auto" max-width="800">
        <v-card-title class="white--text" style="background-color: #A00; padding: 10px;">
          Stage 2 Form
        </v-card-title>
  
        <v-card-text>
          <v-form @submit.prevent="submitStage2">
            <v-row>    
              <v-col cols="6">
                <v-text-field v-model="organisationName" label="Organisation Name" disabled></v-text-field>
              </v-col>
              <v-col cols="6">
                <v-text-field v-model="scope" label="Scope" required></v-text-field>
              </v-col>
              <v-col cols="6">
                <v-file-input label="Stage 2 Plan Upload *" v-model="stage2Plan" required></v-file-input>
              </v-col>

              <v-col cols="6">
                <v-file-input label="Additional Data *" v-model="additionaldata"></v-file-input>
              </v-col>
  
              <v-col cols="6"> -->
                <!-- <v-text-field v-model="mailFrom" label="Mail From" required></v-text-field> -->
                <!-- <v-text-field v-model="mailTo" label="Mail To" required></v-text-field> -->
                <!-- <v-select
                  v-model="mailFrom"
                  label="Mail From"
                  :items="['abc@kvqaindia.com', 'training@kvqaindia.com', 'tech@kvqaindia.com']"
                  required
                ></v-select> -->
              <!-- </v-col>

              <v-col cols="6">
                <v-menu 
                    v-model="menu" 
                    :close-on-content-click="false" 
                    transition="scale-transition"
                    >
                    <template v-slot:activator="{ props }">
                        <v-text-field
                            v-model="selectedDate"
                            label="Select Date"
                            readonly
                            v-bind="props"
                        ></v-text-field>
                    </template>
                 -->
                <!-- <v-date-picker 
                    v-model="selectedDate"
                    @update:modelValue="updateDate"
                ></v-date-picker> -->
                    <!-- <v-container>
                        <v-row justify="space-around">
                        <v-date-picker v-on:update:model-value="changeRoleDate" hide-actions @click.native.stop elevation="24" :show-adjacent-months="true" :view-mode="'year'" :min="'2022-01-01'" :max="'2030-12-31'">
                        </v-date-picker>
                        </v-row>
                    </v-container>
                </v-menu>
            </v-col>

              <v-col cols="12"> -->
                <!-- <v-btn v-model="sendmail" >Send Mail</v-btn> -->
                <!-- <v-btn color="primary" @click="sendEmail">Send Email</v-btn>
              </v-col>
   -->
              <!-- <v-col cols="6">
                <v-menu v-model="menu" :close-on-content-click="false" transition="scale-transition">
                  <template v-slot:activator="{ on, attrs }">
                    <v-text-field
                      v-model="selectedDate"
                      label="Select Date"
                      readonly
                      v-bind="attrs"
                      v-on="on"
                    ></v-text-field>
                  </template>
                  <v-date-picker v-model="selectedDate" @input="menu = false"></v-date-picker>
                </v-menu>
              </v-col> -->
    
            <!-- </v-row>
            <v-conatiner>
            <h4>Stage 2 report</h4>
            <v-row>   
              <v-col cols="6">
                <v-text-field v-model="comment" label="Comment" required></v-text-field>
              </v-col>
              <v-col cols="6">
                <v-menu 
                    v-model="menucomment" 
                    :close-on-content-click="false" 
                    transition="scale-transition"
                    >
                    <template v-slot:activator="{ props }">
                        <v-text-field
                            v-model="selectedCommentDate"
                            label="Select Date"
                            readonly
                            v-bind="props"
                        ></v-text-field>
                    </template> -->
                
                <!-- <v-date-picker 
                    v-model="selectedDate"
                    @update:modelValue="updateDate"
                ></v-date-picker> -->
                    <!-- <v-container>
                        <v-row justify="space-around">
                        <v-date-picker v-on:update:model-value="changeCommentDate" hide-actions @click.native.stop elevation="24">
                        </v-date-picker>
                        </v-row>
                    </v-container> -->
                    <!-- <v-container>
                        <v-row justify="space-around">
                        <v-date-picker v-on:update:model-value="changeCommentDate" hide-actions @click.native.stop elevation="24" :show-adjacent-months="true" :view-mode="'year'" :min="'2022-01-01'" :max="'2030-12-31'">
                        </v-date-picker>
                        </v-row>
                    </v-container>
                </v-menu>
            </v-col>
            <v-col cols="6">
                <v-file-input label="Stage 2 Report Upload *" v-model="stage2Report" required></v-file-input>
              </v-col>
              <v-col cols="6">
                <v-text-field v-model="mailToReport" label="Mail To" required></v-text-field>
              </v-col>
              <v-col cols="12"> -->
                <!-- <v-btn v-model="sendmail" >Send Mail</v-btn> -->
                <!-- <v-btn color="primary" @click="sendEmailReport">Send Email</v-btn>
              </v-col>
            </v-row>
        </v-conatiner>
        <v-col cols="12">
                <v-btn type="submit" color="primary">Submit</v-btn>
        </v-col>
          </v-form>
        </v-card-text>
      </v-card>
    </v-container>
    </v-app>
  </template>
  
  <script>
  import axios from "axios"
  export default {
    props: {
        format: String
    },
    data() {
      return {
        organisationName: this.$route.query.orgName || "", // Get org name from query params
        scope: "",
        stage2Plan: null,
        mailFrom: "tech@kvqaindia.com",
        mailTo: "",
        selectedDate: "",
        menu: false,
        selectedDate: null,
        selectedCommentDate: null,
        menucomment: false,
        stage2Report: null,
        comment: "",
        additionaldata: null,
        mailToReport: ""
      };
    },

    computed: {
        selectedDate() {
            if (!this.selectedDate) return "";
            return new Intl.DateTimeFormat("en-GB", {
                day: "2-digit",
                month: "short",
                year: "numeric",
            }).format(new Date(this.selectedDate));
        },

        selectedCommentDate() {
            if (!this.selectedCommentDate) return "";
            return new Intl.DateTimeFormat("en-GB", {
                day: "2-digit",
                month: "short",
                year: "numeric",
            }).format(new Date(this.selectedCommentDate));
        },
  },
    methods: {
    //   async submitStage2() {
    //     if (!this.scope || !this.stage2Plan || !this.mailTo || !this.selectedDate) {
    //         alert("Please fill in all required fields!");
    //         return;
    //     }

    //     let formData = new FormData();
    //     formData.append("organisationName", this.organisationName);
    //     formData.append("scope", this.scope);
    //     formData.append("stage2Plan", this.stage2Plan);
    //     // formData.append("mailFrom", this.mailFrom);
    //     formData.append("mailTo", this.mailTo);
    //     formData.append("selectedDate", this.selectedDate);
    //     formData.append("selectedCommentDate", this.selectedCommentDate);
    //     formData.append("stage2Report", this.stage2Report);
    //     formData.append("comment", this.comment);

    //     const token = localStorage.getItem("token"); // Adjust if using Vuex

    //     try {
    //         const response = await axios.post("http://127.0.0.1:5000/stage2", formData, {
    //           headers: { 
    //             "Content-Type": "multipart/form-data",
    //             "Authorization": `Bearer ${token}` // Attach JWT token
    //         },
    //     });

    //     alert(response.data.message);
    //     this.$router.push({
    //         path: "application",
    //     });

    //     } catch (error) {
    //         console.error("Error submitting Stage 2:", error.response ? error.response.data : error.message);
    //         alert("Failed to submit Stage 2 form.");
    //     }
    // },

    async submitStage2() {
    if (!this.scope || !this.stage2Plan || !this.mailTo || !this.selectedDate) {
        alert("Please fill in all required fields!");
        return;
    }

    let formData = new FormData();
    formData.append("organisationName", this.organisationName);
    formData.append("scope", this.scope);
    formData.append("stage2Plan", this.stage2Plan);
    formData.append("mailFrom", this.mailFrom);
    formData.append("mailTo", this.mailTo);
    formData.append("selectedDate", this.selectedDate);
    formData.append("selectedCommentDate", this.selectedCommentDate);
    formData.append("stage2Report", this.stage2Report);
    formData.append("comment", this.comment);

    let token = localStorage.getItem("token");

    try {
        // const response = await axios.post("http://127.0.0.1:5000/stage2", formData, {
        const response = await axios.post("http://127.0.0.1:5000/stage2", formData, {
            headers: { 
                "Content-Type": "multipart/form-data",
                "Authorization": `Bearer ${token}`
            }
        });

        alert(response.data.message);
        this.$router.push({ path: "application" });

    } catch (error) {
        if (error.response && error.response.status === 401 && error.response.data.msg === "Token has expired") {
            console.log("Token expired, trying to refresh...");

            // Refresh the token
            const newToken = await this.refreshToken();
            if (!newToken) return;

            // Retry request with new token
            try {
                // const response = await axios.post("http://127.0.0.1:5000/stage2", formData, {
                const response = await axios.post("http://127.0.0.1:5000/stage2", formData, {
                    headers: { 
                        "Content-Type": "multipart/form-data",
                        "Authorization": `Bearer ${newToken}`
                    }
                });

                alert(response.data.message);
                this.$router.push({ path: "application" });

            } catch (retryError) {
                console.error("Retry failed:", retryError);
                alert("Failed to submit Stage 2 form.");
            }
        } else {
            console.error("Error submitting Stage 2:", error.response ? error.response.data : error.message);
            alert("Failed to submit Stage 2 form.");
        }
    }
},


      updateDate() {
        this.selectedDate = date
        
      },

      changeRoleDate(date) {
            this.selectedDate = date
            this.menu = false
        },

        changeCommentDate(date) {
            this.selectedCommentDate = date
            this.menucomment = false
        },

        async sendEmail() {
            if (!this.mailTo || !this.stage2Plan || !this.additionaldata) {
                alert("Please fill in all required fields and upload the necessary files!");
                return;
            }

            console.log("Mail Button is clicked!")

            let emailData = new FormData();
            emailData.append("mailTo", this.mailTo);
            emailData.append("subject", "Stage 2 Plan Submission");
            emailData.append("body", "Please find attached the Stage 2 Plan and Additional Data.");
            emailData.append("attachments", this.stage2Plan);
            emailData.append("attachments", this.additionaldata);

            try {
                // const response = await axios.post("http://127.0.0.1:5000/send-email", emailData, {
                const response = await axios.post("http://127.0.0.1:5000/send-email", emailData, {
                    headers: { "Content-Type": "multipart/form-data" },
                });

                alert(response.data.message);
            } catch (error) {
                console.error("Error sending email:", error.response ? error.response.data : error.message);
                alert("Failed to send email.");
            }
        },

        async sendEmailReport() {
    if (!this.mailToReport || !this.stage2Report) {
        alert("Please enter the recipient email and upload the Stage 1 Report!");
        return;
    }

    console.log("Send Report Email button clicked!");

    let reportEmailData = new FormData();
    reportEmailData.append("mailTo", this.mailToReport);
    reportEmailData.append("subject", "Stage 2 Report Submission");
    reportEmailData.append("body", "Please find attached the Stage 2 Report.");
    reportEmailData.append("attachments", this.stage2Report);

    try {
        // const response = await axios.post("http://127.0.0.1:5000/send-email", reportEmailData, {
        const response = await axios.post("http://127.0.0.1:5000/send-email", reportEmailData, {
            headers: { "Content-Type": "multipart/form-data" },
        });

        alert(response.data.message);
    } catch (error) {
        console.error("Error sending report email:", error.response ? error.response.data : error.message);
        alert("Failed to send report email.");
    }
},

async refreshToken() {
    try {
        const refreshToken = localStorage.getItem("refresh_token"); // Retrieve refresh token
        if (!refreshToken) {
            alert("Session expired. Please log in again.");
            this.$router.push("/login");
            return null;
        }

        // const response = await axios.post("http://127.0.0.1:5000/refresh", {
        const response = await axios.post("http://127.0.0.1:5000/refresh", {
            refresh_token: refreshToken,
        });

        // Save new token
        localStorage.setItem("token", response.data.access_token);
        return response.data.access_token;

    } catch (error) {
        console.error("Error refreshing token:", error);
        alert("Session expired. Please log in again.");
        this.$router.push("/login");
        return null;
    }
},

goBack() {
    this.$router.push('/application');
  },

    // selectedDate() {
    //     if (!this.date) return null;
    //         let format = this.format || "%Y-%m-%d";
    //         format = format.replace('%Y', this.date.getYear() + 1900)
    //             .replace('%m', (this.date.getMonth() + 1 + "").padStart(2, "0"))
    //             .replace('%d', (this.date.getDate() + "").padStart(2, "0"));
    //         return format;
    //     }
    }
  };
  </script>
   -->

<template>
  <v-app>
    <v-container>
      <v-app-bar color="black" dark>
        <v-spacer></v-spacer>
        <span class="white--text text-h6">Welcome to dashboard User!</span>
        <v-spacer></v-spacer>
        <v-btn text color="blue" @click="logout">Logout</v-btn>
        <v-btn color="primary" @click="goBack">Cancel</v-btn>
      </v-app-bar>
    </v-container>

    <v-container>
      <v-card class="pa-5 mt-3 mx-auto" max-width="800">
        <v-card-title
          class="white--text"
          style="background-color:#A00;padding:10px;"
        >
          Stage 2 Form
        </v-card-title>

        <v-card-text>
          <v-form @submit.prevent="submitStage2">
            <v-row>
              <v-col cols="6">
                <v-text-field
                  v-model="organisationName"
                  label="Organisation Name"
                  disabled
                />
              </v-col>

              <v-col cols="6">
                <v-text-field
                  v-model="scope"
                  label="Scope"
                  disabled
                />
              </v-col>

              <!-- EXISTING PLAN FILE -->
              <v-col cols="6">
                <div v-if="stage2PlanFile" class="text-caption mb-1">
                  Uploaded: <strong>{{ stage2PlanFile }}</strong>
                </div>
                <v-file-input
                  label="Stage 2 Plan Upload"
                  v-model="stage2Plan"
                />
              </v-col>

              <v-col cols="6">
                <div v-if="additionalDataFile" class="text-caption mb-1">
                    Uploaded: <strong>{{ additionalDataFile }}</strong>
                </div>
                <v-file-input
                    label="Additional Data"
                    v-model="additionaldata"
                />
                </v-col>

              <v-col cols="6">
                <v-text-field v-model="mailTo" label="Mail To" />
              </v-col>

              <!-- DATE -->
              <v-col cols="6">
                <v-menu v-model="menu" :close-on-content-click="false">
                  <template v-slot:activator="{ props }">
                    <v-text-field
                      v-bind="props"
                      label="Select Date"
                      v-model="formattedSelectedDate"
                      readonly
                    />
                  </template>

                  <v-date-picker
                    v-model="selectedDate"
                    view-mode="year"
                    scrollable
                    @update:model-value="menu = false"
                  />
                </v-menu>
              </v-col>

              <v-col cols="12">
                <v-btn color="primary" @click="saveStage2">
                  Save Stage 2 Plan
                </v-btn>
              </v-col>
            </v-row>

            <v-divider class="my-4"></v-divider>

            <h4>Stage 2 Report</h4>

            <v-row>
              <v-col cols="6">
                <v-text-field v-model="comment" label="Comment" />
              </v-col>

              <v-col cols="6">
                <v-menu v-model="menucomment" :close-on-content-click="false">
                  <template v-slot:activator="{ props }">
                    <v-text-field
                      v-bind="props"
                      label="Comment Date"
                      v-model="formattedSelectedCommentDate"
                      readonly
                    />
                  </template>

                  <v-date-picker
                    v-model="selectedCommentDate"
                    view-mode="year"
                    scrollable
                    @update:model-value="menucomment = false"
                  />
                </v-menu>
              </v-col>

              <!-- EXISTING REPORT FILE -->
              <v-col cols="6">
                <div v-if="stage2ReportFile" class="text-caption mb-1">
                  Uploaded: <strong>{{ stage2ReportFile }}</strong>
                </div>
                <v-file-input
                  label="Stage 2 Report Upload"
                  v-model="stage2Report"
                />
              </v-col>

              <v-col cols="6">
                <v-text-field v-model="mailToReport" label="Mail To" />
              </v-col>

              <v-col cols="12">
                <v-btn color="primary" @click="saveStage2">
                  Save Stage 2 Report
                </v-btn>
              </v-col>
            </v-row>

            <v-col cols="12" class="mt-4">
              <v-btn type="submit" color="primary">Submit</v-btn>
            </v-col>
          </v-form>
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
      auditNumber: this.$route.query.audit_number || "",
      organisationName: "",
      scope: "",

      stage2Plan: null,
      stage2Report: null,
      additionaldata: null,
      additionalDataFile: null,

      stage2PlanFile: null,
      stage2ReportFile: null,

      mailFrom: "tech@kvqaindia.com",
      mailTo: "",
      mailToReport: "",

      selectedDate: null,
      selectedCommentDate: null,
      comment: "",

      menu: false,
      menucomment: false,
    };
  },

  computed: {
    formattedSelectedDate() {
      return this.selectedDate
        ? new Date(this.selectedDate).toLocaleDateString("en-GB")
        : "";
    },
    formattedSelectedCommentDate() {
      return this.selectedCommentDate
        ? new Date(this.selectedCommentDate).toLocaleDateString("en-GB")
        : "";
    },
  },

  mounted() {
    this.auditNumber =
      this.$route.query.audit_number ||
      localStorage.getItem("audit_number");

    if (!this.auditNumber) {
      alert("Audit number missing!");
      return;
    }

    localStorage.setItem("audit_number", this.auditNumber);
    this.organisationName =
      this.$route.query.org_name ||
      localStorage.getItem("organisation_name") ||
      "";
    
    this.fetchStage1Prefill();
    this.fetchStage2Data();
  },

  methods: {
    buildFormData() {
      const fd = new FormData();
      fd.append("audit_number", this.auditNumber);
      fd.append("organisation_name", this.organisationName);
      fd.append("scope", this.scope);
      fd.append("mail_from", this.mailFrom);
      fd.append("mail_to", this.mailTo);
      fd.append("mail_to_report", this.mailToReport);
      fd.append("selected_date", this.selectedDate || "");
      fd.append("selected_comment_date", this.selectedCommentDate || "");
      fd.append("comment", this.comment || "");

      if (this.stage2Plan) fd.append("stage2_plan", this.stage2Plan);
      if (this.stage2Report) fd.append("stage2_report", this.stage2Report);
      if (this.additionaldata) fd.append("additional_data", this.additionaldata);

      return fd;
    },

    async saveStage2() {
      const token = localStorage.getItem("token");
      await axios.post(
        "http://127.0.0.1:5000/stage2",
        this.buildFormData(),
        { headers: { Authorization: `Bearer ${token}` } }
      );
      alert("Stage 2 data saved");
    },

    async submitStage2() {
      await this.saveStage2();
      alert("Stage 2 submitted");
    },

    // async fetchStage2Data() {
    //   const token = localStorage.getItem("token");
    //   const res = await axios
    //     .get(
    //       `http://127.0.0.1:5000/stage2-data?audit_number=${this.auditNumber}`,
    //       { headers: { Authorization: `Bearer ${token}` } }
    //     )
    //     .catch(() => null);

    //   if (!res || !res.data) return;

    //   this.scope = res.data.scope || "";
    //   this.mailTo = res.data.mailTo || "";
    //   this.mailToReport = res.data.mailToReport || "";
    //   this.comment = res.data.comment || "";
    //   this.selectedDate = res.data.selectedDate || null;
    //   this.selectedCommentDate = res.data.selectedCommentDate || null;
    //   this.stage2PlanFile = res.data.stage2PlanFile || null;
    //   this.stage2ReportFile = res.data.stage2ReportFile || null;
    // },

    async fetchStage2Data() {
        const token = localStorage.getItem("token");
        const res = await axios
            .get(
            `http://127.0.0.1:5000/stage2-data?audit_number=${this.auditNumber}`,
            { headers: { Authorization: `Bearer ${token}` } }
            )
            .catch(() => null);

        if (!res || !res.data) return;

        // Only overwrite if Stage 2 data exists
        if (res.data.scope) this.scope = res.data.scope;
        if (res.data.mailTo) this.mailTo = res.data.mailTo;
        if (res.data.mailToReport) this.mailToReport = res.data.mailToReport;
        if (res.data.comment) this.comment = res.data.comment;

        // <-- CONVERT DATES TO VALID DATE OBJECTS -->
        this.selectedDate = res.data.selectedDate
            ? new Date(res.data.selectedDate)
            : null;
        this.selectedCommentDate = res.data.selectedCommentDate
            ? new Date(res.data.selectedCommentDate)
            : null;

        this.stage2PlanFile = res.data.stage2PlanFile;
        this.stage2ReportFile = res.data.stage2ReportFile;
        this.additionalDataFile = res.data.additionalDataFile;
    },

    goBack() {
      this.$router.push("/application");
    },

    logout() {
      localStorage.clear();
      this.$router.push("/");
    },

    async fetchStage1Prefill() {
        try {
            const token = localStorage.getItem("token");

            const response = await axios.get(
            "http://127.0.0.1:5000/stage2-prefill",
            {
                params: { audit_number: this.auditNumber },
                headers: {
                Authorization: `Bearer ${token}`,
                },
            }
            );

            this.organisationName = response.data.organisationName;
            this.scope = response.data.scope;

        } catch (error) {
            console.error("Prefill failed:", error);
            alert("Unable to fetch Stage 1 data. Please complete Stage 1 first.");
            this.$router.push("/application");
        }
    }

  },
};
</script>
