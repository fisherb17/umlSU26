package com.leszko.calculator;

import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class CalculatorTest {

	private Calculator calculator = new Calculator();

	@Test
	public void testSumPositiveNumbers() {
		assertEquals(5, calculator.sum(2, 3));
	}

	@Test
	public void testSumWithZero() {
		assertEquals(7, calculator.sum(7, 0));
	}

	@Test
	public void testSumNegativeNumbers() {
		assertEquals(-5, calculator.sum(-2, -3));
	}

	@Test
	public void testSumMixedSigns() {
		assertEquals(-1, calculator.sum(2, -3));
	}
}
