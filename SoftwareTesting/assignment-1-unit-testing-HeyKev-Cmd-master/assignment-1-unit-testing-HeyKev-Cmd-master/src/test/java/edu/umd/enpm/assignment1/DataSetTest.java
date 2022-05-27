package edu.umd.enpm.assignment1;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;
import static org.junit.jupiter.api.Assertions.assertEquals;

class DataSetTest {

    private DataPoint dp1 = null;
    private DataPoint dp2 = null;
    private DataPoint dp3 = null;
    private DataPoint dp4 = null;
    DataSet ds1=null;
    DataSet ds2=null;

    @BeforeEach
    void setUp() {

        dp1 =new DataPoint(1,1);
        dp2 =new DataPoint(-1,1);
        dp3=new DataPoint(2,3);
        dp4=new DataPoint(-2,-3);
        ds1=new DataSet();
        ds2=new DataSet();
        ds1.addPoint(dp1);
        ds1.addPoint(dp2);
        ds1.addPoint(dp3);

        ds2.addPoint(dp2);
        ds2.addPoint(dp3);
        ds2.addPoint(dp4);
    }

    @AfterEach
    void tearDown() {
        dp1 =null;
        dp2 =null;
        dp3=null;
        dp4=null;
        ds1=null;
        ds2=null;
    }

    @Test
    void testGetDataPoints() {
        assertNotNull(ds1);
        assertNotNull(ds2);
        assertEquals(ds1.getDataPoints(),ds1.dataPoints);
        assertEquals(ds2.getDataPoints(),ds2.dataPoints);

    }

    @Test
    void testAddPoint() {
       ds1.addPoint(new DataPoint(100,100));
       assertEquals(ds1.getDataPoints(),ds1.dataPoints);
    }

    @Test
    void testSubsumes() {
        assertEquals(ds1.subsumes(ds2),false);
    }

    @Test
    void testCompareTo() {
        assertEquals(ds1.compareTo(ds2),1);
    }

    @Test
    void testEquals() {
       assertNotNull(ds1);
       assertNotNull(ds2);
       assertEquals(ds1.equals(ds2),false);
    }

    @Test
    void testHashCode() {
        assertNotNull(ds1);
        assertNotNull(ds2);
        System.out.println(ds1.hashCode());
        assertEquals(4519552,ds1.hashCode());
        assertEquals(4025226,ds2.hashCode());
    }

    @Test
    void testToString() {
        assertNotNull(ds1);
        assertNotNull(ds2);
        assertEquals( "-1, 1 1, 1 2, 3",ds1.toString());
        assertEquals("-2, -3 -1, 1 2, 3",ds2.toString());
    }
}