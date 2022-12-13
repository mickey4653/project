import { Component } from '@angular/core';
import { Todo } from './Todo';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  todos:Todo[]=[];
  newTodo:string;
  Desription:string;
  saveTodo()
  {
    if (this.newTodo)
    {
      let todo=new Todo();
      todo.name=this.newTodo;
      todo.Desription=this.Desription;
      todo.Completed=false;
      this.todos.push(todo);
      this.newTodo="";
    }
    else
    {
      alert("Todo can not be empty!")
    }
  }

  done(id:number)
  {
    this.todos[id].Completed=!this.todos[id].Completed;
  }
  

  remove(id:number)
  {
    this.todos=this.todos.filter((v,i)=>i !=id );
  }
  complete(id:number)
  {
    this.todos[id].Completed=!this.todos[id].Completed; 
  }
}
