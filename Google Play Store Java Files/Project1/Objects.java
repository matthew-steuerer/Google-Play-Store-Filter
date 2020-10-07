package Project1;
import java.util.ArrayList;
import java.util.List;

public class Objects {
    public static void main(String[] args) {
        List<String> object = new ArrayList<>();
        object.add("app");
        object.add("category");
        object.add("rating");
        object.add("reviews");
        object.add("size");
        object.add("installs");
        object.add("type");
        object.add("price");
        object.add("contentRating");
        object.add("genres");
        object.add("lastUpdated");
        object.add("currentVer");
        object.add("androidVer");
        for (String objects : object) {
            
            System.out.printf("%s ", object);
        }
        
        System.out.println();
    }
}
