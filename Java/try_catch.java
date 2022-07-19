public class Excecao {

    public static void main(String[] args) {

        try {
            int[] vetor = new int[4];

            System.out.println("antes da exception");

            vetor[4] = 1;

            System.out.println("esse texto nao sera impresso");
        } catch(ArrayIndexOutOfBoundsException exception) {
            System.out.println("excessao ao acessar um indice do vetor que nao existe");
        }

        System.out.println("esse texto sera impresso apos a exception");
    }
}