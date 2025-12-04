#include <iostream>
#include <fstream>

using namespace std;

vector<vector<char>> create_rows(){
    ifstream inputFile("input.txt");
    vector<vector<char>> rows;
    string line;
    while( !inputFile.eof() ) {
        getline( inputFile, line );
        vector<char> arr;
        for (const char n: line) {
            arr.push_back(n);
        }
        rows.push_back(arr);
    }
    
    return rows;
}

bool out_of_bounds(int x, int y, vector<vector<char>> grid) {
    return x < 0 || y >= grid[0].size() || x >= grid.size() || y < 0;
}

int dirs[8][2] = {{0,1}, {0,-1}, {1,0}, {-1,0}, {1,1}, {1,-1}, {-1,1}, {-1,-1}};
int check_directions(int x, int y, vector<vector<char>> grid) {
    int count = 0;
    for (int i = 0; i < 8; i++) {
        int dx = dirs[i][0];
        int dy = dirs[i][1];
        if (out_of_bounds(x + dx, y + dy, grid)) continue;
        if (grid[dx + x][dy + y] == '@') {
            count += 1;
            if (count == 4) {
                return 0;
            }
        }
    }
    return 1;
}

int main() {
    vector<vector<char>> grid = create_rows();
    int res = 0;

    for (int i = 0; i < grid.size(); i++) {
        for (int j = 0; j < grid[0].size(); j++) {
            if (grid[i][j] == '@') {
                res += check_directions(i, j, grid);
            }
        }
    }
    cout << res;
    return 1;
}