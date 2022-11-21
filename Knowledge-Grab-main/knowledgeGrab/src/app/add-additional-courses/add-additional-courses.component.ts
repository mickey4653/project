import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
import { Router } from '@angular/router';
import { Observable } from 'rxjs';
import { WebRequestService } from 'services/web-request.service';
@Component({
  selector: 'app-add-additional-courses',
  templateUrl: './add-additional-courses.component.html',
  styleUrls: ['./add-additional-courses.component.css']
})
export class AddAdditionalCoursesComponent implements OnInit {
  AddAdditionalCoursesForm:NgForm;

  constructor(private _webService:WebRequestService,
    private _router:Router) { }

  ngOnInit(): void {
  }

  submit(AddAdditionalCoursesForm:NgForm){

    var xhr = new XMLHttpRequest();
    xhr.open("POST", "http://54.174.115.150:3000/course/addmodules", true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.send(JSON.stringify(AddAdditionalCoursesForm.value));

    console.log('your form data:', AddAdditionalCoursesForm.value);
    // this._webService.get('user_AddAdditionalCourses')
  }

}
