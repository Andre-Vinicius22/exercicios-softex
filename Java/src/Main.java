import java.io.*;


public class Main {
	
	public static void main(String[] args) throws IOException, ClassNotFoundException {
		ProductOnline productOnline = new ProductOnline("camiseta", 20.0);
		System.out.println(productOnline.toString());
		
		ObjectOutputStream objectOutput = new ObjectOutputStream(new FileOutputStream("product.bytej"));
        objectOutput.writeObject(productOnline);
        objectOutput.close();
        
        ObjectInputStream objectInput = new ObjectInputStream(new FileInputStream("product.bytej"));
        ProductOnline productOnline1 = (ProductOnline) objectInput.readObject();
        objectInput.close();
        System.out.println(productOnline1.toString());
}
}