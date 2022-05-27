package edu.umd.enpm614.assignment2.services;

import edu.umd.enpm614.assignment2.interfaces.Authentication;
import edu.umd.enpm614.assignment2.interfaces.Frontend;
import org.springframework.stereotype.Component;
import javax.inject.Inject;
import org.springframework.context.annotation.Primary;
import org.springframework.stereotype.Component;
import javax.inject.Named;
@Primary
@Component
public class FrontendHTML implements Frontend {

	private final Authentication authentication;

	@Inject

	public FrontendHTML(Authentication authentication){
		this.authentication=authentication;
	}

	@Override
	public String getType() {
		return "HTML Frontend";
	}
	
	@Override
	public boolean run() {
		System.out.println("running " + this.getType());
		
		// invoke services here if applicable
		authentication.run();

		
		return true;
	}
}
