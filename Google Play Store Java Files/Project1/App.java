package Project1;

public class App {
    String app;
    String category;
    int rating;
    int reviews;
    int size;
    int installs;
    String type;
    int price;
    String contentRating;
    String genres;
    String lastUpdated;
    String currentVer;
    String androidVer;
    App
    (String app, String category, int rating, int reviews, int size, 
            int installs, String type, int price, String contentRating, 
            String genres, String lastUpdated, String currentVer, String 
                    androidVer)
    {
    this.app = app;
    this.category = category;
    this.rating = rating;
    this.reviews = reviews;
    this.size = size;
    this.installs = installs;
    this.type = type;
    this.price = price;
    this.contentRating = contentRating;
    this.lastUpdated = lastUpdated;
    this.currentVer = currentVer;
    this.androidVer = androidVer;
}

public String toString()
{
    return app + " " + category + " " + rating + " " + reviews + " " + size + 
" " + installs + " " + type + " " + price + " " + contentRating + " " + 
lastUpdated + " " + currentVer + " " + androidVer; }

public static void main(String[] args) {
    App b =
            //Filling in strings and ints as an example
    new App ("java", "code", 5, 1024, 21, 2000, "learning", 
    4, "Friendly", "Beginner", "Jan 2020", "Version A360", "Android 8");
    System.out.println(b);
    System.out.println(b.toString());
}
}

