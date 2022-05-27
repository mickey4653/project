import { Component, OnInit } from '@angular/core';
import { KgUserLogin } from 'models/kg-user-login';
import { WebRequestService } from 'services/web-request.service';
import { Observable } from 'rxjs';
import { NgForm } from '@angular/forms';
import { Router } from '@angular/router';
import { NavbarService } from 'services/navbar.service';
import { KgUserReg } from 'models/kg-user-reg';
@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  loginForm:NgForm;

  user:KgUserLogin[]=[];
  role:any ='';
  isLoggedIn:any = false;
  // user:KgUserLogin = new KgUserLogin();

  constructor(private _webService:WebRequestService,
    private _router:Router, private navbarService:NavbarService) {
      this.navbarService.getLoginStatus().subscribe(status => this.isLoggedIn =status);

    }
  // userInput:Observable<KgUserLogin[]>;
  ngOnInit(): void {
    // this._kgService.getUserDetails()
    // .subscribe(
    // data=>this.userInput=data);
}



submit(loginForm:NgForm){

// alert(this.user.email + ' ' + this.user.password);
console.log('your form data:', loginForm.value);
this._webService.getUser('login',loginForm.value).subscribe((res)=>{

if (res){

  console.log(res);
  document.cookie = "userSession=" + res + "; expires=Fri, 31 Dec 2021 12:00:00 UTC";
  alert("Logged in Successfully!");
  this._router.navigateByUrl('/home');
}else{
  console.log(res);
  alert("Logged Not Successfull!");

}

});
}
// reset(login){
// login.resetForm();
// }

loginUser() {
  this.navbarService.updateNavAfterAuth('student');
  this.navbarService.updateLoginStatus(true);
  this.role = this.user;
}


}
