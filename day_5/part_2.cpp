#include <algorithm>
#include <fstream>
#include <iostream>
#include <string>

std::vector<std::vector<long long>> get_input() {
  std::ifstream inp("input.txt");
  std::vector<std::vector<long long>> returned_inp;
  std::string line;
  while (!inp.eof()) {
    getline(inp, line);
    if (line.length() == 0) {
      break;
    }
    size_t pos = line.find("-");
    std::vector<long long> tmp;
    tmp.push_back(std::stoll(line.substr(0, pos)));
    tmp.push_back(std::stoll(line.substr(pos + 1)));
    returned_inp.push_back(tmp);
  }

  return returned_inp;
}

int main() {
  std::vector<std::vector<long long>> inp = get_input();
  std::sort(inp.begin(), inp.end(),
            [&](auto const &a, auto const &b) { return a[0] < b[0]; });
  std::vector<std::vector<long long>> merged;
  long long start = -1;
  long long end = -1;
  for (std::vector<long long> s : inp) {
    if (s[0] > end) {
      merged.push_back({start, end});
      start = s[0];
      end = s[1];
    } else {
      end = std::max(end, s[1]);
    }
  }
  merged.push_back({start, end});
  long long res = 0;
  for (int i = 1; i < merged.size(); i += 1) {
    res += merged[i][1] - merged[i][0] + 1;
  }
  std::cout << res;
  return 0;
}