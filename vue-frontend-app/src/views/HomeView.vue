<template>
  <div class="container" style="margin-top: 100px">
    <!-- Filter notes here -->
    <form
      id="frmSearch"
      name="frmSearch"
      role="form"
      class="was-validated"
      @submit.prevent="getNotes()"
    >
      <div class="row mb-4">
        <div class="col-lg-2 offset-lg-1 text-end">Tags</div>
        <div class="col-lg-2 text-start">
          <select
            ID="ddlType"
            Class="form-control rounded"
            v-model="selectedTags"
          >
            <option value="" selected>Search by...</option>
            <option v-for="tag in tagList" :key="tag.id" :value="tag.name">
              {{ tag.name }}
            </option>
          </select>
        </div>
        <div class="col-lg-1 text-center">Search Key</div>
        <div class="col-lg-4 d-flex">
          <input
            type="text"
            ID="tbTerm"
            v-model="search"
            class="form-control rounded text-black"
          />
        </div>
        <div class="col-lg-1 mx-auto">
          <button
            type="submit"
            ID="btnSearch"
            class="btn-success btn text-white"
          >
            Search
          </button>
        </div>
      </div>
    </form>
    <div class="row">
      <Note :notes="notes" />
    </div>
  </div>
</template>

<script>
import Note from "../components/Note.vue";
import userService from "../services/user.service";
export default {
  components: {
    Note,
  },
  data() {
    return {
      notes: [],
      search: "",
      tagList: [],
      profile: null,
      selectedTags: "",
    };
  },
  created() {
    this.getTags();
    this.getNotes();
    this.getUser();
  },
  methods: {
    /**
     * get all tags for filtering
     */
    getTags() {
      userService.getTags().then((res) => {
        console.log(res);
        this.tagList = res.data.data;
      });
    },
    /**
     * get all notes
     */
    getNotes() {
      userService
        .getNotes(this.search, this.selectedTags)
        .then((res) => {
          let response = res.data;
          if (response.data && response.data.length > 0) {
            this.notes = response.data;
          } else {
            this.notes = [];
          }
        })
        .catch((error) => {
          if (error.response && error.response.status === 401) {
            // Handle the 401 error here
            // we can display this to users.
            console.error(
              "Authentication failed. Redirect to login page or show an error message."
            );
          }
        });
    },
    getUser() {
      userService
        .getUser()
        .then((res) => {
          let response = res.data;
          if (response.data && response.data.length > 0) {
            this.profile = response.data;
          } else {
            this.profile = null;
          }
        })
        .catch((error) => {
          if (error.response && error.response.status === 401) {
            // Handle the 401 error here
            console.error(
              "Authentication failed. Redirect to login page or show an error message."
            );
          }
        });
    },
  },
};
</script>

<style scoped></style>
