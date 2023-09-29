import axios from 'axios';
import authHeader from './auth-header';
import Requests from './requests'

const API_URL = process.env.VUE_APP_APP_URL + "api/";

class UserService {

  /**
   * get user profile information
   * @returns promise
   */
  getUser() {
    return Requests.get(API_URL + 'auth/user/profile/')
  }

  /**
   * get all tags for users
   * @returns promise
   */
  getTags() {
    return Requests.get(API_URL + 'note/tags/')
  }

  /**
   * get all note . Users can also apply search
   * @param {*} searchItem 
   * @param {*} tag 
   * @returns 
   */
  getNotes(searchItem, tag) {
    let queryParams = {
      'q': searchItem,
      'tag': tag,
    }
    return Requests.get(API_URL + 'note/lists-create/', queryParams);
  }

  /**
   * create note
   * @param data 
   * @returns promise
   */
  createNote(data){
    let request = Requests.post(API_URL + 'note/lists-create/', data)
      .then(response => {
        return response.data;
      });
      
    return request
  }

  /**
   * fetch note
   * @param {*} note_id 
   * @returns 
   */
  fetchNote(note_id){
    let request = Requests.get(API_URL + 'note/note/'+note_id+'/')
      .then(response => {
        return response.data;
      });
      
    return request
  }

  editNote(data, note_id){
    let request = Requests.patch(API_URL + 'note/note/'+note_id+'/', data)
      .then(response => {
        return response.data;
      });
      
    return request
  }

  createTag(data){
    let request = axios
      .post(API_URL + 'note/tags', data)
      .then(response => {
        return response.data;
      });
      
    return request
  }

}

export default new UserService();