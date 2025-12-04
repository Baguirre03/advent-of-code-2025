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

vector<vector<int>> find_removable(vector<vector<char>> grid) {
    vector<vector<int>> remove;
    for (int i = 0; i < grid.size(); i++) {
        for (int j = 0; j < grid[0].size(); j++) {
            if (grid[i][j] == '@') {
                int removable = check_directions(i,j,grid);
                if (removable) {
                    remove.push_back({i,j});
                }
            }
        }
    }
    return remove;
}

vector<vector<char>> remove_from_grid(vector<vector<char>> grid, vector<vector<int>> remove) {
    for (int i = 0; i < remove.size(); i++) {
        int x = remove[i][0];
        int y = remove[i][1];
        grid[x][y] = '.';
    }
    return grid;
}

int main() {
    vector<vector<char>> grid = create_rows();
    int res = 0;
    vector<vector<int>> remove = find_removable(grid);
    while (remove.size() != 0) {
        grid = remove_from_grid(grid, remove);
        res += remove.size();
        remove = find_removable(grid);
    }

    cout << res;
    return 1;
}