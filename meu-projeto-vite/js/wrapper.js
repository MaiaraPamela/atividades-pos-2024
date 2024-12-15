const BASE_URL = 'https://jsonplaceholder.typicode.com';

export async function fetchUsers() {
  const response = await fetch(`${BASE_URL}/users`);
  if (!response.ok) throw new Error('Erro ao buscar usuários');
  return await response.json();
}

export async function fetchAlbums(userId) {
  const response = await fetch(`${BASE_URL}/users/${userId}/albums`);
  if (!response.ok) throw new Error('Erro ao buscar álbuns');
  return await response.json();
}

export async function fetchPhotos(albumId) {
  const response = await fetch(`${BASE_URL}/albums/${albumId}/photos`);
  if (!response.ok) throw new Error('Erro ao buscar fotos');
  return await response.json();
}
