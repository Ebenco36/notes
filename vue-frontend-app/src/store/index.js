import { createStore } from 'vuex'
import { auth } from "./auth.module";
import { search } from "./search.module"
export default createStore({
  modules: {
    auth,
    search,
  },
})
