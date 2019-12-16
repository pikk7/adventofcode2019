import java.io.File; 
import java.util.Scanner;
import java.io.FileNotFoundException;
import java.util.ArrayList;

public class Main{
    public static void main(String[] args) {

        ArrayList<ArrayList<Cell> > level=new ArrayList();
        int wire=1;

        try ( Scanner sc = new Scanner( new File("input.txt") ) ) {
            while ( sc.hasNextLine ()) {
            int x,y=0;

            String line = sc.nextLine();
            String[] data=line.split(",");
            
            for(int i=0;i<data.length;++i){
                System.out.println(data[i]);
              
            }
          

            System.out.println("------------------------------");
            }
            } catch ( FileNotFoundException e ) {
            System.err.println ( "asd" );
            }
    }




  

}