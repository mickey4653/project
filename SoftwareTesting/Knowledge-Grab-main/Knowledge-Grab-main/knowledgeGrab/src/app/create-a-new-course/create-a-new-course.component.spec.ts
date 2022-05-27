import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CreateANewCourseComponent } from './create-a-new-course.component';

describe('CreateANewCourseComponent', () => {
  let component: CreateANewCourseComponent;
  let fixture: ComponentFixture<CreateANewCourseComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CreateANewCourseComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(CreateANewCourseComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
