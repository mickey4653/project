package edu.umd.enpm614.assignment2.services;

import edu.umd.enpm614.assignment2.interfaces.Connection;
import edu.umd.enpm614.assignment2.interfaces.Persistance;
import org.springframework.stereotype.Component;
import javax.inject.Inject;
import javax.inject.Named;
import org.springframework.context.annotation.Primary;
import org.springframework.stereotype.Component;
import edu.umd.enpm614.assignment2.interfaces.Connection;
import edu.umd.enpm614.assignment2.interfaces.FileSystem;

@Component
public class PersistanceOracle implements Persistance {


	private final Connection connection;
	private final FileSystem fileSystem;


	@Inject
	public PersistanceOracle(Connection connection, FileSystem filesystem) {
		this.connection = connection;
		this.fileSystem = filesystem;
	}
	@Override
	public String getType() {
		return "Oracle Persistance";
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
