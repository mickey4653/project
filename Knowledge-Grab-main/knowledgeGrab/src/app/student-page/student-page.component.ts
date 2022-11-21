import { Component, OnInit,ElementRef } from '@angular/core';
import { NgForm } from '@angular/forms';
import { Router } from '@angular/router';
import { WebRequestService } from 'services/web-request.service';
import {DiscussionService} from '../services/discussion.service'
import {Discussion} from '../Discussion';
import {ModuleInterface}from '../../../models/module-interface'

@Component({
  selector: 'app-student-page',
  templateUrl: './student-page.component.html',
  styleUrls: ['./student-page.component.css']
})



export class StudentPageComponent implements OnInit {

  discussion_array=[];
  // title:string[];
  // yt_url:string[];
  // txt:string[];
  text="";
  yt_url="https://www.youtube.com/embed/2dZiMBwX_5Q";
  modules_result:ModuleInterface[]= [];
  module_titles=[];
  module_url=[];
  module_txt=[];

  style=['zmdi zmdi-view-dashboard','zmdi zmdi-link','zmdi zmdi-widgets','zmdi zmdi-calendar','zmdi zmdi-info-outline','zmdi zmdi-settings','zmdi zmdi-comment-more'];
  constructor(private _webService:WebRequestService,
    private _router:Router,
    private DiscussionService: DiscussionService,

    ) { }


  get_class_module():void{
      var id=1;
      var result_titles=[];
      var result_url=[];
      var result_txt=[];
      var count=0;

      this._webService.post('get_module','1').subscribe((res)=>{
          if (res){

          console.log('ob in service',Object.values(res));
          for (let i = 0; i < (Object.values(res)[9]).length; i++)
          {
          // console.log('val in ob',Object.values(res)[9][i].title);
          // console.log('val in ob',Object.values(res)[9][i].video_link);
          // console.log('val in ob',Object.values(res)[9][i].Text_description);
          // result_titles.push( (Object.values(res)[9][i].title));
          // result_url.push(  (Object.values(res)[9][i].video_link));
          // result_txt.push((Object.values(res)[9][i].Text_description));
          //
          if((Object.values(res)[9][i].title)!=''){
            this.modules_result[count]={
                title:(Object.values(res)[9][i].title),
                yt_url:(Object.values(res)[9][i].video_link),
                txt:(Object.values(res)[9][i].Text_description)
              };
              count=count+1;

            }
          }

          }

          else{
            alert("comment fail!");
          }
        });
        console.log('still working');
        this.module_titles=result_titles;
        this.module_url=result_url;
        this.module_txt=result_txt;
        console.log('modle result',(this.modules_result));
    }
    get_disscussions(){
      var test=[];
    //get discussion posts
    {this.DiscussionService.getDiscussion().subscribe((discussions) => (
      // this.discussion_array = discussions
      discussions.forEach(function (value) {
        // this.discussion_array.push(value.discussion_text);
        test.push(value);
      })

      ) );
    this.discussion_array=test;
    }
  }


  ngOnInit(): void {
    this.get_class_module();
    this.get_disscussions();

  }



  submit(form:NgForm){

    this.text="";
    //send query to db
    console.log('submited form data:', form.value);
    this._webService.post('send_comment',form.value).subscribe((res)=>{
        if (res){

          console.log(res);

        alert("comment sent successfully!");
        }
        else{
          alert("comment fail!");
        }
      });
    // this.ngOnInit();
    console.log('reload');
    window.location.reload();
    }
  change_video(new_url){
    //change video
    this.yt_url=new_url;
  }

wishList(){
      const queryString = window.location.search;
      const urlParams = new URLSearchParams(queryString);
      var product = urlParams.get('id');
      if(product){

        console.log(product);
        }else{
 product='1';

        }
      this._webService.get('wishlist/add?course_id='+product).subscribe((res)=>{
if (res){
  alert("wishlist clicked and sent data");
console.log(res);

}

      });
    }

    flag(){
      const queryString = window.location.search;
      const urlParams = new URLSearchParams(queryString);
      var product = urlParams.get('id');
if(product){

console.log(product);
}else{

  product='1';
}
      this._webService.get('flags/new?course_id='+product).subscribe((res)=>{
if (res){
  alert("flag clicked and sent data");
console.log(res);


}

});
}
}
