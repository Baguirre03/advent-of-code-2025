#include <iostream>
#include <fstream>
#include <string> 

using namespace std;

vector<vector<int>> create_rows(){
    ifstream inputFile("input.txt");
    vector<vector<int>> rows;
    string line;
    while( !inputFile.eof() ) {
        getline( inputFile, line );
        vector<int> nums;
        for (char n: line) {
            nums.push_back(n - '0');
        }
        rows.push_back(nums);
    }
    
    return rows;
}
int main() {
    vector<vector<int>> rows = create_rows();
    int res = 0;
    for(vector<int> row : rows) {
        int l1[2] = {0, -1};
        int l2[2] = {0, -1};
        for (int i = 0; i < row.size() - 1; i++) {
            if (l1[0] < row[i]) {
                l1[0] = row[i];
                l1[1] = i;
            }
        }
        for (int i = row.size() - 1; i > l1[1]; i--) {
            if (l2[0] < row[i]) {
                l2[0] = row[i];
            }
        }
        int num = (l1[0] * 10) + l2[0];
        res += num;
    }
    cout << res;
    return res;
};