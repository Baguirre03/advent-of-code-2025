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
    long long res = 0;
    for(vector<int> row : rows) {
        int search = row.size() - 12;
        int last_indx = -1;
        vector<int> arr;
        for (int i = 0; i < 12; i++) {
            int add[2] = {0, -1};
            for (int j = last_indx + 1; j < last_indx + search + 1; j++) {
                if(row[j] > add[0]) {
                    add[0] = row[j];
                    add[1] = j;
                }
            }
            arr.push_back(add[0]);
            last_indx = add[1];
            search = row.size() - last_indx - 12 + arr.size();
        }
        string s;
        for (int d : arr) s += to_string(d);
        long long number = stoll(s); 
        res += number;
    }
    cout << res;
    return res;
};



