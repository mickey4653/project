package com.example.AlumniManagementSystem.Model;

import java.util.Date;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;
import org.springframework.data.mongodb.core.mapping.Field;

@Document(collection="Contact_Info")

public class ContactInfo {
	
	@Id
	@Field
	private int ID;
	@Field
	private String FirstName;
	@Field
	private String LastName;
	@Field
	private String Major;
	@Field
	private int ClassOf;
	@Field
	private Date Birthday;
	@Field
	private long tel;
	@Field
	private String Email;
	@Field
	private Date CreatedDate;
	
	
	public int getID() {
		return ID;
	}
	public void setID(int iD) {
		ID = iD;
	}
	public String getFirstName() {
		return FirstName;
	}
	public void setFirstName(String firstName) {
		FirstName = firstName;
	}
	public String getLastName() {
		return LastName;
	}
	public void setLastName(String lastName) {
		LastName = lastName;
	}
	public String getMajor() {
		return Major;
	}
	public void setMajor(String major) {
		Major = major;
	}
	public int getClassOf() {
		return ClassOf;
	}
	public void setClassOf(int class1) {
		ClassOf = class1;
	}
	public Date getBirthday() {
		return Birthday;
	}
	public void setBirthday(Date birthday) {
		Birthday = birthday;
	}
	public long getTel() {
		return tel;
	}
	public void setTel(long tel) {
		this.tel = tel;
	}
	public String getEmail() {
		return Email;
	}
	public void setEmail(String email) {
		Email = email;
	}
	public Date getCreatedDate() {
		return CreatedDate;
	}
	public void setCreatedDate(Date createdDate) {
		CreatedDate = createdDate;
	}
	
	
	
}
