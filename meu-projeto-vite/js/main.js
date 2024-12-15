import { fetchUsers, fetchAlbums, fetchPhotos } from './apiWrapper.js';

const usersList = document.getElementById('usersList');
const albumsList = document.getElementById('albumsList');
const photosList = document.getElementById('photosList');
const userNameSpan = document.getElementById('userName');
const albumTitleSpan = document.getElementById('albumTitle');

export async function loadUsers() {
  try {
    usersList.innerHTML = 'Carregando...';
    const users = await fetchUsers();
    usersList.innerHTML = '';
    users.forEach(user => {
      const userDiv = document.createElement('div');
      userDiv.className = 'item user';
      userDiv.dataset.userId = user.id;
      userDiv.dataset.userName = user.name;
      userDiv.innerHTML = `<p class="list-item">${user.name}</p>`;
      userDiv.addEventListener('click', () => loadAlbums(user.id, user.name));
      usersList.appendChild(userDiv);
    });
  } catch (error) {
    usersList.innerHTML = 'Erro ao carregar usuários';
    console.error(error);
  }
}

async function loadAlbums(userId, userName) {
  try {
    userNameSpan.textContent = userName;
    albumsList.innerHTML = 'Carregando...';
    const albums = await fetchAlbums(userId);
    albumsList.innerHTML = '';
    albums.forEach(album => {
      const albumDiv = document.createElement('div');
      albumDiv.className = 'item album';
      albumDiv.dataset.albumId = album.id;
      albumDiv.dataset.albumTitle = album.title;
      albumDiv.innerHTML = `<p class="list-item">${album.title}</p>`;
      albumDiv.addEventListener('click', () => loadPhotos(album.id, album.title));
      albumsList.appendChild(albumDiv);
    });
  } catch (error) {
    albumsList.innerHTML = 'Erro ao carregar álbuns';
    console.error(error);
  }
}

async function loadPhotos(albumId, albumTitle) {
  try {
    albumTitleSpan.textContent = albumTitle;
    photosList.innerHTML = 'Carregando...';
    const photos = await fetchPhotos(albumId);
    photosList.innerHTML = '';
    photos.forEach(photo => {
      const img = document.createElement('img');
      img.src = photo.thumbnailUrl;
      img.alt = photo.title;
      photosList.appendChild(img);
    });
  } catch (error) {
    photosList.innerHTML = 'Erro ao carregar fotos';
    console.error(error);
  }
}
