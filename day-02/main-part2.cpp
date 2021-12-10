#include <iostream>
#include <fstream>
#include <bits/stdc++.h>

int main(int argc, char* argv[]) {
    int horz = 0;
    int depth = 0;
    int aim = 0;
    std::fstream file;
    file.open(argv[1], std::fstream::in);

    if (!file) {
        std::printf("Unable to read file '%s'\n", argv[1]);
        return 1;
    }
    std::string line;

    while (std::getline(file, line)) {
        std::stringstream instructions(line);
        std::string direction; std::string amount;

        instructions >> direction; 
        instructions >> amount;

        if (direction == "forward") {
            horz += std::stoi(amount);
            depth += aim * std::stoi(amount);
        } else if (direction == "down") {
            aim += std::stoi(amount);
        } else {
            aim -= std::stoi(amount);
        }
    }

    file.close();
    std::printf("%d\n", horz * depth);
}