import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AddAdditionalCoursesComponent } from './add-additional-courses/add-additional-courses.component';
import { AdminComponent } from './admin/admin.component';
import { CreateANewCourseComponent } from './create-a-new-course/create-a-new-course.component';
import { ExamCreationPageComponent } from './exam-creation-page/exam-creation-page.component';

import { HomeComponent } from './home/home.component';
import { InstructorComponent } from './instructor/instructor.component';
import { LoginComponent } from './login/login.component';
import { ProfileComponent } from './profile/profile.component';
import { PageNotFoundComponent } from './page-not-found/page-not-found.component';

import { SignupComponent } from './signup/signup.component';
import { StudentPageComponent } from './student-page/student-page.component';
import { ViewCreateCoursePageComponent } from './view-create-course-page/view-create-course-page.component';
import { WishlistItemComponent } from './wishlist-item/wishlist-item.component';
import { SearchItemComponent } from './search-item/search-item.component';

const routes: Routes = [
  {path:'', redirectTo:'/home', pathMatch:'full'},
  {path:'home', component:HomeComponent},
  {path:'instructor', component:InstructorComponent},
{path:'login', component: LoginComponent},
{path:'signup', component: SignupComponent},
{path:'student', component: StudentPageComponent},
{path:'admin', component: AdminComponent },
{path: 'profile', component: ProfileComponent},
{path: 'view-create-course-page', component: ViewCreateCoursePageComponent},
{path: 'exam-creation-page', component: ExamCreationPageComponent},
{path: 'create-a-new-course', component: CreateANewCourseComponent},
{path: 'add-additional-courses', component: AddAdditionalCoursesComponent},
{path: 'wishlist', component: WishlistItemComponent},
{path: 'searchResult', component:SearchItemComponent},
{ path: '**', component: PageNotFoundComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
export const routingComponents = [HomeComponent,InstructorComponent,LoginComponent,
SignupComponent,StudentPageComponent, AdminComponent, ProfileComponent, ViewCreateCoursePageComponent,
 ExamCreationPageComponent, CreateANewCourseComponent, AddAdditionalCoursesComponent, PageNotFoundComponent,
WishlistItemComponent
];
