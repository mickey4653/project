import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AddAdditionalCoursesComponent } from './add-additional-courses.component';

describe('AddAdditionalCoursesComponent', () => {
  let component: AddAdditionalCoursesComponent;
  let fixture: ComponentFixture<AddAdditionalCoursesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AddAdditionalCoursesComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(AddAdditionalCoursesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
