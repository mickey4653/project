import { Component, OnInit } from '@angular/core';
import { WebRequestService } from 'services/web-request.service';
import { NgForm } from '@angular/forms';
import { Router } from '@angular/router';
import {SearchService} from '../services/search.service'
import {SearchItem} from '../SearchItem';
import {CoursesService} from '../services/courses.service'
import {Courses} from '../Courses';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
// courses =[
// {title:"Gifts", content:"Sample text. Click to select the text box. Click again or double click to start editing the text."},
// {title:"Design", content:"Sample text. Click to select the text box. Click again or double click to start editing the text."},
// {title:"No coding", content:"Sample text. Click to select the text box. Click again or double click to start editing the text."},
// {title:"500+ Sites", content:"Sample text. Click to select the text box. Click again or double click to start editing the text."},
// {title:"Approach", content:"Sample text. Click to select the text box. Click again or double click to start editing the text."},
// {title:"Quality", content:"Sample text. Click to select the text box. Click again or double click to start editing the text."},
// ];
  
  constructor(private courseService: CoursesService, private searchService: SearchService, private _webService:WebRequestService, private _router:Router) { }
  courses: Courses[] = [];
  searchItems: SearchItem[] = [];
  searchQuery: NgForm

  ngOnInit(): void { 
    this.courseService.getCoursesForHomePage().subscribe((courses) => (this.courses = courses) );
  }

  // submitSearch(searchQuery:NgForm){
  //   console.log('Came here!!!', searchQuery.value.search);
  //   this.searchService.getSearchItems(searchQuery.value.search).subscribe((searchItems) => (this.searchItems = searchItems) );
  // }

  submit(contact){
    alert(document.getElementById("successMeg").innerText);
    contact.reset();
  }

}
