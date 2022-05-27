package edu.umd.enpm614.assignment3;

import mockit.Expectations;
import mockit.Mocked;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.stubbing.OngoingStubbing;


import java.sql.SQLException;
import java.util.ArrayList;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.*;

public class UserAdminTest {
    UserAdmin userAdmin;

    @Mocked
    DBConnection dbConnection;

    @BeforeEach
    public void setUp() {
        dbConnection=mock(DBConnection.class);
        userAdmin = new UserAdmin(dbConnection);


    }

    @AfterEach
    public void tearDown() {
        userAdmin = null;
    }

    @Test
    void createUser()throws SQLException {

        new Expectations() {{

            dbConnection.userExists(withEqual("123"));
//            minTimes = 1;
            result = true;


        }};
//    assertEquals(false,userAdmin.createUser("123", ""));
    assertEquals(true,userAdmin.createUser("something", "something"));
    assertEquals(true,userAdmin.createUser("Kev", "123"));
    when( dbConnection.userExists("Kev") ).thenReturn(true)  ;
    when( dbConnection.userExists("something") ).thenReturn(true)  ;
//    repeat
    assertEquals(false,userAdmin.createUser("Kev", "123"));
//    SQL injection

    when( dbConnection.userExists("'SELECT * FROM Users'") ).thenThrow(SQLException.class);
    assertEquals(false,userAdmin.createUser("'SELECT * FROM Users'", "*"));

    }

    @Test
    void removeUser() throws SQLException {
        when( dbConnection.userExists("something") ).thenReturn(true)  ;
        when( dbConnection.isAdmin("userAdmin") ).thenReturn(false)  ;
        assertEquals(true,userAdmin.removeUser("something"));
        when( dbConnection.userExists("userAdmin") ).thenReturn(true)  ;
        when( dbConnection.isAdmin("userAdmin") ).thenReturn(true)  ;
        assertEquals(false,userAdmin.removeUser("userAdmin"));
        when( dbConnection.userExists("nobody") ).thenReturn(false)  ;
        assertEquals(false,userAdmin.removeUser("nobody"));
        //sql exception
        when( dbConnection.userExists("'SELECT * FROM Users'") ).thenThrow(SQLException.class);
        assertEquals(false,userAdmin.removeUser("'SELECT * FROM Users'"));
    }

    @Test
    void runUserReport() throws SQLException {
        new Expectations() {{
            dbConnection.getUsers();
            minTimes = 1;
            new SQLException();
        }};
//        getUsers
        ArrayList<User> userList=new ArrayList<User>();
        userAdmin.runUserReport();
        userList.add(new User("Kev1","123"));
        userList.add(new User("userAdmin1","userAdmin"));
        when( dbConnection.getUsers() ).thenReturn(( userList ))  ;
        userAdmin.runUserReport();
        for (int x=2; x<=12;x++){
            userList.add(new User("Kev"+x,"123"));
        }

        userAdmin.runUserReport();


        when( dbConnection.getUsers() ).thenThrow(SQLException.class);
        userAdmin.runUserReport();



    }
}