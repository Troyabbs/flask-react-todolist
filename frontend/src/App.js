import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [todolist, setTodolist] = useState([]);
  const [task, setTask] = useState('');

  useEffect(() => {
    fetchTodolist();
  }, []);

  const fetchTodolist = async () => {
    const response = await axios.get("/api/todos");
    setTodolist(response.data);
  };

  const addTodo = async () => {
    if (task.trim() === '') return;
    await axios.post("/api/todos", { task });
    setTask('');
    fetchTodolist();
  };

  const updateTodo = async (to)

}