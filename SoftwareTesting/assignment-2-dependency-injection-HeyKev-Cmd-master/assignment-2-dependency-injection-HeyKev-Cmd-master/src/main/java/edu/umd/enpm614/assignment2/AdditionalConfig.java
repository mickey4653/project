package edu.umd.enpm614.assignment2;

import edu.umd.enpm614.assignment2.services.*;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Profile;

import edu.umd.enpm614.assignment2.interfaces.Connection;


import static edu.umd.enpm614.assignment2.Assignment2Application.TASK_2_ENV;

@Profile(TASK_2_ENV)
@Configuration
public class AdditionalConfig {

    public static final String FrontendGWT="edu.umd.enpm614.assignment2.services.FrontendGWT";
    public static final String MiddlewareJBoss="edu.umd.enpm614.assignment2.services.MiddlewareJBoss";
    public static final String PersistanceOracle="edu.umd.enpm614.assignment2.services.PersistanceOracle";
    public static final String AuthenticationTSL="edu.umd.enpm614.assignment2.services.AuthenticationTSL";
    public static final String FileSystemNFS="edu.umd.enpm614.assignment2.services.FileSystemNFS";
    public static final String ConnectionJDBC="edu.umd.enpm614.assignment2.services.ConnectionJDBC";



    @Bean (name="FrontendGWT")
    public FrontendGWT FrontendGWT(){
        return  new FrontendGWT(AuthenticationTSL());
    }
    @Bean (name="MiddlewareJBoss")
    public MiddlewareJBoss MiddlewareJBoss(){
        return  new MiddlewareJBoss();
    }

    @Bean (name="PersistanceOracle")
    public PersistanceOracle PersistanceOracle(){
        return  new PersistanceOracle(Connection(), FileSystemNFS());
    }
    @Bean (name="AuthenticationTSL")
    public AuthenticationTSL AuthenticationTSL(){ return  new AuthenticationTSL();    }
    @Bean (name="FileSystemNFS")
    public FileSystemNFS FileSystemNFS(){
        return  new FileSystemNFS();
    }
    @Bean (name="ConnectionJDBC")
    public Connection Connection(){
        return  new ConnectionPooled();
    }


}
