import { Component, OnInit } from '@angular/core';
import { KgUserReg } from 'models/kg-user-reg';
import { WebRequestService } from 'services/web-request.service';
import { NgForm } from '@angular/forms';
import { Observable } from 'rxjs';
import { Router } from '@angular/router';

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.css']
})
export class SignupComponent implements OnInit {
regForm:NgForm;
// user:KgUserReg= new KgUserReg();

  constructor(private _webService:WebRequestService, private _router:Router){}
// userInput:Observable<KgUserReg[]>;
  ngOnInit(): void {
// this.userInput= this._webService.createUser();
  }

  submit(regForm:NgForm){
// console.log("Form submitted!", signup);
// alert(this.user.firstname + ' ' + this.user.lastname + ' ' + this.user.email + ' ' + this.user.password);
console.log('your form data:', regForm.value);
this._webService.postUser('student', regForm.value).subscribe((res)=>{

if (res){
  console.log(res);
alert("Signed Up Successfully!");
this._router.navigateByUrl('/login');
}

});

}



  }

//   reset(signup){
// signup.resetForm();
//   }

// }
