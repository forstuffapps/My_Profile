import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import java.io.IOException;

public class WebScraper {

    public static void main(String[] args) {
        String url = "https://www.lambtoncollege.ca/";

        try {
            // Connect to the website and get the HTML content
            Document document = Jsoup.connect(url).get();

            // Select the elements containing article titles
            Elements articleTitles = document.select("h2.article-title");

            // Print the titles of articles
            for (Element titleElement : articleTitles) {
                String title = titleElement.text();
                System.out.println("Article Title: " + title);
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
