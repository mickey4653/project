import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
import { Router } from '@angular/router';
import { WebRequestService } from 'services/web-request.service';
import {SearchService} from '../services/search.service'


import { StudentPageComponent } from '../student-page/student-page.component';
import { LoginComponent } from '../login/login.component';
import { AdminComponent } from '../admin/admin.component';
import { NavbarService } from 'services/navbar.service';
import { KgUserReg } from 'models/kg-user-reg';
import {SearchItem} from '../SearchItem';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent implements OnInit {
  searchQuery: NgForm
  

  links: Array<{ text: string, path: string }>;
  isLoggedIn:any = false;
  user:KgUserReg[]=[];
  role:any ='';
  // searchItems: SearchItem[] = [];

  constructor(private searchService: SearchService, private _webService:WebRequestService,
    private _router:Router, private navbarService: NavbarService) {



      this._router.config.unshift(
        { path: 'login', component: LoginComponent },
        { path: 'student', component: StudentPageComponent },
        { path: 'admin', component: AdminComponent },
      );

      this.navbarService.getLoginStatus().subscribe(status => this.isLoggedIn =status);
    }

    ngOnInit(): void {
      this.links = this.navbarService.getLinks();
      this.navbarService.getLoginStatus().subscribe(status => this.isLoggedIn = status);
  }

  submitSearch(searchQuery:String){
    this._router.navigateByUrl('/searchResult');    
    this.searchService.onSubmitSearch(searchQuery);    
  }

  // submitSearch(searchQuery:NgForm){
  //   console.log('Came here!!!' + searchQuery.value.search);
  //   this.searchService.getSearchItems(searchQuery.value.search).subscribe((searchItems) =>{
  //     this.searchItems = searchItems;
  //     this._router.navigateByUrl('/searchResult');      
  //   });
  // }

  // submitSearch(searchQuery:NgForm){

  //   // alert(this.user.email + ' ' + this.user.password);
  //   console.log('Came here!!!', searchQuery.value.search);
  //   this._webService.get('search?query='+searchQuery.value.search).subscribe((res)=>{

  //   if (res){

  //     console.log(res);
  //     alert("Logged in Successfully!");
  //   }

  //   });
  //   }



    loginUser() {
      this.navbarService.updateNavAfterAuth('student');
      this.navbarService.updateLoginStatus(true);
      this.role = this.user;
    }

    // loginAdmin() {
    //   this.navbarService.updateNavAfterAuth('admin');
    //   this.navbarService.updateLoginStatus(true);
    //   this.role = 'admin';
    // }





    logout(){

      document.cookie = "userSession=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
      this.navbarService.updateLoginStatus(false);
    this._router.navigate(['home']);
    }




}
