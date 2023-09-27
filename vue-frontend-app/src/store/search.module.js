export const search = {
  namespaced: true,
  state: {
    searchQuery:[],
    otherQuery: {},
  },
  actions: {
  },
  mutations: {
    setSearchQuery(state, query) {
        state.searchQuery = query;
    }
  },
  getters: {
    searchQueries: (state) => {
      return state.searchQuery
    }
  }
};