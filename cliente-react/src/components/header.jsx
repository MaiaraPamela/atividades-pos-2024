import React from 'react';

function Header({ onFetchUsers }) {
  return (
    <header>
      <button id="fetchUsersBtn" className="btn" onClick={onFetchUsers}>Buscar Usuários</button>
    </header>
  );
}

export default Header;
