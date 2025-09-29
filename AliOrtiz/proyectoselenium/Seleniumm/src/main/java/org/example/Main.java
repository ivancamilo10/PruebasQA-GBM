import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.time.Duration;

public class Main {
    public static void main(String[] args){
        //configurar la ruta del chromedriver
        System.setProperty("webdriver.chrome.driver", "C:\\workplace\\chromedriver-win64\\chromedriver.exe");
        //Crear una instancia
        WebDriver driver = new ChromeDriver();
        //Navegar a Google
        driver.get("https://www.google.com");
        //localizar el elemento buscar
        WebElement searchbox = driver.findElement(By.name("q"));
        searchbox.sendKeys("Pokemon Favorito de ash");
        searchbox.submit();

        WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
        WebElement imagenesLink = wait.until(
                ExpectedConditions.elementToBeClickable(By.linkText("Imágenes")));
        imagenesLink.click();


        //localizadores xpath(el mas comun)
        //driver.findElement(By.xpath("//*[@id=APjFqb""]));
        //driver.findElement(By.id("APjFqb"));
        //driver.findElement(By.name("q"));
        //driver.findElement(By.className("gLFyf"));


        //cerrar el navegador
        driver.quit();
    }
}