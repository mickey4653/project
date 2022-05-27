import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ViewCreateCoursePageComponent } from './view-create-course-page.component';

describe('ViewCreateCoursePageComponent', () => {
  let component: ViewCreateCoursePageComponent;
  let fixture: ComponentFixture<ViewCreateCoursePageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ViewCreateCoursePageComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ViewCreateCoursePageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
