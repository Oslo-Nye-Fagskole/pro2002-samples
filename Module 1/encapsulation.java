public class Animal {
    // Public: accessible everywhere
    public String habitat;

    // Protected: accessible in this class and subclasses
    protected int age;

    // Private: accessible only inside this class
    private String dnaCode;

    // Constructor
    public Animal(String habitat) {
        this.habitat = habitat;
        this.age = 5;
        this.dnaCode = "AGCT";
    }

    // Public method
    public void makeSound() {
        System.out.println("Some generic animal sound");
    }

    // Protected method
    protected void digestFood() {
        System.out.println("Digesting...");
    }

    // Private method
    private void mutateDNA() {
        System.out.println("DNA mutating...");
    }

    public static void main(String[] args) {
        Animal a = new Animal("Savannah");

        // Public: OK
        System.out.println(a.habitat);  // Accessible
        a.makeSound();                  // Accessible

        // Protected: compile-time error if accessed outside class/package
        // System.out.println(a.age);       // ERROR: age has protected access
        // a.digestFood();                  // ERROR: digestFood() has protected access

        // Private: compile-time error
        // System.out.println(a.dnaCode);   // ERROR: dnaCode has private access
        // a.mutateDNA();                   // ERROR: mutateDNA() has private access
    }
}