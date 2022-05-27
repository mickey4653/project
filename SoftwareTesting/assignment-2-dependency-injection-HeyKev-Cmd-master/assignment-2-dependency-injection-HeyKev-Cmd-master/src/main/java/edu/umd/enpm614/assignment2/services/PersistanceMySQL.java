package edu.umd.enpm614.assignment2.services;

import edu.umd.enpm614.assignment2.interfaces.Connection;
import edu.umd.enpm614.assignment2.interfaces.FileSystem;
import edu.umd.enpm614.assignment2.interfaces.Persistance;
import org.springframework.stereotype.Component;
import javax.inject.Inject;

import org.springframework.context.annotation.Primary;
@Primary
@Component
public class PersistanceMySQL implements Persistance {

	private final Connection connection;
	private final FileSystem fileSystem;
	@Inject

	public PersistanceMySQL( Connection connection,FileSystem fileSystem){
		this.connection=connection;
		this.fileSystem=fileSystem;
	}

	@Override
	public String getType() {
		return "MySQL Persistance";
	}
	
	@Override
	public boolean run() {
		System.out.println("running " + this.getType());
		
		// invoke services here if applicable
		connection.run();

		fileSystem.run();

		return true;
	}
}
