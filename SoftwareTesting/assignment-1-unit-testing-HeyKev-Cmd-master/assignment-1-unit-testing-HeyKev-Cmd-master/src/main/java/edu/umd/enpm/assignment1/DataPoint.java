package edu.umd.enpm.assignment1;

import java.util.Objects;

public class DataPoint implements Comparable<DataPoint> {
	private int xValue = 0;
	private int yValue = 0;
	
	/**
	 * Creates an DataPoint with specified xValue and yValue.
	 * 
	 * @param xValue
	 * @param yValue
	 */
	public DataPoint(int xValue, int yValue) {
		this.xValue = xValue;
		this.yValue = yValue;

	}

	/**
	 * Getter and setter for the current Data Point's X value
	 */
	public int getXValue() {
		return xValue;
	}
	public void setXValue(int x) {
		this.xValue = x;
	}

	/**
	 * Getter and setter for the current Data Point's Y value
	 */
	public int getYValue() {
		return yValue;
	}
	public void setValue(int y) {
		this.yValue = y;
	}
	
	/**
	 * DataPoints are ordered by X value, then by Y value.
	 * 
	 * @return		the value 0 if DataPoint's X and Y are both the same
	 * 				the value less than 0 if the argument is greater than this DataPoint
	 * 				the value greater than 0 if the argument is less than this DataPoint
	 */
	public int compareTo(DataPoint o) {
		if (xValue == o.xValue) {
			return yValue - o.yValue;
		}
		
		return xValue - o.xValue;
	}
	
//	public boolean equals(Object obj) {
//		/** TODO
//		 * implement equals() method
//		 *
//		 */
//
//
//		return false;
//	}
	@Override
	public boolean equals(Object o) {
		if (this == o) return true;
		if (!(o instanceof DataPoint)) return false;
		DataPoint dataPoint = (DataPoint) o;
		return xValue == dataPoint.xValue && yValue == dataPoint.yValue;
	}

	@Override
	public int hashCode() {
		int result=17;
		result=result*31+xValue;
		result=result*31+yValue;
		return result;
	}

//	public int hashCode() {
//		/** TODO
//		 * implement hashCode() method
//		 */
//		return 42;
//	}
	
	/**
	 * @return		string representation of the current DataPoint
	 */
	public String toString() {
		return xValue + ", " + yValue;
	}
}