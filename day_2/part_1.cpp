#include <fstream>
#include <iostream>
#include <string>
#include <vector>

std::vector<long> create_input() {
  std::vector<long> res;
  std::ifstream inp("input.txt");
  std::string line;
  while (std::getline(inp, line, ',')) {
    size_t pos = line.find('-');
    long long p1 = std::stoll(line.substr(0, pos));
    long long p2 = std::stoll(line.substr(pos + 1));

    res.push_back(p1);
    res.push_back(p2);
  }

  return res;
}

int main() {
  long long res = 0;
  std::vector<long> inp = create_input();
  for (int i = 0; i < inp.size(); i += 2) {
    long long p1 = inp[i];
    long long p2 = inp[i + 1];
    for (long j = p1; j < p2 + 1; j += 1) {
      std::string num = std::to_string(j);
      if (num.length() % 2)
        continue;
      std::string h1 = num.substr(0, num.length() / 2);
      std::string h2 = num.substr(num.length() / 2);

      if (h1 == h2) {
        res += j;
      }
    }
  }

  std::cout << res;
  return 1;
}
