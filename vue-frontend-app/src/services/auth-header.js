export default function authHeader() {
    let user = JSON.parse(localStorage.getItem('user'));
    if (user && user.access) {
      return { 'bearer': user.access };
    } else {
      return {};
    }
  }