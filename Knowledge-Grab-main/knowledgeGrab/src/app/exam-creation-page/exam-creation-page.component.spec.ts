import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ExamCreationPageComponent } from './exam-creation-page.component';

describe('ExamCreationPageComponent', () => {
  let component: ExamCreationPageComponent;
  let fixture: ComponentFixture<ExamCreationPageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ExamCreationPageComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ExamCreationPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
