import React, { useState } from 'react';
import Header from './components/Header';
import UserList from './components/UserList';
import AlbumList from './components/AlbumList';
import PhotoList from './components/PhotoList';

function App() {
  const [users, setUsers] = useState([]);
  
  const fetchUsers = async () => {
    const response = await fetch('https://jsonplaceholder.typicode.com/users');
    const data = await response.json();
    setUsers(data);
  };

  return (
    <div>
      <Header onFetchUsers={fetchUsers} />
      <main>
        <UserList users={users} />
        <AlbumList />
        <PhotoList />
      </main>
      <footer>
        <p>&copy; 2024 App</p>
      </footer>
    </div>
  );
}

export default App;
