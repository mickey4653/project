package edu.umd.enpm614.assignment2.services;

import edu.umd.enpm614.assignment2.interfaces.FileSystem;
import org.springframework.stereotype.Component;
import org.springframework.context.annotation.Primary;
@Primary
@Component
public class FileSystemNTFS implements FileSystem {
	@Override
	public String getType() {
		return "NTFS FileSystem";
	}
	
	@Override
	public boolean run() {
		System.out.println("running " + this.getType());
		
		// invoke services here if applicable
		
		return true;
	}
}
