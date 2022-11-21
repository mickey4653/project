import { Component, OnInit, Input } from '@angular/core';
import { Courses } from '../Courses';

@Component({
  selector: 'app-course',
  templateUrl: './course.component.html',
  styleUrls: ['./course.component.css']
})
export class CourseComponent implements OnInit {
  @Input('courses') course: Courses;
  constructor() { }

  ngOnInit(): void {
  }

}
