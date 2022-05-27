package edu.umd.enpm614.assignment2.services;

import edu.umd.enpm614.assignment2.interfaces.Authentication;
import org.springframework.stereotype.Component;
import org.springframework.context.annotation.Primary;
@Primary
@Component
public class AuthenticationSSL implements Authentication {
	@Override
	public String getType() {
		return "SSL Authentication";
	}
	
	@Override
	public boolean run() {
		System.out.println("running " + this.getType());
		
		// invoke services here if applicable
		
		return true;
	}
}
