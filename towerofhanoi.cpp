#include <iostream>
using namespace std;

void towerOfHanoi(int n, char from_rod, char aux_rod, char to_rod) {
    if (n == 1) {
        cout << "Move disc 1 from " << from_rod << " to " << to_rod << "\n";
        return;
    } else {
        towerOfHanoi(n - 1, from_rod, to_rod, aux_rod);
        cout << "Move disc " << n << " from " << from_rod << " to " << to_rod << endl;
        towerOfHanoi(n - 1, aux_rod, from_rod, to_rod);
    }
}

int main() {
    cout << "\t\t\t\tTOWER OF HANOI" << endl;
    int N;
    cout << "Enter number of discs: ";
    cin >> N;
    towerOfHanoi(N, 'A', 'B', 'C');
    return 0;
}