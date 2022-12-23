package com.example.AlumniManagementSystem;

import java.text.SimpleDateFormat;
import java.time.LocalDateTime;
import java.util.Date;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;

import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.stereotype.Component;

import com.example.AlumniManagementSystem.Model.ContactInfo;

@Component
public class AplicationRunner implements CommandLineRunner {
	
	@Autowired
	private MongoTemplate mongotemplate;
	
	public AplicationRunner() 
	{
		
	}
	
	public AplicationRunner(MongoTemplate mongotemplate) {
		super();
		this.mongotemplate = mongotemplate;
	}

	@Override
	public void run(String... args) throws Exception {
		// TODO Auto-generated method stub
		ContactInfo person=new ContactInfo();
		
		String sDate1="31/12/1998";  
		Date date1=new SimpleDateFormat("dd/MM/yyyy").parse(sDate1);

		person.setBirthday(date1);		
		person.setClassOf(2022);
		person.setID(77);
		Date d1 = new Date(); 
		person.setCreatedDate(d1);		
		person.setEmail("Luka77@umd.edu");	
		person.setFirstName("Luka");
		person.setLastName("Doncic");
		person.setMajor("Computer Science");		
		person.setTel(Long.parseLong("2407777777777"));
		
		
		mongotemplate.save(person);

		System.out.println("Application Started");
	}

}
