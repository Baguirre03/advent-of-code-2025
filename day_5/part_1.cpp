#include <fstream>
#include <iostream>
#include <string>

std::vector<std::vector<long>> get_input() {
  std::ifstream inp("input.txt");
  std::vector<std::vector<long>> res = {{}, {}};
  bool switched = false;
  std::string line;
  while (!inp.eof()) {
    getline(inp, line);
    if (line.length() == 0) {
      switched = true;
      continue;
    }
    if (switched) {
      res[1].push_back(std::stoll(line));
    } else {
      size_t pos = line.find("-");
      res[0].push_back(std::stoll(line.substr(0, pos)));
      res[0].push_back(std::stoll(line.substr(pos + 1)));
    }
  }

  return res;
}

int main() {
  std::vector<std::vector<long>> inp = get_input();
  std::vector<long> ranges = inp[0];
  std::vector<long> ids = inp[1];
  int res = 0;
  for (long id : ids) {
    for (int i = 0; i < ranges.size(); i += 2) {
      long start = ranges[i];
      long end = ranges[i + 1];
      if (id >= start && id <= end) {
        res += 1;
        break;
      }
    }
  }
  std::cout << res;
  return res;
}