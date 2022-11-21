import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http'
import { Observable, of } from 'rxjs';
// import {WISHLIST} from '../mock-wishlist';
import {Courses} from '../Courses';

@Injectable({
  providedIn: 'root'
})
export class CoursesService {
  constructor(private http:HttpClient) { }

  private apiUrl = 'http://54.174.115.150:3000/courses';
  getCoursesForHomePage(): Observable<Courses[]>{   
    return this.http.get<Courses[]>(this.apiUrl);
  }
}


