#include <iostream>
#include <string>
using namespace std;

class Animal
{
public:
    string habitat; // Public: accessible everywhere

    Animal(const string &h)
        : habitat(h), age(5), dnaCode("AGCT") {} // Initialize all members

    void makeSound() // Public method
    {
        cout << "Some generic animal sound" << endl;
    }

protected:
    int age; // Protected: accessible only in this class and subclasses

    void digestFood() // Protected method
    {
        cout << "Digesting..." << endl;
    }

private:
    string dnaCode; // Private: accessible only inside this class

    void privateMethod() // Private method
    {
        cout << "This is a private method" << endl;
    }
};

int main()
{
    Animal a("Savannah");

    // Public: OK
    cout << a.habitat << endl; // Accessible
    a.makeSound();             // Accessible

    // Protected: compile-time error
    // cout << a.age << endl;       // ERROR: 'age' is protected
    // a.digestFood();              // ERROR: 'digestFood' is protected

    // Private: compile-time error
    // cout << a.dnaCode << endl;   // ERROR: 'dnaCode' is private
    // a.privateMethod();           // ERROR: 'privateMethod' is private

    return 0;
}