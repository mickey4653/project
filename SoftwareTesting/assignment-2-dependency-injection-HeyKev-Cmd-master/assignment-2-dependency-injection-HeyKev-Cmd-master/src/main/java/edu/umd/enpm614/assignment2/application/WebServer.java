package edu.umd.enpm614.assignment2.application;

import edu.umd.enpm614.assignment2.StandardConfig;
import edu.umd.enpm614.assignment2.interfaces.Frontend;
import edu.umd.enpm614.assignment2.interfaces.Middleware;
import edu.umd.enpm614.assignment2.interfaces.Persistance;
import org.springframework.stereotype.Component;

import javax.inject.Inject;
import javax.inject.Named;

@Component
public class WebServer {
	private final Frontend frontend;
	private  final Middleware middleware;
	private  final Persistance persistance;

	@Inject
	public WebServer(Frontend frontend, Middleware middleware, Persistance persistance) {
		this.frontend = frontend;
		this.middleware = middleware;
		this.persistance = persistance;
	}
//	@Inject
//	public WebServer(
//			@Named(StandardConfig.FrontendHTML) Frontend frontend,
//			@Named(StandardConfig.MiddlewareTomcat)Middleware middleware,
//			@Named(StandardConfig.PersistanceMySQL)Persistance persistance
//			){
//		this.frontend = frontend;
//		this.middleware = middleware;
//		this.persistance = persistance;
//	}

	public String getType() {
		return "WebServer";
	}

	public boolean run() {
		System.out.println("running " + this.getType());
		
		// invoke services here if applicable
		frontend.run();
		middleware.run();
		persistance.run();
		
		return true;
	}
}
