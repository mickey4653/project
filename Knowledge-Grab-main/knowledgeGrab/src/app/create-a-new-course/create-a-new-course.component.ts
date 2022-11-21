import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
import { Router } from '@angular/router';
import { Observable } from 'rxjs';
import { WebRequestService } from 'services/web-request.service';
@Component({
  selector: 'app-create-a-new-course',
  templateUrl: './create-a-new-course.component.html',
  styleUrls: ['./create-a-new-course.component.css']
})
export class CreateANewCourseComponent implements OnInit {
  CreateANewCourseForm:NgForm;

  constructor(private _webService:WebRequestService,
    private _router:Router) { }

  ngOnInit(): void {
  }


  submit(CreateANewCourseForm:NgForm){

    CreateANewCourseForm.value.description = (<HTMLInputElement>document.getElementById("discription")).value;

    var xhr = new XMLHttpRequest();
    xhr.open("POST", "http://54.174.115.150:3000/courses/new", true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.send(JSON.stringify(CreateANewCourseForm.value));


    console.log('your form data:', CreateANewCourseForm.value);
    // this._webService.get('add_CreateANewCourseForm')
  }
}
