const apiUrl = "https://jsonplaceholder.typicode.com/";

// Função para buscar usuários
async function fetchUsers() {
  const response = await fetch(`${apiUrl}users`);
  const users = await response.json();
  return users;
}

// Função para buscar todos os "to-dos" de um usuário
async function fetchTodos(userId) {
  const response = await fetch(`${apiUrl}todos?userId=${userId}`);
  const todos = await response.json();
  return todos;
}

// Função para exibir usuários e seus "to-dos"
async function displayUsers() {
  const users = await fetchUsers();
  const userListDiv = document.getElementById('user-list');

  // Limpa a lista de usuários antes de adicionar
  userListDiv.innerHTML = "";

  for (const user of users) {
    // Cria um elemento para cada usuário
    const userDiv = document.createElement('div');
    userDiv.classList.add('user');
    userDiv.innerHTML = `<h3>${user.name}</h3><p>${user.email}</p>`;

    // Cria a lista de "to-dos" para esse usuário
    const todos = await fetchTodos(user.id);
    const todoList = document.createElement('ul');
    todos.forEach(todo => {
      const todoItem = document.createElement('li');
      todoItem.textContent = todo.title;
      todoList.appendChild(todoItem);
    });

    userDiv.appendChild(todoList);
    userListDiv.appendChild(userDiv);
  }
}

// Chama a função de exibição ao carregar a página
displayUsers();
