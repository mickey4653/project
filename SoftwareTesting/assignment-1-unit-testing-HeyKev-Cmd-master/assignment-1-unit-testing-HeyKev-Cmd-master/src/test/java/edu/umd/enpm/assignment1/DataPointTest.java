package edu.umd.enpm.assignment1;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class DataPointTest {
    private DataPoint dp1 = null;
    private DataPoint dp2 = null;
    private DataPoint dp3 = null;
    private DataPoint dp4 = null;
    @BeforeEach
    void setUp() {


        dp1 =new DataPoint(1,1);
        dp2 =new DataPoint(1,1);
        dp3=new DataPoint(2,3);
        dp4=new DataPoint(-2,-3);
    }

    @AfterEach
    void tearDown() {
        dp1=null;
        dp2=null;
        dp3=null;
        dp4=null;
    }

    @Test
    void TestGetXValue() {
        assertNotNull(dp1);
        assertNotNull(dp4);
        assertEquals(dp1.getXValue(),1);
        assertEquals(dp4.getXValue(),-2);

    }

    @Test
    void TestSetXValue() {
        dp3.setXValue(3);
        assertEquals(dp3.getXValue(),3);
    }

    @Test
    void TestGetYValue() {

        assertEquals(dp3.getYValue(),3);
    }

    @Test
    void TestSetValue() {
        dp3.setValue(2);
        assertEquals(dp3.getYValue(),2);
    }

    @Test
    void TestCompareTo() {
        assertEquals(dp1.compareTo(dp2), 0);
        assertEquals(dp1.compareTo(dp3), -1);
        assertEquals(dp1.compareTo(dp4), 3);


    }

    @Test
    void TestTestEquals() {


        assertEquals(dp1.equals(dp2),true);
        assertEquals(dp1.equals(dp3),false);
    }

    @Test
    void TestTestHashCode() {
        assertTrue( dp1.hashCode()==(16369));
    }

    @Test
    void TestToString() {
        assertTrue(dp1.toString().equals("1, 1"));

//        System.out.println(dataPoint.toString());
    }
}