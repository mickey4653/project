import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http'
import { Observable, of } from 'rxjs';
// import {WISHLIST} from '../mock-wishlist';
import {Discussion} from '../Discussion';

@Injectable({
  providedIn: 'root'
})
export class DiscussionService {
  constructor(private http:HttpClient) { }
  // getWishlist(): Wishlist[]{
  //   return WISHLIST;
  // }

  private apiUrl = 'http://54.174.115.150:3000/get_comments';
  getDiscussion(): Observable<Discussion[]>{
    document.cookie = "userid=1";
    console.log('in discussion service.ts', this.http.get<Discussion[]>(this.apiUrl));
    return this.http.get<Discussion[]>(this.apiUrl);
  }

  // getWishlist(): Observable<Wishlist[]>{
  //   const wishlist = of(WISHLIST);
  //   return wishlist;
  // }

}
