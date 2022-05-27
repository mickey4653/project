import { Component, OnInit } from '@angular/core';
import { WebRequestService } from 'services/web-request.service';
import { Observable } from 'rxjs';
import { NgForm } from '@angular/forms';
import { Router } from '@angular/router';
import {WishlistService} from '../services/wishlist.service'
import {Wishlist} from '../Wishlist';
@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent implements OnInit {
  ProfileForm:NgForm;

  constructor(private wishlistService: WishlistService, private _webService:WebRequestService, private _router:Router) { }
  
  wishlist: Wishlist[] = [];

  ngOnInit(): void {
    // this.wishlist = this.wishlistService.getWishlist();
    this.wishlistService.getWishlist().subscribe((wishlist) => (this.wishlist = wishlist) );
  }
  submit(ProfileForm:NgForm){


    var xhr = new XMLHttpRequest();
    xhr.open("POST", "http://54.174.115.150:3000/user/update", true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.send(JSON.stringify(ProfileForm.value));
  
    console.log('your form data:', ProfileForm.value);
    this._webService.get('user_Profile')
  }
}
