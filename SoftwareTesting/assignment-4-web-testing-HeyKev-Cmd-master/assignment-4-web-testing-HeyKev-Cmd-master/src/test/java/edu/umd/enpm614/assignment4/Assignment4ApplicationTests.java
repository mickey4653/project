package edu.umd.enpm614.assignment4;

import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.internal.matchers.Null;
import org.openqa.selenium.By;
import org.openqa.selenium.NoSuchElementException;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.logging.LogEntries;
import org.openqa.selenium.support.ui.Select;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.web.server.LocalServerPort;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
class Assignment4ApplicationTests {
	public static WebDriver driver;
	private static String base_url;

	@LocalServerPort
	private int port;

	@BeforeAll
	public static void setUpClass() throws Exception {
//		Download the version of chrome driver compatible with your OS
//		from here: https://chromedriver.storage.googleapis.com/index.html
//		Copy the unzipped file to "c"
//		Make sure the name of the driver matches this statement:
//		if(System.getProperty("webdriver.chrome.driver") == null) {
//			System.setProperty("webdriver.chrome.driver", "C:\\Users\\kevin\\IdeaProjects\\assignment-4-web-testing-HeyKev-Cmd\\src\\test\\resources\\chromedrivers.exe");
//		}
		SeleniumTest.setUpWebDriver("chromedriver.exe");
		driver = new ChromeDriver();
	}

	@BeforeEach
	public void setUp () {

		base_url="http://localhost:" + port + "/index";
		driver.get(base_url);
	}

	@AfterAll
	public static void tearDownClass() {
		driver.quit();
	}

	@Test
	void contextLoads() throws InterruptedException {
		Thread.sleep(50);

	}
	String build_cal_url(String url,int int1,int int2, String symbol){
		StringBuffer s1=new StringBuffer(url);
		s1.append("?param1="+int1);
		s1.append("&param2="+int2);
		s1.append("&operator="+symbol);
		return String.valueOf(s1);
	}
	String get_result(WebDriver driver,String url){

		driver.get(url);
		String result=driver.findElement(By.cssSelector("body > div > main > div.d-block > div > div.card-body > p")	).getText();
		if (result.indexOf("=") !=-1) {
			result = result.substring(result.indexOf("=") + 1, result.length());
//			return Integer.parseInt(result);
			return result;
		}
		else{
			return result;
		}
	}
	@Test
	void TestCalculator() throws InterruptedException {
		String url=base_url.replace("index","math");
		System.out.println("cal url="+url);

//		assertEquals(3,get_result(driver,base_url+"?param1=&operator=plus"));
		assertEquals("Missing query parameters. Please add all parameters: 'param1', 'param2', and 'operator'.",get_result(driver,url+"?param1=2&operator=plus")	);
		assertEquals("Missing query parameters. Please add all parameters: 'param1', 'param2', and 'operator'.",get_result(driver,url+"?param2=2&operator=plus")	);
//		assertEquals("Missing query parameters. Please add all parameters: 'param1', 'param2', and 'operator'.",get_result(driver,url+"?param2=2&operator=times")	);
		assertEquals("Missing query parameters. Please add all parameters: 'param1', 'param2', and 'operator'.",get_result(driver,url+"?param1=2&operator=times")	);
		//Invalid Operator was used. Try using 'plus' or 'minus'.
		assertEquals("Invalid Operator was used. Try using 'plus' or 'minus'.",get_result(driver,url+"?param1=2&param2=2&operator=times"));
		assertEquals("Param1 and/or Param2 are not real numbers.",get_result(driver,url+"?param1=null&param2=null&operator=times")	);

		//++
		assertEquals("9",get_result(driver,build_cal_url(url,1,8,"plus")));
		//+-

		assertEquals("-7",get_result(driver,build_cal_url(url,1,-8,"plus")));
		//-+
		assertEquals("7",get_result(driver,build_cal_url(url,-1,8,"plus")));
		//--
		assertEquals("-9",get_result(driver,build_cal_url(url,-1,-8,"plus")));
		// minus
		//++
		assertEquals("7",get_result(driver,build_cal_url(url,1,8,"minus")));
		//+-
		assertEquals("-9",get_result(driver,build_cal_url(url,1,-8,"minus")));
		//-+
		assertEquals("9",get_result(driver,build_cal_url(url,-1,8,"minus")));
		//--
		assertEquals("-7",get_result(driver,build_cal_url(url,-1,-8,"minus")));

		//abnormal


		//back to home
		driver.get(base_url);
	}
		boolean send_form(String url,String Email,String Color,int agree){
			//Email Address	email must have "umd.edu" domain
			driver.findElement(By.cssSelector("#inputEmail1")).sendKeys(Email);

			int idx;
			if (Color.equals("Red")) idx=1;
			else if (Color.equals("White")) idx =2;
			else if (Color.equals("Blue") )idx =3;
			else idx=-1;
			//color-Red,White,Blue
			if (idx>=1) driver.findElement(By.cssSelector("#colorOptions > div:nth-child("+idx+") > label > input ")).click();
			if (agree==1)driver.findElement(By.cssSelector("#agreementCheckbox1 > label")).click();
//			else  return false;

			//Submit
			driver.findElement(By.cssSelector("body > div > main > form > button")).submit();

			//get result

			try{
				driver.findElement(By.cssSelector("body > div > main > form > fieldset > fieldset:nth-child(1) > div > p")).getText();
			}
			catch (NoSuchElementException e){
					driver.get(url);
					return true;
				}
			driver.get(url);
			return false;

	}
	@Test
	void TestForm() throws InterruptedException {
		Thread.sleep(50);
		String url=base_url.replace("index","form");
		driver.get(url);
		//agree 1== true 0=false
		//color-Red,White,Blue

		//test email
		assertEquals(true,send_form(url,"test@umd.edu","Blue",1));
		assertEquals(false,send_form(url,"test@gmail.com","Blue",1));
		assertEquals(false,send_form(url,"test@yahoo.com.tw","Blue",1));
		assertEquals(false,send_form(url,"ENPM614","Blue",1));
		assertEquals(false,send_form(url,"","Blue",1));
		assertEquals(false,send_form(url," ","Blue",1));
		assertEquals(false,send_form(url,"test$gmail.com","Blue",1));
		assertEquals(false,send_form(url,"test","Blue",1));
		//test color
		assertEquals(false,send_form(url,"test@umd.edu","Black",1));

		//test agree
		assertEquals(false,send_form(url,"test@umd.edu","Blue",0));
	}

}