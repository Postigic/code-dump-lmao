#include <iostream>
#include <vector>

// typedef std::vector<std::pair<std::string, int>> pairList_t;
// typedef std::string text_t;
// typedef int number_t;

using text_t = std::string;
using number_t = int;

namespace first{
    int i = 1;
}

namespace second{
    int i = 2;
}

int main(){

    // This is a comment
    
    /*
        This
        is
        a
        multi-line
        comment
    */

    // Print statements

    std::cout << "Hello World!" << "\n";
    std::cout << "Lorem ipsum." << "\n";

    // Variables

    int x; // Declaration
    x = 5; // Assignment

    int y = 6; // Declaration and Assignment

    // Data Types

    // Integers (Whole number)
    int age = 21;
    int year = 2023;
    int days = 7;

    // Doubles (Numbers including decimals)
    double price = 10.99;
    double gpa = 2.5;
    double temperature = 25.1;

    // Single characters
    char grade = 'A';
    char initial = 'B';
    char currency = '$';

    // Booleans (true or false)
    bool student = true;
    bool power = false;
    bool forSale = true;

    // Strings (Objects that represent a sequence of text)
    std::string name = "Eru";
    std::string day = "Friday";
    std::string food = "Pizza";
    std::string address = "129 Rake St.";

    // String literals
    std::cout << "Hello " << name << "\n";
    std::cout << "You are " << age << " years old" << "\n";

    // Constants

    const double PI = 3.14159;
    // Attempting to change the value of PI will give "error: assignment of read-only variable 'PI'"
    double radius = 10;
    double circumference = 2 * PI * radius;  
    // These cannot be reassigned
    const int LIGHT_SPEED = 299792458;
    const int WIDTH = 1920;
    const int HEIGHT = 1080;

    /* Namespaces

        Namespaces provide a solution for preventing name conflicts in large projects.
        Since each entity needs a unique name. A namespace allows for indentically
        named entities as long as the namespaces are different.

    */

    int i = 0;
    // int i = 1;
    // This will throw "error: redeclaration of 'int i'"
    
    std::cout << i << "\n";
    std::cout << first::i << "\n";
    std::cout << second::i << "\n";

    using namespace first;

    std::cout << i << "\n";

    /* Typedef
    
        Typedefs are reserved keywords used to create an additional name (alias) for
        another data type. New identifier for an exisiting type. Helps with readability
        and reduces typos. Use when there is a clear benefit. Replaced with "using"
        (works better with templates)
    
    */

    /*
        Without typedef
        ---------------
        std::string firstName = "Avery";
        int age = 21;

        With typedef
        ---------------
        text_t firstName = "Avery";
        numbert_t age = 21;
    */

   // Arithmetic Operators

    return 0;
}