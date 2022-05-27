package edu.umd.enpm614.assignment2.application;

import edu.umd.enpm614.assignment2.StandardConfig;
import org.springframework.stereotype.Component;

import javax.inject.Inject;
import javax.inject.Named;

@Component
public class WebApplication {
	private final WebServer server;

//	@Inject
//	public WebApplication(@Named(StandardConfig.Inject_Server)WebServer server ){
//		this.server = server;
//	}
	@Inject
	public WebApplication(WebServer server) {
		this.server = server;
	}

	public void run() {
		System.out.println("starting web application...");
		server.run();
		
		System.out.println("web application finished.");
	}
}
