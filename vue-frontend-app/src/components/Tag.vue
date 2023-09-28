<template>
  <div class="tag-input">
    <div class="selected-tags">
      <div
        v-for="(tag, index) in selectedTags"
        :key="index"
        class="selected-tag"
      >
        {{ tag }}
        <span @click="removeTag(index)" class="remove-tag-btn">×</span>
      </div>
    </div>
    <input
      type="text"
      v-model="newTag"
      @keydown.enter="addTag"
      @input="searchTags"
      placeholder="Add a tag"
    />
    <div class="tag-list" v-show="showTagList">
      <div
        v-for="(tag, index) in filteredTagList"
        :key="index"
        @click="selectTag(tag)"
        class="tag-item"
      >
        {{ tag }}
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "TagCompnent",
  data() {
    return {
      newTag: "",
      selectedTags: [],
      tagList: ["Tag 1", "Tag 2", "Tag 3", "Tag 4"], // Replace with your tag list data
      showTagList: false,
    };
  },
  computed: {
    filteredTagList() {
      return this.tagList.filter((tag) =>
        tag.toLowerCase().includes(this.newTag.toLowerCase())
      );
    },
  },
  methods: {
    addTag() {
      const tag = this.newTag.trim();
      if (tag !== "" && !this.selectedTags.includes(tag)) {
        this.selectedTags.push(tag);
        this.newTag = "";
        this.showTagList = false;
      }
    },
    removeTag(index) {
      this.selectedTags.splice(index, 1);
    },
    searchTags() {
      this.showTagList = true;
    },
    selectTag(tag) {
      if (!this.selectedTags.includes(tag)) {
        this.selectedTags.push(tag);
        this.newTag = "";
      }
      this.showTagList = false;
    },
  },
};
</script>

<style>
.tag-input {
  position: relative;
}

.selected-tags {
  display: flex;
  flex-wrap: wrap;
  margin-bottom: 8px;
}

.selected-tag {
  background-color: #007bff;
  color: #fff;
  padding: 3px 8px;
  margin-right: 5px;
  margin-bottom: 5px;
  border-radius: 3px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.remove-tag-btn {
  margin-left: 5px;
  cursor: pointer;
}

input[type="text"] {
  width: 100%;
  padding: 5px;
  border: 1px solid #ccc;
  border-radius: 3px;
  font-size: 14px;
  outline: none;
}

.tag-list {
  position: absolute;
  top: 100%;
  left: 0;
  right: 0;
  background-color: #fff;
  border: 1px solid #ccc;
  border-top: none;
  max-height: 150px;
  overflow-y: auto;
}

.tag-item {
  padding: 5px;
  cursor: pointer;
}

.tag-item:hover {
  background-color: #f0f0f0;
}
</style>
