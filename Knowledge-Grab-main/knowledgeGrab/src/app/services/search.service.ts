import { Injectable, EventEmitter } from '@angular/core';
import {Subscription} from 'rxjs/internal/Subscription'
import {HttpClient, HttpHeaders} from '@angular/common/http'

import { Observable, of } from 'rxjs';
import {SearchItem} from '../SearchItem'; 

@Injectable({
  providedIn: 'root'
})
export class SearchService {

  invokeSearchCallFunction = new EventEmitter();
  subsVar : Subscription;

  constructor(private http:HttpClient) { }

  onSubmitSearch(searchQuery: String){
    this.invokeSearchCallFunction.emit(searchQuery);
  }

  private apiUrl = 'http://54.174.115.150:3000/search?query=';
  getSearchItems(item): Observable<SearchItem[]>{
    let str = this.http.get<SearchItem[]>(this.apiUrl+item);
    console.log("Printing return search" + str);
    return str;
  }
     
}
