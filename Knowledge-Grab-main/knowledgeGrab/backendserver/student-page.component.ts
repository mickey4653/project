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
      console.log('object test',this.discussion_array);
      this._webService.post('get_module','1').subscribe((res)=>{
          if (res){
          // console.log('res in service',res);
          console.log('ob in service',Object.values(res));
          for (let i = 0; i < (Object.values(res)[9]).length; i++)
          {
          // console.log('val in ob',Object.values(res)[9][i].title);
          // console.log('val in ob',Object.values(res)[9][i].video_link);
          // console.log('val in ob',Object.values(res)[9][i].title);
          // console.log('val in ob',Object.values(res)[9][i].Text_description);
          result_titles.push( (Object.values(res)[9][i].title). toString());
          result_url.push(  (Object.values(res)[9][i].video_link). toString());
          result_txt.push((Object.values(res)[9][i].Text_description). toString());
          }

          }

          else{
            alert("comment fail!");
          }
        });
        // modules_result[1].tile
        // this.modules_result[0].title[0]=result_titles[0];
        // this.modules_result.yt_url=result_url;
        // this.modules_result.txt=result_txt;

        this.module_titles=result_titles;
        this.module_url=result_url;
        this.module_txt=result_txt;

        // console.log(' modules_result',this.modules_result);
        console.log('modle titles',(this.module_titles));
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



}
