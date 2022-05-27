package edu.umd.enpm614.assignment2.services;

import edu.umd.enpm614.assignment2.interfaces.Frontend;
import edu.umd.enpm614.assignment2.interfaces.Authentication;
import javax.inject.Inject;
import javax.inject.Named;
import org.springframework.stereotype.Component;

@Component
public class FrontendGWT implements Frontend {
	private final Authentication authentication;

	@Inject
	public FrontendGWT(Authentication authentication) {
		this.authentication = authentication;

	}
	@Override
	public String getType() {
		return "GWT Frontend";
	}
	
	@Override
	public boolean run() {
		System.out.println("running " + this.getType());
		
		// invoke services here if applicable
		authentication.run();

		
		return true;
	}
}
