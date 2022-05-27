package edu.umd.enpm614.assignment2;

import edu.umd.enpm614.assignment2.application.WebServer;
import edu.umd.enpm614.assignment2.services.*;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Profile;
import edu.umd.enpm614.assignment2.interfaces.Authentication;
import edu.umd.enpm614.assignment2.interfaces.Connection;
import edu.umd.enpm614.assignment2.interfaces.FileSystem;
import edu.umd.enpm614.assignment2.interfaces.Frontend;
import edu.umd.enpm614.assignment2.interfaces.Middleware;
import edu.umd.enpm614.assignment2.interfaces.Persistance;
import edu.umd.enpm614.assignment2.services.AuthenticationSSL;
import edu.umd.enpm614.assignment2.services.AuthenticationTSL;
import edu.umd.enpm614.assignment2.services.ConnectionPooled;
import edu.umd.enpm614.assignment2.services.FileSystemNTFS;
import edu.umd.enpm614.assignment2.services.FrontendHTML;
import edu.umd.enpm614.assignment2.services.MiddlewareTomcat;
import edu.umd.enpm614.assignment2.services.PersistanceMySQL;
import static edu.umd.enpm614.assignment2.Assignment2Application.TASK_1_ENV;

@Profile(TASK_1_ENV)
@Configuration
public class StandardConfig {
    public static final String Inject_Server="edu.umd.enpm614.assignment2.application.WebServer";
    public static final String FrontendHTML="edu.umd.enpm614.assignment2.services.FrontendHTML";
    public static final String MiddlewareTomcat="edu.umd.enpm614.assignment2.services.MiddlewareTomcat";
    public static final String PersistanceMySQL="edu.umd.enpm614.assignment2.services.PersistanceMySQL";
    public static final String AuthenticationSSL="edu.umd.enpm614.assignment2.services.AuthenticationSSL";
    public static final String FileSystemNTFS="edu.umd.enpm614.assignment2.services.FileSystemNTFS";
    public static final String ConnectionPooled="edu.umd.enpm614.assignment2.services.ConnectionPooled";


     @Bean (name="FrontendHTML")
    public FrontendHTML FrontendHTML(){

         return  new FrontendHTML(AuthenticationSSL());
    }
    @Bean (name="MiddlewareTomcat")
    public MiddlewareTomcat MiddlewareTomcat(){
        return  new MiddlewareTomcat();
    }
    @Bean (name="PersistanceMySQL")
    public PersistanceMySQL PersistanceMySQL(){
        return  new PersistanceMySQL(ConnectionPooled(),FileSystemNTFS());
    }
    @Bean (name="AuthenticationSSL")
    public AuthenticationSSL AuthenticationSSL(){
        return  new AuthenticationSSL();
    }
    @Bean (name="FileSystemNTFS ")
    public FileSystemNTFS  FileSystemNTFS (){
        return  new FileSystemNTFS();
    }
    @Bean (name="ConnectionPooled")
    public ConnectionPooled   ConnectionPooled  (){
        return  new ConnectionPooled();
    }



}
