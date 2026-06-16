# 🍲 Django Recipes - Full Stack Web App + API

Sistema de receitas desenvolvido com Django + Django REST Framework, com autenticação via sessão e JWT, CRUD completo e dashboard de usuário.

## 🚀 Visão geral

Este projeto é uma aplicação web + API onde usuários podem:

- Criar, editar e excluir receitas
- Salvar receitas como rascunho ou publicar
- Fazer login e registro de conta
- Visualizar apenas suas próprias receitas no dashboard
- Consumir API REST autenticada com JWT

---

## ⚙️ Funcionalidades

### 👤 Usuários
- Registro de conta
- Login/logout
- Autenticação via sessão (frontend)
- Autenticação via JWT (API)
- Dashboard com receitas do usuário

### 🍽️ Receitas
- CRUD completo (Create, Read, Update, Delete)
- Upload de imagem
- Sistema de publicação (`is_published`)
- Rascunhos privados
- Slug automático baseado no título

### 🔎 Busca e filtros
- Busca por título
- Filtro por categoria
- Paginação de resultados

### 🔐 API (DRF)
- Endpoints REST completos
- JWT authentication
- Permissões por usuário
- Proteção de dados privados

---

## 🛠️ Tecnologias

- Python 3
- Django
- Django REST Framework
- SimpleJWT
- SQLite (default)
- HTML + Django Templates
- dotenv (.env)

---

## 📦 Instalação

### 1. Clone o projeto
```bash
git clone https://github.com/snagywolf/django-recipes.git
cd django-recipes
