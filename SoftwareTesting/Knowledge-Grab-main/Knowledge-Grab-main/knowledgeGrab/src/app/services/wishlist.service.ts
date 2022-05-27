import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http'
import { Observable, of } from 'rxjs';
// import {WISHLIST} from '../mock-wishlist';
import {Wishlist} from '../Wishlist';

@Injectable({
  providedIn: 'root'
})
export class WishlistService {
  constructor(private http:HttpClient) { }
  // getWishlist(): Wishlist[]{
  //   return WISHLIST;
  // }

  private apiUrl = 'http://54.174.115.150:3000/wishlist';
  getWishlist(): Observable<Wishlist[]>{
    let str = this.http.get<Wishlist[]>(this.apiUrl);
    console.log("Wishlist COmp" + str);
    return str;
  }

  // getWishlist(): Observable<Wishlist[]>{
  //   const wishlist = of(WISHLIST);
  //   return wishlist;
  // }

}
