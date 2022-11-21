import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RouterModule, Router } from '@angular/router';
import { AppRoutingModule, routingComponents } from './app-routing.module';
import { AppComponent } from './app.component';
import { HeaderComponent } from './header/header.component';
import { FooterComponent } from './footer/footer.component';
// import { InstructorComponent } from './instructor/instructor.component';
// import { SignupComponent } from './signup/signup.component';
// import { PageNotFoundComponent } from './page-not-found/page-not-found.component';
// import { HomeComponent } from './home/home.component';
// import { LoginComponent } from './login/login.component';
// import { ProfileComponent } from './profile/profile.component';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
// import { StudentPageComponent } from './student-page/student-page.component';
// import { WishlistItemComponent } from './wishlist-item/wishlist-item.component';
import { AdminComponent } from './admin/admin.component';
import { AddAdditionalCoursesComponent } from './add-additional-courses/add-additional-courses.component';
import { CategoryComponent } from './category/category.component';
import { SearchItemComponent } from './search-item/search-item.component';
import { CourseComponent } from './course/course.component';
// import { CreateANewCourseComponent } from './create-a-new-course/create-a-new-course.component';
// import { ExamCreationPageComponent } from './exam-creation-page/exam-creation-page.component';
// import { ViewCreateCoursePageComponent } from './view-create-course-page/view-create-course-page.component';
// import { ProfileComponent } from './profile/profile.component';
// import { StudentPageComponent } from './student-page/student-page.component';
// import { AdminComponent } from './admin/admin.component';
// import { KgapiserviceService } from 'services/kgApi.service';
@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    routingComponents,
    FooterComponent,
    CategoryComponent,
    SearchItemComponent,
    CourseComponent,
    // StudentPageComponent,
    // ProfileComponent,
    // WishlistItemComponent
    // AddAdditionalCoursesComponent,
   // CreateANewCourseComponent,
   // ExamCreationPageComponent,
    // ViewCreateCoursePageComponent,
    // ProfileComponent,
    // AdminComponent,
    // StudentPageComponent,


  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    RouterModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
